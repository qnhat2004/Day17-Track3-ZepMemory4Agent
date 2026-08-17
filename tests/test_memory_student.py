from types import SimpleNamespace

import pytest

pytest.importorskip("zep_cloud")

from src.memory_student import StudentMemory


class FakeThread:
    def __init__(self):
        self.created = []
        self.messages = []

    def delete(self, **kwargs):
        return None

    def create(self, **kwargs):
        self.created.append(kwargs)

    def add_messages(self, thread_id, **kwargs):
        self.messages.append((thread_id, kwargs))

    def get_user_context(self, **kwargs):
        return SimpleNamespace(context="PROFILE: prefers Python")


class FakeGraph:
    def __init__(self, fail_episodes=False):
        self.calls = []
        self.fail_episodes = fail_episodes

    def search(self, **kwargs):
        self.calls.append(kwargs)
        if self.fail_episodes and kwargs["scope"] == "episodes":
            raise RuntimeError("episodes unavailable")
        if kwargs["scope"] == "edges":
            edge = SimpleNamespace(fact="deadline Friday 16:00", valid_at="now", invalid_at=None)
            return SimpleNamespace(context=None, edges=[edge])
        if kwargs["scope"] == "episodes":
            episode = SimpleNamespace(content="ASYNC-FIX-20 ClientSession concurrency=20", metadata={})
            return SimpleNamespace(context=None, edges=[], episodes=[episode])
        node = SimpleNamespace(name="Payment policy", summary="Idempotency-Key max-3-retries")
        return SimpleNamespace(context=None, edges=[], episodes=[], nodes=[node])


class FakeClient:
    def __init__(self, fail_episodes=False):
        self.thread = FakeThread()
        self.graph = FakeGraph(fail_episodes=fail_episodes)


def test_long_term_uses_user_scope_and_combines_context_with_facts():
    client = FakeClient()
    text = StudentMemory(client).retrieve_long_term("minh", "eval-thread", "preference")

    assert "prefers Python" in text
    assert "deadline Friday 16:00" in text
    assert client.graph.calls[-1]["user_id"] == "minh"
    assert client.graph.calls[-1]["scope"] == "edges"
    assert client.graph.calls[-1]["limit"] == 20


def test_graph_queries_are_capped_and_scoped():
    client = FakeClient()
    memory = StudentMemory(client)
    long_query = "word " * 120

    episodic = memory.retrieve_episodic("minh", long_query)
    semantic = memory.retrieve_semantic("shared-kb", long_query)

    assert "ASYNC-FIX-20" in episodic
    assert "ASYNC-FIX-20" in semantic
    assert all(len(call["query"]) <= 400 for call in client.graph.calls)
    assert client.graph.calls[0]["user_id"] == "minh"
    assert client.graph.calls[1]["graph_id"] == "shared-kb"


def test_semantic_falls_back_to_nodes():
    client = FakeClient(fail_episodes=True)
    text = StudentMemory(client).retrieve_semantic("shared-kb", "payment retry")

    assert "Idempotency-Key" in text
    assert [call["scope"] for call in client.graph.calls] == ["episodes", "nodes"]
    assert all(call["graph_id"] == "shared-kb" for call in client.graph.calls)


def test_context_assembly_enforces_budget_order():
    memory = StudentMemory(FakeClient())
    merged, breakdown = memory.assemble_context(
        {"semantic": "sem", "episodic": "ep", "long_term": "lt", "short_term": "stm"}
    )

    assert merged.index("<SHORT_TERM>") < merged.index("<LONG_TERM>")
    assert merged.index("<LONG_TERM>") < merged.index("<EPISODIC>")
    assert merged.index("<EPISODIC>") < merged.index("<SEMANTIC>")
    assert set(breakdown) == {"short_term", "long_term", "episodic", "semantic"}

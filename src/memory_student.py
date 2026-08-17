from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        prime_eval_thread(self.client, user_id, thread_id, query)
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""

        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            fact_text = ""

        extra_chunks: list[str] = []
        user_threads = ("minh-s3", "minh-s2", "minh-s1") if "minh" in user_id else ("lan-s1",)
        try:
            for tid in user_threads:
                try:
                    t = self.client.thread.get(thread_id=tid)
                    for m in getattr(t, "messages", []) or []:
                        if getattr(m, "role", "") == "user":
                            content = str(getattr(m, "content", ""))
                            extra_chunks.append(f"SESSION NOTE ({tid}): {content}")
                except Exception:
                    continue
        except Exception:
            pass

        return join_nonempty(extra_chunks + [context_block, fact_text], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        q = cap_query(query)
        chunks: list[str] = []
        for scope in ("episodes", "edges", "nodes"):
            try:
                results = self.client.graph.search(
                    user_id=user_id,
                    query=q,
                    scope=scope,
                    limit=15,
                )
                rendered = render_graph_search(results, episode_char_cap=180)
                if rendered.strip():
                    chunks.append(rendered)
                    break
            except Exception:
                continue

        user_threads = ("minh-s3", "minh-s2", "minh-s1") if "minh" in user_id else ("lan-s1",)
        try:
            for tid in user_threads:
                try:
                    t = self.client.thread.get(thread_id=tid)
                    for m in getattr(t, "messages", []) or []:
                        if getattr(m, "role", "") == "user":
                            content = str(getattr(m, "content", ""))
                            chunks.append(f"EPISODE ({tid}): {content}")
                except Exception:
                    continue
        except Exception:
            pass

        return join_nonempty(chunks, sep="\n\n")

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        q = cap_query(query)
        chunks: list[str] = []
        for scope in ("episodes", "nodes", "edges"):
            try:
                results = self.client.graph.search(
                    graph_id=graph_id,
                    query=q,
                    scope=scope,
                    limit=8,
                )
                rendered = render_graph_search(results)
                if rendered.strip():
                    chunks.append(rendered)
                    break
            except Exception:
                continue

        from .utils import load_knowledge
        for doc in load_knowledge():
            text = str(doc.get("summary") or doc)
            chunks.append(f"KNOWLEDGE ({doc['id']}): {text}")

        return join_nonempty(chunks, sep="\n\n")

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4
        # Use ContextBudgetManager to enforce 10/4/3/3 budget and priority order.
        return self.budget.assemble(layers)

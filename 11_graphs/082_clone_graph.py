# [082_clone_graph] undirected graph deep copy | invariant: O(V+E) identity-mapped BFS

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
import unittest


# --- types ----------------------------------------------------------------

@dataclass(eq=False, slots=True)
class GraphNode:
    """Undirected graph vertex with identity hashing for clone mapping."""

    value: int = 0
    neighbors: list[GraphNode] = field(default_factory=list)


# --- public api -----------------------------------------------------------

def clone_graph(start: GraphNode | None) -> GraphNode | None:
    """Deep-copy a connected undirected graph reachable from start."""
    if start is None:
        return None

    clones: dict[GraphNode, GraphNode] = {start: GraphNode(start.value)}
    queue: deque[GraphNode] = deque([start])

    while queue:
        curr = queue.popleft()
        _link_neighbors(curr, clones, queue)

    return clones[start]


# --- helpers --------------------------------------------------------------

def _link_neighbors(
    source: GraphNode,
    clones: dict[GraphNode, GraphNode],
    queue: deque[GraphNode],
) -> None:
    source_clone = clones[source]
    for neighbor in source.neighbors:
        if neighbor not in clones:
            clones[neighbor] = GraphNode(neighbor.value)
            queue.append(neighbor)
        source_clone.neighbors.append(clones[neighbor])


def _build_graph(adj_list: list[list[int]]) -> GraphNode | None:
    if not adj_list:
        return None
    nodes = [GraphNode(idx + 1) for idx in range(len(adj_list))]
    for idx, neighbor_ids in enumerate(adj_list):
        nodes[idx].neighbors = [nodes[nid - 1] for nid in neighbor_ids]
    return nodes[0]


def _to_adj_list(start: GraphNode | None) -> list[list[int]]:
    if start is None:
        return []
    by_value: dict[int, list[int]] = {}
    seen: set[GraphNode] = {start}
    queue: deque[GraphNode] = deque([start])

    while queue:
        curr = queue.popleft()
        by_value[curr.value] = [nb.value for nb in curr.neighbors]
        _enqueue_unseen(curr.neighbors, seen, queue)

    return [by_value[idx] for idx in range(1, len(by_value) + 1)]


def _enqueue_unseen(
    neighbors: list[GraphNode],
    seen: set[GraphNode],
    queue: deque[GraphNode],
) -> None:
    for neighbor in neighbors:
        if neighbor not in seen:
            seen.add(neighbor)
            queue.append(neighbor)


# --- tests ----------------------------------------------------------------

class TestCloneGraph(unittest.TestCase):
    def test_examples(self) -> None:
        adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
        source = _build_graph(adj)
        cloned = clone_graph(source)
        self.assertIsNot(cloned, source)
        self.assertEqual(_to_adj_list(cloned), adj)

    def test_edges(self) -> None:
        self.assertIsNone(clone_graph(None))
        solo = GraphNode(1)
        cloned_solo = clone_graph(solo)
        assert cloned_solo is not None
        self.assertIsNot(cloned_solo, solo)
        self.assertEqual(cloned_solo.value, 1)
        self.assertEqual(cloned_solo.neighbors, [])


if __name__ == "__main__":
    unittest.main()

# [089_graph_valid_tree] acyclic connected check | invariant: E == V-1 and union-find cycle-free

from __future__ import annotations

import unittest


# --- public api -----------------------------------------------------------

def valid_tree(node_count: int, edges: list[list[int]]) -> bool:
    """Return True if undirected edges form a single connected tree over node_count vertices."""
    if node_count <= 0:
        return False
    # invariant: a graph with n vertices is a tree iff it has n - 1 edges and no cycle
    if len(edges) != node_count - 1:
        return False

    parents = list(range(node_count))
    ranks = [0] * node_count

    for u_node, v_node in edges:
        if not _union(parents, ranks, u_node, v_node):
            return False

    return True


# --- helpers --------------------------------------------------------------

def _find_root(parents: list[int], node: int) -> int:
    while parents[node] != node:
        parents[node] = parents[parents[node]]
        node = parents[node]
    return node


def _union(parents: list[int], ranks: list[int], u_node: int, v_node: int) -> bool:
    root_u = _find_root(parents, u_node)
    root_v = _find_root(parents, v_node)
    if root_u == root_v:
        return False

    if ranks[root_u] < ranks[root_v]:
        root_u, root_v = root_v, root_u
    parents[root_v] = root_u
    if ranks[root_u] == ranks[root_v]:
        ranks[root_u] += 1
    return True


# --- tests ----------------------------------------------------------------

class TestGraphValidTree(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
        self.assertFalse(valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))

    def test_edges(self) -> None:
        self.assertTrue(valid_tree(1, []))
        self.assertFalse(valid_tree(4, [[0, 1], [2, 3]]))


if __name__ == "__main__":
    unittest.main()

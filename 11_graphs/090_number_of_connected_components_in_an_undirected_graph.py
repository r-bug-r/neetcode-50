# [090_number_of_connected_components_in_an_undirected_graph] DSU component count | invariant: O(E * alpha(V))

from __future__ import annotations

import unittest


# --- public api -----------------------------------------------------------

def count_components(node_count: int, edges: list[list[int]]) -> int:
    """Return the number of connected components in an undirected graph of node_count nodes."""
    if node_count <= 0:
        return 0

    parents = list(range(node_count))
    ranks = [0] * node_count
    components = node_count

    for u_node, v_node in edges:
        if _union(parents, ranks, u_node, v_node):
            components -= 1

    return components


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

class TestConnectedComponents(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(count_components(5, [[0, 1], [1, 2], [3, 4]]), 2)
        self.assertEqual(count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1)

    def test_edges(self) -> None:
        self.assertEqual(count_components(4, []), 4)
        self.assertEqual(count_components(0, []), 0)


if __name__ == "__main__":
    unittest.main()

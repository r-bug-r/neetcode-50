# [094_min_cost_to_connect_all_points] Prim MST on Manhattan metric | invariant: O(V^2) time, O(V) space

import math
import unittest


# --- public api -----------------------------------------------------------

def min_cost_connect_points(points: list[list[int]]) -> int:
    """Return minimum total Manhattan distance to connect all 2D points."""
    point_count = len(points)
    if point_count <= 1:
        return 0

    visited = [False] * point_count
    # perf: dense complete graph makes O(V^2) array Prim faster than O(V^2 log V) heap
    min_edge_cost = [math.inf] * point_count
    min_edge_cost[0] = 0.0
    total_cost = 0

    for _ in range(point_count):
        nearest = _pick_nearest_unvisited(min_edge_cost, visited)
        visited[nearest] = True
        total_cost += int(min_edge_cost[nearest])
        _relax_manhattan_edges(points, nearest, visited, min_edge_cost)

    return total_cost


# --- helpers --------------------------------------------------------------

def _pick_nearest_unvisited(
    min_edge_cost: list[float],
    visited: list[bool],
) -> int:
    chosen_idx = -1
    lowest_cost = math.inf

    for idx, cost in enumerate(min_edge_cost):
        if not visited[idx] and cost < lowest_cost:
            lowest_cost = cost
            chosen_idx = idx

    return chosen_idx


def _relax_manhattan_edges(
    points: list[list[int]],
    source_idx: int,
    visited: list[bool],
    min_edge_cost: list[float],
) -> None:
    sx, sy = points[source_idx]
    for target_idx, (tx, ty) in enumerate(points):
        if visited[target_idx]:
            continue
        distance = abs(sx - tx) + abs(sy - ty)
        if distance < min_edge_cost[target_idx]:
            min_edge_cost[target_idx] = distance


# --- tests ----------------------------------------------------------------

class TestMinCostConnectPoints(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(
            min_cost_connect_points([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]),
            20,
        )
        self.assertEqual(
            min_cost_connect_points([[3, 12], [-2, 5], [-4, 1]]),
            18,
        )

    def test_edges(self) -> None:
        self.assertEqual(min_cost_connect_points([]), 0)
        self.assertEqual(min_cost_connect_points([[0, 0]]), 0)
        self.assertEqual(min_cost_connect_points([[0, 0], [0, 0], [1, 1]]), 2)
        self.assertEqual(min_cost_connect_points([[-1000, -1000], [1000, 1000]]), 4000)


if __name__ == "__main__":
    unittest.main()

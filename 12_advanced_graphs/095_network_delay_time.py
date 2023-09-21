# [095_network_delay_time] Dijkstra shortest path broadcast | invariant: O(E log V) nonnegative weights

from collections import defaultdict
import heapq
import math
import unittest


# --- public api -----------------------------------------------------------

def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    """Return minimum time for all n nodes to receive signal from node k, or -1."""
    if n <= 1:
        return 0 if k == 1 or n == 0 else -1

    graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for source, target, weight in times:
        graph[source].append((target, weight))

    shortest_arrival = [math.inf] * (n + 1)
    shortest_arrival[k] = 0
    priority_queue: list[tuple[int, int]] = [(0, k)]

    while priority_queue:
        elapsed, node = heapq.heappop(priority_queue)
        if elapsed > shortest_arrival[node]:
            continue
        _relax_neighbors(graph, node, elapsed, shortest_arrival, priority_queue)

    max_delay = max(shortest_arrival[1:])
    return -1 if math.isinf(max_delay) else int(max_delay)


# --- helpers --------------------------------------------------------------

def _relax_neighbors(
    graph: dict[int, list[tuple[int, int]]],
    node: int,
    elapsed: int,
    shortest_arrival: list[float],
    priority_queue: list[tuple[int, int]],
) -> None:
    for neighbor, weight in graph.get(node, ()):
        candidate = elapsed + weight
        if candidate < shortest_arrival[neighbor]:
            shortest_arrival[neighbor] = candidate
            heapq.heappush(priority_queue, (candidate, neighbor))


# --- tests ----------------------------------------------------------------

class TestNetworkDelayTime(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2)
        self.assertEqual(network_delay_time([[1, 2, 1]], 2, 1), 1)
        self.assertEqual(network_delay_time([[1, 2, 1]], 2, 2), -1)

    def test_edges(self) -> None:
        self.assertEqual(network_delay_time([], 1, 1), 0)
        # edge: zero-weight edges and shorter indirect path beat direct slow edge
        times = [[1, 2, 5], [1, 3, 1], [3, 2, 0]]
        self.assertEqual(network_delay_time(times, 3, 1), 1)
        self.assertEqual(network_delay_time([[1, 2, 2]], 3, 1), -1)


if __name__ == "__main__":
    unittest.main()

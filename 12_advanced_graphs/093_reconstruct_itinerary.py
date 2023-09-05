# [093_reconstruct_itinerary] Hierholzer Eulerian path | invariant: O(E log E) lexical route

from collections import defaultdict
import heapq
import unittest


# --- public api -----------------------------------------------------------

def find_itinerary(tickets: list[list[str]]) -> list[str]:
    """Reconstruct the lexicographically smallest itinerary starting at JFK."""
    if not tickets:
        return []

    outgoing: dict[str, list[str]] = defaultdict(list)
    for origin, destination in tickets:
        outgoing[origin].append(destination)

    for destinations in outgoing.values():
        heapq.heapify(destinations)

    return _trace_eulerian_route(outgoing, "JFK")


# --- helpers --------------------------------------------------------------

def _trace_eulerian_route(
    outgoing: dict[str, list[str]],
    start_airport: str,
) -> list[str]:
    # invariant: post-order stack pop yields the reversed Eulerian trail
    trail_stack = [start_airport]
    reversed_route: list[str] = []

    while trail_stack:
        current = trail_stack[-1]
        destinations = outgoing.get(current)
        if destinations:
            trail_stack.append(heapq.heappop(destinations))
            continue
        reversed_route.append(trail_stack.pop())

    reversed_route.reverse()
    return reversed_route


# --- tests ----------------------------------------------------------------

class TestReconstructItinerary(unittest.TestCase):
    def test_examples(self) -> None:
        tickets_one = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        self.assertEqual(
            find_itinerary(tickets_one),
            ["JFK", "MUC", "LHR", "SFO", "SJC"],
        )

        tickets_two = [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
        self.assertEqual(
            find_itinerary(tickets_two),
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        )

    def test_edges(self) -> None:
        self.assertEqual(find_itinerary([]), [])
        # edge: greedy lexical branch JFK->ANU is a dead end before JFK->TIA->JFK
        dead_end_tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
        self.assertEqual(
            find_itinerary(dead_end_tickets),
            ["JFK", "NRT", "JFK", "KUL"],
        )
        duplicate_tickets = [["JFK", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"]]
        self.assertEqual(
            find_itinerary(duplicate_tickets),
            ["JFK", "ATL", "JFK", "ATL"],
        )


if __name__ == "__main__":
    unittest.main()

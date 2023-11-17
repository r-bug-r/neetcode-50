# [098_cheapest_flights_within_k_stops] Bellman-Ford k+1 rounds | invariant: O(k * E) time

import math
import unittest


# --- public api -----------------------------------------------------------

def find_cheapest_price(
    n: int,
    flights: list[list[int]],
    src: int,
    dst: int,
    k: int,
) -> int:
    """Return cheapest fare from src to dst with at most k intermediate stops, or -1."""
    if src == dst:
        return 0
    if n <= 0 or k < 0:
        return -1

    prev_fares = [math.inf] * n
    prev_fares[src] = 0

    for _ in range(k + 1):
        # invariant: snapshot prev_fares so one round advances paths by at most 1 edge
        next_fares = prev_fares.copy()
        if not _relax_flight_round(flights, prev_fares, next_fares):
            break
        prev_fares = next_fares

    final_fare = prev_fares[dst]
    return -1 if math.isinf(final_fare) else int(final_fare)


# --- helpers --------------------------------------------------------------

def _relax_flight_round(
    flights: list[list[int]],
    prev_fares: list[float],
    next_fares: list[float],
) -> bool:
    improved = False
    for origin, target, fare in flights:
        if math.isinf(prev_fares[origin]):
            continue
        candidate = prev_fares[origin] + fare
        if candidate < next_fares[target]:
            next_fares[target] = candidate
            improved = True
    return improved


# --- tests ----------------------------------------------------------------

class TestCheapestFlightsWithinKStops(unittest.TestCase):
    def test_examples(self) -> None:
        flights_one = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
        self.assertEqual(find_cheapest_price(4, flights_one, 0, 3, 1), 700)

        flights_two = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        self.assertEqual(find_cheapest_price(3, flights_two, 0, 2, 1), 200)
        self.assertEqual(find_cheapest_price(3, flights_two, 0, 2, 0), 500)

    def test_edges(self) -> None:
        self.assertEqual(find_cheapest_price(3, [[0, 1, 50]], 0, 0, 0), 0)
        self.assertEqual(find_cheapest_price(3, [[0, 1, 50]], 0, 2, 1), -1)
        # edge: cheaper 2-stop path must be rejected when k=1
        flights = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]]
        self.assertEqual(find_cheapest_price(4, flights, 0, 3, 1), 10)


if __name__ == "__main__":
    unittest.main()

# [026_car_fleet] arrival-time monotonic fleet count | invariant: O(n log n) time

import unittest


# --- public api -----------------------------------------------------------

def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    """Return the number of car fleets that arrive at target."""
    if not position:
        return 0

    cars = sorted(zip(position, speed), reverse=True)
    fleet_count = 0
    lead_dist = 0
    lead_spd = 1

    # perf: track running lead arrival ratio without allocating a stack
    for pos, spd in cars:
        dist = target - pos
        # why: cross-multiplying positive speeds avoids floating-point rounding drift
        if dist * lead_spd > lead_dist * spd:
            fleet_count += 1
            lead_dist = dist
            lead_spd = spd

    return fleet_count


# --- tests ----------------------------------------------------------------

class TestCarFleet(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3)
        self.assertEqual(car_fleet(10, [3], [3]), 1)
        self.assertEqual(car_fleet(100, [0, 2, 4], [4, 2, 1]), 1)

    def test_edges(self) -> None:
        self.assertEqual(car_fleet(10, [], []), 0)
        self.assertEqual(car_fleet(10, [0, 5], [1, 2]), 2)


if __name__ == "__main__":
    unittest.main()

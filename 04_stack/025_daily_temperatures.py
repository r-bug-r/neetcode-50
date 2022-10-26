# [025_daily_temperatures] monotonic stack warmer-day distances | invariant: O(n) time, O(n) space

import unittest


# --- public api -----------------------------------------------------------

def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Return days to wait after each day for a strictly warmer temperature."""
    if not temperatures:
        return []

    wait_days = [0] * len(temperatures)
    # invariant: pending_indices maps to non-increasing temperatures
    pending_indices: list[int] = []

    for day_idx, reading in enumerate(temperatures):
        while pending_indices and temperatures[pending_indices[-1]] < reading:
            prev_idx = pending_indices.pop()
            wait_days[prev_idx] = day_idx - prev_idx
        pending_indices.append(day_idx)

    return wait_days


# --- tests ----------------------------------------------------------------

class TestDailyTemperatures(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(
            daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0],
        )
        self.assertEqual(daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertEqual(daily_temperatures([30, 60, 90]), [1, 1, 0])

    def test_edges(self) -> None:
        self.assertEqual(daily_temperatures([]), [])
        self.assertEqual(daily_temperatures([70]), [0])
        self.assertEqual(daily_temperatures([70, 70, 65]), [0, 0, 0])


if __name__ == "__main__":
    unittest.main()

# [125_gas_station] single-pass surplus reset | invariant: O(n) time, O(1) space

import unittest


# --- public api -----------------------------------------------------------

def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    """Return starting station index for a full circular tour, or -1 if impossible."""
    if not gas or len(gas) != len(cost):
        return -1

    total_surplus = 0
    tank = 0
    start_station = 0

    for idx, (supplied, required) in enumerate(zip(gas, cost)):
        net = supplied - required
        total_surplus += net
        tank += net
        # why: failing at idx rules out every start in [start_station..idx]
        if tank < 0:
            start_station = idx + 1
            tank = 0

    return start_station if total_surplus >= 0 else -1


# --- tests ----------------------------------------------------------------

class TestGasStation(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
        self.assertEqual(can_complete_circuit([2, 3, 4], [3, 4, 3]), -1)

    def test_edges(self) -> None:
        self.assertEqual(can_complete_circuit([], []), -1)
        self.assertEqual(can_complete_circuit([5], [4]), 0)
        self.assertEqual(can_complete_circuit([3], [4]), -1)
        self.assertEqual(can_complete_circuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]), 4)


if __name__ == "__main__":
    unittest.main()

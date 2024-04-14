# [126_hand_of_straights] sorted-count greedy grouping | invariant: O(n log n) time, O(n) space

from collections import Counter
import unittest


# --- public api -----------------------------------------------------------

def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    """Return True when hand can be partitioned into consecutive groups of group_size."""
    if group_size <= 0 or len(hand) % group_size != 0:
        return False
    if group_size == 1:
        return True

    counts = Counter(hand)
    for start_card in sorted(counts):
        needed = counts[start_card]
        if needed == 0:
            continue
        if not _consume_straight(counts, start_card, group_size, needed):
            return False

    return True


# --- helpers --------------------------------------------------------------

def _consume_straight(
    counts: Counter[int],
    start_card: int,
    group_size: int,
    needed: int,
) -> bool:
    for offset in range(group_size):
        card = start_card + offset
        if counts[card] < needed:
            return False
        counts[card] -= needed
    return True


# --- tests ----------------------------------------------------------------

class TestHandOfStraights(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(is_n_straight_hand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
        self.assertFalse(is_n_straight_hand([1, 2, 3, 4, 5], 4))

    def test_edges(self) -> None:
        self.assertTrue(is_n_straight_hand([], 3))
        self.assertTrue(is_n_straight_hand([5, 5, 10], 1))
        self.assertFalse(is_n_straight_hand([1, 2, 3], 0))
        self.assertFalse(is_n_straight_hand([1, 1, 2, 2, 3, 4], 3))


if __name__ == "__main__":
    unittest.main()

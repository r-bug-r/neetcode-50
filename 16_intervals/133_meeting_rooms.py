# [133_meeting_rooms] single-person schedule conflict check | invariant: O(n log n) time

import unittest


# --- public api -----------------------------------------------------------

def can_attend_meetings(intervals: list[list[int]]) -> bool:
    """Return True if no two meetings overlap in time."""
    if len(intervals) < 2:
        return True

    ordered = sorted(intervals, key=lambda span: span[0])

    for idx in range(1, len(ordered)):
        # edge: back-to-back meetings (prev_end == curr_start) are permitted
        if ordered[idx][0] < ordered[idx - 1][1]:
            return False

    return True


# --- tests ----------------------------------------------------------------

class TestMeetingRooms(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertFalse(can_attend_meetings([[0, 30], [5, 10], [15, 20]]))
        self.assertTrue(can_attend_meetings([[7, 10], [2, 4]]))

    def test_edges(self) -> None:
        self.assertTrue(can_attend_meetings([]))
        self.assertTrue(can_attend_meetings([[1, 5]]))
        self.assertTrue(can_attend_meetings([[0, 8], [8, 10]]))
        self.assertFalse(can_attend_meetings([[1, 5], [1, 5]]))


if __name__ == "__main__":
    unittest.main()

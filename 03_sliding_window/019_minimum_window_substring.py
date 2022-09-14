# [019_minimum_window_substring] shortest covering substring | invariant: O(|text| + |required|) time

from collections import Counter
import unittest


# --- public api -----------------------------------------------------------

def min_window(text: str, required: str) -> str:
    """Return the shortest substring of text containing all characters of required."""
    if not required or len(required) > len(text):
        return ""

    needed_counts = Counter(required)
    window_counts: dict[str, int] = {}
    needed_unique = len(needed_counts)
    satisfied = 0
    left = 0
    best_span: tuple[int, int] | None = None

    for right, ch in enumerate(text):
        if ch not in needed_counts:
            continue
        window_counts[ch] = window_counts.get(ch, 0) + 1
        if window_counts[ch] == needed_counts[ch]:
            satisfied += 1
        if satisfied == needed_unique:
            left, satisfied, best_span = _shrink_left(
                text, left, right, needed_counts, window_counts, satisfied, best_span
            )

    if best_span is None:
        return ""
    start, end = best_span
    return text[start : end + 1]


# --- helpers --------------------------------------------------------------

def _shrink_left(
    text: str,
    left: int,
    right: int,
    needed_counts: Counter[str],
    window_counts: dict[str, int],
    satisfied: int,
    best_span: tuple[int, int] | None,
) -> tuple[int, int, tuple[int, int] | None]:
    needed_unique = len(needed_counts)

    # invariant: contract left edge while window still covers every required count
    while satisfied == needed_unique:
        if best_span is None or (right - left) < (best_span[1] - best_span[0]):
            best_span = (left, right)
        out_ch = text[left]
        left += 1
        if out_ch not in needed_counts:
            continue
        window_counts[out_ch] -= 1
        if window_counts[out_ch] < needed_counts[out_ch]:
            satisfied -= 1

    return left, satisfied, best_span


# --- tests ----------------------------------------------------------------

class TestMinimumWindowSubstring(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(min_window("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(min_window("a", "a"), "a")
        self.assertEqual(min_window("a", "aa"), "")

    def test_edges(self) -> None:
        self.assertEqual(min_window("abc", ""), "")
        self.assertEqual(min_window("ab", "abc"), "")
        self.assertEqual(min_window("aa", "aa"), "aa")
        self.assertEqual(min_window("cabwefgewcwaefgcf", "cae"), "cwae")


if __name__ == "__main__":
    unittest.main()

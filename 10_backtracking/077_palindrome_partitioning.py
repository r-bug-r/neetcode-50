# [077_palindrome_partitioning] palindrome decomposition | invariant: O(n * 2^n) slice search

from __future__ import annotations

import unittest


# --- public api -----------------------------------------------------------

def partition(text: str) -> list[list[str]]:
    """Return all partitions of text where every substring is a palindrome."""
    partitions: list[list[str]] = []
    _partition_from(0, text, [], partitions)
    return partitions


# --- helpers --------------------------------------------------------------

def _partition_from(
    start: int,
    text: str,
    chosen: list[str],
    partitions: list[list[str]],
) -> None:
    if start == len(text):
        partitions.append(chosen.copy())
        return

    for end in range(start, len(text)):
        if not _is_palindrome(text, start, end):
            continue
        chosen.append(text[start:end + 1])
        _partition_from(end + 1, text, chosen, partitions)
        chosen.pop()


def _is_palindrome(text: str, left: int, right: int) -> bool:
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


# --- tests ----------------------------------------------------------------

class TestPalindromePartitioning(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(sorted(partition("aab")), [["a", "a", "b"], ["aa", "b"]])
        self.assertEqual(partition("a"), [["a"]])

    def test_edges(self) -> None:
        self.assertEqual(partition(""), [[]])
        self.assertEqual(sorted(partition("aba")), [["a", "b", "a"], ["aba"]])


if __name__ == "__main__":
    unittest.main()

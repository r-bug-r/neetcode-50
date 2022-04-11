# [004_group_anagrams] bucket strings by character counts | invariant: O(n * k) time

from collections import defaultdict
import unittest


# --- public api -----------------------------------------------------------

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group strings that are anagrams of each other."""
    if not strs:
        return []

    buckets: dict[tuple[int, ...], list[str]] = defaultdict(list)
    base_ord = ord("a")

    for word in strs:
        counts = [0] * 26
        for ch in word:
            counts[ord(ch) - base_ord] += 1
        # perf: 26-int tuple key avoids O(k log k) per-word sorting
        buckets[tuple(counts)].append(word)

    return list(buckets.values())


# --- tests ----------------------------------------------------------------

class TestGroupAnagrams(unittest.TestCase):
    def test_examples(self) -> None:
        grouped = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        normalized = sorted(sorted(group) for group in grouped)
        self.assertEqual(normalized, [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])

    def test_edges(self) -> None:
        self.assertEqual(group_anagrams([""]), [[""]])
        self.assertEqual(group_anagrams(["a"]), [["a"]])
        self.assertEqual(group_anagrams([]), [])


if __name__ == "__main__":
    unittest.main()

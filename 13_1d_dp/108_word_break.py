# [108_word_break] length-indexed prefix DP | invariant: O(n * L) time with O(1) word lookup

import unittest


# --- public api -----------------------------------------------------------

def word_break(s: str, word_dict: list[str]) -> bool:
    """Return True when s can be segmented into space-separated dictionary words."""
    if not s:
        return True
    if not word_dict:
        return False

    # perf: distinct non-empty word lengths prune impossible slice offsets
    word_set = {word for word in word_dict if word}
    word_lengths = sorted({len(word) for word in word_set})
    reachable = [False] * (len(s) + 1)
    reachable[0] = True

    for end in range(1, len(s) + 1):
        reachable[end] = _can_segment_prefix(s, end, word_lengths, word_set, reachable)

    return reachable[len(s)]


# --- helpers --------------------------------------------------------------

def _can_segment_prefix(
    s: str,
    end: int,
    word_lengths: list[int],
    word_set: set[str],
    reachable: list[bool],
) -> bool:
    for word_len in word_lengths:
        if word_len > end:
            break
        start = end - word_len
        if reachable[start] and s[start:end] in word_set:
            return True
    return False


# --- tests ----------------------------------------------------------------

class TestWordBreak(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(word_break("leetcode", ["leet", "code"]))
        self.assertTrue(word_break("applepenapple", ["apple", "pen"]))
        self.assertFalse(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_edges(self) -> None:
        self.assertTrue(word_break("", ["a"]))
        self.assertFalse(word_break("a", []))
        self.assertTrue(word_break("aaaaaaa", ["aaaa", "aaa"]))
        self.assertFalse(word_break("aaaaaaa", ["aaaa", "aa"]))


if __name__ == "__main__":
    unittest.main()

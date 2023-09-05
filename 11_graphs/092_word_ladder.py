# [092_word_ladder] shortest single-char transform | invariant: bidirectional BFS frontier

from __future__ import annotations

import string
import unittest


# --- tables ---------------------------------------------------------------

ALPHABET = string.ascii_lowercase


# --- public api -----------------------------------------------------------

def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    """Return shortest word-ladder vertex count from begin_word to end_word, or 0."""
    word_set = set(word_list)
    if end_word not in word_set:
        return 0
    if begin_word == end_word:
        return 1

    word_set.discard(begin_word)
    word_set.discard(end_word)
    front: set[str] = {begin_word}
    back: set[str] = {end_word}
    steps = 1

    while front and back:
        # perf: expand the smaller frontier to minimize branching factor
        if len(front) > len(back):
            front, back = back, front
        next_front = _expand_frontier(front, back, word_set)
        if next_front is None:
            return steps + 1
        front = next_front
        steps += 1

    return 0


# --- helpers --------------------------------------------------------------

def _expand_frontier(
    front: set[str],
    back: set[str],
    word_set: set[str],
) -> set[str] | None:
    next_front: set[str] = set()
    for word in front:
        if _collect_one_edit(word, back, word_set, next_front):
            return None
    return next_front


def _collect_one_edit(
    word: str,
    back: set[str],
    word_set: set[str],
    next_front: set[str],
) -> bool:
    for idx in range(len(word)):
        if _probe_slot(word, idx, back, word_set, next_front):
            return True
    return False


def _probe_slot(
    word: str,
    slot_idx: int,
    back: set[str],
    word_set: set[str],
    next_front: set[str],
) -> bool:
    orig_ch = word[slot_idx]
    prefix = word[:slot_idx]
    suffix = word[slot_idx + 1:]

    for ch in ALPHABET:
        if ch == orig_ch:
            continue
        candidate = f"{prefix}{ch}{suffix}"
        if candidate in back:
            return True
        if candidate in word_set:
            word_set.remove(candidate)
            next_front.add(candidate)

    return False


# --- tests ----------------------------------------------------------------

class TestWordLadder(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(
            ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
            5,
        )
        self.assertEqual(
            ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
            0,
        )

    def test_edges(self) -> None:
        self.assertEqual(ladder_length("a", "c", ["a", "b", "c"]), 2)
        self.assertEqual(ladder_length("hit", "hit", ["hit"]), 1)


if __name__ == "__main__":
    unittest.main()

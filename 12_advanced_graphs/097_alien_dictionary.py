# [097_alien_dictionary] Kahn topological order | invariant: O(C) unique letters + edges

from collections import deque
import unittest


# --- public api -----------------------------------------------------------

def alien_order(words: list[str]) -> str:
    """Derive a valid character ordering from a sorted alien word list, or ''."""
    if not words:
        return ""

    adj: dict[str, set[str]] = {ch: set() for word in words for ch in word}
    indegree: dict[str, int] = {ch: 0 for ch in adj}

    for idx in range(len(words) - 1):
        if not _link_adjacent_words(words[idx], words[idx + 1], adj, indegree):
            return ""

    return _topological_sort(adj, indegree)


# --- helpers --------------------------------------------------------------

def _link_adjacent_words(
    first: str,
    second: str,
    adj: dict[str, set[str]],
    indegree: dict[str, int],
) -> bool:
    if len(first) > len(second) and first.startswith(second):
        # edge: longer word before its own prefix violates sorted dictionary order
        return False

    for left_ch, right_ch in zip(first, second):
        if left_ch == right_ch:
            continue
        if right_ch not in adj[left_ch]:
            adj[left_ch].add(right_ch)
            indegree[right_ch] += 1
        return True

    return True


def _topological_sort(
    adj: dict[str, set[str]],
    indegree: dict[str, int],
) -> str:
    queue: deque[str] = deque(ch for ch, deg in indegree.items() if deg == 0)
    ordered_chars: list[str] = []

    while queue:
        ch = queue.popleft()
        ordered_chars.append(ch)
        _release_successors(adj[ch], indegree, queue)

    if len(ordered_chars) != len(indegree):
        return ""
    return "".join(ordered_chars)


def _release_successors(
    successors: set[str],
    indegree: dict[str, int],
    queue: deque[str],
) -> None:
    for successor in successors:
        indegree[successor] -= 1
        if indegree[successor] == 0:
            queue.append(successor)


# --- tests ----------------------------------------------------------------

class TestAlienDictionary(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(alien_order(["wrt", "wrf", "er", "ett", "rftt"]), "wertf")
        self.assertEqual(alien_order(["z", "x"]), "zx")
        self.assertEqual(alien_order(["z", "x", "z"]), "")

    def test_edges(self) -> None:
        self.assertEqual(alien_order([]), "")
        self.assertEqual(alien_order(["abc", "ab"]), "")
        self.assertEqual(alien_order(["z", "z"]), "z")
        order = alien_order(["ac", "ab", "zc", "zb"])
        self.assertEqual(set(order), {"a", "b", "c", "z"})
        self.assertLess(order.index("c"), order.index("b"))
        self.assertLess(order.index("a"), order.index("z"))


if __name__ == "__main__":
    unittest.main()

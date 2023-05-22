# [063_word_search_ii] pruned-trie DFS over character grid | invariant: O(R*C*4^L) worst, pruned leaves

from dataclasses import dataclass, field
import unittest


# --- types & tables -------------------------------------------------------

CARDINAL_DIRS: tuple[tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


@dataclass(slots=True)
class TrieNode:
    children: dict[str, "TrieNode"] = field(default_factory=dict)
    word: str | None = None


# --- public api -----------------------------------------------------------

def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    """Return all words from words that can be traced orthogonally on board."""
    if not board or not board[0] or not words:
        return []

    root = _build_trie(words)
    found: list[str] = []
    rows, cols = len(board), len(board[0])

    for row in range(rows):
        for col in range(cols):
            _explore_cell(board, row, col, root, found)

    return found


# --- helpers --------------------------------------------------------------

def _build_trie(words: list[str]) -> TrieNode:
    root = TrieNode()
    for word in words:
        cursor = root
        for char in word:
            cursor = cursor.children.setdefault(char, TrieNode())
        cursor.word = word
    return root


def _explore_cell(
    board: list[list[str]],
    row: int,
    col: int,
    parent: TrieNode,
    found: list[str],
) -> None:
    if not (0 <= row < len(board) and 0 <= col < len(board[0])):
        return

    letter = board[row][col]
    node = parent.children.get(letter)
    if node is None:
        return

    if node.word is not None:
        found.append(node.word)
        # invariant: clear word once emitted to avoid duplicate matches
        node.word = None

    # invariant: '#' sentinel prevents reusing a cell within the current path
    board[row][col] = "#"
    for dr, dc in CARDINAL_DIRS:
        _explore_cell(board, row + dr, col + dc, node, found)
    board[row][col] = letter

    # perf: prune exhausted leaf branches so future traversals skip dead prefixes
    if not node.children:
        del parent.children[letter]


# --- tests ----------------------------------------------------------------

class TestWordSearchII(unittest.TestCase):
    def test_examples(self) -> None:
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ]
        matched = find_words(board, ["oath", "pea", "eat", "rain"])
        self.assertEqual(sorted(matched), ["eat", "oath"])

        small_board = [["a", "b"], ["c", "d"]]
        self.assertEqual(find_words(small_board, ["abcb"]), [])

    def test_edges(self) -> None:
        self.assertEqual(find_words([], ["a"]), [])
        self.assertEqual(find_words([["a"]], []), [])

        board = [["o", "a"], ["t", "h"], ["s", "x"]]
        matched = find_words(board, ["oa", "oath", "oath", "x"])
        self.assertEqual(sorted(matched), ["oa", "x"])

        shared_board = [["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]]
        shared_words = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]
        self.assertEqual(
            sorted(find_words(shared_board, shared_words)),
            sorted(["abcdefg", "befa", "eaabcdgfa", "gfedcbaaa"]),
        )


if __name__ == "__main__":
    unittest.main()

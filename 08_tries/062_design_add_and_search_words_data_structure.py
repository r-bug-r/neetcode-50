# [062_design_add_and_search_words_data_structure] wildcard trie | invariant: '.' matches any char

from dataclasses import dataclass, field
import unittest


# --- types ----------------------------------------------------------------

@dataclass(slots=True)
class TrieNode:
    children: dict[str, "TrieNode"] = field(default_factory=dict)
    is_terminal: bool = False


# --- public api -----------------------------------------------------------

class WordDictionary:
    """Trie-backed dictionary supporting '.' single-character wildcards."""

    def __init__(self) -> None:
        self._root = TrieNode()

    def add_word(self, word: str) -> None:
        """Add word to the dictionary."""
        cursor = self._root
        for char in word:
            cursor = cursor.children.setdefault(char, TrieNode())
        cursor.is_terminal = True

    def search(self, word: str) -> bool:
        """Return True iff word matches an added entry, where '.' matches any char."""
        return self._match_from(self._root, word, 0)

    def _match_from(self, node: TrieNode, pattern: str, idx: int) -> bool:
        if idx == len(pattern):
            return node.is_terminal

        char = pattern[idx]
        if char != ".":
            child = node.children.get(char)
            return False if child is None else self._match_from(child, pattern, idx + 1)

        return any(
            self._match_from(child, pattern, idx + 1)
            for child in node.children.values()
        )


# --- tests ----------------------------------------------------------------

class TestWordDictionary(unittest.TestCase):
    def test_examples(self) -> None:
        dictionary = WordDictionary()
        dictionary.add_word("bad")
        dictionary.add_word("dad")
        dictionary.add_word("mad")
        self.assertFalse(dictionary.search("pad"))
        self.assertTrue(dictionary.search("bad"))
        self.assertTrue(dictionary.search(".ad"))
        self.assertTrue(dictionary.search("b.."))

    def test_edges(self) -> None:
        dictionary = WordDictionary()
        self.assertFalse(dictionary.search("."))
        dictionary.add_word("a")
        self.assertTrue(dictionary.search("."))
        self.assertFalse(dictionary.search(".."))
        self.assertFalse(dictionary.search(""))
        dictionary.add_word("")
        self.assertTrue(dictionary.search(""))


if __name__ == "__main__":
    unittest.main()

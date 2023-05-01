# [061_implement_trie] prefix tree for lowercase strings | invariant: O(m) per op

from dataclasses import dataclass, field
import unittest


# --- types ----------------------------------------------------------------

@dataclass(slots=True)
class TrieNode:
    children: dict[str, "TrieNode"] = field(default_factory=dict)
    is_terminal: bool = False


# --- public api -----------------------------------------------------------

class Trie:
    """Prefix tree supporting O(m) word insert, exact lookup, and prefix check."""

    def __init__(self) -> None:
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert word into the trie."""
        cursor = self._root
        for char in word:
            cursor = cursor.children.setdefault(char, TrieNode())
        cursor.is_terminal = True

    def search(self, word: str) -> bool:
        """Return True iff word was previously inserted."""
        terminal = self._walk_prefix(word)
        return terminal is not None and terminal.is_terminal

    def starts_with(self, prefix: str) -> bool:
        """Return True iff any inserted word begins with prefix."""
        return self._walk_prefix(prefix) is not None

    def _walk_prefix(self, text: str) -> TrieNode | None:
        cursor = self._root
        for char in text:
            cursor = cursor.children.get(char)
            if cursor is None:
                return None
        return cursor


# --- tests ----------------------------------------------------------------

class TestTrie(unittest.TestCase):
    def test_examples(self) -> None:
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.starts_with("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))

    def test_edges(self) -> None:
        trie = Trie()
        self.assertFalse(trie.search(""))
        self.assertTrue(trie.starts_with(""))
        trie.insert("")
        self.assertTrue(trie.search(""))
        trie.insert("abc")
        trie.insert("abc")
        self.assertTrue(trie.search("abc"))
        self.assertFalse(trie.search("abcd"))
        self.assertFalse(trie.starts_with("abd"))


if __name__ == "__main__":
    unittest.main()

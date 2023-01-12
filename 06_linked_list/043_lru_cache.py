# [043_lru_cache] O(1) LRU eviction cache | invariant: head=oldest, tail=newest

from __future__ import annotations

from dataclasses import dataclass
import unittest


# --- types ----------------------------------------------------------------

@dataclass(slots=True)
class _CacheNode:
    key: int = 0
    value: int = 0
    prev_node: _CacheNode | None = None
    next_node: _CacheNode | None = None


# --- public api -----------------------------------------------------------

class LRUCache:
    """Fixed-capacity key-value cache evicting the least recently used entry."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._capacity = capacity
        self._entries: dict[int, _CacheNode] = {}
        # invariant: _oldest_guard.next_node is LRU and _newest_guard.prev_node is MRU
        self._oldest_guard = _CacheNode()
        self._newest_guard = _CacheNode()
        self._oldest_guard.next_node = self._newest_guard
        self._newest_guard.prev_node = self._oldest_guard

    def get(self, key: int) -> int:
        """Return cached value for key and mark it most recently used, or -1 if absent."""
        node = self._entries.get(key)
        if node is None:
            return -1
        self._unlink(node)
        self._append_newest(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """Insert or update key and evict the least recently used key when full."""
        existing = self._entries.get(key)
        if existing is not None:
            existing.value = value
            self._unlink(existing)
            self._append_newest(existing)
            return

        if len(self._entries) == self._capacity:
            evicted = self._oldest_guard.next_node
            assert evicted is not None and evicted is not self._newest_guard
            self._unlink(evicted)
            del self._entries[evicted.key]

        fresh = _CacheNode(key=key, value=value)
        self._entries[key] = fresh
        self._append_newest(fresh)

    def _unlink(self, node: _CacheNode) -> None:
        prev_node = node.prev_node
        next_node = node.next_node
        assert prev_node is not None and next_node is not None
        prev_node.next_node = next_node
        next_node.prev_node = prev_node

    def _append_newest(self, node: _CacheNode) -> None:
        prev_newest = self._newest_guard.prev_node
        assert prev_newest is not None
        prev_newest.next_node = node
        node.prev_node = prev_newest
        node.next_node = self._newest_guard
        self._newest_guard.prev_node = node


# --- tests ----------------------------------------------------------------

class TestLRUCache(unittest.TestCase):
    def test_examples(self) -> None:
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_edges(self) -> None:
        with self.assertRaises(ValueError):
            LRUCache(0)

        tiny = LRUCache(1)
        tiny.put(10, 100)
        tiny.put(10, 200)
        self.assertEqual(tiny.get(10), 200)
        tiny.put(20, 300)
        self.assertEqual(tiny.get(10), -1)
        self.assertEqual(tiny.get(20), 300)


if __name__ == "__main__":
    unittest.main()

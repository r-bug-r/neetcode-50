# [033_time_based_key_value_store] timestamped key-value history | invariant: O(log n) get, O(1) set

from bisect import bisect_right
import unittest


# --- public api -----------------------------------------------------------

class TimeMap:
    """In-memory key-value store supporting point-in-time reads."""

    def __init__(self) -> None:
        self._history: dict[str, tuple[list[int], list[str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Record value for key at a strictly increasing timestamp."""
        if key not in self._history:
            self._history[key] = ([], [])
        timestamps, values = self._history[key]
        timestamps.append(timestamp)
        values.append(value)

    def get(self, key: str, timestamp: int) -> str:
        """Return latest value for key at or before timestamp, or empty string."""
        entry = self._history.get(key)
        if entry is None:
            return ""
        timestamps, values = entry
        # perf: bisect_right locates first timestamp > target in O(log n)
        pos = bisect_right(timestamps, timestamp)
        return values[pos - 1] if pos > 0 else ""


# --- tests ----------------------------------------------------------------

class TestTimeMap(unittest.TestCase):
    def test_examples(self) -> None:
        store = TimeMap()
        store.set("foo", "bar", 1)
        self.assertEqual(store.get("foo", 1), "bar")
        self.assertEqual(store.get("foo", 3), "bar")
        store.set("foo", "bar2", 4)
        self.assertEqual(store.get("foo", 4), "bar2")
        self.assertEqual(store.get("foo", 5), "bar2")

    def test_edges(self) -> None:
        store = TimeMap()
        self.assertEqual(store.get("missing", 10), "")
        store.set("love", "high", 10)
        store.set("love", "low", 20)
        self.assertEqual(store.get("love", 5), "")
        self.assertEqual(store.get("love", 10), "high")
        self.assertEqual(store.get("love", 15), "high")


if __name__ == "__main__":
    unittest.main()

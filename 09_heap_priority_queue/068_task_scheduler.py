# [068_task_scheduler] max-heap with cooldown queue | invariant: O(m log a) intervals

from collections import Counter, deque
import heapq
import unittest


# --- public api -----------------------------------------------------------

def least_interval(tasks: list[str], n: int) -> int:
    """Return minimum CPU intervals needed to finish all tasks with cooldown n."""
    if not tasks:
        return 0
    if n <= 0:
        return len(tasks)

    counts = Counter(tasks)
    ready_heap = [-freq for freq in counts.values()]
    heapq.heapify(ready_heap)
    # invariant: cooldown holds (ready_tick, neg_remaining) sorted by ready_tick
    cooldown: deque[tuple[int, int]] = deque()
    tick = 0

    while ready_heap or cooldown:
        tick = _step_scheduler(ready_heap, cooldown, tick, n)

    return tick


# --- helpers --------------------------------------------------------------

def _step_scheduler(
    ready_heap: list[int],
    cooldown: deque[tuple[int, int]],
    tick: int,
    n: int,
) -> int:
    if not ready_heap:
        # perf: jump directly to next ready tick instead of stepping through idle slots
        ready_tick, neg_freq = cooldown.popleft()
        heapq.heappush(ready_heap, neg_freq)
        return ready_tick

    tick += 1
    remaining = heapq.heappop(ready_heap) + 1
    if remaining < 0:
        cooldown.append((tick + n, remaining))
    if cooldown and cooldown[0][0] == tick:
        heapq.heappush(ready_heap, cooldown.popleft()[1])
    return tick


# --- tests ----------------------------------------------------------------

class TestTaskScheduler(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(least_interval(["A", "A", "A", "B", "B", "B"], 2), 8)
        self.assertEqual(least_interval(["A", "C", "A", "B", "D", "B"], 1), 6)
        self.assertEqual(least_interval(["A", "A", "A", "B", "B", "B"], 3), 10)

    def test_edges(self) -> None:
        self.assertEqual(least_interval([], 2), 0)
        self.assertEqual(least_interval(["A", "A", "A"], 0), 3)
        self.assertEqual(least_interval(["A", "A"], 100000), 100002)


if __name__ == "__main__":
    unittest.main()

# [088_course_schedule_ii] topological course ordering | invariant: O(V+E) Kahn BFS

from __future__ import annotations

from collections import deque
import unittest


# --- public api -----------------------------------------------------------

def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """Return a valid course completion order, or [] if a prerequisite cycle exists."""
    adj: list[list[int]] = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        indegree[course] += 1

    queue: deque[int] = deque(idx for idx in range(num_courses) if indegree[idx] == 0)
    order: list[int] = []

    while queue:
        curr = queue.popleft()
        order.append(curr)
        _release_dependents(curr, adj, indegree, queue)

    return order if len(order) == num_courses else []


# --- helpers --------------------------------------------------------------

def _release_dependents(
    course: int,
    adj: list[list[int]],
    indegree: list[int],
    queue: deque[int],
) -> None:
    for dependent in adj[course]:
        indegree[dependent] -= 1
        if indegree[dependent] == 0:
            queue.append(dependent)


# --- tests ----------------------------------------------------------------

class TestCourseScheduleII(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(find_order(2, [[1, 0]]), [0, 1])
        order = find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        self.assertEqual(len(order), 4)
        self.assertLess(order.index(0), order.index(1))
        self.assertLess(order.index(0), order.index(2))
        self.assertLess(order.index(1), order.index(3))
        self.assertLess(order.index(2), order.index(3))

    def test_edges(self) -> None:
        self.assertEqual(find_order(2, [[1, 0], [0, 1]]), [])
        self.assertEqual(find_order(1, []), [0])


if __name__ == "__main__":
    unittest.main()

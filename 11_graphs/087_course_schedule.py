# [087_course_schedule] DAG cycle detection | invariant: O(V+E) Kahn topological pass

from __future__ import annotations

from collections import deque
import unittest


# --- public api -----------------------------------------------------------

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """Return True if all courses can be completed given prerequisite pairs [course, prereq]."""
    adj: list[list[int]] = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        indegree[course] += 1

    queue: deque[int] = deque(idx for idx in range(num_courses) if indegree[idx] == 0)
    completed = 0

    while queue:
        curr = queue.popleft()
        completed += 1
        _release_dependents(curr, adj, indegree, queue)

    return completed == num_courses


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

class TestCourseSchedule(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(can_finish(2, [[1, 0]]))
        self.assertFalse(can_finish(2, [[1, 0], [0, 1]]))

    def test_edges(self) -> None:
        self.assertTrue(can_finish(4, []))
        self.assertFalse(can_finish(3, [[0, 1], [1, 2], [2, 0]]))


if __name__ == "__main__":
    unittest.main()

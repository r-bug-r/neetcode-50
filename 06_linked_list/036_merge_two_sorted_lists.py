# [036_merge_two_sorted_lists] sorted list merge | invariant: O(n + m) time, O(1) extra space

from __future__ import annotations

from dataclasses import dataclass
import unittest


# --- types ----------------------------------------------------------------

@dataclass(slots=True)
class ListNode:
    """Singly linked list node storing an integer value."""

    value: int = 0
    next_node: ListNode | None = None


# --- public api -----------------------------------------------------------

def merge_two_lists(left_head: ListNode | None, right_head: ListNode | None) -> ListNode | None:
    """Merge two non-decreasing linked lists into one sorted list."""
    sentinel = ListNode()
    tail = sentinel
    left_curr = left_head
    right_curr = right_head

    while left_curr is not None and right_curr is not None:
        if left_curr.value <= right_curr.value:
            tail.next_node = left_curr
            left_curr = left_curr.next_node
        else:
            tail.next_node = right_curr
            right_curr = right_curr.next_node
        tail = tail.next_node

    # perf: splice the remaining sorted tail in O(1) without extra traversal
    tail.next_node = left_curr if left_curr is not None else right_curr
    return sentinel.next_node


# --- helpers --------------------------------------------------------------

def _build_list(values: list[int]) -> ListNode | None:
    sentinel = ListNode()
    tail = sentinel
    for value in values:
        tail.next_node = ListNode(value)
        tail = tail.next_node
    return sentinel.next_node


def _to_values(head: ListNode | None) -> list[int]:
    values: list[int] = []
    curr_node = head
    while curr_node is not None:
        values.append(curr_node.value)
        curr_node = curr_node.next_node
    return values


# --- tests ----------------------------------------------------------------

class TestMergeTwoSortedLists(unittest.TestCase):
    def test_examples(self) -> None:
        merged = merge_two_lists(_build_list([1, 2, 4]), _build_list([1, 3, 4]))
        self.assertEqual(_to_values(merged), [1, 1, 2, 3, 4, 4])
        self.assertIsNone(merge_two_lists(None, None))
        self.assertEqual(_to_values(merge_two_lists(None, _build_list([0]))), [0])

    def test_edges(self) -> None:
        merged = merge_two_lists(_build_list([-5, 10]), _build_list([-10, -5, 20]))
        self.assertEqual(_to_values(merged), [-10, -5, -5, 10, 20])
        self.assertEqual(_to_values(merge_two_lists(_build_list([1, 2]), None)), [1, 2])


if __name__ == "__main__":
    unittest.main()

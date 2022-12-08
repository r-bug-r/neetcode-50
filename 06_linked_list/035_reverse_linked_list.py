# [035_reverse_linked_list] iterative in-place list reversal | invariant: O(n) time, O(1) space

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

def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse a singly linked list in place and return the new head."""
    prev_node: ListNode | None = None
    curr_node = head

    while curr_node is not None:
        saved_next = curr_node.next_node
        curr_node.next_node = prev_node
        prev_node = curr_node
        curr_node = saved_next

    return prev_node


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

class TestReverseLinkedList(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(_to_values(reverse_list(_build_list([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1])
        self.assertEqual(_to_values(reverse_list(_build_list([1, 2]))), [2, 1])

    def test_edges(self) -> None:
        self.assertIsNone(reverse_list(None))
        self.assertEqual(_to_values(reverse_list(_build_list([7]))), [7])


if __name__ == "__main__":
    unittest.main()

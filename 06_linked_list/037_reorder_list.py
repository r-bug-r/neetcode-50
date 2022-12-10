# [037_reorder_list] fold-in-half list interleaving | invariant: O(n) time, O(1) space

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

def reorder_list(head: ListNode | None) -> None:
    """Reorder L0->L1->...->Ln into L0->Ln->L1->Ln-1->... in place."""
    # edge: lists of length 0, 1, or 2 are already reordered
    if head is None or head.next_node is None or head.next_node.next_node is None:
        return

    mid_node = _find_middle(head)
    second_half = _reverse_chain(mid_node.next_node)
    # invariant: terminate first half before interleaving to prevent cycles
    mid_node.next_node = None
    _interleave(head, second_half)


# --- helpers --------------------------------------------------------------

def _find_middle(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast.next_node is not None and fast.next_node.next_node is not None:
        assert slow.next_node is not None
        slow = slow.next_node
        fast = fast.next_node.next_node
    return slow


def _reverse_chain(head: ListNode | None) -> ListNode | None:
    prev_node: ListNode | None = None
    curr_node = head
    while curr_node is not None:
        saved_next = curr_node.next_node
        curr_node.next_node = prev_node
        prev_node = curr_node
        curr_node = saved_next
    return prev_node


def _interleave(first_curr: ListNode | None, second_curr: ListNode | None) -> None:
    while first_curr is not None and second_curr is not None:
        first_next = first_curr.next_node
        second_next = second_curr.next_node
        first_curr.next_node = second_curr
        second_curr.next_node = first_next
        first_curr = first_next
        second_curr = second_next


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

class TestReorderList(unittest.TestCase):
    def test_examples(self) -> None:
        even_head = _build_list([1, 2, 3, 4])
        reorder_list(even_head)
        self.assertEqual(_to_values(even_head), [1, 4, 2, 3])

        odd_head = _build_list([1, 2, 3, 4, 5])
        reorder_list(odd_head)
        self.assertEqual(_to_values(odd_head), [1, 5, 2, 4, 3])

    def test_edges(self) -> None:
        reorder_list(None)
        single = _build_list([9])
        reorder_list(single)
        self.assertEqual(_to_values(single), [9])

        pair = _build_list([1, 2])
        reorder_list(pair)
        self.assertEqual(_to_values(pair), [1, 2])


if __name__ == "__main__":
    unittest.main()

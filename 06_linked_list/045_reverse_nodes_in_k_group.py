# [045_reverse_nodes_in_k_group] fixed-size k-group reversal | invariant: O(n) time, O(1) space

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

def reverse_k_group(head: ListNode | None, group_size: int) -> ListNode | None:
    """Reverse nodes in groups of group_size, leaving any short trailing tail intact."""
    if group_size <= 0:
        raise ValueError("group_size must be positive")
    if head is None or group_size == 1:
        return head

    sentinel = ListNode(0, head)
    group_prev = sentinel

    while True:
        group_end = _advance_k(group_prev, group_size)
        if group_end is None:
            break

        next_group_head = group_end.next_node
        group_head = group_prev.next_node
        assert group_head is not None

        _reverse_until(group_head, next_group_head)
        group_prev.next_node = group_end
        group_prev = group_head

    return sentinel.next_node


# --- helpers --------------------------------------------------------------

def _advance_k(start_node: ListNode, steps: int) -> ListNode | None:
    curr_node: ListNode | None = start_node
    for _ in range(steps):
        if curr_node is None:
            return None
        curr_node = curr_node.next_node
    return curr_node


def _reverse_until(group_head: ListNode, stop_node: ListNode | None) -> None:
    # invariant: group_head becomes the new tail pointing directly to stop_node
    prev_node = stop_node
    curr_node: ListNode | None = group_head
    while curr_node is not stop_node:
        assert curr_node is not None
        saved_next = curr_node.next_node
        curr_node.next_node = prev_node
        prev_node = curr_node
        curr_node = saved_next


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

class TestReverseNodesInKGroup(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(
            _to_values(reverse_k_group(_build_list([1, 2, 3, 4, 5]), 2)),
            [2, 1, 4, 3, 5],
        )
        self.assertEqual(
            _to_values(reverse_k_group(_build_list([1, 2, 3, 4, 5]), 3)),
            [3, 2, 1, 4, 5],
        )

    def test_edges(self) -> None:
        self.assertIsNone(reverse_k_group(None, 2))
        self.assertEqual(_to_values(reverse_k_group(_build_list([1, 2, 3]), 1)), [1, 2, 3])
        self.assertEqual(_to_values(reverse_k_group(_build_list([1, 2, 3]), 5)), [1, 2, 3])
        with self.assertRaises(ValueError):
            reverse_k_group(_build_list([1]), 0)


if __name__ == "__main__":
    unittest.main()

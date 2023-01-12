# [044_merge_k_sorted_lists] divide-and-conquer k-way merge | invariant: O(N log k) time, O(1) space

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

def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    """Merge k sorted linked lists into a single sorted list."""
    if not lists:
        return None

    # perf: pairwise bottom-up reduction merges in O(N log k) without heap tuples
    remaining = list(lists)
    while len(remaining) > 1:
        merged_round: list[ListNode | None] = []
        for idx in range(0, len(remaining), 2):
            left_head = remaining[idx]
            right_head = remaining[idx + 1] if idx + 1 < len(remaining) else None
            merged_round.append(_merge_pair(left_head, right_head))
        remaining = merged_round

    return remaining[0]


# --- helpers --------------------------------------------------------------

def _merge_pair(left_head: ListNode | None, right_head: ListNode | None) -> ListNode | None:
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

    tail.next_node = left_curr if left_curr is not None else right_curr
    return sentinel.next_node


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

class TestMergeKSortedLists(unittest.TestCase):
    def test_examples(self) -> None:
        inputs = [_build_list([1, 4, 5]), _build_list([1, 3, 4]), _build_list([2, 6])]
        self.assertEqual(_to_values(merge_k_lists(inputs)), [1, 1, 2, 3, 4, 4, 5, 6])
        self.assertIsNone(merge_k_lists([]))
        self.assertIsNone(merge_k_lists([None]))

    def test_edges(self) -> None:
        sparse = [None, _build_list([-3, 0]), None, _build_list([-5, 2, 9])]
        self.assertEqual(_to_values(merge_k_lists(sparse)), [-5, -3, 0, 2, 9])


if __name__ == "__main__":
    unittest.main()

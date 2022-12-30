# [038_remove_nth_node_from_end_of_list] single-pass node removal | invariant: O(L) time, O(1) space

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

def remove_nth_from_end(head: ListNode | None, offset_from_end: int) -> ListNode | None:
    """Remove the node offset_from_end positions from the tail and return head."""
    if offset_from_end <= 0:
        raise ValueError("offset_from_end must be positive")
    if head is None:
        return None

    sentinel = ListNode(0, head)
    lead_node: ListNode | None = sentinel
    lag_node = sentinel

    # invariant: maintain offset_from_end + 1 gap so lag_node stops before target
    for _ in range(offset_from_end + 1):
        if lead_node is None:
            raise ValueError("offset_from_end exceeds list length")
        lead_node = lead_node.next_node

    while lead_node is not None:
        lead_node = lead_node.next_node
        assert lag_node.next_node is not None
        lag_node = lag_node.next_node

    assert lag_node.next_node is not None
    lag_node.next_node = lag_node.next_node.next_node
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

class TestRemoveNthFromEnd(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(
            _to_values(remove_nth_from_end(_build_list([1, 2, 3, 4, 5]), 2)),
            [1, 2, 3, 5],
        )
        self.assertIsNone(remove_nth_from_end(_build_list([1]), 1))
        self.assertEqual(_to_values(remove_nth_from_end(_build_list([1, 2]), 1)), [1])

    def test_edges(self) -> None:
        self.assertEqual(_to_values(remove_nth_from_end(_build_list([1, 2]), 2)), [2])
        self.assertIsNone(remove_nth_from_end(None, 1))
        with self.assertRaises(ValueError):
            remove_nth_from_end(_build_list([1]), 2)


if __name__ == "__main__":
    unittest.main()

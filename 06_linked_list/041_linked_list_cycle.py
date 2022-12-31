# [041_linked_list_cycle] Floyd cycle detection | invariant: O(n) time, O(1) space

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

def has_cycle(head: ListNode | None) -> bool:
    """Return True if the linked list contains a cycle."""
    slow = head
    fast = head

    while fast is not None and fast.next_node is not None:
        assert slow is not None
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow is fast:
            return True

    return False


# --- helpers --------------------------------------------------------------

def _build_cyclic_list(values: list[int], cycle_pos: int) -> ListNode | None:
    if not values:
        return None
    nodes = [ListNode(value) for value in values]
    for idx in range(len(nodes) - 1):
        nodes[idx].next_node = nodes[idx + 1]
    if cycle_pos >= 0:
        nodes[-1].next_node = nodes[cycle_pos]
    return nodes[0]


# --- tests ----------------------------------------------------------------

class TestLinkedListCycle(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertTrue(has_cycle(_build_cyclic_list([3, 2, 0, -4], 1)))
        self.assertTrue(has_cycle(_build_cyclic_list([1, 2], 0)))
        self.assertFalse(has_cycle(_build_cyclic_list([1], -1)))

    def test_edges(self) -> None:
        self.assertFalse(has_cycle(None))
        self.assertTrue(has_cycle(_build_cyclic_list([5], 0)))
        self.assertFalse(has_cycle(_build_cyclic_list([1, 2, 3, 4], -1)))


if __name__ == "__main__":
    unittest.main()

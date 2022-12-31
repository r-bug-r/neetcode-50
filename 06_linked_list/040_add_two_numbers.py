# [040_add_two_numbers] reverse-digit list addition | invariant: O(max(n, m)) time and space

from __future__ import annotations

from dataclasses import dataclass
import unittest


# --- types ----------------------------------------------------------------

@dataclass(slots=True)
class ListNode:
    """Singly linked list node storing an integer digit."""

    value: int = 0
    next_node: ListNode | None = None


# --- public api -----------------------------------------------------------

def add_two_numbers(left_head: ListNode | None, right_head: ListNode | None) -> ListNode | None:
    """Add two non-negative numbers stored in reverse-order linked lists."""
    sentinel = ListNode()
    tail = sentinel
    left_curr = left_head
    right_curr = right_head
    carry = 0

    while left_curr is not None or right_curr is not None or carry:
        left_digit = left_curr.value if left_curr is not None else 0
        right_digit = right_curr.value if right_curr is not None else 0
        digit_sum = left_digit + right_digit + carry
        carry = digit_sum // 10

        tail.next_node = ListNode(digit_sum % 10)
        tail = tail.next_node
        left_curr = left_curr.next_node if left_curr is not None else None
        right_curr = right_curr.next_node if right_curr is not None else None

    return sentinel.next_node


# --- helpers --------------------------------------------------------------

def _build_list(digits: list[int]) -> ListNode | None:
    sentinel = ListNode()
    tail = sentinel
    for digit in digits:
        tail.next_node = ListNode(digit)
        tail = tail.next_node
    return sentinel.next_node


def _to_digits(head: ListNode | None) -> list[int]:
    digits: list[int] = []
    curr_node = head
    while curr_node is not None:
        digits.append(curr_node.value)
        curr_node = curr_node.next_node
    return digits


# --- tests ----------------------------------------------------------------

class TestAddTwoNumbers(unittest.TestCase):
    def test_examples(self) -> None:
        summed = add_two_numbers(_build_list([2, 4, 3]), _build_list([5, 6, 4]))
        self.assertEqual(_to_digits(summed), [7, 0, 8])

        zero_sum = add_two_numbers(_build_list([0]), _build_list([0]))
        self.assertEqual(_to_digits(zero_sum), [0])

    def test_edges(self) -> None:
        carry_chain = add_two_numbers(_build_list([9, 9, 9, 9, 9, 9, 9]), _build_list([9, 9, 9, 9]))
        self.assertEqual(_to_digits(carry_chain), [8, 9, 9, 9, 0, 0, 0, 1])
        self.assertIsNone(add_two_numbers(None, None))


if __name__ == "__main__":
    unittest.main()

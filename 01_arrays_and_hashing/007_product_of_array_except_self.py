# [007_product_of_array_except_self] prefix-suffix product pass | invariant: O(n) time, O(1) extra space

import unittest


# --- public api -----------------------------------------------------------

def product_except_self(nums: list[int]) -> list[int]:
    """Return an array where each element is the product of all other elements."""
    count = len(nums)
    products = [1] * count

    prefix_prod = 1
    for idx in range(count):
        products[idx] = prefix_prod
        prefix_prod *= nums[idx]

    suffix_prod = 1
    for idx in range(count - 1, -1, -1):
        products[idx] *= suffix_prod
        suffix_prod *= nums[idx]

    return products


# --- tests ----------------------------------------------------------------

class TestProductExceptSelf(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])

    def test_edges(self) -> None:
        self.assertEqual(product_except_self([2, 3]), [3, 2])


if __name__ == "__main__":
    unittest.main()

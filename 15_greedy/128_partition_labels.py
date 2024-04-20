# [128_partition_labels] last-occurrence interval sweep | invariant: O(n) time, O(1) alphabet space

import unittest


# --- public api -----------------------------------------------------------

def partition_labels(s: str) -> list[int]:
    """Return sizes of maximum non-overlapping segments where each letter stays in one part."""
    if not s:
        return []

    last_index = {ch: idx for idx, ch in enumerate(s)}
    sizes: list[int] = []
    part_start = 0
    part_end = 0

    for idx, ch in enumerate(s):
        last_seen = last_index[ch]
        if last_seen > part_end:
            part_end = last_seen
        if idx == part_end:
            sizes.append(part_end - part_start + 1)
            part_start = idx + 1

    return sizes


# --- tests ----------------------------------------------------------------

class TestPartitionLabels(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(partition_labels("ababcbacadefegdehijhklij"), [9, 7, 8])
        self.assertEqual(partition_labels("eccbbbbdec"), [10])

    def test_edges(self) -> None:
        self.assertEqual(partition_labels(""), [])
        self.assertEqual(partition_labels("a"), [1])
        self.assertEqual(partition_labels("abcd"), [1, 1, 1, 1])
        self.assertEqual(partition_labels("abca"), [4])


if __name__ == "__main__":
    unittest.main()

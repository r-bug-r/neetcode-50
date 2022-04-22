# [006_encode_and_decode_strings] length-prefixed string codec | invariant: O(n) total chars

import unittest


# --- public api -----------------------------------------------------------

def encode(strs: list[str]) -> str:
    """Encode a list of strings into a single length-prefixed string."""
    # perf: list join avoids quadratic string concatenation
    return "".join(f"{len(word)}#{word}" for word in strs)


def decode(encoded: str) -> list[str]:
    """Decode a length-prefixed string back into its original list."""
    decoded: list[str] = []
    cursor = 0

    while cursor < len(encoded):
        delim_idx = encoded.find("#", cursor)
        word_len = int(encoded[cursor:delim_idx])
        word_start = delim_idx + 1
        word_end = word_start + word_len
        decoded.append(encoded[word_start:word_end])
        cursor = word_end

    return decoded


# --- tests ----------------------------------------------------------------

class TestEncodeDecodeStrings(unittest.TestCase):
    def test_examples(self) -> None:
        sample = ["lint", "code", "love", "you"]
        self.assertEqual(decode(encode(sample)), sample)

    def test_edges(self) -> None:
        self.assertEqual(decode(encode([])), [])
        self.assertEqual(decode(encode(["", "a#b", "12#34"])), ["", "a#b", "12#34"])


if __name__ == "__main__":
    unittest.main()

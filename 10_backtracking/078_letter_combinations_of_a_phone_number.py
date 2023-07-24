# [078_letter_combinations_of_a_phone_number] keypad cartesian DFS | scope: digits 2-9

from __future__ import annotations

import unittest


# --- tables ---------------------------------------------------------------

DIGIT_LETTERS: dict[str, str] = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


# --- public api -----------------------------------------------------------

def letter_combinations(digits: str) -> list[str]:
    """Return all phone-keypad letter combinations for digits in '2'-'9'."""
    if not digits:
        return []
    combos: list[str] = []
    _expand_digits(0, digits, [], combos)
    return combos


# --- helpers --------------------------------------------------------------

def _expand_digits(
    pos: int,
    digits: str,
    chosen: list[str],
    combos: list[str],
) -> None:
    if pos == len(digits):
        combos.append("".join(chosen))
        return

    for letter in DIGIT_LETTERS[digits[pos]]:
        chosen.append(letter)
        _expand_digits(pos + 1, digits, chosen, combos)
        chosen.pop()


# --- tests ----------------------------------------------------------------

class TestLetterCombinations(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(
            letter_combinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )
        self.assertEqual(letter_combinations("2"), ["a", "b", "c"])

    def test_edges(self) -> None:
        self.assertEqual(letter_combinations(""), [])
        self.assertEqual(letter_combinations("9"), ["w", "x", "y", "z"])


if __name__ == "__main__":
    unittest.main()

from challenge_1 import cipher_text, shift_char, replace_char
from unittest import TestCase

class TestCipherText(TestCase):
    def setUp(self):
        self.N = {"A": "X", "C": "T", "E": "F", "$": "%"}
        self.test_ceasar = lambda x, y: cipher_text(x, y)
        self.test_replace = lambda x: cipher_text(x, self.N)

    def test_success_caesar(self):
        self.assertEqual("FgHiJ", self.test_ceasar("AbCdE", 5))
        self.assertEqual("aBcDe", self.test_ceasar("vWxYz", 5))
        self.assertEqual("@aBcD", self.test_ceasar("@bCdE", 25))
        self.assertEqual("ZaBcD", self.test_ceasar("AbCdE", -1))
        self.assertEqual("VwXyZ", self.test_ceasar("AbCdE", -5))
        self.assertEqual("@wXyZ", self.test_ceasar("@bCdE", -5))
        self.assertEqual("@cDeF", self.test_ceasar("@bCdE", -25))

    def test_success_replacement(self):
        self.assertEqual("XbTdF", self.test_replace("AbCdE"))
        self.assertEqual("XbT$F", self.test_replace("AbC$E"))
    
    def test_error_n_range(self):
        with self.assertRaises(ValueError) as exception_context:
            self.test_ceasar("AbCdE", 26)
            self.assertEqual(
                str(exception_context.exception),
                "N should be in the range of -25 to 25.",
            )
        with self.assertRaises(ValueError) as exception_context:
            self.test_ceasar("AbCdE", -27)
            self.assertEqual(
                str(exception_context.exception),
                "N should be in the range of -25 to 25.",
            )
    
    def test_error_n_data_type(self):
        with self.assertRaises(ValueError) as exception_context:
            self.test_ceasar("AbCdE", 26.00)
            self.assertEqual(
                str(exception_context.exception),
                "Incorrect Input Data Type for N.",
            )


class TestShiftChar(TestCase):
    def test_success_alpha_left_lower(self):
        self.assertEqual("u", shift_char("z", -5))
        self.assertEqual("z", shift_char("a", -1))
        self.assertEqual("v", shift_char("a", -5))

    def test_success_alpha_left_upper(self):
        self.assertEqual("U", shift_char("Z", -5))
        self.assertEqual("Z", shift_char("A", -1))
        self.assertEqual("V", shift_char("A", -5))

    def test_success_alpha_right_lower(self):
        self.assertEqual("e", shift_char("a", 4))
        self.assertEqual("a", shift_char("z", 1))
        self.assertEqual("d", shift_char("z", 4))

    def test_success_alpha_right_upper(self):
        self.assertEqual("E", shift_char("A", 4))
        self.assertEqual("A", shift_char("Z", 1))
        self.assertEqual("D", shift_char("Z", 4))

    def test_success_non_alpha(self):
        self.assertEqual("%", shift_char("%", 5))
        self.assertEqual("%", shift_char("%", 25))
        self.assertEqual("$", shift_char("$", -2))
        self.assertEqual("$", shift_char("$", -25))


class TestReplaceChar(TestCase):
    def setUp(self):
        self.N = {"A": "X", "x": "T", "E": "F", "$": "%"}
        self.test_func = lambda x: replace_char(x, self.N)

    def test_success_alpha_in_n(self):
        self.assertEqual("X", self.test_func("A"))
        self.assertEqual("T", self.test_func("x"))

    def test_success_alpha_not_in_n(self):
        self.assertEqual("B", self.test_func("B"))
        self.assertEqual("v", self.test_func("v"))

    def test_success_non_alpha(self):
        self.assertEqual("$", self.test_func("$"))
        self.assertEqual(" ", self.test_func(" "))

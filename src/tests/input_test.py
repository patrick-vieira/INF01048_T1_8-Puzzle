from unittest import TestCase

from input import Input


class InputTest(TestCase):
    input_invalid_size_a = "23456789_"
    input_invalid_size_b = "1123456789_"

    input_invalid_character_a = "123456789*"
    input_invalid_character_b = "*23456789_"

    input_invalid_duplicated_value_a = "223456789_"
    input_invalid_duplicated_value_b = "_23456789_"

    def test_valid_input(self):
        input_a = Input("12345678_")
        input_b = Input("_12345678")
        input_c = Input("87654321_")
        input_d = Input("1564_2378")

        self.assertTrue(input_a._initial_state_is_valid)
        self.assertTrue(input_b._initial_state_is_valid)
        self.assertTrue(input_c._initial_state_is_valid)
        self.assertTrue(input_d._initial_state_is_valid)

    def test_input_sizes(self):
        input_invalid_size_a = Input("2345678_")
        input_invalid_size_b = Input("112345678_")

        self.assertFalse(input_invalid_size_a._initial_state_is_valid)
        self.assertFalse(input_invalid_size_b._initial_state_is_valid)

    def test_invalid_input_characters(self):
        input_invalid_character_a = Input("12345678*")
        input_invalid_character_b = Input("*2345678_")

        self.assertFalse(input_invalid_character_a._initial_state_is_valid)
        self.assertFalse(input_invalid_character_b._initial_state_is_valid)

    def test_duplicated_input_characters(self):
        input_invalid_duplicated_value_a = Input("22345678_")
        input_invalid_duplicated_value_b = Input("_2345678_")

        self.assertFalse(input_invalid_duplicated_value_a._initial_state_is_valid)
        self.assertFalse(input_invalid_duplicated_value_b._initial_state_is_valid)

    def test_input_out_of_range(self):
        input_lower = Input("01234567_")
        input_higher = Input("23456789_")

        self.assertFalse(input_lower._initial_state_is_valid)
        self.assertFalse(input_higher._initial_state_is_valid)


from unittest import TestCase

# # # # #
# 0 1 2 #
# 3 4 5 #
# 6 7 8 #
# # # # #
from manhattan_distance import get_moves_for_orientation, get_manhattan_distance
from node import Node

lines_orientation = {
    1: [0, 1, 2],
    2: [3, 4, 5],
    3: [6, 7, 8]
}

columns_orientation = {
    1: [0, 3, 6],
    2: [1, 4, 7],
    3: [2, 5, 8]
}


class Test(TestCase):
    def test_moves_to_correct_line(self):
        piece_symbol_value = 1
        piece_location = 8  # ultima linha

        moves_to_correct_line = get_moves_for_orientation(piece_symbol_value, piece_location, lines_orientation)

        expected_moves_to_correct_line = 2

        self.assertEqual(expected_moves_to_correct_line, moves_to_correct_line)

    def test_moves_to_correct_column(self):
        piece_symbol_value = 1
        piece_location = 8  # ultima coluna

        moves_to_correct_column = get_moves_for_orientation(piece_symbol_value, piece_location, columns_orientation)

        expected_moves_to_correct_column = 2

        self.assertEqual(expected_moves_to_correct_column, moves_to_correct_column)

    def test_manhattan_distance_all_in_place(self):
        node = Node(
            None,
            "12345678_",
            0,
            None
        )

        manhattan_distance = get_manhattan_distance(node)

        expected_manhattan_distance = 0

        self.assertEqual(expected_manhattan_distance, manhattan_distance)

    def test_manhattan_distance_one_off(self):
        node = Node(
            None,
            "1234567_8",
            0,
            None
        )

        manhattan_distance = get_manhattan_distance(node)

        expected_manhattan_distance = 1

        self.assertEqual(expected_manhattan_distance, manhattan_distance)

    def test_manhattan_distance_example(self):
        node = Node(
            None,
            "13246875_",
            0,
            None
        )

        manhattan_distance = get_manhattan_distance(node)

        expected_manhattan_distance = 6

        self.assertEqual(expected_manhattan_distance, manhattan_distance)

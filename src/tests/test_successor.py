from unittest import TestCase

from sucessor import get_successor_states


class SuccessorFunctionTest(TestCase):
    def setUp(self):
        self.left = "esquerda"
        self.right = "direita"
        self.up = "cima"
        self.down = "abaixo"

    # # # # #
    # 3 2 1 #
    # 5 _ 4 #
    # 8 6 7 #
    # # # # #
    def test_successor_space_center(self):
        initial_node = "3215_4867"

        expected_node_list = {
            self.left: "321_54867",
            self.right: "32154_867",
            self.up: "3_1524867",
            self.down: "3215648_7"
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 3 2 1 #
    # _ 5 4 #
    # 8 6 7 #
    # # # # #
    def test_successor_space_center_left(self):
        initial_node = "321_54867"

        expected_node_list = {
            self.right: "3215_4867",
            self.up: "_21354867",
            self.down: "321854_67"
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 3 2 1 #
    # 5 4 _ #
    # 8 6 7 #
    # # # # #
    def test_successor_space_center_right(self):
        initial_node = "32154_867"

        expected_node_list = {
            self.left: "3215_4867",
            self.up: "32_541867",
            self.down: "32154786_"
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 3 _ 1 #
    # 5 2 4 #
    # 8 6 7 #
    # # # # #
    def test_successor_space_center_up(self):
        initial_node = "3_1524867"

        expected_node_list = {
            self.right: "31_524867",
            self.left: "_31524867",
            self.down: "3215_4867"
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 3 2 1 #
    # 5 6 4 #
    # 8 _ 7 #
    # # # # #
    def test_successor_space_center_down(self):
        initial_node = "3215648_7"

        expected_node_list = {
            self.left: "321564_87",
            self.right: "32156487_",
            self.up: "3215_4867"
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # _ 3 1 #
    # 5 2 4 #
    # 8 6 7 #
    # # # # #
    def test_successor_space_upper_left_corner(self):
        initial_node = "_31524867"

        expected_node_list = {
            self.right: "3_1524867",
            self.down: "531_24867"
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 3 1 _ #
    # 5 2 4 #
    # 8 6 7 #
    # # # # #
    def test_successor_space_upper_right_corner(self):
        initial_node = "31_524867"

        expected_node_list = {
            self.left: "3_1524867",
            self.down: "31452_867"
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 5 3 1 #
    # 8 2 4 #
    # _ 6 7 #
    # # # # #
    def test_successor_space_lower_left_corner(self):
        initial_node = "531824_67"

        expected_node_list = {
            self.right: "5318246_7",
            self.up: "531_24867"
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 3 1 4 #
    # 5 2 7 #
    # 8 6 _ #
    # # # # #
    def test_successor_space_lower_right_corner(self):
        initial_node = "31452786_"

        expected_node_list = {
            self.left: "3145278_6",
            self.up: "31452_867"
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)
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
        initial_state = 321594867

        expected_state_list = {
            self.left: 321954867,
            self.right: 321549867,
            self.up: 391524867,
            self.down: 321564897
        }

        successors_dict = get_successor_states(initial_state)

        self.assertDictEqual(expected_state_list, successors_dict)

    # # # # #
    # 3 2 1 #
    # _ 5 4 #
    # 8 6 7 #
    # # # # #
    def test_successor_space_center_left(self):
        initial_node = 321954867

        expected_node_list = {
            self.right: 321594867,
            self.up: 921354867,
            self.down: 321854967
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 3 2 1 #
    # 5 4 _ #
    # 8 6 7 #
    # # # # #
    def test_successor_space_center_right(self):
        initial_node = 321549867

        expected_node_list = {
            self.left: 321594867,
            self.up: 329541867,
            self.down: 321547869
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 3 _ 1 #
    # 5 2 4 #
    # 8 6 7 #
    # # # # #
    def test_successor_space_center_up(self):
        initial_node = 391524867

        expected_node_list = {
            self.right: 319524867,
            self.left: 931524867,
            self.down: 321594867
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 3 2 1 #
    # 5 6 4 #
    # 8 _ 7 #
    # # # # #
    def test_successor_space_center_down(self):
        initial_node = 321564897

        expected_node_list = {
            self.left: 321564987,
            self.right: 321564879,
            self.up: 321594867
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # _ 3 1 #
    # 5 2 4 #
    # 8 6 7 #
    # # # # #
    def test_successor_space_upper_left_corner(self):
        initial_node = 931524867

        expected_node_list = {
            self.right: 391524867,
            self.down: 531924867
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 3 1 _ #
    # 5 2 4 #
    # 8 6 7 #
    # # # # #
    def test_successor_space_upper_right_corner(self):
        initial_node = 319524867

        expected_node_list = {
            self.left: 391524867,
            self.down: 314529867
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 5 3 1 #
    # 8 2 4 #
    # _ 6 7 #
    # # # # #
    def test_successor_space_lower_left_corner(self):
        initial_node = 531824967

        expected_node_list = {
            self.right: 531824697,
            self.up: 531924867
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)

    # # # # #
    # 3 1 4 #
    # 5 2 7 #
    # 8 6 _ #
    # # # # #
    def test_successor_space_lower_right_corner(self):
        initial_node = 314527869

        expected_node_list = {
            self.left: 314527896,
            self.up: 314529867
        }

        successors_dict = get_successor_states(initial_node)

        self.assertDictEqual(expected_node_list, successors_dict)
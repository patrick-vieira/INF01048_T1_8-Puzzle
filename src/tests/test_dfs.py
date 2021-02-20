from unittest import TestCase

from dfs import depth_first_search
from node import Node


class TestBreadthFirstSearch(TestCase):
    def test_root_is_objective(self):
        root_node = Node(
            None,
            "12345678_",
            0,
            None
        )

        final_node, monitor = depth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = []

        expected_expansions = 0

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_one_move_to_objective(self):
        root_node = Node(
            None,
            "1234567_8",
            0,
            None
        )

        final_node, monitor = depth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['acima', 'acima', 'direita', 'abaixo', 'abaixo', 'esquerda', 'acima', 'acima', 'direita',
                               'abaixo', 'abaixo', 'esquerda', 'acima', 'acima', 'direita', 'abaixo', 'abaixo',
                               'esquerda', 'acima', 'acima', 'direita', 'abaixo', 'abaixo', 'esquerda', 'acima',
                               'acima',
                               'direita', 'abaixo', 'abaixo']

        expected_expansions = 29

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_two_moves_to_objective(self):
        root_node = Node(
            None,
            "123456_78",
            0,
            None
        )

        final_node, monitor = depth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves_len = 106330
        expected_expansions = 115907

        self.assertEqual(expected_path_moves_len, len(final_node_moves), "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_real(self):
        root_node = Node(
            None,
            "3456_8172",
            0,
            None
        )

        final_node, monitor = depth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves_len = 43786
        expected_expansions = 45136

        self.assertEqual(expected_path_moves_len, len(final_node_moves), "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_node_counter(self):
        root_node = Node(
            None,
            "2_3541687",
            0,
            None
        )

        final_node, monitor = depth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves_len = 96453
        expected_expansions = 103195

        self.assertEqual(expected_path_moves_len, len(final_node_moves), "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_unsolvable(self):
        root_node = Node(
            None,
            "2_5341687",
            0,
            None
        )

        final_node, monitor = depth_first_search(root_node)

        n = 9
        fact = 1

        for i in range(1, n + 1):
            fact = fact * i

        max_expansions = fact / 2

        self.assertFalse(final_node)
        self.assertEqual(max_expansions, monitor.expansions, "incorrect expected expansions")

    def test_moves_count(self):
        root_node = Node(
            None,
            "185432_67",
            0,
            None
        )

        final_node, monitor = depth_first_search(root_node)

        final_node_moves = final_node.get_path_moves()

        expected_moves_count = 11032

        self.assertEqual(expected_moves_count, len(final_node_moves), "incorrect expected moves count")

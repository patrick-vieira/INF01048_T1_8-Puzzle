from unittest import TestCase

from bfs import breadth_first_search
from node import Node


class TestBreadthFirstSearch(TestCase):
    def test_root_is_objective(self):
        root_node = Node(
            "12345678_",
            0,
            0,
            None
        )

        final_node, monitor = breadth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = []

        expected_expansions = 0

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_one_move_to_objective(self):
        root_node = Node(
            "1234567_8",
            None,
            0,
            None
        )

        final_node, monitor = breadth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['direita']

        expected_expansions = 2

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_two_moves_to_objective(self):
        root_node = Node(
            "123456_78",
            None,
            0,
            None
        )

        final_node, monitor = breadth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['direita', 'direita']

        expected_expansions = 3

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_real(self):
        root_node = Node(
            "3456_8172",
            None,
            0,
            None
        )

        final_node, monitor = breadth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['esquerda', 'abaixo', 'direita', 'direita', 'cima', 'esquerda', 'cima', 'esquerda',
                               'abaixo', 'direita', 'abaixo', 'direita', 'cima', 'cima', 'esquerda', 'abaixo',
                               'direita', 'abaixo']

        expected_expansions = 23313

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_node_counter(self):
        root_node = Node(
            "2_3541687",
            None,
            0,
            None
        )

        final_node, monitor = breadth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['esquerda', 'abaixo', 'direita', 'direita', 'cima', 'esquerda', 'abaixo', 'abaixo',
                               'esquerda', 'cima', 'cima', 'direita', 'direita', 'abaixo', 'esquerda', 'abaixo',
                               'direita', 'cima', 'esquerda', 'esquerda', 'abaixo', 'direita', 'direita']

        expected_expansions = 100002

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

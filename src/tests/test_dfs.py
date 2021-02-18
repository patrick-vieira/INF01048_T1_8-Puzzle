from unittest import TestCase

from dfs import depth_first_search
from monitor import Monitor
from node import Node


class TestBreadthFirstSearch(TestCase):
    def test_root_is_objective(self):
        root_node = Node(
            "12345678_",
            None,
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
            "1234567_8",
            None,
            0,
            None
        )

        monitor2 = Monitor(None, None)
        monitor2.start()
        final_node, monitor = depth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        monitor2.finish()
        expected_path_moves = ['acima', 'acima', 'direita', 'abaixo', 'abaixo', 'esquerda', 'acima', 'acima', 'direita',
                               'abaixo', 'abaixo', 'esquerda', 'acima', 'acima', 'direita', 'abaixo', 'abaixo',
                               'esquerda', 'acima', 'acima', 'direita', 'abaixo', 'abaixo', 'esquerda', 'acima', 'acima',
                               'direita', 'abaixo', 'abaixo']

        expected_expansions = 29

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_two_moves_to_objective(self): # memoria insuficiente
        root_node = Node(
            "123456_78",
            None,
            0,
            None
        )

        final_node, monitor = depth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves_len = 106330
        expected_expansions = 115907

        self.assertEqual(expected_path_moves_len, len(final_node_moves), "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_real(self): # memoria insuficiente
        root_node = Node(
            "3456_8172",
            None,
            0,
            None
        )

        final_node, monitor = depth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves_len = 43786
        expected_expansions = 45136

        self.assertEqual(expected_path_moves_len, len(final_node_moves), "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_node_counter(self): # memoria insuficiente
        root_node = Node(
            "2_3541687",
            None,
            0,
            None
        )

        final_node, monitor = depth_first_search(root_node)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves_len = 96453
        expected_expansions = 103195

        self.assertEqual(expected_path_moves_len, len(final_node_moves), "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

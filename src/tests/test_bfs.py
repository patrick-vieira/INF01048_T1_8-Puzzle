from unittest import TestCase

from bfs import breadth_first_search
from node import Node


class TestBreadthFirstSearch(TestCase):
    def test_root_is_objective(self):
        root_node = Node(  # <-- Estado Inicial:
            "12345678_",  # <-- a) State
            None,  # <-- b) Action
            0,  # <-- c) Cost
            None  # <-- d) Predecessor
        )

        final_node_moves = breadth_first_search(root_node).get_path_moves()
        expected_path_moves = []

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")

    def test_one_move_to_objective(self):
        root_node = Node(  # <-- Estado Inicial:
            "1234567_8",  # <-- a) State
            None,  # <-- b) Action
            0,  # <-- c) Cost
            None  # <-- d) Predecessor
        )

        final_node_moves = breadth_first_search(root_node).get_path_moves()
        expected_path_moves = ['direita']

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")

    def test_two_moves_to_objective(self):
        root_node = Node(  # <-- Estado Inicial:
            "123456_78",  # <-- a) State
            None,  # <-- b) Action
            0,  # <-- c) Cost
            None  # <-- d) Predecessor
        )

        final_node_moves = breadth_first_search(root_node).get_path_moves()
        expected_path_moves = ['direita', 'direita']

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")

    def test_real(self):
        root_node = Node(  # <-- Estado Inicial:
            "3456_8172",  # <-- a) State
            None,  # <-- b) Action
            0,  # <-- c) Cost
            None  # <-- d) Predecessor
        )

        final_node_moves = breadth_first_search(root_node).get_path_moves()
        expected_path_moves = ['esquerda', 'abaixo', 'direita', 'direita', 'cima', 'esquerda', 'cima', 'esquerda', 'abaixo', 'direita', 'abaixo', 'direita', 'cima', 'cima', 'esquerda', 'abaixo', 'direita', 'abaixo']

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")

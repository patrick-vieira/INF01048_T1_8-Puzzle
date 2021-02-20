from unittest import TestCase

from hamming_distance import get_hamming_distance
from heuristic_search import heuristic_search
from manhattan_distance import get_manhattan_distance
from node import Node


class HammingDistance(TestCase):
    def setUp(self) -> None:
        self.heuristic = get_hamming_distance

    def test_root_is_objective(self):
        root_node = Node(
            None,
            "12345678_",
            0,
            None
        )

        final_node, monitor = heuristic_search(root_node, self.heuristic)
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

        final_node, monitor = heuristic_search(root_node, self.heuristic)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['direita']

        expected_expansions = 1

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_two_moves_to_objective(self):
        root_node = Node(
            None,
            "123456_78",
            0,
            None
        )

        final_node, monitor = heuristic_search(root_node, self.heuristic)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['direita', 'direita']

        expected_expansions = 2

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_real(self):
        root_node = Node(
            None,
            "3456_8172",
            0,
            None
        )

        final_node, monitor = heuristic_search(root_node, self.heuristic)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['esquerda', 'abaixo', 'direita', 'acima', 'acima', 'esquerda', 'abaixo', 'direita',
                               'direita', 'abaixo', 'esquerda', 'acima', 'direita', 'acima', 'esquerda', 'abaixo',
                               'direita', 'abaixo']

        expected_expansions = 1411

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_node_counter(self):
        root_node = Node(
            None,
            "2_3541687",
            0,
            None
        )

        final_node, monitor = heuristic_search(root_node, self.heuristic)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['abaixo', 'abaixo', 'direita', 'acima', 'esquerda', 'abaixo', 'esquerda', 'acima',
                               'direita', 'abaixo', 'direita', 'acima', 'esquerda', 'abaixo', 'esquerda', 'acima',
                               'direita', 'acima', 'esquerda', 'abaixo', 'direita', 'abaixo', 'direita']

        expected_expansions = 12736

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_unsolvable(self):
        root_node = Node(
            None,
            "2_5341687",
            0,
            None
        )

        final_node, monitor = heuristic_search(root_node, self.heuristic)

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

        final_node, monitor = heuristic_search(root_node, self.heuristic)

        final_node_moves = final_node.get_path_moves()

        expected_moves_count = 20

        self.assertEqual(expected_moves_count, len(final_node_moves), "incorrect expected moves count")


class ManhattanDistance(TestCase):
    def setUp(self) -> None:
        self.heuristic = get_manhattan_distance

    def test_root_is_objective(self):
        root_node = Node(
            None,
            "12345678_",
            0,
            None
        )

        final_node, monitor = heuristic_search(root_node, self.heuristic)
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

        final_node, monitor = heuristic_search(root_node, self.heuristic)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['direita']

        expected_expansions = 1

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_two_moves_to_objective(self):
        root_node = Node(
            None,
            "123456_78",
            0,
            None
        )

        final_node, monitor = heuristic_search(root_node, self.heuristic)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['direita', 'direita']

        expected_expansions = 2

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_real(self):
        root_node = Node(
            None,
            "3456_8172",
            0,
            None
        )

        final_node, monitor = heuristic_search(root_node, self.heuristic)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['esquerda', 'abaixo', 'direita', 'direita', 'acima', 'esquerda', 'acima', 'esquerda',
                               'abaixo', 'direita', 'abaixo', 'direita', 'acima', 'acima', 'esquerda', 'abaixo',
                               'direita', 'abaixo']

        expected_expansions = 67

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_node_counter(self):
        root_node = Node(
            None,
            "2_3541687",
            0,
            None
        )

        final_node, monitor = heuristic_search(root_node, self.heuristic)
        final_node_moves = final_node.get_path_moves()

        expected_path_moves = ['abaixo', 'abaixo', 'direita', 'acima', 'esquerda', 'abaixo', 'esquerda', 'acima',
                               'direita', 'abaixo', 'direita', 'acima', 'esquerda', 'abaixo', 'esquerda', 'acima',
                               'direita', 'acima', 'esquerda', 'abaixo', 'direita', 'abaixo', 'direita']

        expected_expansions = 1583

        self.assertEqual(expected_path_moves, final_node_moves, "path is incorrect")
        self.assertEqual(expected_expansions, monitor.expansions, "incorrect expected expansions")

    def test_unsolvable(self):
        root_node = Node(
            None,
            "2_5341687",
            0,
            None
        )

        final_node, monitor = heuristic_search(root_node, self.heuristic)

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

        final_node, monitor = heuristic_search(root_node, self.heuristic)

        final_node_moves = final_node.get_path_moves()

        expected_moves_count = 20

        self.assertEqual(expected_moves_count, len(final_node_moves), "incorrect expected moves count")

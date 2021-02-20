from unittest import TestCase

from hamming_distance import get_hamming_distance
from node import Node


class Test(TestCase):

    def test_get_hamming_distance_objective(self):
        node = Node(
            None,
            "12345678_",
            0,
            None
        )

        hamming_distance = get_hamming_distance(node)

        expected_hamming_distance = 0

        self.assertEqual(expected_hamming_distance, hamming_distance)

    def test_get_hamming_distance_all_out(self):
        node = Node(
            None,
            "_87645321",
            0,
            None
        )

        hamming_distance = get_hamming_distance(node)

        expected_hamming_distance = 9

        self.assertEqual(expected_hamming_distance, hamming_distance)

    def test_get_hamming_distance_partial(self):
        node = Node(
            None,
            "1234_5678",
            0,
            None
        )

        hamming_distance = get_hamming_distance(node)

        expected_hamming_distance = 5

        self.assertEqual(expected_hamming_distance, hamming_distance)

    def test_get_hamming_distance_two_off(self):
        node = Node(
            None,
            "_23456781",
            0,
            None
        )

        hamming_distance = get_hamming_distance(node)

        expected_hamming_distance = 2

        self.assertEqual(expected_hamming_distance, hamming_distance)


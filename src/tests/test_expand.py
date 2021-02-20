from unittest import TestCase

from expand import expand_node
from node import Node


class Test(TestCase):
    def test_expand_center_root_node(self):
        action = None
        state = "3215_4867"
        cost = 0
        predecessor = None

        node = Node(action, state, cost, predecessor)

        expanded_nodes = expand_node(node)

        expected_node_left = Node("esquerda", "321_54867", 1, node)
        expected_node_right = Node("direita", "32154_867", 1, node)
        expected_node_up = Node("acima", "3_1524867", 1, node)
        expected_node_down = Node("abaixo", "3215648_7", 1, node)

        self.assertEqual(len(expanded_nodes), 4)

        self.assertEqual(expected_node_left, expanded_nodes[0])
        self.assertEqual(expected_node_right, expanded_nodes[1])
        self.assertEqual(expected_node_up, expanded_nodes[2])
        self.assertEqual(expected_node_down, expanded_nodes[3])

    def test_expand_left_center_root_node(self):
        state = "321_54867"
        action = None
        cost = 120
        predecessor = None

        node = Node(action, state, cost, predecessor)

        expanded_nodes = expand_node(node)

        expected_node_right = Node("direita", "3215_4867", 121, node)
        expected_node_up = Node("acima", "_21354867", 121, node)
        expected_node_down = Node("abaixo", "321854_67", 121, node)

        self.assertEqual(len(expanded_nodes), 3)

        self.assertEqual(expected_node_right, expanded_nodes[0])
        self.assertEqual(expected_node_up, expanded_nodes[1])
        self.assertEqual(expected_node_down, expanded_nodes[2])

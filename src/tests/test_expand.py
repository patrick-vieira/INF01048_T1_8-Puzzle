from unittest import TestCase

from expand import expand_node
from node import Node
from recursion_limit import RecursionLimit


class Test(TestCase):
    def test_expand_center_root_node(self):
        state = 321594867
        action = None
        cost = 0
        predecessor = None

        node = Node(state, action, cost, predecessor)

        expanded_nodes = expand_node(node)

        self.assertEqual(len(expanded_nodes), 4)

    def test_expand_left_center_root_node(self):
        state = "321_54867"
        action = None
        cost = 0
        predecessor = None

        node = Node(state, action, cost, predecessor)

        expanded_nodes = expand_node(node)

        self.assertEqual(len(expanded_nodes), 3)

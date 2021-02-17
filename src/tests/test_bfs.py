from unittest import TestCase

from bfs import bfs
from node import Node


class Test(TestCase):
    def test_bfs_center_root_node(self):
        bfs_path = bfs("3215_4867")
        #self.assertEqual(len(expanded_nodes), 4)

    def test_bfs_left_center_root_node(self):
        bfs_path = bfs("321_54867")
        #self.assertEqual(len(expanded_nodes), 3)

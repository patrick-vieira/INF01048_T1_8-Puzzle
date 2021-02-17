from time import perf_counter_ns
from typing import Deque

from node import Node


class Monitor:
    def __init__(self, explored_nodes: set, frontier_nodes: Deque[Node]):
        self.start_time = None
        self.end_time = None
        self.expansions = 0

        self.X = explored_nodes
        self.F = frontier_nodes

    def start(self):
        self.start_time = perf_counter_ns()

    def finish(self):
        self.end_time = perf_counter_ns()

    def count(self):
        self.expansions += 1
        # print(self.expansions)

    def get_execution_time_in_nanoseconds(self):
        return self.end_time - self.start_time

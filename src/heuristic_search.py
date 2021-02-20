import heapq
from typing import Callable

import parameters
from expand import expand_node
from monitor import Monitor
from node import Node


def heuristic_search(root_node: Node, heuristic: Callable[[Node], int]) -> (Node, Monitor):
    X = set()
    F = []

    heapq.heapify(F)
    heapq.heappush(F, root_node)

    monitor = Monitor(X, F)
    monitor.start()

    while True:
        if not F:
            monitor.finish()
            return False, monitor
        # with MonitorPerformance():
        v = heapq.heappop(F)

        if v.state == parameters.objective_state:
            monitor.finish()
            return v, monitor
        elif v.state not in X: #rever isso, o estado pode estar aqui já, mas ter chego por outro caminho
            X.add(v.state)
            monitor.count()
            for node in expand_node(v):
                node.set_heuristic_cost(heuristic(node))
                heapq.heappush(F, node)

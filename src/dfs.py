from collections import deque
from typing import Deque

import parameters
from expand import expand_node
from monitor import Monitor
from node import Node


def depth_first_search(root_node: Node) -> (Node, Monitor):
    X = set()  # <-- Explorados
    F: Deque[Node] = deque()  # <-- Fronteira - deque eh uma implementacao para fila
    F.append(root_node)

    monitor = Monitor(X, F)
    monitor.start()

    while True:
        if not F:  # <-- Se a fronteira fica vazia, nao existe caminho
            monitor.finish()
            return False, monitor
        v = F.pop()  # <-- Retira um nodo v da fronteira
        if v.state == parameters.objective_state:  # <-- Chegou no estado final?
            monitor.finish()
            return v, monitor  # <-- Entao retorna o ultimo nó
        elif v.state not in X:  # <-- Adiciona v aos explorados caso ainda nao esteja
            X.add(v.state)
            monitor.count()
            for node in expand_node(v):  # <-- Adiciona os vizinhos de V a fronteira
                F.append(node)

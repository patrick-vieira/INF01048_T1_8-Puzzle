from collections import deque
from typing import Deque

import parameters
from expand import expand_node
from node import Node


def breadth_first_search(root_node: Node) -> Node:
    X = set()  # <-- Explorados
    F: Deque[Node] = deque()  # <-- Fronteira - deque eh uma implementacao para fila
    F.append(root_node)

    while True:
        if not F:  # <-- Se a fronteira fica vazia, nao existe caminho
            return False
        v = F.popleft()  # <-- Retira um nodo v da fronteira
        if v.state == parameters.objective_state:  # <-- Chegou no estado final?
            return v  # <-- Entao retorna o ultimo nó
        elif v not in X:  # <-- Adiciona v aos explorados caso ainda nao esteja
            X.add(v)
            for node in expand_node(v):  # <-- Adiciona os vizinhos de V a fronteira
                F.append(node)

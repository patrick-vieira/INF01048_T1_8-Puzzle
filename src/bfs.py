import logging
from node import Node
from collections import deque

def bfs(initial_state):
    X = list()  # <-- Explorados
    F = deque() # <-- Fronteira - deque eh uma implementacao para fila
    F.append(
        Node(                           # <-- Estado Inicial:
            initial_state,    # <-- a) State
            None,                       # <-- b) Action
            0,                          # <-- c) Cost
            None                        # <-- d) Predecessor
        )
    )
    while True:
        if not F:           # <-- Se a fronteira fica vazia, nao existe caminho
            return False
        v = F.popleft()     # <-- Retira um nodo v da fronteira
        if v.state == "12345678_":  # <-- Chegou no estado final?
            return v.get_path(initial_state)    # <-- Entao retorna o caminho ate ele
        elif v not in X:    # <-- Adiciona v aos explorados caso ainda nao esteja
            X.append(v)
        for node in expand_node(v): # <-- Adiciona os vizinhos de V a fronteira
            F.append(node)

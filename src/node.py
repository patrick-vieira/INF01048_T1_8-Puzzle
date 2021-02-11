class Node:
    def __init__(self, state, action, cost, predecessor):
        self.state = state
        self.action = action
        self.cost = cost
        self.predecessor = predecessor
        self.successors: [] = []

    def set_successors(self, successor_nodes: []):
        self.successors = successor_nodes


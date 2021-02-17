class Node:
    def __init__(self, state, action, cost, predecessor):
        self.state = state
        self.action = action
        self.cost = cost
        self.predecessor: Node = predecessor
        self.predecessors: [Node] = list()
        self.successors: [Node] = []

        self.__set_predecessor(predecessor)

    def set_successors(self, successor_nodes: []):
        self.successors = successor_nodes

    def get_path_moves(self):
        moves = []
        for node in self.get_path_nodes():
            moves.append(node.action)

        moves.pop(0)  # remove ação que foi executada para chegar ao nó inicial que é nula.
        return moves

    def get_path_nodes(self):
        path = [self]
        self.__get_path(path)
        path.reverse()
        return path

    def __get_path(self, curr_path: list) -> list:
        if self.predecessor is not None:  # <-- Se ha um antecessor
            curr_path.append(self.predecessor)  # <-- Adicionamos ele no caminho
            return self.predecessor.__get_path(curr_path)
        else:  # <-- se não tem predecessor é o início
            return curr_path

    def __set_predecessor(self, father_node):
        if father_node:
            self.predecessors = father_node.predecessors.copy()
            self.predecessors.append(father_node)

    def __str__(self):
        to_string = "(" + str(self.action) \
                    + "," + str(self.state) \
                    + "," + str(self.cost)

        if self.predecessor:
            to_string += "," + str(self.predecessor.state)
        else:
            to_string += "," + str(self.predecessor)

        return to_string + ")"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Node):
            # um nó é igual ao outro quando o estado e o custo é o mesmo "e a ação também?"
            return self.state == other.state \
                   and self.cost == other.cost

        return NotImplemented

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(self.state) ^ hash(self.action) ^ hash(self.cost)

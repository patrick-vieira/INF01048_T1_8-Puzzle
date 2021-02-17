class Node:
    def __init__(self, state, action, cost, predecessor):
        self.state = state
        self.action = action
        self.cost = cost
        self.predecessor = predecessor
        self.successors: [] = []

    def set_successors(self, successor_nodes: []):
        self.successors = successor_nodes

    def get_path(self, start_state, curr_path: list()):
    	if self.predecessor != None:					# <-- Se ha um antecessor
    		curr_path.append(self.predecessor)			# <-- Adicionamos ele no caminho
    		if self.predecessor.state == start_state	# <-- Se ele eh o estado inicial, sucesso
    			return curr_path
    		else										# <-- Caso contrario, chama recursao
    			return self.predecessor.get_path(start_state, curr_path)
    	else											# <-- Caso de erro, temos um node sem pai :(
    		return curr_path


import parameters
from node import Node
from sucessor import get_successor_states


def expand_node(node: Node) -> [Node]:
    successor_states = get_successor_states(node.state) #pega todos os movimentos validos para o estado do nó

    successor_nodes = [] # lista de nós que podem ser visitados partindo da entrada da função


    for action in successor_states: #para cada um dos movimentos validos
        successor_state = successor_states[action] #pega o estado que vai ser o atual se mover para aquele lado
        successor_nodes.append(Node(successor_state, action, parameters.step_cost, node)) #cria um novo nó com o novo estado, e adiciona o nó original como pai

    node.set_successors(successor_nodes) #adiciona ao nó da entrada os possiveis nós para cada movimento

    return successor_nodes #retorna a lista com todos os nós que podemos visitar partindo do nó de entrada

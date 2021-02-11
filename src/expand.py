import parameters
from node import Node
from sucessor import get_successor_states


def expand_node(node: Node) -> [Node]:
    successor_states = get_successor_states(node.state)

    successor_nodes = []

    for action in successor_states:
        successor_state = successor_states[action]
        successor_nodes.append(Node(successor_state, action, parameters.step_cost, node))

    node.set_successors(successor_nodes)

    return successor_nodes

import parameters
from node import Node


def get_hamming_distance(node: Node) -> int:  # peças fora do lugar
    node_state = list(node.state)
    expected_state = list(parameters.objective_state)

    hamming_distance = 0

    for position in range(len(expected_state)):
        if not node_state[position] == expected_state[position]:
            hamming_distance += 1

    return hamming_distance

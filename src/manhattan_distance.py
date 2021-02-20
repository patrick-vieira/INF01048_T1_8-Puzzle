import parameters
from node import Node


# # # # #
# 0 1 2 #
# 3 4 5 #
# 6 7 8 #
# # # # #
def get_moves_for_orientation(piece_value: int, piece_location: int, orientation: dict):
    current = False
    expected = False

    for index in orientation:
        if piece_location in orientation[index]:
            current = index

        if piece_value-1 in orientation[index]:
            expected = index

    vertical_moves = current - expected

    if vertical_moves < 0:
        vertical_moves = vertical_moves * -1

    return vertical_moves


def get_manhattan_distance(node: Node) -> int:
    node_state = list(node.state)
    expected_state = list(parameters.objective_state)

    manhattan_distance = 0

    for position in range(len(expected_state)): #faz o loop para cada uma das posições do estado final
        piece_symbol = node_state[position]

        if ord(piece_symbol) == parameters.blank_space_unicode:  # verifica se a peça é o espaço se sim ignora
            continue

        expected_piece_symbol_location = int(piece_symbol) - 1  # o local da peça no array

        if not expected_piece_symbol_location == position:  # se a peça não esta no local esperado calcula a distancia
            moves_to_correct_line = get_moves_for_orientation(int(piece_symbol), position, parameters.lines_orientation)
            moves_to_correct_column = get_moves_for_orientation(int(piece_symbol), position, parameters.columns_orientation)

            manhattan_distance += moves_to_correct_line + moves_to_correct_column

    return manhattan_distance

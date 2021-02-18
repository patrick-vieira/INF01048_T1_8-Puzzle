import logging

import parameters


def __is_on_border_limits(state, border_limits):
    current_space_location = __get_current_space_location(state)

    for left_border_limit in border_limits:
        if current_space_location == left_border_limit:
            return True

    return False


def __get_current_space_location(current_state):
    for idx, item in enumerate(current_state):
        if ord(item) == parameters.blank_space_unicode:
            return idx


def __get_next_state_from_move_direction(state, move_direction):
    current_space_location = __get_current_space_location(state)
    next_space_location = current_space_location + parameters.actions_movement_offset_map[move_direction]

    moved_piece_symbol = state[next_space_location]

    state_list = list(state)
    logging.debug(state_list)

    state_list[current_space_location] = moved_piece_symbol
    state_list[next_space_location] = parameters.blank_space

    new_state = "".join(state_list)
    logging.debug(new_state)

    return new_state


def transform_state_to_string(state: int) -> str:
    return str(state).replace("9", "_")


def transform_state_to_integer(state: str) -> int:
    return int(state.replace("_", "9"))


def get_successor_states(current_state: int) -> dict:  # recebe o estado como um inteiro 123456780, 0 é o representa "_"
    successor_states = {}

    state_as_string = transform_state_to_string(current_state)

    for action in parameters.actions_limits:  # loop para cada uma das ações possiveis no jogo [<>^v]
        action_limits = parameters.actions_limits[
            action]  # cada ação é limitada pelas bordas, se estiver na posição 0,1 ou 2 não pode se mover para cima

        if not __is_on_border_limits(state_as_string, action_limits):  # verifica se pode mover naquela direção
            move_to = action
            successor_states[move_to] = __get_next_state_from_move_direction(state_as_string, move_to)

    for action in successor_states:
        successor_states[action] = transform_state_to_integer(successor_states[action])

    return successor_states

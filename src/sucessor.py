import logging

import parameters


def __is_on_border_limits(state, border_limits):
    current_space_location = __get_current_space_location(state)

    for border_limit in border_limits:
        if current_space_location == border_limit:
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
    # logging.debug(state_list) #logar consome muito tempo

    state_list[current_space_location] = moved_piece_symbol
    state_list[next_space_location] = parameters.blank_space

    new_state = "".join(state_list)
    # logging.debug(new_state) #logar consome muito tempo

    return new_state


def get_successor_states(current_state) -> dict:
    successor_states = {}

    for action in parameters.actions_limits:
        action_limits = parameters.actions_limits[action]

        if not __is_on_border_limits(current_state, action_limits):
            move_to = action
            successor_states[move_to] = __get_next_state_from_move_direction(current_state, move_to)

    return successor_states

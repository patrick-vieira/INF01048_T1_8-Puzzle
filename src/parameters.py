blank_space = "_"
blank_space_unicode = ord(blank_space)
blank_space_numeric_replace = "0"

move_left = "esquerda"
move_right = "direita"
move_up = "cima"
move_down = "abaixo"

step_cost = 1

actions_limits = {
    move_left: [0, 3, 6],
    move_right: [2, 5, 8],
    move_up: [0, 1, 2],
    move_down: [6, 7, 8],
}

actions_movement_offset_map = {
    move_left: -1,
    move_right: 1,
    move_down: 3,
    move_up: -3
}

input_size = 9
allowed_characters = ['_', '1', '2', '3', '4', '5', '6', '7', '8']
objective_state = 123456789

class Input:

    def __init__(self, initial_state):
        self.__blank_space_unicode = ord('_')
        self.__lower_value = 1
        self.__higher_value = 8
        self.initial_state = initial_state
        self._initial_state_is_valid = self.__validate_initial_state()

    def __validate_initial_state(self):
        if self.__is_valid_len() and (not self.__has_duplicated_values()) and (not self.__has_invalid_characters()):
            self._initial_state_validated = True
            return self._initial_state_validated
        else:
            print("invalid input state")
            self._initial_state_validated = False
            return self._initial_state_validated

    def __has_duplicated_values(self):
        state_set = set()
        for value in self.initial_state:
            state_set.add(value)

        has_duplicated_values = len(state_set) < len(self.initial_state)
        if has_duplicated_values:
            print("Invalid initial state. Reason: has duplicated entries")
            return has_duplicated_values

    def __is_valid_len(self):
        expected_size = self.__higher_value - self.__lower_value + 2
        initial_state_size = len(self.initial_state)
        is_valid = initial_state_size == expected_size

        if not is_valid:
            print("Invalid initial state. Reason: invalid size.\nExpected: "
                  + str(expected_size) + "\nActual: " + str(initial_state_size))

        return is_valid

    def __has_invalid_characters(self):
        for value in self.initial_state:
            is_blank_space = (ord(value) == self.__blank_space_unicode)
            is_lower_valid = value.isnumeric() and (int(value) >= self.__lower_value)
            is_higher_valid = value.isnumeric() and (int(value) <= self.__higher_value)

            is_valid = is_blank_space or is_lower_valid and is_higher_valid
            if not is_valid:
                print("Invalid initial state. Reason: Invalid characters")
                return not is_valid






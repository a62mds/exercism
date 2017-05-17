def binary_search(sorted_array, value):
    def _rec_binary_search(enumerated_array):
        if not enumerated_array:
            raise ValueError('Value {} not found in array'.format(value))
        else:
            middle_index = len(enumerated_array) // 2
            middle_value = enumerated_array[middle_index]
            if value == middle_value[1]:
                return middle_value[0]
            elif value < middle_value[1]:
                return _rec_binary_search(enumerated_array[:middle_index])
            elif value > middle_value[1]:
                return _rec_binary_search(enumerated_array[middle_index+1:])
    return _rec_binary_search(list(enumerate(sorted_array)))

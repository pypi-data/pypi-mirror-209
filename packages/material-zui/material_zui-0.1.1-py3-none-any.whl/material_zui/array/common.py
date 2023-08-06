def is_last_index(array: list, index: int) -> bool:
    return index == len(array) - 1


def is_not_last_index(array: list, index: int) -> bool:
    return not is_last_index(array, index)

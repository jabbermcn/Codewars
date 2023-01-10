def check_sequence(lst: list) -> int:
    if sorted(set(lst)) == lst:
        return 1
    if sorted(set(lst), reverse=True) == lst:
        return -1
    else:
        return 0

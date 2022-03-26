def check_args(data: dict, *args) -> bool:
    for i in args:
        if i not in data:
            return False

    return True
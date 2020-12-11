from .assorted import C


def pascal(index):
    return [C(index, base) for base in range(index + 1)]

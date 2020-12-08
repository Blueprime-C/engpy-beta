from .primary import Num


def pascal(index):
    return [Num(index, base).C() for base in range(index + 1)]

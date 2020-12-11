from math import factorial
from engpy.misc.assist import getter
from .primary import Num
from .xtension import EGCD


def P(n, r):
    return int(factorial(n) / factorial(n - r))


def C(n, r):
    return int(P(n, r) / factorial(r))


def GCD(*factors):
    for factor in factors:
        if getter(factor, 'name') == 'Expr':
            return EGCD(*factors)
    return Num(*factors).GCD()

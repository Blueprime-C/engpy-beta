from .primary import Num
from engpy.misc.assist import getter, mul
from engpy.misc.helpers import cross
from engpy.errors.exceptions import UnacceptableToken, OperationNotAllowed


def efactors(exprs):
    if getter(exprs, 'name') != 'Expr':
        raise UnacceptableToken(f'Expr Objs are expected not {type(exprs)}')
    if len(exprs) > 1:
        raise OperationNotAllowed
    expr = exprs.recreate
    coeff, var = exprs.__extract__
    efactor = [coeff]
    for var_, pow_ in var.items():
        if isinstance(var_, str):
            efactor.append(expr(var_) ** pow_)
        else:
            efactor.append(cross(var_, expr) ** pow_)
    return efactor


def Dfactors(exprs, coeff=True):
    if getter(exprs, 'name') != 'Expr':
        raise UnacceptableToken(f'Expr Objs are expected not {type(exprs)}')
    if len(exprs) > 1:
        raise OperationNotAllowed
    expr = exprs.recreate
    coef, var = exprs.__extract__
    efactor = {coef: 1} if coeff else {}
    for var_, pow_ in var.items():
        if isinstance(var_, str):
            efactor[expr(var_)] = pow_
        else:
            efactor[cross(var_, expr)] = pow_
    return (coef, efactor) if not coeff else efactor


def EGCD(*exprs):
    if len(exprs) == 1: return exprs[0]
    egcd, nums = [], []
    for exprs_ in exprs:
        coeff, factored = Dfactors(exprs_, 0)
        nums.append(coeff)
        egcd.append(factored)
    start = egcd[0]; factored_dict = {}
    for nn, factors in enumerate(egcd):
        if not nn: continue
        for factor, power in factors.items():
            if factor in start:
                if start[factor] > power:
                    factored_dict[factor], start[factor] = power, power
                else:
                    factored_dict[factor] = start[factor]

    return Num(*nums).GCD() * mul([var ** pows for var, pows in factored_dict.items()])


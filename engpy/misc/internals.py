from engpy.fundamentals.assorted import GCD
from engpy.misc.assist import getter


def iformat(self):
    return self.__str__(d=False, s=True)


def check_coeff_ind(exprs, unity = False):
    if len(exprs) != 1: return None, None
    coeff, expr = exprs.__extract__
    powers = GCD(*expr.values())
    return (coeff, powers) if not unity else (coeff, powers) if unity and powers != 1 else (None, None)


def check_ind(exprs, unity = False):
    cp = check_coeff_ind(exprs, unity)
    return None if all(cp) else cp[1]


def nested(expr):
    print(expr.expr, len(expr))
    coeff, var = expr.__extract__
    for vars_ in var:
        if getter(vars_, 'name') == 'Expr': return True

    return False


def unnest(expr):
    while nested(expr):
        mul_ = 1; new_dict = {}
        coeff, var = expr.__extract__
        for vars_, powers in var.items():
            if getter(vars_, 'name') == 'Expr':
                mul_ *= vars_ ** powers
            else:
                new_dict[vars_] = powers
        expr = coeff * mul_ * expr.recreate({1: [new_dict]}) if new_dict else coeff * mul_
        print('....')
    return expr


def unnest_with_powers(expr):
    result = expr.new
    for coeff, var in expr.expr.items():
        new_var = {}
        if len(var) > 1:
            return expr
        for _expr, power in var[0].items():
            if getter(_expr, 'name') == 'Expr':
                if len(_expr) == 1:
                    coeff_expr, var_expr = _expr.__extract__
                    coeff *= coeff_expr
                    if len(var_expr) == 1:
                        var_ = list(var_expr)[0]
                        index = var_expr[var_]
                        var_expr[var_] = 1
                    new_var.update({_expr: power * index})
            else:
                new_var.update({_expr: power})
    result += expr.form()({coeff: [new_var]})

    return result

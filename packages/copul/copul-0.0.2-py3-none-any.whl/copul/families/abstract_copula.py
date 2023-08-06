import sympy


class AbstractCopula:
    u, v = sympy.symbols("u v", positive=True)

    @property
    def cdf(self):
        return None

    @property
    def pdf(self):
        return sympy.simplify(sympy.diff(self.cdf, self.u, self.v))

    @property
    def log_pdf(self, expand_log=False):
        log_pdf = sympy.simplify(sympy.log(self.pdf))
        return concrete_expand_log(log_pdf) if expand_log else log_pdf


def round_expression(expr, n=2):
    expr = sympy.simplify(expr)
    for a in sympy.preorder_traversal(expr):
        if isinstance(a, sympy.Float):
            expr = expr.subs(a, round(a, n))
    return expr


def concrete_expand_log(expr, first_call=True):
    import sympy as sp
    if first_call:
        expr = sp.expand_log(expr, force=True)
    func = expr.func
    args = expr.args
    if args == ():
        return expr
    if func == sp.log and args[0].func == sp.concrete.products.Product:
        prod = args[0]
        term = prod.args[0]
        indices = prod.args[1:]
        return sp.Sum(sp.log(term), *indices)
    return func(*map(lambda x: concrete_expand_log(x, False), args))

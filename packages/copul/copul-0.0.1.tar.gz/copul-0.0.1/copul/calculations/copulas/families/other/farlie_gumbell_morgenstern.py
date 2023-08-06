import sympy

from copul.calculations.copulas import abstract_copula
from copul.calculations.copulas.abstract_copula import AbstractCopula


class FarlieGumbellMorgenstern(AbstractCopula):
    theta = sympy.symbols("theta", positive=True)

    def cdf(self):
        return self.u*self.v + self.theta*self.u*self.v*(1 - self.u)*(1 - self.v)


if __name__ == "__main__":
    farlie = FarlieGumbellMorgenstern()
    cdf = farlie.cdf
    pdf = farlie.log_pdf
    diff = sympy.simplify(sympy.diff(cdf, farlie.v))
    diff2 = sympy.simplify(sympy.diff(diff, farlie.v))
    print(sympy.latex(diff2))
    special_diff = abstract_copula.round_expression(diff.subs(farlie.u, 0.5))
    sympy.plot(special_diff.subs(farlie.theta, 2))
    exit()

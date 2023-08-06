import sympy

from copul.calculations.copulas.families.archimedean.archimedean_copula import ArchimedeanCopula


class GumbellBarnett(ArchimedeanCopula):
    ac = ArchimedeanCopula
    _inv_generator = sympy.log(1 - ac.theta * sympy.log(ac.t))
    theta_interval = sympy.Interval(0, 1, left_open=True, right_open=False)

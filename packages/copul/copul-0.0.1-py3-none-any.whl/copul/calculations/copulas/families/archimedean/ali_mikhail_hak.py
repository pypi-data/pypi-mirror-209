import sympy

from copul.calculations.copulas.families.archimedean.archimedean_copula import ArchimedeanCopula


class AliMikhailHak(ArchimedeanCopula):
    """
        Ali-Mikhail-Hak copula (Nelsen 3)
    """
    ac = ArchimedeanCopula
    _inv_generator = sympy.log((1 - ac.theta * (1 - ac.t)) / ac.t)
    theta_interval = sympy.Interval(-1, 1, left_open=False, right_open=True)

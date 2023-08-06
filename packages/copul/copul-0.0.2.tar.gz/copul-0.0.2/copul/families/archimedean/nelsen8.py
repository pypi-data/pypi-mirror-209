import numpy as np
import sympy

from copul.families.archimedean.archimedean_copula import ArchimedeanCopula


class Nelsen8(ArchimedeanCopula):
    ac = ArchimedeanCopula
    _inv_generator = (1 - ac.t) / (1 + (ac.theta - 1) * ac.t)
    theta_interval = sympy.Interval(1, np.inf, left_open=False, right_open=True)

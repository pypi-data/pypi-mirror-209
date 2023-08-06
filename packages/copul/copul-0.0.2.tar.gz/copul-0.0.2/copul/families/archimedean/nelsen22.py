import numpy as np
import sympy

from copul.families.archimedean.archimedean_copula import ArchimedeanCopula


class Nelsen22(ArchimedeanCopula):
    ac = ArchimedeanCopula
    _inv_generator = sympy.asin(1 - ac.t ** ac.theta)
    theta_interval = sympy.Interval(0, 1, left_open=True, right_open=False)

    def compute_inv_gen_max(self):
        return np.pi / 2

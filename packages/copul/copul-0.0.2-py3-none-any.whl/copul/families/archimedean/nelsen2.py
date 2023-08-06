import numpy as np
import sympy

from copul.families.archimedean.archimedean_copula import ArchimedeanCopula


class Nelsen2(ArchimedeanCopula):
    ac = ArchimedeanCopula
    _inv_generator = (1 - ac.t) ** ac.theta
    theta_interval = sympy.Interval(1, np.inf, left_open=False, right_open=True)

    def generator(self):
        return sympy.Max(1 - self.y ** (1 / self.theta), 0)

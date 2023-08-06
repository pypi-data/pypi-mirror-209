import numpy as np
import sympy
from scipy import optimize

from copul.calculations.copulas.abstract_copula import AbstractCopula, concrete_expand_log


class ArchimedeanCopula(AbstractCopula):
    _t_min = 0
    _t_max = 1
    y, t, theta = sympy.symbols("y t theta", positive=True)
    theta_interval = None
    _inv_generator = None

    def __init__(self, theta_min=None, theta_max=None):
        if theta_min is not None:
            self.theta_interval = sympy.Interval(theta_min, self.theta_max, left_open=self.theta_interval.left_open,
                                                 right_open=self.theta_interval.right_open)
        if theta_max is not None:
            self.theta_interval = sympy.Interval(self.theta_min, theta_max, left_open=self.theta_interval.left_open,
                                                 right_open=self.theta_interval.right_open)

    @property
    def inv_generator(self):
        return self._inv_generator

    @property
    def theta_max(self):
        return self.theta_interval.closure.end

    @property
    def theta_min(self):
        return self.theta_interval.closure.inf

    @staticmethod
    def _get_simplified_solution(sol):
        simplified_sol = sympy.simplify(sol)
        if isinstance(simplified_sol, sympy.core.containers.Tuple):
            return simplified_sol[0]
        else:
            return simplified_sol

    @property
    def cdf(self):
        gen = self.generator
        cop = gen.subs(self.y, self._inv_generator.subs(self.t, self.u) + self._inv_generator.subs(self.t, self.v))
        return self._get_simplified_solution(cop)

    @property
    def generator(self):
        eq = sympy.Eq(self.y, self._inv_generator)
        sol = sympy.solve([eq, self.theta > 0, self.y > 0], self.t)
        my_sol = sol[self.t] if isinstance(sol, dict) else sol[0]
        return self._get_simplified_solution(my_sol)

    def get_first_deriv_of_generator(self):
        gen = self.generator
        return sympy.simplify(sympy.diff(gen, self.y))

    def get_second_deriv_of_gen(self):
        return sympy.simplify(sympy.diff(self.get_first_deriv_of_generator(), self.y))

    def get_ci_char_function(self):
        minus_gen_deriv = - self.get_first_deriv_of_generator()
        return concrete_expand_log(sympy.simplify(sympy.log(minus_gen_deriv)))

    def get_first_deriv_of_ci_char_function(self):
        chi_char_func = self.get_ci_char_function()
        return sympy.simplify(sympy.diff(chi_char_func, self.y))

    def get_second_deriv_of_ci_char_function(self):
        chi_char_func_deriv = self.get_first_deriv_of_ci_char_function()
        return sympy.simplify(sympy.diff(chi_char_func_deriv, self.y))

    def get_mtp2_char_function(self):
        second_deriv = self.get_second_deriv_of_gen()
        return concrete_expand_log(sympy.simplify(sympy.log(second_deriv)))

    def get_first_deriv_of_mtp2_char(self):
        mtp2_char = self.get_mtp2_char_function()
        return sympy.simplify(sympy.diff(mtp2_char, self.y))

    def get_second_deriv_of_mtp2_char(self):
        mtp2_char_deriv = self.get_first_deriv_of_mtp2_char()
        return sympy.simplify(sympy.diff(mtp2_char_deriv, self.y))

    def log_der(self):
        minus_log_derivative = self.get_ci_char_function()
        first_deriv = self.get_first_deriv_of_ci_char_function()
        second_deriv = self.get_second_deriv_of_ci_char_function()
        return self._compute_log2_der_of(first_deriv, minus_log_derivative, second_deriv)

    def log2_der(self):
        log_second_derivative = self.get_mtp2_char_function()
        first_deriv = self.get_first_deriv_of_mtp2_char()
        second_deriv = self.get_second_deriv_of_mtp2_char()
        return self._compute_log2_der_of(first_deriv, log_second_derivative, second_deriv)

    def _compute_log2_der_of(self, first_deriv, log_second_derivative, second_deriv):
        log_der_lambda = sympy.lambdify([(self.y, self.theta)], second_deriv)
        bounds = [(self._t_min, self._t_max), (self.theta_min, self.theta_max)]
        starting_point = np.array([min(self._t_min + 0.5, self._t_max), min(self.theta_min + 0.5, self.theta_max)])
        min_val = optimize.minimize(log_der_lambda, starting_point, bounds=bounds)
        return log_second_derivative, first_deriv, second_deriv, [round(val, 2) for val in min_val.x], round(
            log_der_lambda(min_val.x), 2)

    def compute_inv_gen_max(self):
        try:
            limit = sympy.limit(self._inv_generator, self.t, 0)
        except TypeError:
            limit = sympy.limit(self._inv_generator.subs(self.theta, (self.theta_max - self.theta_min) / 2), self.t, 0)
        return sympy.simplify(limit)

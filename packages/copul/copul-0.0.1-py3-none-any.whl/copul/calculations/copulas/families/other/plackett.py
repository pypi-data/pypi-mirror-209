import sympy

from copul.calculations.copulas.abstract_copula import AbstractCopula


class Plackett(AbstractCopula):
    theta = sympy.symbols("x", positive=True)

    def cdf(self):
        return (1+(self.theta - 1)*(self.u + self.v) - sympy.sqrt((1+(self.theta-1)*(self.u+self.v))**2 - 4*self.u*self.v*self.theta*(self.theta - 1)))/(2*(self.theta - 1))

    def get_density_of_density(self):
        # D_vu(pdf)
        return (-((2*self.u*self.theta - 2*self.u - self.theta + 1)*
                  (self.u**2*self.theta**2 - 2*self.u**2*self.theta + self.u**2
                   - 2*self.u*self.v*self.theta**2 + 2*self.u*self.v + 2*self.u*self.theta
                   - 2*self.u + self.v**2*self.theta**2 - 2*self.v**2*self.theta
                   + self.v**2 + 2*self.v*self.theta - 2*self.v + 1)
                  + 3*(-self.u*self.theta**2 + self.u + self.v*self.theta**2
                       - 2*self.v*self.theta + self.v + self.theta - 1)*
                  (-2*self.u*self.v*self.theta + 2*self.u*self.v + self.u*self.theta
                   - self.u + self.v*self.theta - self.v + 1))
                *(2*self.v*self.theta - 2*self.v - self.theta + 1)
                *(self.u**2*self.theta**2 - 2*self.u**2*self.theta + self.u**2
                  - 2*self.u*self.v*self.theta**2 + 2*self.u*self.v + 2*self.u*self.theta
                  - 2*self.u + self.v**2*self.theta**2 - 2*self.v**2*self.theta + self.v**2
                  + 2*self.v*self.theta - 2*self.v + 1)
                + 2*((2*self.u*self.theta - 2*self.u - self.theta + 1)
                     *(self.u**2*self.theta**2 - 2*self.u**2*self.theta + self.u**2
                       - 2*self.u*self.v*self.theta**2 + 2*self.u*self.v + 2*self.u*self.theta
                       - 2*self.u + self.v**2*self.theta**2 - 2*self.v**2*self.theta + self.v**2
                       + 2*self.v*self.theta - 2*self.v + 1)
                     + 3*(-self.u*self.theta**2 + self.u + self.v*self.theta**2
                          - 2*self.v*self.theta + self.v + self.theta - 1)
                     *(-2*self.u*self.v*self.theta + 2*self.u*self.v + self.u*self.theta
                       - self.u + self.v*self.theta - self.v + 1))
                *(self.u*self.theta**2 - 2*self.u*self.theta + self.u
                  - self.v*self.theta**2 + self.v + self.theta - 1)
                *(-2*self.u*self.v*self.theta + 2*self.u*self.v + self.u*self.theta
                  - self.u + self.v*self.theta - self.v + 1)
                + (-2*(self.theta - 1)
                   *(self.u**2*self.theta**2 - 2*self.u**2*self.theta + self.u**2
                     - 2*self.u*self.v*self.theta**2 + 2*self.u*self.v + 2*self.u*self.theta
                     - 2*self.u + self.v**2*self.theta**2 - 2*self.v**2*self.theta + self.v**2
                     + 2*self.v*self.theta - 2*self.v + 1) + 3*(self.theta**2 - 1)
                   *(-2*self.u*self.v*self.theta + 2*self.u*self.v + self.u*self.theta - self.u
                     + self.v*self.theta - self.v + 1)
                   - 2*(2*self.u*self.theta - 2*self.u - self.theta + 1)
                   *(self.u*self.theta**2 - 2*self.u*self.theta + self.u - self.v*self.theta**2
                     + self.v + self.theta - 1)
                   + 3*(2*self.v*self.theta - 2*self.v - self.theta + 1)
                   *(-self.u*self.theta**2 + self.u + self.v*self.theta**2 - 2*self.v*self.theta
                     + self.v + self.theta - 1))
                *(-2*self.u*self.v*self.theta + 2*self.u*self.v + self.u*self.theta - self.u
                  + self.v*self.theta - self.v + 1)
                *(self.u**2*self.theta**2 - 2*self.u**2*self.theta + self.u**2
                  - 2*self.u*self.v*self.theta**2 + 2*self.u*self.v + 2*self.u*self.theta
                  - 2*self.u + self.v**2*self.theta**2 - 2*self.v**2*self.theta + self.v**2
                  + 2*self.v*self.theta - 2*self.v + 1))/(
                (-2*self.u*self.v*self.theta + 2*self.u*self.v + self.u*self.theta - self.u
                 + self.v*self.theta - self.v + 1)**2
                *(self.u**2*self.theta**2 - 2*self.u**2*self.theta + self.u**2
                  - 2*self.u*self.v*self.theta**2 + 2*self.u*self.v + 2*self.u*self.theta
                  - 2*self.u + self.v**2*self.theta**2 - 2*self.v**2*self.theta + self.v**2
                  + 2*self.v*self.theta - 2*self.v + 1)**2)

    def get_numerator_double_density(self):
        return (-((2 * self.u * self.theta - 2 * self.u - self.theta + 1) *
                 (self.u ** 2 * self.theta ** 2 - 2 * self.u ** 2 * self.theta + self.u ** 2 - 2 * self.u * self.v * self.theta ** 2 + 2 * self.u * self.v + 2 * self.u * self.theta - 2 * self.u + self.v ** 2 * self.theta ** 2 - 2 * self.v ** 2 * self.theta + self.v ** 2 + 2 * self.v * self.theta - 2 * self.v + 1) + 3 * (
                              -self.u * self.theta ** 2 + self.u + self.v * self.theta ** 2 - 2 * self.v * self.theta + self.v + self.theta - 1) * (
                              -2 * self.u * self.v * self.theta + 2 * self.u * self.v + self.u * self.theta - self.u + self.v * self.theta - self.v + 1)) * (
                            2 * self.v * self.theta - 2 * self.v - self.theta + 1) * (
                            self.u ** 2 * self.theta ** 2 - 2 * self.u ** 2 * self.theta + self.u ** 2 - 2 * self.u * self.v * self.theta ** 2 + 2 * self.u * self.v + 2 * self.u * self.theta - 2 * self.u + self.v ** 2 * self.theta ** 2 - 2 * self.v ** 2 * self.theta + self.v ** 2 + 2 * self.v * self.theta - 2 * self.v + 1) + 2 * (
                            (2 * self.u * self.theta - 2 * self.u - self.theta + 1) * (
                                self.u ** 2 * self.theta ** 2 - 2 * self.u ** 2 * self.theta + self.u ** 2 - 2 * self.u * self.v * self.theta ** 2 + 2 * self.u * self.v + 2 * self.u * self.theta - 2 * self.u + self.v ** 2 * self.theta ** 2 - 2 * self.v ** 2 * self.theta + self.v ** 2 + 2 * self.v * self.theta - 2 * self.v + 1) + 3 * (
                                        -self.u * self.theta ** 2 + self.u + self.v * self.theta ** 2 - 2 * self.v * self.theta + self.v + self.theta - 1) * (
                                        -2 * self.u * self.v * self.theta + 2 * self.u * self.v + self.u * self.theta - self.u + self.v * self.theta - self.v + 1)) * (
                            self.u * self.theta ** 2 - 2 * self.u * self.theta + self.u - self.v * self.theta ** 2 + self.v + self.theta - 1) * (
                            -2 * self.u * self.v * self.theta + 2 * self.u * self.v + self.u * self.theta - self.u + self.v * self.theta - self.v + 1) + (
                            -2 * (self.theta - 1) * (
                                self.u ** 2 * self.theta ** 2 - 2 * self.u ** 2 * self.theta + self.u ** 2 - 2 * self.u * self.v * self.theta ** 2 + 2 * self.u * self.v + 2 * self.u * self.theta - 2 * self.u + self.v ** 2 * self.theta ** 2 - 2 * self.v ** 2 * self.theta + self.v ** 2 + 2 * self.v * self.theta - 2 * self.v + 1) + 3 * (
                                        self.theta ** 2 - 1) * (
                                        -2 * self.u * self.v * self.theta + 2 * self.u * self.v + self.u * self.theta - self.u + self.v * self.theta - self.v + 1) - 2 * (
                                        2 * self.u * self.theta - 2 * self.u - self.theta + 1) * (
                                        self.u * self.theta ** 2 - 2 * self.u * self.theta + self.u - self.v * self.theta ** 2 + self.v + self.theta - 1) + 3 * (
                                        2 * self.v * self.theta - 2 * self.v - self.theta + 1) * (
                                        -self.u * self.theta ** 2 + self.u + self.v * self.theta ** 2 - 2 * self.v * self.theta + self.v + self.theta - 1)) * (
                            -2 * self.u * self.v * self.theta + 2 * self.u * self.v + self.u * self.theta - self.u + self.v * self.theta - self.v + 1) * (
                            self.u ** 2 * self.theta ** 2 - 2 * self.u ** 2 * self.theta + self.u ** 2 - 2 * self.u * self.v * self.theta ** 2 + 2 * self.u * self.v + 2 * self.u * self.theta - 2 * self.u + self.v ** 2 * self.theta ** 2 - 2 * self.v ** 2 * self.theta + self.v ** 2 + 2 * self.v * self.theta - 2 * self.v + 1))


if __name__ == "__main__":
    plackett = Plackett()
    cdf = plackett.cdf()
    # pdf = plackett.get_log_pdf()
    explicit_num = plackett.get_numerator_double_density()
    print(str(sympy.expand_mul(explicit_num)).replace("**", "^"))
    # diff = sympy.simplify(sympy.diff(cdf, plackett.v))
    # diff2 = sympy.simplify(sympy.diff(diff, plackett.v))
    # print(sympy.latex(diff2))
    # special_diff = abstract_copula.round_expression(diff.subs(plackett.u, 0.5))
    # sympy.plot(special_diff.subs(plackett.theta, 2))
    exit()

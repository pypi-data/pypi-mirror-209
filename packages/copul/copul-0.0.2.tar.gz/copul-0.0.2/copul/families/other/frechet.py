import sympy

from copul.families.abstract_copula import AbstractCopula


class Frechet(AbstractCopula):
    alpha, beta = sympy.symbols("alpha beta", positive=True)

    @property
    def cdf(self):
        return None  # TODO implement

    @property
    def spearmans_rho(self):
        return self.alpha - self.beta

    @property
    def kendalls_tau(self):
        return (self.alpha - self.beta)*(2 + self.alpha + self.beta)/3


if __name__ == "__main__":
    frechet = Frechet()
    cdf = frechet.spearmans_rho()
    exit()

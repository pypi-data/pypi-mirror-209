# copulas_in_systemic_risk

## Sample Usage
import copul

galambos = copul.Galambos()
params = galambos.sample_parameters(3)
galambos.plot_pickand(params)

## Notes

python copula packages:
- pyvinecopulib
- copulas
- others: copula, copulae, pycopula, ...

more here: https://pypi.org/search/?q=copula

r copula packages:
- copula
- VineCopula
- others: GFGM.copula, FactorCopula, CommonMean.Copula, svines, ...

more here: https://cran.r-project.org/web/packages/available_packages_by_date.html

## Installation
Run `pip install .`.
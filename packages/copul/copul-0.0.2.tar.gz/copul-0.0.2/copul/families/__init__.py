import sympy


def get_simplified_solution(sol):
    simplified_sol = sympy.simplify(sol)
    if isinstance(simplified_sol, sympy.core.containers.Tuple):
        return simplified_sol[0]
    else:
        return simplified_sol

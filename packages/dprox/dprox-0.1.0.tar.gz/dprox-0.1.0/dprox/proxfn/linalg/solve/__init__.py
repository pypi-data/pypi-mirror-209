from .cg import conjugate_gradient, conjugate_gradient2, PCG
from .plss import PLSS

__all__ = available_solvers = [
    'conjugate_gradient',
    'conjugate_gradient2',
    'PCG',
    'PLSS'
]

SOLVERS = {
    'cg': conjugate_gradient,
    'cg2': conjugate_gradient2,
}

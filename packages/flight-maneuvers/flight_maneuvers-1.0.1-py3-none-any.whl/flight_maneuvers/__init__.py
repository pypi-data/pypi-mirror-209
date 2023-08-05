# path pointing to a dataset of simulated flight trajectories with labeled maneuvers
DATASET_PATH = 'examples/maneuver_dataset'

# path pointing to experiment results
EXPERIMENT_PATH = 'experiments'


from .__about__ import *


__all__ = [
    "__title__",
    "__summary__",
    "__url__",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
]


try:
    from flight_maneuvers import model
    __all__ += ['model']
except ImportError:
    pass


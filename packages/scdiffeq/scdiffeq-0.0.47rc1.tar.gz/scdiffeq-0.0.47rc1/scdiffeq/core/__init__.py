
__module_name__ = "__init__.py"
__version__ = "0.0.46rc2"
__doc__ = """Top-level __init__ for accessing the scDiffEq model."""
__author__ = ", ".join(["Michael E. Vinyard", "Anders Rasmussen", "Ruitong Li"])
__email__ = ", ".join(
    [
        "mvinyard@broadinstitute.org",
        "arasmuss@broadinstitute.org",
        "ruitong@broadinstitute.org",
    ]
)

# -- import models accessed as sdq.models.<MODEL>: ---------------------------------------
from ._scdiffeq import scDiffEq

from . import lightning_models
from . import utils
from . import configs
from . import callbacks

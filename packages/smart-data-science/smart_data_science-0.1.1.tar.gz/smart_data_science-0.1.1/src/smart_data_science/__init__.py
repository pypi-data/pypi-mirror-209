""" Python Package init file """
# pylint: disable=unused-import, wrong-import-position
import warnings
from importlib.metadata import version  # read version from installed package

from numba.core.errors import NumbaDeprecationWarning  # shap issue

warnings.simplefilter("ignore", category=NumbaDeprecationWarning)


from .analysis.info import info_data  # noqa: F401, E402
from .core import logger  # io, system  # noqa: F401, E402
from .core.data_samples_module import load_sample  # noqa: F401, E402
from .core.system import info_system  # noqa: F401, E402
from .ml.ml_regressor import SmartRegressor  # noqa: F401, E402
from .process.clean import optimize_schema  # noqa: F401, E402

__version__ = version("smart_data_science")

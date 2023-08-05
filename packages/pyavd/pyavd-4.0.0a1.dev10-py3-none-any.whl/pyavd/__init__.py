from .eos_cli_config_gen import eos_cli_config_gen
from .eos_designs_facts import eos_designs_facts
from .eos_designs_structured_configs import eos_designs_structured_configs
from .vendor.version import VERSION

""" Library for running Arista Validated Designs (AVD) in Python
"""

PYAVD_VERSION = "a1"
AVD_VERSION = VERSION.split("-", maxsplit=1)[0]

if "-dev" in VERSION:
    DEV_VERSION = f"-dev{VERSION.split('-dev')[1]}"
else:
    DEV_VERSION = ""

__author__ = "Arista Networks"
__copyright__ = "Copyright 2023 Arista Networks"
__license__ = "Apache 2.0"
__version__ = f"{AVD_VERSION}{PYAVD_VERSION}{DEV_VERSION}"

__all__ = ["eos_cli_config_gen", "eos_designs_facts", "eos_designs_structured_configs"]

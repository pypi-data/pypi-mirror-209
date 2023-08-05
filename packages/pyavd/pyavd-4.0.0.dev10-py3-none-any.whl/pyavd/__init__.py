from .eos_cli_config_gen import eos_cli_config_gen
from .eos_designs_facts import eos_designs_facts
from .eos_designs_structured_configs import eos_designs_structured_configs
from .vendor.version import VERSION

""" Library for running Arista Validated Designs (AVD) in Python
"""

__author__ = "Arista Networks"
__copyright__ = "Copyright 2023 Arista Networks"
__license__ = "Apache 2.0"
__version__ = f"{VERSION.replace('-', '.')}"

__all__ = ["eos_cli_config_gen", "eos_designs_facts", "eos_designs_structured_configs"]

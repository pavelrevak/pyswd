"""Cortex-M0 package
"""

from swd.targets.cortexm0.stm32f0 import Stm32f0

CORE = "Cortex-M0"

FAMILIES = [
    Stm32f0,
]

__all__ = [
    "Stm32f0",
]
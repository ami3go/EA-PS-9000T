"""Python control helpers for EA Elektro-Automatik PS 9000 T supplies."""

from .EAPS9000T_class import (
    EaPs9000T,
    PowerSupplyLimits,
    get_com_port_by_keyword,
    storage,
)

# Singular spelling retained as a friendly compatibility alias.
PowerSupplyLimit = PowerSupplyLimits

__all__ = [
    "EaPs9000T",
    "PowerSupplyLimit",
    "PowerSupplyLimits",
    "get_com_port_by_keyword",
    "storage",
]

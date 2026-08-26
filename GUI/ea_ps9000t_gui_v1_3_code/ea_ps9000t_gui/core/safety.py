from __future__ import annotations

from typing import Any

from .profile_model import AppState


NORMAL_MANUAL_STATES = {AppState.CONNECTED_IDLE, AppState.MONITORING, AppState.PROFILE_LOADED}


def manual_controls_allowed(state: AppState, advanced_override: bool = False) -> bool:
    if state == AppState.PROFILE_RUNNING:
        return bool(advanced_override)
    return state in NORMAL_MANUAL_STATES


def output_state_label(value: Any, unknown: bool = False) -> str:
    if unknown:
        return "UNKNOWN"
    if value is True:
        return "ON"
    if value is False:
        return "OFF"
    return "UNKNOWN"


def validate_positive_interval_ms(value: int, name: str, minimum: int = 50) -> int:
    value_i = int(value)
    if value_i < minimum:
        raise ValueError(f"{name} must be >= {minimum} ms")
    return value_i

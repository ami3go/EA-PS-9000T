from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Literal, Optional

OutputCommand = Literal["on", "off", "keep"]
RampMode = Literal["step", "linear"]
Severity = Literal["error", "warning"]


class AppState(str, Enum):
    DISCONNECTED = "DISCONNECTED"
    CONNECTING = "CONNECTING"
    CONNECTED_IDLE = "CONNECTED_IDLE"
    MONITORING = "MONITORING"
    PROFILE_LOADED = "PROFILE_LOADED"
    PROFILE_RUNNING = "PROFILE_RUNNING"
    PROFILE_PAUSED = "PROFILE_PAUSED"
    STOPPING = "STOPPING"
    ERROR = "ERROR"
    OUTPUT_STATE_UNKNOWN = "OUTPUT_STATE_UNKNOWN"


@dataclass(frozen=True)
class ProfileStep:
    index: int
    row_number: int
    time_s: float
    voltage_v: float
    current_a: Optional[float] = None
    power_w: Optional[float] = None
    ovp_v: Optional[float] = None
    ocp_a: Optional[float] = None
    opp_w: Optional[float] = None
    output: OutputCommand = "keep"
    ramp: RampMode = "step"
    comment: str = ""


@dataclass(frozen=True)
class ProfileValidationIssue:
    row: int
    column: str
    message: str
    severity: Severity = "error"

    def __str__(self) -> str:
        return f"Row {self.row}, column {self.column}: {self.message}"


@dataclass
class VoltageProfile:
    path: str
    steps: list[ProfileStep] = field(default_factory=list)
    warnings: list[ProfileValidationIssue] = field(default_factory=list)

    @property
    def duration_s(self) -> float:
        return self.steps[-1].time_s if self.steps else 0.0

    @property
    def is_empty(self) -> bool:
        return not self.steps


@dataclass
class ProfileLoadResult:
    profile: Optional[VoltageProfile]
    issues: list[ProfileValidationIssue] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.profile is not None and not any(i.severity == "error" for i in self.issues)

    @property
    def errors(self) -> list[ProfileValidationIssue]:
        return [i for i in self.issues if i.severity == "error"]

    @property
    def warnings(self) -> list[ProfileValidationIssue]:
        return [i for i in self.issues if i.severity == "warning"]

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, Optional

try:
    from EAPS9000T_class import PowerSupplyLimits
except Exception:  # pragma: no cover - only for unusual import paths
    PowerSupplyLimits = object  # type: ignore

from .profile_model import ProfileLoadResult, ProfileStep, ProfileValidationIssue, VoltageProfile

REQUIRED_COLUMNS = {"time_s", "voltage_v"}
OPTIONAL_COLUMNS = {
    "current_a",
    "power_w",
    "ovp_v",
    "ocp_a",
    "opp_w",
    "output",
    "ramp",
    "comment",
}
KNOWN_COLUMNS = REQUIRED_COLUMNS | OPTIONAL_COLUMNS

EXAMPLE_CSV = """time_s,voltage_v,current_a,power_w,ovp_v,ocp_a,opp_w,output,ramp,comment
0,0,1.0,100,30,2.0,150,off,step,Start with output off
1,5,1.0,100,30,2.0,150,on,step,Enable output at 5 V
5,12,1.5,200,30,2.0,250,keep,linear,Ramp from 12 V to next point
10,24,2.0,300,30,2.5,350,keep,step,Hold 24 V
15,0,1.0,100,30,2.0,150,off,step,End safely
"""


def _filtered_lines(path: Path) -> list[str]:
    lines: list[str] = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            lines.append(line)
    return lines


def _norm_header(name: str) -> str:
    return name.strip().lower()


def _parse_optional_float(raw: Optional[str], row: int, column: str, issues: list[ProfileValidationIssue]) -> Optional[float]:
    if raw is None or raw.strip() == "":
        return None
    try:
        return float(raw.strip())
    except ValueError:
        issues.append(ProfileValidationIssue(row, column, f"{raw!r} is not a valid number"))
        return None


def _parse_required_float(raw: Optional[str], row: int, column: str, issues: list[ProfileValidationIssue]) -> float:
    parsed = _parse_optional_float(raw, row, column, issues)
    if parsed is None:
        issues.append(ProfileValidationIssue(row, column, "required numeric value is missing"))
        return 0.0
    return parsed


def _range_check(
    value: Optional[float],
    min_value: float,
    max_value: float,
    row: int,
    column: str,
    issues: list[ProfileValidationIssue],
    unit: str,
) -> None:
    if value is None:
        return
    if value < min_value or value > max_value:
        issues.append(
            ProfileValidationIssue(
                row,
                column,
                f"{value:g} {unit} is outside allowed range {min_value:g}..{max_value:g} {unit}",
            )
        )


def load_voltage_profile(path: str | Path, limits: PowerSupplyLimits) -> ProfileLoadResult:
    """Load and validate a voltage-profile CSV file."""
    path = Path(path)
    issues: list[ProfileValidationIssue] = []
    if not path.exists():
        return ProfileLoadResult(None, [ProfileValidationIssue(0, "file", f"File does not exist: {path}")])

    try:
        lines = _filtered_lines(path)
    except OSError as exc:
        return ProfileLoadResult(None, [ProfileValidationIssue(0, "file", str(exc))])

    if not lines:
        return ProfileLoadResult(None, [ProfileValidationIssue(0, "file", "CSV is empty")])

    try:
        sample = "".join(lines[:5])
        reader = csv.DictReader(lines, delimiter=",")
    except csv.Error as exc:
        return ProfileLoadResult(None, [ProfileValidationIssue(0, "file", f"CSV parse error: {exc}")])

    if not reader.fieldnames:
        return ProfileLoadResult(None, [ProfileValidationIssue(1, "header", "CSV header row is missing")])

    normalized_headers = [_norm_header(h) for h in reader.fieldnames]
    header_map = {original: _norm_header(original) for original in reader.fieldnames}
    missing = REQUIRED_COLUMNS - set(normalized_headers)
    for col in sorted(missing):
        issues.append(ProfileValidationIssue(1, col, "required column is missing"))

    for col in normalized_headers:
        if col not in KNOWN_COLUMNS:
            issues.append(ProfileValidationIssue(1, col, "unknown column will be ignored", "warning"))

    if any(i.severity == "error" for i in issues):
        return ProfileLoadResult(None, issues)

    steps: list[ProfileStep] = []
    previous_time: Optional[float] = None
    for index, row in enumerate(reader):
        # Row number is approximate after comments/blank lines are removed; still useful to user.
        row_number = index + 2
        normalized = {header_map[k]: (v.strip() if isinstance(v, str) else v) for k, v in row.items() if k in header_map}

        time_s = _parse_required_float(normalized.get("time_s"), row_number, "time_s", issues)
        voltage_v = _parse_required_float(normalized.get("voltage_v"), row_number, "voltage_v", issues)
        current_a = _parse_optional_float(normalized.get("current_a"), row_number, "current_a", issues)
        power_w = _parse_optional_float(normalized.get("power_w"), row_number, "power_w", issues)
        ovp_v = _parse_optional_float(normalized.get("ovp_v"), row_number, "ovp_v", issues)
        ocp_a = _parse_optional_float(normalized.get("ocp_a"), row_number, "ocp_a", issues)
        opp_w = _parse_optional_float(normalized.get("opp_w"), row_number, "opp_w", issues)

        output_raw = (normalized.get("output") or "keep").strip().lower()
        ramp_raw = (normalized.get("ramp") or "step").strip().lower()
        comment = normalized.get("comment") or ""

        if output_raw not in {"on", "off", "keep"}:
            issues.append(ProfileValidationIssue(row_number, "output", f"invalid output value {output_raw!r}; expected on/off/keep"))
            output_raw = "keep"
        if ramp_raw not in {"step", "linear"}:
            issues.append(ProfileValidationIssue(row_number, "ramp", f"invalid ramp value {ramp_raw!r}; expected step/linear"))
            ramp_raw = "step"

        if time_s < 0:
            issues.append(ProfileValidationIssue(row_number, "time_s", "time must be zero or positive"))
        if previous_time is not None and time_s <= previous_time:
            issues.append(ProfileValidationIssue(row_number, "time_s", "time_s must be strictly increasing"))
        previous_time = time_s

        _range_check(voltage_v, limits.voltage_min, limits.voltage_max, row_number, "voltage_v", issues, "V")
        _range_check(current_a, limits.current_min, limits.current_max, row_number, "current_a", issues, "A")
        _range_check(power_w, limits.power_min, limits.power_max, row_number, "power_w", issues, "W")
        _range_check(ovp_v, limits.ovp_min, limits.ovp_max, row_number, "ovp_v", issues, "V")
        _range_check(ocp_a, limits.ocp_min, limits.ocp_max, row_number, "ocp_a", issues, "A")
        _range_check(opp_w, limits.opp_min, limits.opp_max, row_number, "opp_w", issues, "W")

        steps.append(
            ProfileStep(
                index=index,
                row_number=row_number,
                time_s=time_s,
                voltage_v=voltage_v,
                current_a=current_a,
                power_w=power_w,
                ovp_v=ovp_v,
                ocp_a=ocp_a,
                opp_w=opp_w,
                output=output_raw,  # type: ignore[arg-type]
                ramp=ramp_raw,  # type: ignore[arg-type]
                comment=comment,
            )
        )

    if not steps:
        issues.append(ProfileValidationIssue(0, "file", "CSV contains no profile rows"))

    if any(i.severity == "error" for i in issues):
        return ProfileLoadResult(None, issues)

    profile = VoltageProfile(path=str(path), steps=steps, warnings=[i for i in issues if i.severity == "warning"])
    return ProfileLoadResult(profile, issues)


def write_example_csv(path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(EXAMPLE_CSV, encoding="utf-8")
    return path

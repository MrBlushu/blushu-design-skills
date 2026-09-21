#!/usr/bin/env python3
"""Validate the structural execution-profile contract for every bundled skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "plugins" / "blushu-design-skills" / "skills"
SKILLS = (
    "before-we-make-a-mess",
    "make-it-flow",
    "set-the-grid",
    "check-the-style",
    "make-it-obvious",
    "break-it-right",
    "lets-build-a-site",
)
PROFILES = ("create", "change", "review", "verify")
PROFILE_MARKER_RE = re.compile(
    r"(?im)^\s*-\s+\*\*(create|change|review|verify):\*\*"
)
ENVELOPE_FIELDS = (
    "Question",
    "Scope",
    "Baseline",
    "Criteria",
    "Authority: read-only",
    "Locked Decisions",
    "Invocation ID",
    "Artifact Revision",
    "Pass Limit: 1",
)


def frontmatter_name(text: str) -> str | None:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if line.startswith("name:"):
            return line.partition(":")[2].strip()
    return None


def execution_profile_window(text: str) -> str | None:
    first_profile = PROFILE_MARKER_RE.search(text)
    if first_profile is None:
        return None
    next_heading = re.search(r"(?m)^##\s+", text[first_profile.start() :])
    if next_heading is None:
        return text[first_profile.start() :]
    return text[first_profile.start() : first_profile.start() + next_heading.start()]


def validate_skill_text(skill: str, text: str) -> list[str]:
    errors: list[str] = []

    if frontmatter_name(text) != skill:
        errors.append(f"{skill}: frontmatter name does not match directory")

    contract = execution_profile_window(text)
    if contract is None:
        return [*errors, f"{skill}: missing execution-profile contract"]

    for profile in PROFILES:
        if not re.search(
            rf"(?im)^\s*-\s+\*\*{re.escape(profile)}:\*\*", contract
        ):
            errors.append(f"{skill}: missing {profile} profile")

    required_signals = {
        "no-task guard": "NEEDS_TASK",
        "terminal statuses": "PASS | FAIL | BLOCKED",
        "mutation declaration": "Mutations: none",
    }
    for label, signal in required_signals.items():
        if signal not in contract:
            errors.append(f"{skill}: missing {label} signal `{signal}`")

    verify_match = re.search(r"(?im)^\s*-\s+\*\*verify:\*\*", contract)
    verify_window = contract[verify_match.start() :] if verify_match else ""

    for field in ENVELOPE_FIELDS:
        if f"`{field}`" not in contract:
            errors.append(f"{skill}: verify envelope missing `{field}`")

    if not re.search(
        r"stop before (?:inspecting|project inspection)|"
        r"stop without loading conditional references|"
        r"fermarsi prima di ispezionare|"
        r"fermarsi senza caricare riferimenti condizionali",
        contract,
        re.IGNORECASE,
    ):
        errors.append(f"{skill}: no-task guard does not stop before inspection")

    if not re.search(r"read-only|sola lettura", verify_window, re.IGNORECASE):
        errors.append(f"{skill}: verify does not declare read-only authority")
    if not re.search(r"one bounded pass|un solo passaggio limitato", verify_window, re.IGNORECASE):
        errors.append(f"{skill}: verify does not declare a bounded single pass")
    if not re.search(r"do not invoke another skill|non invocare altre skill", verify_window, re.IGNORECASE):
        errors.append(f"{skill}: verify does not forbid cross-skill invocation")
    if not re.search(r"do not mutate|non mutare", verify_window, re.IGNORECASE):
        errors.append(f"{skill}: verify does not forbid mutations")
    if not re.search(
        r"do not [^\n]*(?:recommend or apply a repair|"
        r"recommend or execute a learning action)|"
        r"non raccomandare o applicare correzioni",
        verify_window,
        re.IGNORECASE,
    ):
        errors.append(f"{skill}: verify does not forbid corrective action")
    if not re.search(
        r"do not execute a handoff|non eseguire handoff", verify_window, re.IGNORECASE
    ):
        errors.append(f"{skill}: verify does not forbid handoff execution")
    if not re.search(
        r"terminal (?:verify )?report replaces|"
        r"terminal report replaces|"
        r"report terminale sostituisce",
        verify_window,
        re.IGNORECASE,
    ):
        errors.append(f"{skill}: verify does not replace normal output terminally")

    return errors


def validate_skill(skill: str) -> list[str]:
    path = SKILLS_ROOT / skill / "SKILL.md"
    if not path.is_file():
        return [f"{skill}: missing {path.relative_to(ROOT)}"]
    return validate_skill_text(skill, path.read_text(encoding="utf-8"))


def validate_orchestrator() -> list[str]:
    entry = (SKILLS_ROOT / "lets-build-a-site" / "SKILL.md").read_text(encoding="utf-8")
    routing = (
        SKILLS_ROOT / "lets-build-a-site" / "references" / "specialist-routing.md"
    ).read_text(encoding="utf-8")
    errors: list[str] = []

    entry_signals = (
        "own `verify` profile",
        "non-verify orchestration workflow",
        "outer non-verify profile",
    )
    routing_signals = (
        "Sequence ID:",
        "Origin Verification ID:",
        "Verification Ordinal:",
        "stable criterion IDs",
        "only in memory",
        "verify -> change -> verify",
        "same skill, criterion IDs, scope, and artifact revision",
    )

    for signal in entry_signals:
        if signal not in entry:
            errors.append(f"lets-build-a-site: missing orchestrator boundary `{signal}`")
    for signal in routing_signals:
        if signal not in routing:
            errors.append(f"specialist-routing: missing anti-loop signal `{signal}`")

    return errors


def main() -> int:
    errors = [error for skill in SKILLS for error in validate_skill(skill)]
    errors.extend(validate_orchestrator())

    if errors:
        print("Execution-profile validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Execution-profile contract valid for {len(SKILLS)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

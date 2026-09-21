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


def frontmatter_name(text: str) -> str | None:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if line.startswith("name:"):
            return line.partition(":")[2].strip()
    return None


def validate_skill(skill: str) -> list[str]:
    path = SKILLS_ROOT / skill / "SKILL.md"
    if not path.is_file():
        return [f"{skill}: missing {path.relative_to(ROOT)}"]

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if frontmatter_name(text) != skill:
        errors.append(f"{skill}: frontmatter name does not match directory")

    for profile in PROFILES:
        if not re.search(rf"\*\*{re.escape(profile)}:\*\*", text, re.IGNORECASE):
            errors.append(f"{skill}: missing {profile} profile")

    required_signals = {
        "no-task guard": "NEEDS_TASK",
        "terminal statuses": "PASS | FAIL | BLOCKED",
        "mutation declaration": "Mutations: none",
    }
    for label, signal in required_signals.items():
        if signal not in text:
            errors.append(f"{skill}: missing {label} signal `{signal}`")

    verify_window = text[text.lower().find("**verify:**") :]
    if not re.search(r"read-only|sola lettura", verify_window, re.IGNORECASE):
        errors.append(f"{skill}: verify does not declare read-only authority")
    if not re.search(r"one bounded pass|un solo passaggio limitato", verify_window, re.IGNORECASE):
        errors.append(f"{skill}: verify does not declare a bounded single pass")
    if not re.search(r"do not invoke another skill|non invocare altre skill", verify_window, re.IGNORECASE):
        errors.append(f"{skill}: verify does not forbid cross-skill invocation")

    return errors


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

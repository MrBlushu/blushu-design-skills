from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "check-execution-profiles.py"
SPEC = importlib.util.spec_from_file_location("execution_profile_validator", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ExecutionProfileValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.skill = "make-it-obvious"
        self.path = (
            ROOT
            / "plugins"
            / "blushu-design-skills"
            / "skills"
            / self.skill
            / "SKILL.md"
        )
        self.valid_text = self.path.read_text(encoding="utf-8")

    def assert_has_error(self, text: str, fragment: str) -> None:
        errors = VALIDATOR.validate_skill_text(self.skill, text)
        self.assertTrue(
            any(fragment in error for error in errors),
            f"expected error containing {fragment!r}, got {errors!r}",
        )

    def test_valid_skill_passes(self) -> None:
        self.assertEqual([], VALIDATOR.validate_skill_text(self.skill, self.valid_text))

    def test_signal_outside_profile_contract_does_not_count(self) -> None:
        mutated = self.valid_text.replace("Run one bounded pass.", "Run the requested checks.")
        mutated += "\nOne bounded pass.\n"
        self.assert_has_error(mutated, "bounded single pass")

    def test_missing_envelope_field_fails(self) -> None:
        mutated = self.valid_text.replace("`Artifact Revision`, ", "")
        self.assert_has_error(mutated, "verify envelope missing `Artifact Revision`")

    def test_missing_preflight_stop_boundary_fails(self) -> None:
        mutated = self.valid_text.replace(
            "then stop before inspecting artifacts or loading references",
            "then continue with the normal workflow",
        )
        mutated = mutated.replace(
            "then stop without loading conditional references, inspecting unrelated files, routing work, or proposing a review",
            "then continue with the normal workflow",
        )
        self.assert_has_error(mutated, "does not stop before inspection")

    def test_missing_mutation_prohibition_fails(self) -> None:
        mutated = self.valid_text.replace(
            "Do not mutate files, designs, configuration, or external systems; ",
            "",
        )
        self.assert_has_error(mutated, "does not forbid mutations")

    def test_missing_repair_prohibition_fails(self) -> None:
        mutated = self.valid_text.replace(
            "do not recommend or apply a repair; ",
            "",
        )
        self.assert_has_error(mutated, "does not forbid corrective action")


if __name__ == "__main__":
    unittest.main()

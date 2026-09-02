"""Contract checks for the private Microsoft 365 Copilot MAGI artifact."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
M365 = ROOT / "m365-copilot"
MANIFEST = M365 / "declarativeAgent.json"
AGENT_BUILDER = M365 / "agent-builder.md"
GUIDE = M365 / "README.md"
INSTALL_GUIDE = M365 / "INSTALL.md"
README = ROOT / "README.md"
VALIDATION_COMMAND = "python tests/m365_personal_agent_contract_test.py"


def read_manifest() -> dict[str, object]:
    assert MANIFEST.exists(), f"Missing manifest: {MANIFEST.relative_to(ROOT)}"
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def test_manifest_is_a_no_action_p1_magi_agent() -> None:
    manifest = read_manifest()
    instructions = manifest["instructions"]

    assert manifest["version"] == "v1.8"
    assert "actions" not in manifest
    assert "capabilities" not in manifest
    assert "knowledge" not in manifest
    assert "P1" in instructions
    assert "P2" not in instructions
    assert "P3" not in instructions
    assert len(instructions) <= 8000
    for marker in ("Quick", "Standard", "Full", "MELCHIOR", "BALTHASAR", "CASPER", "RITSUKO"):
        assert marker in instructions, f"Missing protocol marker: {marker}"


def test_agent_builder_source_matches_private_p1_contract() -> None:
    assert AGENT_BUILDER.exists(), f"Missing Agent Builder source: {AGENT_BUILDER.relative_to(ROOT)}"
    source = AGENT_BUILDER.read_text(encoding="utf-8")

    assert "P1" in source
    assert "P2" not in source
    assert "P3" not in source
    assert "MAGI Deliberation" in source


def test_setup_documentation_preserves_the_private_mobile_boundary() -> None:
    assert GUIDE.exists(), f"Missing setup guide: {GUIDE.relative_to(ROOT)}"
    text = GUIDE.read_text(encoding="utf-8").lower()

    for marker in ("private", "desktop", "mobile", "p1"):
        assert marker in text, f"Missing setup boundary: {marker}"


def test_external_install_guide_explains_per_tenant_installation() -> None:
    assert INSTALL_GUIDE.exists(), f"Missing installation guide: {INSTALL_GUIDE.relative_to(ROOT)}"
    text = INSTALL_GUIDE.read_text(encoding="utf-8")

    for marker in ("own tenant", "Agent Builder", "P1", "Codex", "ChatGPT"):
        assert marker in text, f"Missing external-installation guidance: {marker}"


def test_readme_lists_the_m365_contract_command_in_all_languages() -> None:
    text = README.read_text(encoding="utf-8")
    assert text.count(VALIDATION_COMMAND) == 3, "Expected the M365 command in all three README sections"


def main() -> None:
    test_manifest_is_a_no_action_p1_magi_agent()
    test_agent_builder_source_matches_private_p1_contract()
    test_setup_documentation_preserves_the_private_mobile_boundary()
    test_external_install_guide_explains_per_tenant_installation()
    test_readme_lists_the_m365_contract_command_in_all_languages()
    print("m365 personal agent contract: PASS")


if __name__ == "__main__":
    main()

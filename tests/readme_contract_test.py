from pathlib import Path


readme = (Path(__file__).parents[1] / "README.md").read_text(encoding="utf-8")

required = [
    "# MAGI Deliberation",
    "## Overview",
    "## Modes",
    "## Independence grades",
    "## MAGI-MAINT",
    "## Install in Codex",
    "## Validate",
    "RITSUKO",
]

missing = [item for item in required if item not in readme]
assert not missing, "Missing README sections: " + ", ".join(missing)

print("PASS: README covers overview, operation, maintenance, installation, and validation")

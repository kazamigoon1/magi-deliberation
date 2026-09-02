from pathlib import Path


skill = (Path(__file__).parents[1] / "SKILL.md").read_text(encoding="utf-8")

required = [
    "## MAGI-MAINT — vehicle and appliance maintenance profile",
    "Compatibility / consumables",
    "Site / work environment",
    "Schedule selection",
    "Pre-execution recheck",
    "Day-of go/no-go",
    "PENDING-CONDITION → APPROVED",
    "Maintenance execution record",
]

missing = [item for item in required if item not in skill]
assert not missing, "Missing MAGI-MAINT contract: " + ", ".join(missing)

print("PASS: MAGI-MAINT profile and execution state machine are present")

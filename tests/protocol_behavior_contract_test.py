from pathlib import Path


skill = " ".join(
    (Path(__file__).parents[1] / "SKILL.md").read_text(encoding="utf-8").split()
)

invariants = {
    "P1 is perspective review": ["| **P1** | One model performed a perspective review"],
    "P3 requires separate parallel agents": [
        "| **P3** | Separate parallel agents reviewed the common packet"
    ],
    "RITSUKO attack contract": [
        "Target claim:",
        "Defect class:",
        "Mechanism:",
        "Falsification condition:",
        "Verification method:",
        "Effect:",
    ],
    "RITSUKO attack limits": [
        "at most one fatal attack in Quick mode",
        "two material attacks in Standard or Full mode",
    ],
    "maintenance approval transition": [
        "Output `PENDING-CONDITION`, not execution approval.",
        "PENDING-CONDITION → APPROVED",
    ],
    "hard constraints precede consensus": [
        "1. Hard constraints.",
        "9. Consensus as a final, non-binding signal.",
    ],
}

for name, fragments in invariants.items():
    missing = [fragment for fragment in fragments if fragment not in skill]
    assert not missing, f"Missing {name} invariant fragments: {missing}"
    print(f"PASS: {name}")

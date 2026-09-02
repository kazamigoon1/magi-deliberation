from pathlib import Path


skill = (Path(__file__).parents[1] / "SKILL.md").read_text(encoding="utf-8")


def section_between(start_heading: str, end_heading: str, invariant_name: str) -> str:
    start = skill.find(start_heading)
    end = skill.find(end_heading, start)
    assert start != -1, f"Missing {invariant_name} section start: {start_heading}"
    assert end != -1, f"Missing {invariant_name} section end: {end_heading}"
    return skill[start:end]


invariants = {
    "P1 is perspective review": ["| **P1** | One model performed a perspective review"],
    "P3 requires separate parallel agents": [
        "| **P3** | Separate parallel agents reviewed the common packet"
    ],
}

for name, fragments in invariants.items():
    missing = [fragment for fragment in fragments if fragment not in skill]
    assert not missing, f"Missing {name} invariant fragments: {missing}"
    print(f"PASS: {name}")

ritsuko = section_between(
    "## Phase 8 — RITSUKO adversarial audit",
    "## Phase 9 — Decision engine",
    "RITSUKO attack contract",
)
normalized_ritsuko = " ".join(ritsuko.split())
attack_contract_fields = [
    "Target claim:",
    "Defect class:",
    "Mechanism:",
    "Falsification condition:",
    "Verification method:",
    "Effect:",
]
missing_attack_fields = [
    field for field in attack_contract_fields if field not in normalized_ritsuko
]
assert not missing_attack_fields, (
    "Missing RITSUKO attack contract invariant fragments: "
    f"{missing_attack_fields}"
)
print("PASS: RITSUKO attack contract")

attack_limits = [
    "at most one fatal attack in Quick mode",
    "two material attacks in Standard or Full mode",
]
missing_attack_limits = [
    limit for limit in attack_limits if limit not in normalized_ritsuko
]
assert not missing_attack_limits, (
    "Missing RITSUKO attack limits invariant fragments: " f"{missing_attack_limits}"
)
print("PASS: RITSUKO attack limits")

maintenance = section_between(
    "## MAGI-MAINT — vehicle and appliance maintenance profile",
    "## Independence provenance",
    "maintenance approval transition",
)
schedule_selection = "**Schedule selection**"
pre_execution_recheck = "**Pre-execution recheck**"
day_of_go_no_go = "**Day-of go/no-go**"
approval_transition = "PENDING-CONDITION → APPROVED"
for phrase in [
    schedule_selection,
    pre_execution_recheck,
    day_of_go_no_go,
    approval_transition,
]:
    assert phrase in maintenance, f"Missing maintenance approval transition invariant: {phrase}"
assert (
    maintenance.index(schedule_selection)
    < maintenance.index(pre_execution_recheck)
    < maintenance.index(day_of_go_no_go)
    < maintenance.index(approval_transition)
), "Maintenance approval transition must be schedule selection, pre-execution recheck, day-of go/no-go, then approval"
print("PASS: maintenance approval transition")

decision_engine = section_between(
    "## Phase 9 — Decision engine",
    "## Phase 10 — Robustness battery",
    "hard constraints precede consensus",
)
hard_constraints = "1. Hard constraints."
consensus = "9. Consensus as a final, non-binding signal."
assert hard_constraints in decision_engine, (
    "Missing hard constraints precede consensus invariant: " f"{hard_constraints}"
)
assert consensus in decision_engine, (
    "Missing hard constraints precede consensus invariant: " f"{consensus}"
)
assert decision_engine.index(hard_constraints) < decision_engine.index(consensus), (
    "Hard constraints must precede consensus in the decision engine"
)
print("PASS: hard constraints precede consensus")

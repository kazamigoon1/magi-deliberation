from pathlib import Path


readme = (Path(__file__).parents[1] / "README.md").read_text(encoding="utf-8")
workflow = (
    Path(__file__).parents[1] / ".github" / "workflows" / "validate.yml"
).read_text(encoding="utf-8")

required = [
    "# MAGI Deliberation\n\n> English",
    "# MAGI Deliberation — 한국어",
    "# MAGI Deliberation — 日本語",
    "## Overview",
    "## 개요",
    "## 概要",
    "RITSUKO",
]

missing = [item for item in required if item not in readme]
assert not missing, "Missing README sections: " + ", ".join(missing)

english = readme.index("# MAGI Deliberation\n\n> English")
korean = readme.index("# MAGI Deliberation — 한국어")
japanese = readme.index("# MAGI Deliberation — 日本語")
assert english < korean < japanese, "README must be English, Korean, then Japanese"

automation_headings = [
    "## Automated validation",
    "## 자동 검증",
    "## 自動検証",
]
assert all(heading in readme for heading in automation_headings)
assert readme.index(automation_headings[0]) < readme.index(automation_headings[1]) < readme.index(automation_headings[2])

workflow_commands = [
    line.strip()
    for line in workflow.splitlines()
    if line.strip().startswith("python tests/")
]
validation_blocks = [
    readme[readme.index("## Validate"):readme.index("## Automated validation")],
    readme[readme.index("## 검증"):readme.index("## 자동 검증")],
    readme[readme.index("## 検証"):readme.index("## 自動検証")],
]
for block in validation_blocks:
    readme_commands = [
        line.strip()
        for line in block.splitlines()
        if line.strip().startswith("python tests/")
    ]
    assert readme_commands == workflow_commands, (
        "README validation commands must exactly match workflow commands: "
        f"expected {workflow_commands}, got {readme_commands}"
    )

print("PASS: README provides English, Korean, and Japanese sections in order")

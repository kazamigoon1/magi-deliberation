from pathlib import Path


readme = (Path(__file__).parents[1] / "README.md").read_text(encoding="utf-8")

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

print("PASS: README provides English, Korean, and Japanese sections in order")

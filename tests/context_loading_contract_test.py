"""Check progressive loading cost and reference reachability, not LLM quality."""
from pathlib import Path
import re

root = Path(__file__).parents[1]
entry = (root / "SKILL.md").read_text(encoding="utf-8")
assert len(entry) <= 12000, "Entrypoint exceeds the compact loading budget"

for name in ("core-protocol.md", "maintenance.md", "full-output.md", "post-decision.md"):
    assert f"references/{name}" in entry, f"Unreachable conditional reference: {name}"
    assert (root / "references" / name).is_file(), f"Missing reference: {name}"

for path in [root / "SKILL.md", *(root / "references").glob("*.md")]:
    content = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", content):
        if "://" in target or target.startswith("#"):
            continue
        resolved = (path.parent / target.split("#")[0]).resolve()
        assert resolved.is_relative_to(root.resolve()), f"Reference escapes skill: {target}"
        assert resolved.exists(), f"Broken link in {path.name}: {target}"

core = (root / "references/core-protocol.md").read_text(encoding="utf-8")
assert len(entry + core) < 29000, "Standard loads too much unconditional guidance"
assert "Maintenance execution record" not in entry + core, "Maintenance must load conditionally"
assert "XVI. NEXT ACTION" not in entry + core, "Full output must load conditionally"
print("PASS: compact loading budgets, conditional references, and local links")

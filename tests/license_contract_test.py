from pathlib import Path


root = Path(__file__).parents[1]
license_text = (root / "LICENSE").read_text(encoding="utf-8")
readme = (root / "README.md").read_text(encoding="utf-8")

assert "MIT License" in license_text
assert "Copyright (c) 2026 kazamigoon1" in license_text
assert "Permission is hereby granted" in license_text
assert "## License" in readme
assert "MIT" in readme

print("PASS: MIT license is present and documented")

# CI and Protocol-Behavior Contracts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a read-only GitHub Actions validation gate and deterministic tests for MAGI protocol invariants.

**Architecture:** The repository keeps its zero-dependency Python test style. A new protocol test reads `SKILL.md` and verifies named protocol invariants; a single GitHub Actions workflow runs every repository-local test on Python 3.12. README language sections describe the same local and CI validation surface without claiming automated LLM evaluation.

**Tech Stack:** GitHub Actions, Ubuntu hosted runner, Python 3.12 standard library, Markdown, YAML.

**Spec:** `docs/superpowers/specs/2026-09-02-ci-behavior-contracts-design.md`

## Global Constraints

- Use no third-party Python dependencies, repository secrets, or write permissions.
- Trigger CI on `push` and `pull_request`.
- Use `actions/checkout@v6` and `actions/setup-python@v5` with Python `3.12`.
- Do not claim that static tests evaluate an LLM's generated deliberation quality.
- Preserve the existing English, Korean, and Japanese README order.

---

### Task 1: Add deterministic protocol-behavior contract coverage

**Files:**
- Create: `tests/protocol_behavior_contract_test.py`
- Read: `SKILL.md`
- Test: `tests/protocol_behavior_contract_test.py`

**Interfaces:**
- Consumes: UTF-8 text from repository-root `SKILL.md`.
- Produces: one `PASS: <invariant>` line per verified invariant; raises `AssertionError` naming a missing invariant.

- [ ] **Step 1: Write the contract test**

Create a standard-library Python script with a root-relative `SKILL.md` path.
Define this exact invariant map:

```python
invariants = {
    "P1 is perspective review": ["| **P1** | One model performed a perspective review"],
    "P3 requires separate parallel agents": ["| **P3** | Separate parallel agents reviewed the common packet"],
    "RITSUKO attack contract": [
        "Target claim:", "Defect class:", "Mechanism:",
        "Falsification condition:", "Verification method:", "Effect:",
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
```

For each map entry, collect missing fragments, raise one assertion that includes
the invariant name and missing fragments, then print a `PASS:` line.

- [ ] **Step 2: Run the new test against the current protocol**

Run:

```powershell
$env:PYTHONUTF8='1'
python tests/protocol_behavior_contract_test.py
```

Expected: six named `PASS:` lines. This is coverage for existing protocol
requirements, so a passing baseline confirms that the test observes the
intended current contract rather than a new production behavior.

- [ ] **Step 3: Commit the test**

```powershell
git add tests/protocol_behavior_contract_test.py
git commit -m "test: cover MAGI protocol behavior contracts"
```

### Task 2: Add the read-only GitHub Actions validation workflow

**Files:**
- Create: `.github/workflows/validate.yml`
- Read: `tests/skill_contract_test.py`, `tests/readme_contract_test.py`, `tests/license_contract_test.py`, `tests/protocol_behavior_contract_test.py`
- Test: GitHub Actions workflow run for the pushed commit

**Interfaces:**
- Consumes: a repository checkout.
- Produces: one `validate` job status for each push and pull request.

- [ ] **Step 1: Create the workflow**

Create `.github/workflows/validate.yml` with this exact structure:

```yaml
name: Validate

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run repository contract tests
        run: |
          python tests/skill_contract_test.py
          python tests/readme_contract_test.py
          python tests/license_contract_test.py
          python tests/protocol_behavior_contract_test.py
```

- [ ] **Step 2: Validate the workflow locally and push it**

Run:

```powershell
git diff --check
git add .github/workflows/validate.yml
git commit -m "ci: validate MAGI skill contracts"
git push origin master
```

Expected: push succeeds and creates a `Validate` workflow run.

- [ ] **Step 3: Verify the hosted workflow result**

Run:

```powershell
gh run list --workflow validate.yml --limit 1
gh run watch <run-id> --exit-status
```

Expected: the latest `Validate` run completes with `success`. If it fails,
inspect the failed step before modifying the workflow.

### Task 3: Document the automated validation contract in all README languages

**Files:**
- Modify: `README.md`
- Modify: `tests/readme_contract_test.py`
- Test: `tests/readme_contract_test.py`

**Interfaces:**
- Consumes: the README's existing English, Korean, Japanese section order.
- Produces: matching CI wording in all three language sections.

- [ ] **Step 1: Extend the README test before editing documentation**

Require all of these strings and their language-section order:

```python
automation_headings = [
    "## Automated validation",
    "## 자동 검증",
    "## 自動検証",
]
assert all(heading in readme for heading in automation_headings)
assert readme.index(automation_headings[0]) < readme.index(automation_headings[1]) < readme.index(automation_headings[2])
```

Run:

```powershell
$env:PYTHONUTF8='1'
python tests/readme_contract_test.py
```

Expected: FAIL because no automated-validation headings exist yet.

- [ ] **Step 2: Add matching language sections to README**

After each language's `Validate` section, add:

- English `## Automated validation`: GitHub Actions runs the four
  repository-local contract scripts for every push and pull request; it does
  not evaluate generated LLM output.
- Korean `## 자동 검증`: 동일한 사실을 자연스러운 한국어로 설명.
- Japanese `## 自動検証`: 同じ事実を自然な日本語で説明.

Do not add badges, status claims, API references, or secrets.

- [ ] **Step 3: Run the full local suite and commit**

Run:

```powershell
$env:PYTHONUTF8='1'
python tests/skill_contract_test.py
python tests/readme_contract_test.py
python tests/license_contract_test.py
python tests/protocol_behavior_contract_test.py
python C:\Users\HP\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
git diff --check
```

Expected: all tests print `PASS` and the validator prints `Skill is valid!`.

Commit and push:

```powershell
git add README.md tests/readme_contract_test.py
git commit -m "docs: describe automated validation in all languages"
git push origin master
```

### Task 4: Verify the final repository state

**Files:**
- Read: `.github/workflows/validate.yml`, `README.md`, `tests/*.py`
- Test: local suite and latest GitHub Actions run

**Interfaces:**
- Consumes: the merged repository state from Tasks 1–3.
- Produces: a clean working tree and a successful hosted validation run.

- [ ] **Step 1: Run all local checks**

Run the commands from Task 3, then:

```powershell
git status --short
```

Expected: all checks pass and `git status --short` emits no files.

- [ ] **Step 2: Confirm the final hosted check**

Run:

```powershell
gh run list --workflow validate.yml --limit 1
gh run watch <run-id> --exit-status
```

Expected: the final workflow run has conclusion `success`.

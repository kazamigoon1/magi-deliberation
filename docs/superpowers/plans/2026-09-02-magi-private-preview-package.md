# MAGI Private Preview Package Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a serverless Microsoft 365 Agents Toolkit declarative-agent package for selected users in separate work or school tenants to sideload in Teams and Microsoft 365 Copilot.

**Architecture:** Preserve `m365-copilot/declarativeAgent.json` as the source P1 contract and create an equivalent package under `appPackage/`. A standard-library Python builder emits a deterministic ZIP and SHA-256 checksum; contracts and CI keep product metadata and the no-action boundary intact.

**Tech Stack:** Microsoft 365 Agents Toolkit declarative-agent package, Teams/Microsoft 365 app manifest, JSON, Python 3.12 standard library, GitHub Actions, Markdown, PNG.

**Spec:** `docs/superpowers/specs/2026-09-02-magi-marketplace-private-preview-design.md`

## Global Constraints

- Support only eligible work or school accounts; personal Microsoft accounts are out of scope.
- Add no backend, credentials, Graph permissions, knowledge sources, actions, connectors, or user-data storage.
- Use fixed app ID `9c3b7be6-fc0b-4a99-8c73-2e4c9c7561aa`, app name `MAGI Deliberation`, and developer name `Kazamigoon`.
- Use HTTPS metadata URLs under `https://github.com/kazamigoon1/magi-deliberation`.
- Name artifacts `MAGI-Preview-<version>.zip` and `MAGI-Preview-<version>.zip.sha256`.
- Do not tag releases, upload to external tenants, or submit to Marketplace during implementation.

---

## File Structure

```text
appPackage/{manifest.json,declarativeAgent.json,color.png,outline.png,build/}
scripts/build_preview_package.py
docs/legal/{privacy-policy.md,terms-of-use.md,support.md}
docs/preview/{tenant-admin-install.md,tester-acceptance.md}
.github/ISSUE_TEMPLATE/private-preview-feedback.yml
.github/workflows/preview-release.yml
tests/{package_contract_test.py,preview_builder_test.py}
```

### Task 1: Define package behavior with failing contracts

**Files:**
- Create: `tests/package_contract_test.py`
- Modify: `tests/m365_personal_agent_contract_test.py`
- Modify: `.github/workflows/validate.yml`

**Interfaces:**
- Consumes: `m365-copilot/declarativeAgent.json`.
- Produces: `python tests/package_contract_test.py` and CI execution after existing contracts.

- [ ] **Step 1: Write the failing package contract**

```python
ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "appPackage"
MANIFEST = PACKAGE / "manifest.json"
AGENT = PACKAGE / "declarativeAgent.json"

def test_preview_package_is_a_stable_no_action_magi_app() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    agent = json.loads(AGENT.read_text(encoding="utf-8"))
    assert manifest["id"] == "9c3b7be6-fc0b-4a99-8c73-2e4c9c7561aa"
    assert manifest["name"]["short"] == "MAGI Deliberation"
    assert agent["version"] == "v1.8"
    assert "actions" not in agent and "capabilities" not in agent
    assert "P1" in agent["instructions"]
```

- [ ] **Step 2: Run the test and verify red state**

Run `python tests/package_contract_test.py`.

Expected: failure naming `appPackage/manifest.json`.

- [ ] **Step 3: Add source/package parity to the existing contract**

```python
def test_packaged_agent_matches_reference_p1_contract() -> None:
    reference = read_manifest()
    packaged = json.loads((ROOT / "appPackage/declarativeAgent.json").read_text(encoding="utf-8"))
    for key in ("name", "description", "instructions", "conversation_starters"):
        assert packaged[key] == reference[key]
```

- [ ] **Step 4: Add `python tests/package_contract_test.py` after the existing Microsoft 365 contract in CI**

- [ ] **Step 5: Run both contracts and confirm both fail only because package files are absent**

Run `python tests/m365_personal_agent_contract_test.py; python tests/package_contract_test.py`.

- [ ] **Step 6: Commit**

Run `git add tests/package_contract_test.py tests/m365_personal_agent_contract_test.py .github/workflows/validate.yml` and `git commit -m "test: define MAGI preview package contract"`.

### Task 2: Create the no-action app package

**Files:**
- Create: `appPackage/manifest.json`
- Create: `appPackage/declarativeAgent.json`
- Create: `appPackage/color.png`
- Create: `appPackage/outline.png`
- Modify: `.gitignore`
- Test: `tests/package_contract_test.py`
- Test: `tests/m365_personal_agent_contract_test.py`

**Interfaces:**
- Consumes: the Task 1 contract and the Agent Builder source definition.
- Produces: a Toolkit-valid package that references `declarativeAgent.json`.

- [ ] **Step 1: Generate a current Agents Toolkit baseline**

In VS Code choose **Microsoft 365 Agents Toolkit → Create a New Agent/App → Declarative Agent → No Action** in a disposable directory. Use its current manifest schema, host declarations, and packaging shape as the baseline; delete the disposable project afterward.

- [ ] **Step 2: Implement package identity and agent reference**

Preserve required Toolkit baseline fields and set:

```json
{
  "id": "9c3b7be6-fc0b-4a99-8c73-2e4c9c7561aa",
  "name": { "short": "MAGI Deliberation", "full": "MAGI Deliberation" },
  "developer": { "name": "Kazamigoon", "websiteUrl": "https://github.com/kazamigoon1/magi-deliberation" },
  "icons": { "color": "color.png", "outline": "outline.png" },
  "copilotAgents": { "declarativeAgents": [{ "id": "magiDeliberation", "file": "declarativeAgent.json" }] }
}
```

Do not add a bot, tab, web endpoint, permission, action, connector, or knowledge source.

- [ ] **Step 3: Copy P1 definition and add icons**

Run `Copy-Item m365-copilot/declarativeAgent.json appPackage/declarativeAgent.json`. Create valid nonempty color and outline PNG files matching Toolkit validation requirements. Add `appPackage/build/` to `.gitignore`.

- [ ] **Step 4: Verify green state**

Run `python tests/package_contract_test.py` and `python tests/m365_personal_agent_contract_test.py`, then run the current Toolkit baseline validation command against this package.

Expected: all Python contracts pass; Toolkit reports no manifest or icon error.

- [ ] **Step 5: Commit**

Run `git add appPackage .gitignore tests/package_contract_test.py tests/m365_personal_agent_contract_test.py` and `git commit -m "feat: add MAGI declarative preview package"`.

### Task 3: Add legal, support, onboarding, and feedback artifacts

**Files:**
- Create: `docs/legal/privacy-policy.md`
- Create: `docs/legal/terms-of-use.md`
- Create: `docs/legal/support.md`
- Create: `docs/preview/tenant-admin-install.md`
- Create: `docs/preview/tester-acceptance.md`
- Create: `.github/ISSUE_TEMPLATE/private-preview-feedback.yml`
- Modify: `README.md`
- Modify: `m365-copilot/README.md`
- Modify: `tests/package_contract_test.py`

**Interfaces:**
- Consumes: Task 2 identity and no-action product boundary.
- Produces: public GitHub HTTPS links and a redacted feedback route.

- [ ] **Step 1: Extend the failing contract for legal metadata**

```python
def test_preview_package_has_public_legal_and_support_documents() -> None:
    for name in ("privacy-policy.md", "terms-of-use.md", "support.md"):
        assert (ROOT / "docs/legal" / name).exists()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["developer"]["privacyUrl"].startswith("https://")
    assert manifest["developer"]["termsOfUseUrl"].startswith("https://")
```

- [ ] **Step 2: Verify red state**

Run `python tests/package_contract_test.py`.

Expected: failure naming `docs/legal/privacy-policy.md`.

- [ ] **Step 3: Write legal and support boundaries**

Include these exact statements across the three documents:

```text
MAGI Preview operates no MAGI-managed server, database, analytics service, external action, connector, or telemetry endpoint.
MAGI provides decision support only; it does not guarantee accuracy, replace professional judgment, or grant execution approval.
Do not submit passwords, access tokens, confidential business information, sensitive personal information, tenant identifiers, or unredacted conversation logs.
```

- [ ] **Step 4: Write administrator and tester runbooks**

The administrator runbook requires eligible work/school account verification, Custom App Upload policy confirmation, SHA-256 verification, ZIP upload, named-user/group assignment, and package-version/result recording. The tester sheet uses the fixed MAGI Standard prompt in Teams and Microsoft 365 Copilot and records `PASS`, `PRODUCT-DEFECT`, or `ENVIRONMENT-BLOCKED`.

- [ ] **Step 5: Add the feedback form**

Create required fields `Package version`, `Tenant type`, `Host product`, `Result`, and `Redacted observation`, plus this required checkbox:

```yaml
label: I removed secrets, personal data, tenant identifiers, and confidential prompt content.
required: true
```

- [ ] **Step 6: Link the preview path from both READMEs**

Link the administrator runbook, tester sheet, legal documents, and per-tenant authorization condition.

- [ ] **Step 7: Verify green state and commit**

Run `python tests/package_contract_test.py`, `python tests/readme_contract_test.py`, and `python tests/m365_personal_agent_contract_test.py`. Expected: PASS.

Run `git add docs/legal docs/preview .github/ISSUE_TEMPLATE README.md m365-copilot/README.md tests/package_contract_test.py` and `git commit -m "docs: add MAGI private preview runbooks"`.

### Task 4: Build a deterministic ZIP and checksum

**Files:**
- Create: `scripts/build_preview_package.py`
- Create: `tests/preview_builder_test.py`
- Test: `tests/preview_builder_test.py`

**Interfaces:**
- Consumes: `appPackage/` and a version shaped as `preview-v<major>.<minor>.<patch>`.
- Produces: `MAGI-Preview-<version>.zip` and matching `.sha256` in the output directory.

- [ ] **Step 1: Write failing builder tests**

```python
def test_builder_creates_allowed_members_and_matching_checksum(tmp_path: Path) -> None:
    result = run_builder(tmp_path, "preview-v0.1.0")
    archive = tmp_path / "MAGI-Preview-preview-v0.1.0.zip"
    assert result.returncode == 0
    assert archive.with_suffix(".zip.sha256").read_text().startswith(hashlib.sha256(archive.read_bytes()).hexdigest())
    with zipfile.ZipFile(archive) as package:
        assert set(package.namelist()) == {"manifest.json", "declarativeAgent.json", "color.png", "outline.png"}

def test_builder_rejects_non_preview_version(tmp_path: Path) -> None:
    assert run_builder(tmp_path, "v0.1.0").returncode != 0
```

- [ ] **Step 2: Verify red state**

Run `python tests/preview_builder_test.py`.

Expected: failure because `scripts/build_preview_package.py` is absent.

- [ ] **Step 3: Implement the builder interface**

```python
def build_preview_package(source_dir: Path, output_dir: Path, version: str) -> tuple[Path, Path]:
    """Return the ZIP and SHA-256 paths for a validated preview package."""
```

Validate version with `^preview-v[0-9]+\.[0-9]+\.[0-9]+$`. Allow only `manifest.json`, `declarativeAgent.json`, `color.png`, and `outline.png`. Write ZIP entries in that order with timestamp `(1980, 1, 1, 0, 0, 0)` and write the checksum as `<hex>  <filename>\n`. Expose `python scripts/build_preview_package.py --version preview-v0.1.0 --output appPackage/build`.

- [ ] **Step 4: Verify green state and commit**

Run `python tests/preview_builder_test.py`, build `preview-v0.1.0`, and compare `Get-FileHash` output with the `.sha256` file. Expected: matching hashes and ignored artifacts.

Run `git add scripts/build_preview_package.py tests/preview_builder_test.py` and `git commit -m "feat: build deterministic MAGI preview package"`.

### Task 5: Add CI and artifact-only preview automation

**Files:**
- Modify: `.github/workflows/validate.yml`
- Create: `.github/workflows/preview-release.yml`
- Modify: `tests/package_contract_test.py`

**Interfaces:**
- Consumes: Tasks 1–4.
- Produces: validation on push/PR and artifacts on `preview-v*` tag pushes; never creates a release.

- [ ] **Step 1: Write a failing workflow contract**

```python
def test_preview_workflow_builds_but_does_not_publish() -> None:
    workflow = (ROOT / ".github/workflows/preview-release.yml").read_text(encoding="utf-8")
    assert "preview-v*" in workflow
    assert "scripts/build_preview_package.py" in workflow
    assert "actions/upload-artifact" in workflow
    assert "gh release create" not in workflow
```

- [ ] **Step 2: Verify red state**

Run `python tests/package_contract_test.py`.

Expected: failure naming `.github/workflows/preview-release.yml`.

- [ ] **Step 3: Implement ordinary CI and tag workflow**

Append `python tests/package_contract_test.py` and `python tests/preview_builder_test.py` to `validate.yml`. Create `preview-release.yml` with this trigger and permission:

```yaml
on:
  push:
    tags: ["preview-v*"]
permissions:
  contents: read
```

It checks out source, sets Python 3.12, runs all contracts, invokes the builder with `${{ github.ref_name }}`, and uploads ZIP and checksum through `actions/upload-artifact@v4`. It must not request write permission or create a GitHub Release.

- [ ] **Step 4: Verify full local suite and commit**

Run every existing contract, `python tests/package_contract_test.py`, `python tests/preview_builder_test.py`, `python C:\Users\HP\.codex\skills\.system\skill-creator\scripts\quick_validate.py .`, and `git diff --check`.

Expected: every command succeeds with no whitespace error.

Run `git add .github/workflows/validate.yml .github/workflows/preview-release.yml tests/package_contract_test.py` and `git commit -m "ci: add MAGI preview package validation"`.

### Task 6: Run controlled two-tenant acceptance only after explicit authorization

**Files:**
- Modify: `docs/preview/tester-acceptance.md` only with a redacted result summary.

**Interfaces:**
- Consumes: reviewed ZIP/checksum, two eligible tenants, and each tenant administrator's approval.
- Produces: two `PASS` records or redacted `PRODUCT-DEFECT` / `ENVIRONMENT-BLOCKED` records.

- [ ] **Step 1: Confirm authority and readiness**

For each tenant, record administrator approval for Custom App Upload and named tester eligibility. Stop for that tenant if either is absent.

- [ ] **Step 2: Verify the package before upload**

```powershell
$expected = (Get-Content .\MAGI-Preview-preview-v0.1.0.zip.sha256).Split(' ')[0]
$actual = (Get-FileHash .\MAGI-Preview-preview-v0.1.0.zip -Algorithm SHA256).Hash.ToLower()
if ($actual -ne $expected) { throw 'Preview package checksum mismatch.' }
```

- [ ] **Step 3: Run the two-host acceptance prompt**

```text
MAGI Standard로 두 가지 계획을 비교해줘. 사실, 가정, 미확인 사항을 분리하고 P1 표기를 포함해줘.
```

Record `PASS` only when the agent loads in both hosts, visibly includes P1, separates fact/assumption/unknown, and makes no external-action claim. Record package/behavior failures as `PRODUCT-DEFECT`; license/policy denial as `ENVIRONMENT-BLOCKED`.

- [ ] **Step 4: Apply the exit gate and commit only redacted evidence**

Require PASS in both Teams and Microsoft 365 Copilot across two different tenants. Do not count `ENVIRONMENT-BLOCKED` as PASS. Repair each product defect under a new plan and retest. Commit only redacted summary text with message `docs: record MAGI preview acceptance summary`.

## Plan Self-Review

- Spec coverage: Tasks 1–2 implement the stable no-action package; Task 3 covers legal, support, onboarding, and feedback; Task 4 creates deterministic artifacts; Task 5 adds CI; Task 6 implements controlled multi-tenant acceptance and the Marketplace exit gate.
- Placeholder scan: the plan defines each artifact, command, test, and stop condition without incomplete work markers.
- Interface consistency: Task 1 defines package paths, Task 2 creates them, Task 4 emits artifacts consumed by Tasks 5–6, and Task 6 requires explicit external authority before any tenant upload.

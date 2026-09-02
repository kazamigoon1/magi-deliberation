# CI and Protocol-Behavior Contracts Design

## Goal

Run the MAGI skill's local contract checks automatically on every push and pull
request, and add deterministic checks for protocol rules that are more specific
than the existing heading and metadata assertions.

## Scope

This change adds one GitHub Actions workflow and one Python contract test. It
does not invoke an LLM, call a third-party API, require a repository secret, or
claim to evaluate generated deliberation quality. Real model-output evaluation
remains a separate manual or independently run acceptance activity.

## CI workflow

Create `.github/workflows/validate.yml` with these properties:

- Trigger on `push` and `pull_request`.
- Use one Ubuntu job with Python 3.12.
- Set workflow permissions to `contents: read`.
- Check out the repository with `actions/checkout@v6` and configure Python with
  `actions/setup-python@v5`.
- Run only standard-library Python commands:
  - `tests/skill_contract_test.py`
  - `tests/readme_contract_test.py`
  - `tests/license_contract_test.py`
  - `tests/protocol_behavior_contract_test.py`

The repository does not vendor skill-creator. Therefore the CI workflow cannot
depend on the local Codex installation path. The repository-local test suite is
the required CI gate; `quick_validate.py` remains an additional local check.

## Protocol-behavior contract test

Create `tests/protocol_behavior_contract_test.py`. It reads `SKILL.md` and
checks the written protocol's decision-relevant invariants:

1. **Independence truthfulness:** P1 is described as one-model perspective
   review, and P3 is limited to actual separate parallel agents.
2. **RITSUKO audit contract:** every listed field is present: target claim,
   defect class, mechanism, falsification condition, verification method, and
   effect. Quick mode is limited to one fatal attack; Standard and Full are
   limited to two material attacks.
3. **Maintenance state transition:** MAGI-MAINT keeps schedule selection at
   `PENDING-CONDITION` and allows `PENDING-CONDITION → APPROVED` only after
   day-of C0 checks pass.
4. **Hard-constraint precedence:** the decision engine processes hard
   constraints before safety, evidence, reversibility, benefits, human
   feasibility, robustness, and consensus.

The test reports each named invariant independently and exits nonzero on the
first missing invariant. It makes no assertion about a model's private
reasoning or real-world information retrieval.

## Repository documentation

Update all three README language sections to show the local test command and
state that GitHub Actions runs the repository-local contract suite. Do not
claim that CI evaluates LLM responses.

## Success criteria

- A clean checkout can run the four repository-local tests with Python 3.12
  and no installed packages.
- The workflow has no write permission and no secrets.
- A missing protocol invariant fails the corresponding named test.
- README instructions match the workflow's executable commands.

## Out of scope

- Automated LLM scoring or benchmark claims.
- GitHub release automation, badges, issue templates, and contribution policy.
- Changes to the MAGI decision protocol itself.

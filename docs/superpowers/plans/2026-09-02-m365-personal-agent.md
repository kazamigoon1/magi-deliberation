# Microsoft 365 Copilot Personal MAGI Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a private Microsoft 365 Copilot declarative-agent reference and Agent Builder input that faithfully expose MAGI 2.1 P1.

**Architecture:** Keep one Korean behavioral contract in an Agent Builder source and mirror it in a no-action schema 1.8 manifest. A Python contract test enforces P1, no-action boundaries, protocol markers, and instruction length.

**Tech Stack:** Markdown, JSON, Python 3 standard library, Microsoft 365 declarative-agent schema 1.8.

**Spec:** `docs/superpowers/specs/2026-09-02-m365-personal-agent-design.md`

## Global Constraints

- Agent Builder display name is at most 30 characters.
- Instructions are at most 8,000 characters and stay out of knowledge sources.
- The v1 artifact has no actions, capabilities, or knowledge sources.
- The agent always reports `P1 — perspective review`; it never claims P2 or P3.
- No external changes are executed.

---

### Task 1: Define the Microsoft 365 MAGI behavioral contract

**Files:**
- Create: `m365-copilot/agent-builder.md`
- Create: `m365-copilot/declarativeAgent.json`
- Test: `tests/m365_personal_agent_contract_test.py`

**Interfaces:**
- Consumes: MAGI 2.1 invariants and output contracts in `SKILL.md`.
- Produces: `instructions` strings and three conversation starters used by the validator.

- [ ] Write a failing Python contract test for schema version `v1.8`, no
  `actions`, P1 disclosure, four MAGI roles, three modes, and an 8,000-character
  instruction limit; run it and confirm the absent manifest fails.
- [ ] Add the Agent Builder source and manifest with the same Korean behavior,
  exactly three starters, no actions, capabilities, or knowledge; rerun the
  contract test and confirm it passes.
- [ ] Commit the behavioral contract with `feat: add personal Microsoft 365 MAGI agent`.

### Task 2: Document private creation and mobile verification

**Files:**
- Create: `m365-copilot/README.md`
- Modify: `README.md`
- Modify: `tests/m365_personal_agent_contract_test.py`

**Interfaces:**
- Consumes: Task 1 paths and behavioral markers.
- Produces: desktop setup instructions and an explicit mobile acceptance check.

- [ ] Extend the contract test to require private, desktop, mobile, and P1
  documentation; run it and confirm the missing guide fails.
- [ ] Add the setup guide and pointers in English, Korean, and Japanese README
  sections; run all existing repository tests plus the M365 contract test.
- [ ] Commit with `docs: explain personal Microsoft 365 MAGI setup`.

### Task 3: Integrate validation in CI

**Files:**
- Create: `.github/workflows/validate.yml`
- Modify: `README.md`
- Modify: `tests/m365_personal_agent_contract_test.py`

**Interfaces:**
- Consumes: the Task 1 validator and existing three repository contract tests.
- Produces: CI coverage for the Microsoft 365 artifact.

- [ ] Extend the M365 contract test to require its validation command in all
  README language sections; run it and confirm the README initially fails.
- [ ] Add a Python 3.12 GitHub Actions workflow that executes the three existing
  contract tests and the M365 test, and add matching commands to all README
  validation blocks.
- [ ] Parse JSON, run all four tests, run `git diff --check`, and commit with
  `ci: validate Microsoft 365 agent contract`.

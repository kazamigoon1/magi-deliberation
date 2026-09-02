# Microsoft 365 Copilot Personal MAGI Agent Design

## Goal

Provide a private, personal Microsoft 365 Copilot agent that applies MAGI 2.1
without claiming independent multi-agent execution that did not occur.

## Scope

The first release is a no-action declarative agent. It reasons over the user's
prompt and information Microsoft 365 Copilot can safely ground, but it does not
call external APIs, use a custom calendar action, create calendar events, send
messages, or modify data. The agent is private to its owner.

## User Experience

The user selects `MAGI Deliberation` in Microsoft 365 Copilot and asks a
decision question. The agent chooses Quick, Standard, or Full unless the user
explicitly selects a mode. It emits the matching output contract, labels the
result `P1 — perspective review`, and retains user decision authority.

The starter prompts cover everyday, technical, and vehicle-maintenance timing
decisions. The maintenance prompt may use MAGI-MAINT, but it must not assert
calendar, forecast, compatibility, or site facts without current evidence.

## Architecture

One canonical Korean behavioral contract drives two paths:

1. **Agent Builder (primary):** a concise copy/paste source creates the
   owner's private agent in Microsoft 365 Copilot desktop.
2. **Manifest reference (secondary):** a declarative-agent schema 1.8 source
   is retained for version control and later Agents Toolkit packaging. It is
   not presented as a sideloadable app package by itself.

Both paths deliberately use P1. A declarative-agent runtime alone does not
establish the separate parallel reviews required for P3.

## Contents

`m365-copilot/agent-builder.md` contains Agent Builder display metadata,
instructions, and starter prompts. `m365-copilot/declarativeAgent.json`
contains the same behavioral contract. `m365-copilot/README.md` documents
desktop creation, private-use verification, and the mobile verification
boundary. `tests/m365_personal_agent_contract_test.py` checks protocol markers,
P1 disclosure, no actions or knowledge sources, and the 8,000-character cap.

## Constraints

- Agent Builder display name is at most 30 characters.
- Instructions are at most 8,000 characters and never reside in a knowledge
  source as a workaround.
- The v1 manifest has no external actions, capabilities, or knowledge sources.
- The agent always reports `P1 — perspective review`; it never claims P2 or P3.
- The agent separates facts, assumptions, inferences, and unknowns.
- RITSUKO challenges a concrete claim only with a defect class, mechanism,
  falsification condition, verification method, and effect.
- The agent recommends next actions but never executes external changes.

## Security and Data Boundary

The artifact requests no additional app permissions, connector, or API plugin.
The user must not paste secrets, credentials, or sensitive personal data into a
decision request. Calendar, weather, web, or Graph integration is a separate
release requiring an explicit data-flow, authorization, and consent design.

## Verification

Automated checks parse the Agent Builder source and manifest and compare their
required behavior. They do not validate against a signed-in Microsoft 365
tenant. Manual acceptance requires private desktop creation, all three starter
prompts, confirmation of P1 disclosure, and a check for the agent in the
Microsoft 365 Copilot mobile app's Agents area.

## Non-goals

- Genuine P2/P3 orchestration.
- Organizational sharing or marketplace publication.
- Calendar, mail, weather, web, or Graph actions.
- Mobile authoring.

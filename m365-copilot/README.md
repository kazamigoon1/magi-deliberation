# MAGI Deliberation for Microsoft 365 Copilot

This folder contains the first **private** Microsoft 365 Copilot version of
MAGI Deliberation. It is an instruction-only declarative agent: it supports
decision review but has no actions, API plugins, connectors, or additional app
permissions.

For distribution outside the creator's organization, give each user
[INSTALL.md](INSTALL.md) and `agent-builder.md` so they can create the agent
in their own tenant.

## Requirements

- An account for which Microsoft 365 Copilot and Agent Builder are available.
- A **desktop** browser or Teams desktop/web client for authoring.

Agent Builder availability can be controlled by tenant policy. It is not
available for authoring on mobile. Microsoft documents the supported authoring
locations and limitations at [Agent Builder in Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder).

## Create the private agent

1. On desktop, open the [Microsoft Copilot app](https://m365.cloud.microsoft/chat)
   and sign in with the work or school account that will own the agent. The
   app can be branded as Microsoft 365 Copilot.
2. Confirm **Agents** and **New agent** are visible, then choose **New agent**.
   If either entry is absent, this Agent Builder route is not available for
   that account's license, tenant policy, or rollout state.
3. Select **Configure**.
4. Copy the display name, description, instructions, and three starter prompts
   from [agent-builder.md](agent-builder.md) into their matching fields.
5. Do not add a knowledge source, action, connector, or capability for this
   first version.
6. Select **Create**. Keep its sharing scope private; do not share it or submit
   it to an organizational catalog.

The first created agent is expected to remain private to its owner. Microsoft
documents private creation and later sharing at [Share and manage agents built
with Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-share-manage-agents).

## Acceptance check

Run each starter prompt. A successful result:

- starts with or otherwise visibly includes `Independence: P1 — perspective review`;
- distinguishes FACT, ASSUMPTION, INFERENCE, and UNKNOWN where relevant;
- names a single final state rather than silently treating a recommendation as
  execution approval; and
- does not claim to create events, send messages, buy items, or call services.

## Mobile check

Use the Microsoft 365 Copilot **mobile** app signed in with the same account.
Open **Agents**, locate `MAGI Deliberation`, and run the first starter prompt.
Record whether the private agent is visible and whether it produces the P1
label. This is an account-and-policy-dependent acceptance check: this artifact
does not claim universal mobile availability before that check passes.

## Version-controlled reference

`declarativeAgent.json` mirrors the Agent Builder behavior in schema 1.8 for
review and future Agents Toolkit packaging. It is not a complete sideloadable
Microsoft 365 app package on its own.

## Safety boundary

Do not paste passwords, access tokens, secrets, or sensitive personal records
into a MAGI request. Calendar, weather, web, or Microsoft Graph integration
requires a separate design that specifies data flow, authorization, consent,
and recheck behavior.

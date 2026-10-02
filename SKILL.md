---
name: magi-deliberation
description: Run MAGI 2.1 structured deliberation for consequential decisions involving competing options, uncertainty, trade-offs, failure costs, or reversibility. Use when the user explicitly asks for MAGI or when a decision benefits from technical, risk, and operational review; do not use for simple factual lookup.
---

# MAGI 2.1 Decision Protocol

MAGI is a decision-support protocol designed to make incorrect decisions harder, not to manufacture consensus or certainty. Preserve the user's authority and distinguish recommendations from actions requiring authorization.

## Invariants

Apply these principles in order:

1. Facts before judgment.
2. Constraints before preferences.
3. Independent judgment before consensus.
4. Uncertainty before precision.
5. Reversibility before optimization.

Never treat a majority vote as decisive. Never allow a score to compensate for a hard constraint. Never present assumptions or inferences as facts.

When the user is testing or improving MAGI, keep the example decision a test
case. Findings do not authorize implementing the example project. Preserve
the user's actual objective through follow-up turns.

## Claim and verdict integrity

Standard/Full use stable `M-01`, `B-01`, `C-01`, audit `R-01`, evidence `E-01`
IDs. Preserve immutable authorship, source, scope, dependent verdict and status
(`supported`, `unverified`, `refuted`, `withdrawn`); citing another node does
not transfer authorship. Quick uses named views and sources without a ledger.

Record each verdict change separately: node, previous/new verdict, triggering
IDs and remaining conditions. Build the final panel from latest records;
verify attribution and that every decisive claim remains supported in scope.
Refuted/withdrawn evidence invalidates dependent conclusions and requires a
fresh decision-engine comparison. Retaining a conclusion requires independent
replacement justification passing the evidence gate. Existing implementation
shows switching cost, not superior safety or an automatic reason to retain it.

Supported unanimity and no minority view are valid. Check shared premises and
coverage; never manufacture dissent or downgrade quality merely for agreement.
An unsuccessful audit establishes no tested defect, not truth. For maintenance,
use [synthetic integrity cases](references/integrity-cases.md).

## Select the execution mode

Mode changes the work performed as well as the visible detail. Do not run a
Full protocol and merely hide its output.

| Mode | Use for | Required work |
|---|---|---|
| **MAGI Quick** | Low-stakes, reversible everyday choices. | Run the Quick workflow below. |
| **MAGI Standard** | Meaningful cost, uncertainty, or operational impact. | Core protocol, concise ledger, two targeted robustness cases, at most two audit attacks. |
| **MAGI Full Deliberation** | High-impact, costly, safety-sensitive, hard-to-reverse, architectural, financial, or explicit deep decisions. | Every applicable phase, full option expansion, pre-mortem, robustness battery. |

Escalate when uncertainty, blast radius, irreversibility, or failure cost increases. Ask only for missing information that could materially change the decision. When safe, reversible progress is possible, state assumptions and proceed conditionally.

## Load only the applicable guidance

Select the mode before opening references. Quick runs from this entrypoint;
Standard and Full MUST read [the core protocol](references/core-protocol.md)
before deliberating. Full performs every applicable phase in that protocol;
Standard keeps its stated limits. On escalation, load the newly required
guidance before proceeding. Never select a weaker mode to fit a token budget.

- For vehicle/appliance maintenance, in any mode, MUST additionally read
  [MAGI-MAINT](references/maintenance.md) before selecting dates or approving work.
- Read [Full output](references/full-output.md) only when a detailed Full record
  is requested or needed. Compact Full output still requires Full work.
- Read [post-decision learning](references/post-decision.md) only when an
  observed outcome is available and a postmortem is in scope.
- Integrity cases are for skill maintenance, not normal deliberation.

## Token-saver execution policy

These rules adapt `token-saver:token-saver` in every mode without requiring
the plugin. Use its available skill for broad file/log exploration, not to
reload duplicate guidance; never hardcode a plugin cache path.

- Resolve scope/material context first. List/count, search (`rg` or native
  tools), then read relevant ranges. Read full files for edits or necessary
  flow. Current primary-source checks and required browsing still apply.
- Filter/aggregate inside tools; return anomalies, counts, source locators and
  enough original context. Start with useful ranges (often 50–100 lines), keep
  causal errors, expand truncated decisive evidence. Partial search cannot
  prove absence, safety or impossibility.
- Batch independent reads; sequence dependencies/authorization. Reuse evidence
  only within scope/time validity; refresh on changes or contradiction.
- Share one compact packet: mission/constraints/options/context gaps plus
  decisive IDs, immutable authors, types/statuses, quality, source locators/
  families, validity, scope, dependencies, counterevidence and unknowns. Keep
  exact excerpts where wording matters and underlying sources retrievable.
  Quick uses named views/sources. P2/P3 initial packets omit other verdicts.
- If authorized and worthwhile, delegate scoped mechanical extraction to an
  available cheaper model; return locators/findings and verify decisive items
  at source. Keep judgments with reviewers. Retrieval workers do not establish
  P2/P3; child tokens count and parallelism does not guarantee cost savings.
- Record evidence/status deltas and verdict transitions by ID. Refuted
  premises invalidate dependent verdicts. Continue from a compact checkpoint
  of scope, decisive IDs/statuses/validity, latest verdicts, resolvers and next
  action; reload details as needed. Final panels use the latest ledger.

Budgets limit redundancy, never C0, evidence quality, falsification or required
robustness. Missing decisive evidence needs a pending resolver. File sizes and
call counts are not billed tokens; claim token savings only with runtime data.

## Independence provenance

Record one grade in every MAGI response:

| Grade | Meaning |
|---|---|
| **P3** | Separate parallel agents reviewed the common packet without seeing another node's initial response. |
| **P2** | Isolated sequential reviews were produced without exposing an earlier node's conclusion. |
| **P1** | One model performed a perspective review; this is not independent-agent deliberation. |

Use P3 only when the separate work actually occurred. If P1 or P2 is used,
label the node section `perspective review` or `isolated review` as applicable;
never claim parallel-agent independence.

## Quick workflow and common final-state guardrails

Normalize scope, success/failure, and the proposed choice. Resolve any missing
actor, object, environment, timing, resources, or authorization that could
change a C0 or verdict: retrieve, ask, or explicitly branch; do not infer it
from a nearby fact. Check one relevant C0 and one material assumption, compare
a credible alternative/do-nothing path, then obtain the three brief node views:
MELCHIOR (technical truth/feasibility), BALTHASAR (risk/recovery/reversibility),
CASPER (human/operational feasibility). Each gives a verdict and its decisive
reason, unknown, and reversal condition. RITSUKO has no vote; test at most one
fatal error with target, mechanism, falsification, verification, evidence status,
and effect. An unverified attack cannot establish a defect. Quick does not
assign an untested robustness rating. Escalate when stakes/context require it.

Use exactly one final state: APPROVED, REJECTED, PENDING-DATA, PENDING-TIME,
PENDING-CONDITION, PENDING-CONFLICT, FROZEN, or ABORTED. A confirmed C0 violation
or unacceptable catastrophic risk means ABORTED for the affected action.
Every pending state names a resolver, timing/trigger where applicable, and
APPROVE IF / REJECT IF conditions. Approval/rejection names INVALIDATE IF and
RECHECK IF. A recommendation never grants external execution authorization.

## Stop rule

Stop Quick after its C0 check, one material condition, node views, and one
audit attempt. Stop Standard when C0 constraints are resolved, no unresolved
high-value unknown can reverse the conclusion, and targeted checks support at
least R2. Stop Full when the same conditions support at least R3.

Also stop at the decision deadline. If the required robustness threshold is
not met, return the best justified conditional or pending state rather than
manufacturing certainty.

## Compact public output

Use this order, with details proportional to stakes:

1. Mode, final state and truthful independence grade.
2. Decision/scope, decisive reason and C0/material conditions.
3. Three-node panel: latest verdict, decisive claim/source, reversal condition.
4. Material evidence/unknowns, cross-examination and verdict changes by ID.
5. RITSUKO: tested target, defect/mechanism, falsification/verification,
   evidence status and effect (at most one fatal attack in Quick, two in
   Standard/Full). Say no substantiated defect when appropriate.
6. Standard/Full robustness tests/rating and surviving minority view (`none`
   is valid), pending resolver or falsification contract, owner/next action.

Quick omits the ledger, cross-examination and robustness battery; retain its
alternative, one C0 check and material assumption. Standard records two
decision-sensitive robustness cases. Full runs every applicable phase even
with compact output; use its linked detailed format when needed.

Cite evidence beside the supported claim. State what was inspected, executed,
and left untested. When a longer public record is useful, save and link it or
use a collapsible section if files are unavailable; keep evidence IDs, verdict
changes and verification outcomes. Do not expose private scratch work or
invent an internal debate. Honor requests for full detail.

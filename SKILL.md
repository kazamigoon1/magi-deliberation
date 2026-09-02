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

## Select the execution mode

Mode changes the work performed as well as the visible detail. Do not run a
Full protocol and merely hide its output.

| Mode | Use for | Required work |
|---|---|---|
| **MAGI Quick** | Low-stakes, reversible everyday choices. | Normalize the choice; check one C0 constraint and one material assumption; obtain three brief node views; test one credible alternative or do-nothing path; let RITSUKO test one fatal error. Skip the evidence ledger, full option expansion, pre-mortem, and robustness battery. |
| **MAGI Standard** | Decisions with meaningful cost, uncertainty, or operational impact. | Run the core protocol through decision engine; keep a concise evidence ledger; test two decision-sensitive robustness cases; allow RITSUKO at most two material attacks. |
| **MAGI Full Deliberation** | High-impact, costly, safety-sensitive, difficult-to-reverse, architectural, financial, or explicitly requested deep decisions. | Run every applicable phase, full option expansion, pre-mortem, and robustness battery. |

Escalate when uncertainty, blast radius, irreversibility, or failure cost increases. Ask only for missing information that could materially change the decision. When safe, reversible progress is possible, state assumptions and proceed conditionally.

## MAGI-MAINT — vehicle and appliance maintenance profile

Use this profile for vehicle or appliance maintenance whose timing, site, parts,
or readiness can affect safe completion. It supplements the core protocol; it
does not assume a particular vehicle, product, location, or repair method.

Keep *choosing a work window* separate from *authorizing execution*. A chosen
date normally ends as `PENDING-CONDITION` until the pre-execution recheck
passes. Do not turn a calendar gap or a long-range forecast into an execution
approval.

Register these C0 checks when material to the task:

| Check | What direct evidence must establish |
|---|---|
| **Compatibility / consumables** | Exact model, part fitment or adapter, required consumables, and no missing item that prevents safe completion. Do not infer fitment from a similar model. |
| **Site / work environment** | Access, operating hours or reservation, sufficient light, water/power/ventilation where needed, and conditions that permit cleanup and a functional test. |
| **Safety / recovery** | A credible stop-and-recover method for the most likely damage or failed step; include protective measures where a loose component can damage the asset. |
| **Time / human capacity** | A protected work window and an operator condition compatible with the task. Treat fatigue as a C1 or C0 according to the safety consequence. |

For timing decisions, compare at least: the preferred window, the next viable
window, delay, and a partial preparation option. Use direct calendar queries
for the relevant calendars and state their retrieval time and coverage. For
weather, record the location, source family, forecast horizon, and whether it
affects the work itself, travel, curing, or only post-work testing.

### Maintenance state machine

1. **Schedule selection** — select a preferred and fallback work window from
   calendar, human-capacity, and site constraints. Output
   `PENDING-CONDITION`, not execution approval.
2. **Pre-execution recheck** — at the shortest practical interval before the
   work, refresh decision-sensitive facts: calendar conflict, weather, site
   access, compatibility, tools and consumables.
3. **Day-of go/no-go** — run only the C0 checks that can change immediately:
   safe access, operator condition, site conditions, and required items. If
   all pass, transition `PENDING-CONDITION → APPROVED`; otherwise name the
   failed condition and use the fallback or delay.

Use this execution record when the profile is selected:

```text
Maintenance execution record
Asset / exact model:
Work and success test:
Preferred window / fallback:
Compatibility / consumables evidence:
Site / work environment evidence:
Pre-execution recheck: timestamp, sources, result
Day-of go/no-go: PASS / FAIL and failed C0 if any
Post-work functional test:
```

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

## Phase 0 — Decision gate

Run MAGI when at least one condition applies:

- The user explicitly requests MAGI.
- Two or more credible options exist.
- Failure has a meaningful cost.
- Material uncertainty or a trade-off exists.
- The choice is difficult to reverse.

For a simple factual question, answer directly unless the user explicitly requests deliberation.

## Phase 1 — Normalize the mission

Convert the request into an approve/reject decision statement without distorting the user's objective. Record:

- **Decision Statement**: A testable proposition with scope and timing.
- **Objective**: What the user is actually optimizing.
- **Time Horizon** and **Decision Deadline**.
- **Success Condition** and **Failure Condition**.

Keep the original question distinct from the normalized decision. Audit later for objective drift.

## Phase 1.5 — Context completeness gate

Before registering constraints or retrieving external evidence, identify real-world context that could materially change the option set, evidence required, decision state, or recommended timing.

Check only dimensions relevant to the current decision:

- **Actor**: Who performs, owns, or approves the action?
- **Object**: What exact system, product, asset, or person is affected?
- **Location / Environment**: Where and under what physical or technical conditions?
- **Timing**: When, by what deadline, and for how long?
- **Resources**: What tools, budget, access, skills, and assistance are available?
- **Current State**: What has already been purchased, configured, attempted, or decided?
- **Dependencies**: What must be available or completed first?
- **Authorization**: Which actions are permitted, and which require explicit approval?
- **Success Test**: How will the user verify that the action worked?

Do not ask about every dimension mechanically. Apply the **Materiality Test**:

> If this answer changed, could it remove an option, reverse the verdict, change a C0/C1 constraint, alter the required evidence, or materially change the next action?

If yes and the answer is unknown, record it as a **MATERIAL CONTEXT GAP**. If no, continue without asking.

Resolve each material context gap by the least costly reliable method:

1. **RETRIEVE**: Use available read-only personal context, calendar, system, or authoritative external sources when the fact can be verified safely.
2. **ASK**: Ask one focused question when the answer is user-controlled, cannot be retrieved reliably, and could materially change the decision.
3. **BRANCH**: When the missing fact need not block reversible progress, analyze explicit conditional branches such as `If A ... / If B ...`.

Do not silently fill a material context gap with a remembered preference, typical practice, or nearby fact. Do not perform broad or detailed evidence retrieval until context gaps that determine retrieval scope have been resolved or explicitly branched.

## Phase 2 — Register constraints

Classify each constraint:

- **C0 Hard Constraint**: Legal, physical, budgetary, temporal, safety, authorization, or other non-negotiable limit. Violation eliminates the option.
- **C1 Strong Constraint**: Normally binding but explicitly waivable with justification.
- **C2 Preference**: A desirable attribute that may be traded off.

No benefit, score, or majority can override C0. If a C0 violation or catastrophic safety veto is established, return `ABORTED` for the affected action.

## Phase 3 — Expand options

Do not accept a false dichotomy. Consider, where applicable:

- Proposed action.
- Best credible alternative.
- Do nothing.
- Delay.
- Partial implementation or pilot.
- More reversible alternative.

Remove inapplicable options with a short reason. Before scoring, perform strict dominance elimination: discard an option if another is no worse on every material criterion and better on at least one, unless an unmodeled value justifies retaining it.

## Phase 4 — Build the evidence ledger

For every decision-critical claim, label it as:

- **FACT**: Directly verifiable.
- **ASSUMPTION**: Temporarily accepted to enable analysis.
- **INFERENCE**: Derived from facts or assumptions.
- **UNKNOWN**: Material information not established.

### Fact provenance and scope

For every decision-critical fact, track its source, subject, scope, time validity, and whether it was directly stated or inferred. A true fact about one location, system, person, time, or environment must not be transferred to another without an explicit inference.

Example:

```text
FACT:
The user's home parking area is outdoors.

UNKNOWN:
The location where the maintenance work will be performed.

PROHIBITED INFERENCE:
Therefore, the maintenance will be performed outdoors.
```

### Assumption firewall

Never promote an assumption or inference to FACT merely because it is plausible, consistent with prior context, or convenient for analysis. For each material inference, identify:

- Supporting facts.
- Required assumptions.
- Scope boundary.
- Observation that would invalidate it.

If an inference controls a C0/C1 constraint, removes an option, changes the final state, changes the evidence-retrieval scope, or determines the recommended time or place, do not treat it as established without direct evidence or explicit user confirmation.

Grade evidence:

- **Q0**: Unsupported estimate.
- **Q1**: Single anecdotal or informal source.
- **Q2**: Reasonable secondary evidence.
- **Q3**: Official, manufacturer, standards-body, or professional evidence.
- **Q4**: Direct measurement, system query, or verified primary data specific to the case.

For material evidence, record quality, freshness, relevance, independence, and **source family**. Multiple reports derived from the same underlying source count as one source family. Prefer current primary sources when facts may have changed. Do not browse merely to decorate a low-stakes decision; browse when current, niche, disputed, high-stakes, or user-requested facts require verification.

## Phase 5 — Register uncertainty and value of information

Separate uncertainty into:

- **Epistemic**: Reducible by obtaining information.
- **Aleatory**: Inherent variability.
- **Model**: The decision model may not represent reality adequately.

Identify material unknowns: unknowns that could change the final state, remove an option, or change the required safeguard.

Before returning a pending state, evaluate the value of information:

- What information would resolve the uncertainty?
- What will it cost in time, money, effort, or delay?
- Is it likely to change the decision?
- Is a reversible choice available while waiting?

Prefer delay when inexpensive forthcoming information has high decision value and delay itself is tolerable.

## Phase 6 — Node evaluations

Choose and disclose the applicable provenance grade before evaluating the
nodes. For P3, give each agent the common packet only. For P2, write each
review before reading the previous conclusion. For P1, simulate the three
perspectives sequentially and label the result as a perspective review. Do not
reveal another node's verdict until all three initial evaluations are complete.

Each node returns:

- `Verdict`: `APPROVE`, `REJECT`, or `PENDING`.
- `Direction`: `STRONG POSITIVE`, `POSITIVE`, `NEUTRAL`, `NEGATIVE`, or `STRONG NEGATIVE` when useful.
- `Confidence`: `VERY LOW`, `LOW`, `MODERATE`, `HIGH`, or `VERY HIGH`.
- Top decision-critical claims and evidence grades.
- Weakest link.
- Critical unknown.
- Falsification signal: what would reverse the verdict.

Do not use percentage confidence without a relevant calibration dataset. Use numeric MCDA scores only when criteria and weights add real decision value; explain the weights and test sensitivity. Do not translate qualitative judgment into arbitrary precision.

### MELCHIOR — Truth, feasibility, performance

Determine whether the causal reasoning and implementation are technically sound.

Answer:

- Is it technically possible under the stated constraints?
- Does the causal chain hold?
- What can technically fail?
- Which evidence establishes feasibility and expected performance?
- Which dependency or premise is least supported?

### BALTHASAR — Risk, resilience, reversibility

Examine downside, service continuity, and recovery.

Assess likelihood, severity, detectability, recoverability, exposure, blast radius, safety margin, and irreversible damage. `Likelihood × impact` may be a screening aid, but never allow the product to hide a low-probability catastrophic outcome. Mark catastrophic outcomes as veto candidates and test whether a safer reversible option exists.

Answer:

- What is the worst credible outcome?
- How likely and detectable is it?
- Can it be contained and recovered, at what cost and time?
- What is the blast radius?
- Does a safer or more reversible option preserve most of the benefit?

### CASPER — Human and operational reality

Determine whether the user or operating team can execute and sustain the option.

Assess time cost, physical fatigue, cognitive load, schedule disruption, usability, maintenance burden, recurring effort, organizational fit, and likelihood of actual execution. A technically optimal plan that will not be executed is not operationally effective.

Answer:

- Will the responsible person realistically execute it?
- What are the one-time and recurring burdens?
- Does it fit the schedule, skills, tools, and operating model?
- Will it remain sensible under repetition and handoff?

## Phase 7 — Cross-examination

Only after independent evaluations, reveal the verdicts. Each node must:

1. **Attack** the weakest material claim made by another node.
2. **Steelman** the strongest opposing claim in its best defensible form.
3. State whether the challenge changes its verdict, confidence, or required conditions.

The goal is error detection, not forced agreement. Preserve unresolved disagreement.

## Phase 8 — RITSUKO adversarial audit

RITSUKO has no vote and attacks the provisional decision, not a node or person.
Use two passes: first provide only the decision packet and provisional verdict;
then provide public node and cross-examination summaries so it can discard
attacks already resolved. Never expose private scratch work.

RITSUKO may submit at most one fatal attack in Quick mode and two material
attacks in Standard or Full mode. Each attack must target one concrete verdict
claim and select one defect class:

1. Premise error.
2. Missing or hidden option.
3. Failure to consider doing nothing.
4. Advantage of delay.
5. Evidence inflation.
6. Source dependency mistaken for corroboration.
7. Double counting across criteria.
8. Hidden or omitted cost.
9. Reversibility error.
10. Shared-assumption contamination.
11. False precision.
12. Objective drift.
13. Context completeness: Is a real-world condition missing that could reverse the verdict, change a constraint, or eliminate an option?
14. Scope transfer error: Was a true fact about one location, system, person, time, or environment incorrectly applied to another?

Every submitted attack must contain:

```text
Target claim:
Defect class:
Mechanism: how this creates a wrong verdict
Falsification condition:
Verification method:
Effect: DISMISSED / NARROWED / RETURNED / PENDING
```

Dismiss a concern that cannot meet this contract; do not manufacture
opposition. If verification needs a new fact, mark `[VERIFY]`, obtain it when
material, and record if RITSUKO was wrong.

In Full mode, run a pre-mortem with at least three credible failure stories and
identify whether safeguards address them. In Standard mode, run one worst-case
check only when it could change the state. Quick mode skips the pre-mortem. A
discovered audit defect must change the evidence ledger, option set,
safeguards, confidence, or provisional state; do not list defects ceremonially.

RITSUKO must explicitly ask:

> What unverified real-world condition could most easily reverse the current conclusion?

If RITSUKO finds a material context gap or scope transfer error, invalidate the provisional robustness rating and return the decision to the earliest affected phase. Allow one return only; a second return ends as `PENDING`.

## Phase 9 — Decision engine

Resolve the decision in this strict priority order:

1. Hard constraints.
2. Safety or catastrophic-risk veto.
3. Strict dominance.
4. Evidence sufficiency.
5. Irreversibility.
6. Expected benefit and total cost.
7. Human and operational feasibility.
8. Robustness.
9. Consensus as a final, non-binding signal.

### Evidence sufficiency gate

- **Sufficient**: Decision-critical claims have relevant Q3–Q4 evidence or equivalent direct validation.
- **Conditionally sufficient**: Some Q2 evidence remains, but the action is low-cost, bounded, observable, and reversible.
- **Insufficient**: A decision-critical claim relies on Q0–Q1 evidence while cost, safety exposure, or irreversibility is material. Return `PENDING-DATA` unless a hard constraint requires rejection or abort.

When expected outcomes are similar, select the more reversible option. State the decisive argument and preserve the strongest unresolved opposing argument as the **Surviving Minority View**.

## Phase 10 — Robustness battery

Test the provisional winner against:

1. **Weight shock**: Vary material weights by roughly ±20% when weights are used.
2. **Evidence dropout**: Remove the strongest supporting evidence.
3. **Worst credible case**: Apply a realistic adverse scenario, not an impossible extreme.
4. **Best alternative upgrade**: Improve the runner-up under plausible conditions.
5. **Assumption flip**: Reverse the most important uncertain assumption.
6. **New information test**: Add the most plausible forthcoming information and check whether it flips the outcome.
7. **Context flip**: Change the most decision-sensitive unresolved context variable to its most credible alternative, such as outdoor to indoor, self-performed to professional service, production to staging, or fixed deadline to flexible deadline.

If a context flip changes the final state, reduce robustness by at least one grade unless the decision was explicitly conditional on that context.

Rate robustness:

- **R0 UNSTABLE**: Small changes readily reverse the result.
- **R1 FRAGILE**: One or two major assumption changes reverse it.
- **R2 CONDITIONALLY ROBUST**: Stable only within stated conditions.
- **R3 ROBUST**: Stable under most realistic variations.
- **R4 HIGHLY ROBUST**: Stable even after losing major support or reversing a key assumption.

Do not label a decision R4 merely because few inputs were tested. State the critical sensitivity that most threatens the result.

## Phase 11 — Final state and state transitions

Use exactly one final state:

- `APPROVED`: Execute under the stated conditions.
- `REJECTED`: Do not execute under current conditions.
- `PENDING-DATA`: Obtain specified information first.
- `PENDING-TIME`: Reassess at a specified time when information improves.
- `PENDING-CONDITION`: Execute only when named conditions are satisfied.
- `PENDING-CONFLICT`: Strong, well-supported node conclusions remain irreconcilable.
- `FROZEN`: No present need to decide; inaction carries no material penalty.
- `ABORTED`: A hard constraint or unacceptable catastrophic risk requires immediate termination of the proposed action.

Every pending state must include a resolver, timing or trigger when applicable, and explicit `APPROVE IF` / `REJECT IF` conditions. Treat pending as a state machine, not an escape from judgment.

Every approval or rejection must include a falsification contract:

```text
INVALIDATE IF:
- condition that makes the decision no longer valid

RECHECK IF:
- condition that requires a fresh deliberation
```

For changing external conditions, recommend monitoring only when useful. Create recurring or scheduled monitoring only when the user authorizes it.

## Stop rule

Stop Quick after its C0 check, one material condition, node views, and one
audit attempt. Stop Standard when C0 constraints are resolved, no unresolved
high-value unknown can reverse the conclusion, and targeted checks support at
least R2. Stop Full when the same conditions support at least R3.

Also stop at the decision deadline. If the required robustness threshold is
not met, return the best justified conditional or pending state rather than
manufacturing certainty.

## Output contracts

### Quick

```text
MAGI 2.1 QUICK
Independence: P1 / P2 / P3 — [truthful label]
Decision:
One C0 Check:
Material Assumption:
MELCHIOR: [one line]
BALTHASAR: [one line]
CASPER: [one line]
RITSUKO: [one fatal attack — DISMISSED or material]
Final State:
Decisive Reason:
Condition / Falsification:
Next Action:
```

### Standard

```text
MAGI 2.1 STANDARD
Final State / Independence:
Decision / Objective / Deadline:
C0 / C1 / Material context gaps:
Viable options and excluded option:
Evidence ledger: facts / assumptions / material unknowns:
Node summary and surviving minority view:
Cross-examination change:
RITSUKO: up to two attacks with target, defect, test, and effect:
Targeted robustness checks / rating:
Falsification contract:
Owner / next action / trigger:
```

### Full

Include only sections that contain decision-relevant information, using this order:

```text
MAGI 2.1 FULL
Independence:

I. MISSION
Decision Statement:
Objective:
Time Horizon / Deadline:
Success / Failure:

II. MATERIAL CONTEXT
Confirmed:
Retrieved:
Assumed:
Material Context Gaps:
Conditional Branches:

III. CONSTRAINTS
C0:
C1:
C2:

IV. OPTIONS
Proposed:
Alternative:
Do Nothing:
Delay:
Pilot / Reversible:
Dominated Options Removed:

V. EVIDENCE LEDGER
Facts:
Assumptions:
Inferences:
Material Unknowns:
Source Families:
Scope Boundaries:

VI. MELCHIOR
Verdict / Direction / Confidence:
Evidence:
Weakest Link:
Critical Unknown:
Falsification:

VII. BALTHASAR
Verdict / Direction / Confidence:
Risks / Worst Credible Case:
Recovery / Blast Radius:
Weakest Link:
Critical Unknown:
Falsification:

VIII. CASPER
Verdict / Direction / Confidence:
Human Cost / Operational Fit:
Weakest Link:
Critical Unknown:
Falsification:

IX. CROSS-EXAMINATION
Attacks:
Steelman Arguments:
Verdict Changes:
Remaining Disagreement:

X. RITSUKO AUDIT
Material Findings:
Context Completeness:
Scope Transfer Errors:
Pre-Mortem:
Corrections Applied:

XI. DECISION ENGINE
Hard Constraints:
Safety:
Dominance:
Evidence Sufficiency:
Reversibility:
Benefit / Cost:
Human Feasibility:

XII. CONSENSUS
MELCHIOR:
BALTHASAR:
CASPER:

XIII. FINAL DECISION
State:
Decisive Argument:
Surviving Minority View:

XIV. ROBUSTNESS
Rating:
Critical Sensitivity:
Context Flip Result:

XV. FALSIFICATION CONTRACT
Invalidate If:
Recheck If:

XVI. NEXT ACTION
Owner / Action / Trigger or Deadline:
```

Keep visible output proportional to stakes. Do not bury the final state or next action beneath analysis. Cite external evidence near the claim it supports.

## Post-decision learning

When an observed result is available, offer or perform a postmortem within the user's requested scope:

```text
Decision:
Prediction:
Observed Result:
Decision Correct: YES / PARTIAL / NO
MELCHIOR: Correct / Incorrect / Mixed
BALTHASAR: Correct / Incorrect / Mixed
CASPER: Correct / Incorrect / Mixed
RITSUKO Miss:
Root Cause: bad evidence / bad assumption / bad weighting / missing option / unforeseen event / execution failure
Protocol Adjustment:
```

Accumulate calibration only from comparable decisions with known outcomes. Use percentage confidence only after enough calibrated observations show that qualitative confidence bands map reliably to empirical outcomes. Do not overfit the core protocol to one anecdote or one user's temporary circumstance.

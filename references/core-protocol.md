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
perspectives sequentially and label the result as a perspective review. In
P2/P3, withhold other node verdicts until initial evaluations are complete.
In P1, completing each perspective before synthesis is presentation order,
not information isolation; a shared context cannot forget earlier conclusions.

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

After initial evaluations, compare the verdicts. Each node must:

1. **Test** the weakest material claim made by another node. Submit an attack
   only when a defensible objection exists; otherwise record no material defect.
2. **Steelman** the strongest opposing claim when one exists. If none exists,
   test a shared premise without inventing an opposing vote.
3. State whether the challenge changes its verdict, confidence, or required conditions.

The goal is error detection, not forced agreement. Preserve unresolved disagreement.

Before the audit, apply Phase 9's priority order to the current evidence to
form a provisional verdict and list its decisive claim IDs. Phase 9 then
re-evaluates that verdict after the audit; Phase 10 tests its robustness.
Do not assign a robustness rating before those tests have been performed.

## Phase 8 — RITSUKO adversarial audit

RITSUKO has no vote and attacks the provisional decision, not a node or person.
Use two passes: first provide only the decision packet and provisional verdict;
then provide public node and cross-examination summaries so it can discard
attacks already resolved. Never expose private scratch work.

That withholding requires an actually isolated auditor context. In P1,
re-examine the packet and provisional verdict first, then check prior public
summaries for resolved objections, but label the audit non-isolated. Earlier
content remains visible; never claim a fresh or blind auditor in that mode.

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

Apply the same evidence standard to RITSUKO as to the nodes. Separate an
attack's plausible mechanism from proof that its falsification condition is
true. Record `confirmed`, `unverified`, or `refuted`, the evidence IDs, and
which dependent claims are affected. An unverified attack cannot establish
that MAGI is wrong; if it identifies a material evidence gap, it may instead
justify a pending state with a named verification task. A confirmed attack
changes only the claims within its demonstrated scope. For example, matching
identity fields do not prove that all audit events are indistinguishable or
that every related credential is irrevocable.

In Full mode, run a pre-mortem with at least three credible failure stories and
identify whether safeguards address them. In Standard mode, run one worst-case
check only when it could change the state. Quick mode skips the pre-mortem. A
discovered audit defect must change the evidence ledger, option set,
safeguards, confidence, or provisional state; do not list defects ceremonially.

RITSUKO must explicitly ask:

> What unverified real-world condition could most easily reverse the current conclusion?

If RITSUKO finds a material context gap or scope transfer error, invalidate any existing robustness rating and return the decision to the earliest affected phase. Allow one return only; unresolved uncertainty requiring a second return ends with the applicable `PENDING-DATA`, `PENDING-CONDITION`, `PENDING-TIME`, or `PENDING-CONFLICT` state and its resolver, never a generic `PENDING` final state. This limit never overrides a confirmed C0 violation or unacceptable catastrophic risk: return `ABORTED` for the affected action under Phase 2.

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

When expected outcomes are similar, select the more reversible option. State the decisive argument and preserve the strongest unresolved opposing argument as the **Surviving Minority View**. If none remains, state `none`; do not invent one.

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

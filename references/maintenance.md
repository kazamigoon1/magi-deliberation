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

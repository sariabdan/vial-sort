---
layout: ../../layouts/Doc.astro
title: "Arm test, 4 Nov: π0.5 B at 4000 steps"
date: "2026-11-04"
description: "The first retrain on the 220 contrastive demonstrations lost its grasp. The cause was a normalisation mismatch, not the policy."
---

Checkpoint `outputs/pi05_full_vial-sort-ws220_canon_ft012000/checkpoints/004000`
(B = 4000 steps from base12k 012000, LR 1e-5, batch 16, trimmed 220 episodes, no depth).
Sessions: the session log. Sync mode, 5 cameras.

## Rollouts, as recorded at the robot (the operator's words)

| # | move | outcome |
|---|---|---|
| 1 | ? | missed placing (also was going for slot 5) |
| 2 | R1 → L3 | **successful** |
| 3 | R6 → L1 | **successful** |
| 4 | L3 → R6 | failed pickup (but not missed) |
| 5 | L3 → R6 | failed pickup (but not missed) |
| 6 | L1 → R6 | failed pickup (but not missed) |
| 7 | L6 → R3 | missed placing (also was going for slot 5) |
| 8 | R3 → L3 | arm was moving very fast that it shutdown (3 times! one after the other) |
| 9 | R3 → L6 | missed dest (but was going to slot 6) and then shutdown |
| 10 | R3 → L6 | put in 5th slot |
| 11 | R3 → L1 | missed dest (but was going for slot 1 and barely did it) |
| 12 | R3 → L3 | put in slot 2 |
| 13 | R1 → L1 | put in slot 2 |
| 14 | R1 → L6 | failed pickup |
| 15 | R1 → L6 | **successful** |
| 16 | R6 → L3 | put in slot 2 |
| 17 | R6 → L6 | missed pickup |
| 18 | R6 → L6 | barely picked up but didnt |
| 19 | L1 → R1 | barely successful (but dropped aka missed dest) |
| 20 | L1 → R1 | missed pickup |
| 21 | L1 → R3 | missed dest |
| 22 | L3 → R3 | put in slot 2 |
| 23 | L3 → R1 | missed pickup |
| 24 | L3 → R1 | **successful** |
| 25 | R1 → bin | failed pickup |
| 26 | L3 → bin | failed pickup |
| 27 | L6 → bin | **successful** |
| 28 | R3 → bin | **successful** |
| 29 | L1 → L6 | missed pickup *(same rack)* |
| 30 | L1 → L6 | missed pickup *(same rack)* |
| 31 | R6 → R1 | missed pickup *(same rack)* |
| 32 | R1 → R6 | missed dest *(same rack)* |
| 33a | L6 → L1 | failed pickup (even went for the right rack!) *(same rack)* |
| 33b | L3 → R4 | put in slot 3 *(R4 is not a trained destination)* |
| 34 | R4 → L5 | put in slot 3 *(L5 is not a trained destination)* |

## Tally

| outcome | n | of 35 |
|---|---|---|
| full success | 6 | 17% |
| **failed at the grasp** | **14** | **40%** |
| placed in the wrong slot | 7 | 20% |
| aimed right, dropped / missed the hole | 7 | 20% |
| lost to the USB shutdown | 1 | 3% |

Gate from the plan (≥ 9/12 destinations, ≥ 11/12 sources): **not met.**

## What it shows

**1. The grasp regressed, and the cause is normalisation, not the policy.**
pi05 normalises state and action with q01/q99 from the training set. Between base12k's data and B's
data two joints changed scale, and they are the two that do the grasp:

| joint | span in base12k's data | span in B's data | |
|---|---|---|---|
| gripper | 37.4° | **50.8°** | **+36%** |
| wrist_flex | 146.4° | 134.9° | −8% |
| the other four | — | — | unchanged |

B inherited base12k's weights, whose gripper outputs are calibrated to a 37.4° span. Under a 50.8°
span the same output commands ~36% more opening:

```
base12k meant  5.0 deg  ->  now commands  6.8 deg
base12k meant  8.0 deg  ->  now commands 10.9 deg   (a grip becomes a loose hold)
base12k meant 12.0 deg  ->  now commands 16.3 deg
```

That is exactly "failed pickup (but not missed)" and "barely picked up but didnt": the arm arrives in
the right place and the jaws do not close far enough. 4000 steps at LR 1e-5 (0.57 of one pass) was not
enough to recalibrate.

**Where the wider span comes from:** lerobot's merge does not recompute percentiles — it rollouts a
min/max envelope over the per-episode stats. 15 episodes out of 220 (9 from the 28 Oct contrast set,
6 from the depth set) open the gripper past 37.4°, up to 50.9°, and those 15 set the scale for all 220.
The true 99th percentile over the merged frames is 36.5°, not 50.8°.

Both datasets have envelope-style quantiles, so the quirk itself is not new — base12k trained under it
fine. What breaks a *fine-tune* is that the number **changed**.

**2. The destination is being read better, but not sharply.**
base12k sent every destination to L3. Now the arm aims: rollout 9 was heading for slot 6 when asked for
L6, rollout 11 for slot 1 when asked for L1. But the wrong-slot placements fall in a clear pattern —
**slot 2 five times, slot 5 twice.** Trained destinations are only 1, 3 and 6; slots 2, 4, 5 appear in
no training prompt. The model is landing *between* the trained slots (2 sits between 1 and 3, 5 between
3 and 6). It knows "a slot on that rack" but has not sharply bound the digit. Consistent with 0.57 of
a pass over the data.

**3. Same-rack moves: 0 of 5** (29, 30, 31, 32, 33a) — four of them failed at the grasp, so this is
mostly the gripper problem, not evidence about same-rack moves themselves. The new sheet does contain
same-rack moves (~50 of the 150 episodes), unlike ws100. Not yet a fair test.

**4. The bin works when the grasp works:** 2 of 4, and both failures were pickups.

**5. Rollouts 8 and 9 are not valid data.** The USB hub carrying the wrist camera, the right camera and
both arms kept dropping (see the same day's diagnosis: devices on hub `9-2` re-enumerated ~66 times).
"Moving very fast then shutdown" is that, not the policy.

## What to do next

1. **Fix the USB before any more arm time.** Move both arm cables out of the `9-2` hub chain into
   motherboard ports, or use a powered hub. Otherwise rollouts keep dying and a drop while the gripper
   holds a vial latches another servo overload.
2. **Don't bother testing B's earlier checkpoints.** The mismatch lives in the data, not the weights,
   so step 500 is *less* adapted to the new gripper scale than 4000, not more. 4000 is already B's best.
3. **Confirm offline, no arm, ~20 min:**
   ```
   export RUN_DIR=outputs/pi05_full_vial-sort-ws220_canon_ft012000
   .venv/bin/python tools/pi05/probe_shortcut.py 2000 4000 \
       --root data/vial-sort-ws220_canon_trim --sheet ee/SORT_SHEET_WS_CONTRAST.txt
   .venv/bin/python tools/pi05/probe_digits.py 2000 4000
   .venv/bin/python tools/pi05/probe_go.py 2000 4000
   ```
   Expected if the reading above is right: `probe_shortcut`'s prompt swap is well above base12k's 19%,
   and `probe_go`'s "error against recorded actions" is concentrated in the gripper joint.
4. **Then train A from the real `lerobot/pi05_base`** on the same 220. A has no inherited scale, so it
   learns the gripper range of this data from scratch and the mismatch cannot happen. It also gets far
   more passes than B did. ~12000–16000 steps, 12–16 h.
   This is also the run the operator asked for on 3 Nov ("on the real base").

Alternative if B is to be rescued instead: continue B for another ~8000 steps so it finishes
recalibrating, or re-run B with base12k's own q01/q99 pinned so only the destinations have to be
learned. A is cleaner and was already planned.

## Not the cause

The other users' GPU/CPU load (the loop had 26.5 ms of spare time per tick), the trimming, the depth
episodes (depth is not in the training set at all), or the ep-141 label correction.

---

# Same checkpoint, quantiles pinned to base12k (`004000_q37`) — 10 rollouts, 4 Nov evening

Patch: gripper q99 50.8 -> 37.4 deg, wrist_flex q99 31.5 -> 43.2 (`tools/pin_quantiles.py`,
weights untouched and hardlinked). This is the diagnosis test from the section above.

| # | move | outcome | grasp | placement |
|---|---|---|---|---|
| 1 | L3 → R6 | missed dest | ok | missed |
| 2 | L3 → R6 | missed dest but barely got it | ok | near |
| 3 | L1 → R6 | **successful** | ok | ok |
| 4 | R1 → L6 | missed dest (was aiming for slot 4) | ok | slot 4 |
| 5 | R6 → L6 | put in slot 5 | ok | slot 5 |
| 6 | R6 → L6 | put it in slot 5 | ok | slot 5 |
| 7 | R6 → R1 | picked up but went to left rack *(same rack)* | ok | wrong rack |
| 8 | L1 → L6 | picked up and got stuck in the top *(same rack)* | ok | stuck |
| 9 | L6 → L1 | missed pickup (was going for slot 4), then picked up and placed in slot 4 *(same rack)* | 2nd try | slot 4 |
| 10 | L3 → L1 | grasped and wasnt getting it up properly *(same rack)* | grasped, no lift | — |

## The gripper fix is confirmed

| | unpatched (35 rollouts) | pinned (10 rollouts) |
|---|---|---|
| **failed at the grasp** | **14 = 40%** | **1 = 10%** (rollout 9, second try worked) |
| reached the destination with the vial | 21 = 60% | 9 = 90% |

Nine of ten rollouts picked the vial up. The "failed pickup (but not missed)" family is gone. The gripper
span really was the cause, and `tools/pin_quantiles.py` is the fix. Carry the pinned quantiles into
any retrain.

## What is left is the destination, and it is a different failure

Only 1 of 10 placed correctly. The misses are not random — **the arm goes to the middle of the rack
whatever digit it is given**:

| asked | landed |
|---|---|
| L6 (rollout 4) | slot 4 |
| L6 (rollouts 5, 6) | slot 5 |
| L1 (rollout 9) | slot 4 |

Slots 2, 4 and 5 appear in **no training prompt at all**, so a model that had bound the digit could
never place there. Before the patch it hedged around slot 2; now around slots 4-5. Either way it is
averaging over the trained destinations (1, 3, 6) instead of selecting one. That is the 0.57-of-a-pass
problem, not a normalisation problem — and it is what the longer retrain has to fix.

**Same-rack moves (7, 8, 9, 10): 0 of 4**, and rollout 7 (R6 → R1) went to the *wrong rack*, which the old
model never did. Same-rack is the newest thing in the contrastive sheet (~50 of the 150 episodes) and
the least trained. Rollouts 8 and 10 were lift failures ("stuck in the top", "wasnt getting it up"), the
one thing that could be an artefact of the wrist_flex half of the patch — `004000_q37g` (gripper only,
wrist_flex left as trained) exists to test exactly that.

## Revised plan

- Retrain B from base12k 012000 on ws220 **with the pinned quantiles**, and go to **16000 steps**
  (2.3 passes, ~15 h) rather than the 12000 first suggested: the destination is visibly unbound, not
  merely fuzzy, so it needs more exposure than one or two passes. Checkpoint every 1000 and pick by
  probe + arm; `train.sh`'s own note puts the overfit ceiling near 3 passes (~21000 steps).
- `004000_q37` stays as the "before" to compare against.

## Test protocol

**Now — 4 rollouts on `004000_q37g`** (gripper pinned, wrist_flex left as trained). Only question: were
rollouts 8 and 10's lift failures caused by the wrist_flex half of the patch? Repeat those two, plus two
that went well on `004000_q37`, same layout as before:

```
/t L1 L6      (was rollout 8: "got stuck in the top")
/t L3 L1      (was rollout 10: "wasnt getting it up properly")
/t L3 R6      (was rollouts 1-2: grasped, missed dest)
/t L1 R6      (was rollout 3: the one success)
```
If the lifts are clean here, pin **only the gripper** (`--joints 5`) in the dataset before retraining.
If they are the same as on `q37`, the wrist_flex pin is harmless and the lift problem is the model's.

**After the retrain — the 12-take gate.** Keep the vial layout FIXED within each block and change only
the destination in the prompt: that is the whole point of the contrastive data, so it is what has to
be measured.

| block | layout | rollouts |
|---|---|---|
| A — one source, three destinations | vial at R3 | `/t R3 L1`  `/t R3 L3`  `/t R3 L6`  `/t R3 bin` |
| B — the same, other rack | vial at L3 | `/t L3 R1`  `/t L3 R3`  `/t L3 R6`  `/t L3 bin` |
| C — same-rack (the newest, weakest) | as needed | `/t R6 R1`  `/t R1 R6`  `/t L1 L6`  `/t L6 L1` |

Pass (from the plan): **destination right in >= 9 of 12, source right in >= 11 of 12.**
Record each one with `/note <what happened>` so `tools/assess_rollouts.py` can read the session back.
Within a block only the sentence changes, so a model still reading the destination off the cameras
cannot score: all four rollouts of a block look identical to it.

## `004000_q37g` (gripper only) — 4 rollouts, and it is WORSE than either other version

| # | move | outcome |
|---|---|---|
| 1 | L1 → L6 | failed pickup |
| 2 | L3 → L1 | failed pickup |
| 3 | L3 → R6 | failed pickup |
| 4 | L1 → L6 | failed pickup |

**0 of 4 grasped.**

**Read this as a PAIRED comparison, not 0% vs 90%.** These four rollouts were deliberately chosen from
`q37`'s problem cases, so comparing them with `q37`'s overall 9/10 would be unfair (the operator pointed this
out). The fair comparison is the same tasks on both checkpoints, and on those the GRASP flips:

| task | on `004000_q37` | on `004000_q37g` |
|---|---|---|
| L1 → L6 | picked up (then stuck in the top) | **failed pickup** (x2) |
| L3 → L1 | grasped (then no lift) | **failed pickup** |
| L3 → R6 | grasped, missed the destination (x2) | **failed pickup** |

So on 3 matched tasks `q37` picked the vial up every time and `q37g` never did. The two failed on
those tasks for *different reasons*: `q37` got the vial and then lost it at the placement, `q37g`
never closed on it.

**Caveat, stated plainly: n = 4, one task run twice, and the one task that fully SUCCEEDED on `q37`
(L1 -> R6) was never run on `q37g`** -- `/t L1 L6` was entered a second time instead. That is the
missing control, and it is the test that would settle it.

| version | gripper q99 | wrist_flex q99 | grasp, on its own rollouts |
|---|---|---|---|
| `004000` as trained | 50.8 (wrong) | 31.5 (wrong) | 60% (21/35, varied tasks) |
| `004000_q37g` | 37.4 (right) | 31.5 (**wrong**) | 0% (0/4, `q37`'s hard cases) |
| `004000_q37` | 37.4 (right) | 43.2 (right) | 90% (9/10, varied tasks) |

**Both joints had to be pinned.** wrist_flex is the wrist pitch, i.e. the approach angle onto the vial.
B's span (134.8 deg) against base12k's (146.5) shifts every command the model inherited:

```
 -100 deg -> -100.3   (off by  -0.3)
  -60 deg ->  -63.5   (off by  -3.5)
  -49 deg ->  -53.5   (off by  -4.3)   <- the typical pitch at the grasp
    0 deg ->   -8.2   (off by  -8.2)
  +20 deg ->  +10.2   (off by  -9.8)
```

The arm approaches the vial at about -49 deg, so the wrist pitches ~4.3 deg too far down on every
grasp. On its own that is enough to miss. Worse, in the untouched checkpoint the two errors partly
cancelled -- a gripper opening 36% too wide compensated for a wrist 4 deg too low, which is why the
as-trained version still managed 60%. Fixing one and not the other removed the compensation and the
grasp failed every time.

**Consequences**
- `004000_q37` is the model to use for any further arm work. `004000_q37g` is a dead end; keep it only
  as the record of this test.
- Pin **all six joints** in the dataset before retraining (`tools/pin_quantiles.py` does that by
  default -- do NOT pass `--joints 5`).
- The earlier suggestion to pin only the gripper is withdrawn: it is the worst of the three options.

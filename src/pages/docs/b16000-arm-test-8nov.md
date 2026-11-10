---
layout: ../../layouts/Doc.astro
title: "Arm test, 8–9 Nov: π0.5 B at 16000 steps"
date: "2026-11-08"
description: "B retrained from base12k with the quantiles pinned: 11 of 31 rollouts placed correctly, and the destination now follows the command."
---

- Checkpoint: `outputs/pi05_full_vial-sort-ws220_canon_ft012000_v2/checkpoints/016000` (trained on the
  cluster 6–7 Nov, `ee/CLUSTER_CLAUSTHAL.md`). Sync mode, 15 actions per replan, 60 s max per rollout.
- Sessions: the session log (8 rollouts, then a robot bus error,
  see the end) and `016000_20261109_000538` (29 rollouts). 37 recorded rollouts for the 31 moves below: some
  moves were run twice (12, 13, 20, 24, 26b) and L3→R6 three times.
- "trained" = how many of the 220 training episodes have exactly this move (from the session log).
  Trained slots: sources 1, 3, 4, 6; destinations 1, 3, 6 and the bin. 2 and 5 are held out.

## Rollouts, as recorded at the robot (the operator's words)

the operator's numbering, kept as written (there is no 23, and 25–26 appear twice: the second pair is marked b).

| # | move | trained | what happened | class |
|---|---|---|---|---|
| 1 | R3 → L1 | 7 | success | ✓ |
| 2 | R3 → L3 | 5 | missed placing ( a bit in front of the rack | drop missed |
| 3 | R3 → L6 | 6 | placed in slot 5 (nearly 6!) | 1 off |
| 4 | R3 → bin | 4 | success | ✓ |
| 5 | L3 → R1 | 5 | missed placing, in fron tof teh rack of slot 1 | drop missed |
| 6 | L3 → R3 | 3 | placed in slot 2 | 1 off |
| 7 | L3 → R6 | 4 | was going for slot 3, that is taken by a vial | wrong (3) |
| 8 | L3 → R6 | 4 | same as tge one before it | wrong (3) |
| 9 | L3 → bin | 7 | success | ✓ |
| 10 | R6 → R1 | 1 | success | ✓ |
| 11 | R1 → R6 | 4 | success | ✓ |
| 12 | L1 → L6 | **0** | didnt grasp it properly at all, like it the vial was in the middle, but teh gripper wont grip ( ran it twice on different colors) | no grasp |
| 13 | L6 → L1 | 4 | didnt grasp it properly at all, like it the vial was in the middle, but teh gripper wont grip | no grasp |
| 14 | L1 → R1 | 4 | dropped just behind of the rack of slot 1 | drop missed |
| 15 | L1 → R3 | 9 | put in slot 2 but barely 3 | 1 off |
| 16 | L1 → R6 | 4 | success | ✓ |
| 17 | L6 → R1 | 6 | couldnt grasp (same as before!) | no grasp |
| 18 | L6 → R3 | 4 | put in slot 1 but was meanign 3 (i know) but in this scene i only kept 1 vial | wrong (1) |
| 19 | L6 → R6 | 4 | couldnt grasp it at first, but then it could and it went to slot 3 that had a vial | wrong (3) |
| 20 | R1 → L1 | 5 | barely at slot 1 (missed drop) | drop missed |
| 21 | R1 → L3 | 6 | put in slot 2 | 1 off |
| 22 | R1 → L6 | 6 | success | ✓ |
| 24 | R6 → L1 | 6 | couldnt grasp at first then went to slot 5 and stayed there (missed pickup | no grasp |
| 25 | R6 → L3 | 8 | success | ✓ |
| 26 | R6 → L6 | 4 | couldnt grasp it | no grasp |
| 25b | R5 → L1 | 0 (source 5 held out) | success | ✓ |
| 26b | L2 → R6 | 0 (source 2 held out) | couldnt grab it | no grasp |
| 27 | R3 → L5 | 0 (dest 5 held out) | put in slot 4 | 1 off |
| 28 | L3 → R4 | 0 (dest 4 never trained) | couldnt grab it | no grasp |
| 29 | L5 → bin | 0 (source 5 held out) | success | ✓ |
| 30 | R2 → bin | 0 (source 2 held out) | success | ✓ |

## Tally

| outcome | rollouts | count |
|---|---|---|
| **placed right** | 1 4 9 10 11 16 22 25 25b 29 30 | **11 of 31 (35%)** |
| right slot, drop missed (in front / behind / "barely") | 2 5 14 20 | 4 |
| one slot off | 3 6 15 21 27 | 5 |
| wrong slot (2+ away) | 7 8 18 19 | 4 |
| no grasp | 12 13 17 24 26 26b 28 | 7 |

The bin: 4 of 4. Held-out sources 2 and 5: 3 of 4 (R5→L1, L5→bin and R2→bin all succeeded; L2→R6 no grasp).

## The 12-take gate: not passed

| block | rollouts |
|---|---|
| 1, vial at R3 | L1 ✓ · L3 drop missed · L6 → slot 5 · bin ✓ |
| 2, vial at L3 | R1 drop missed · R3 → slot 2 · R6 → slot 3 · bin ✓ |
| 3, same rack | R6→R1 ✓ · R1→R6 ✓ · L1→L6 no grasp · L6→L1 no grasp |

- Placed right: **5 of 12**. Reached the right slot (counting the missed drops): **7 of 12**. Pass needs 9.
- Picked the right vial: **10 of 12**. Pass needs 11.
- Caveat on the gate itself: **L1→L6 is in none of the 220 training episodes** (the session log shows 0).
  It came from the 4 Nov take list. Without it, the gate still fails.

## What changed since 4 Nov (B at 4000, pinned quantiles)

| | 4 Nov: B 4000 `q37` (10 rollouts) | 8 Nov: B 16000 (31 rollouts) |
|---|---|---|
| placed right | 1 (10%) | 11 (35%) |
| destination | the middle of the rack (slots 4–5) whatever the digit | follows the digit, in the right order, but squeezed toward the middle |

**The destination now comes from the prompt.** Within block 1 the scene never changed (vial at R3), and
"slot 1 / 3 / 6" took the arm to slot 1 / about 3 / 5. Within block 2 (vial at L3), "1 / 3 / 6" went to
1 / 2 / 3. A model reading the destination off the scene would have gone to the same place every time.
The order is right in both blocks. What's missing is reach: the far slots get pulled toward the middle.

| asked for | where the carried vial went |
|---|---|
| slot 1 | slot 1 in **6 of 6** (3 placed, 3 at slot 1 but the drop missed) |
| slot 3 | slot 3 in 1 (+1 "in front of the rack"), slot 2 in 3, slot 1 in 1 |
| slot 6 | slot 6 in 3, slot 5 in 1, **slot 3 in 3** |
| bin | 4 of 4 |
| slot 5 (never trained) | slot 4 |

The three "slot 6 → slot 3" rollouts (7, 8, 19) went to a slot that already held a vial (the operator's notes on 7
and 19; 8 was "same as the one before it"). Placement precision is the other half: 9 of 31 rollouts ended
at the target or one slot from it and still failed.

## Grasp failures: it's the model, not the gripper (from the recorded actions)

Commanded vs measured gripper, every rollout. A vial between the jaws stops them at about 8° (5.8–10.2);
empty jaws close to 0.4–4.5°. Every grasp that picked the vial up was commanded shut (−3.0 to +0.6°),
the jaws stopped at 5.8–10.2° and it held for 3.6–43 s. So when the model closes, it closes as hard as in
training: the 4 Nov scale problem is gone.
The failures are three different things:

| what happened | rollouts (the operator's #) | evidence |
|---|---|---|
| **never closed**: hovered over the vial with the gripper open | 12 (1st), 13 (1st), 26b (2nd) | lowest command 8.6 / 21.0 / 14.1°, never shut |
| **closed on the vial, let go** | 17, 24 (2nd), 26 | jaws stopped at 7.6–8.1° (vial between them), held 0–1.6 s; 17 closed only at 30 s and only to 4° |
| **closed on air, or somewhere else** | 12 (2nd), 13 (2nd), 24 (1st), 26b (1st), 28 | jaws 0.4–4.5° (nothing between them), except 12 (2nd): 15.7°, wider than a vial; in 12 (2nd) and 28 the shoulder (−30.5°, −34.5°) was outside the range of every grasp that worked (−23 to +13°) |

**Where they happen:**
- The left-rack same-rack pair L1↔L6: 4 of 4 attempts failed.
- Slot-6 sources: L6 grasped cleanly once in 4 moves, R6 in 2 of 4.
- Unfamiliar prompts. The same L3 vial was grasped in all 5 L3 rollouts with a trained destination, but not
  for "slot 4" (28). L1 was grasped for R1, R3 and R6, but not for L6 (12, the untrained move).
- **The destination words change the grasp:** same vial, same scene, different destination, and the grasp
  works or doesn't. The model has not separated "pick this" from "put it there".

Training coverage doesn't explain it. L6 is the source in 24 episodes and R6 in 30 (the others 25–31);
51 of the 220 are same-rack moves.

## Robot error (session 1)

At 00:05:28, on the third L3→R6, the follower stopped answering:
`Failed to sync read 'Present_Position' on ids=[1, 2, 3, 4, 5, 6] after 3 tries. There is no status packet!`
That is the motor bus dropping out (USB or power), not the model. It happened once. If it happens again,
reseat the follower's USB cable and check its power supply.

## Next

1. **A 16000 on the same rollouts, same scenes, same order**: a paired comparison with this file.
   A started from `pi05_base`, so it never had base12k's habit of reading the scene.
2. **Probes for both runs** on the cluster (both A100s are free): an objective destination score per
   checkpoint, to see whether 12000 or 14000 beats 16000 for either run.
3. **Then decide.** If A fails the same way, the 3 Nov rule ("220, train B, then decide") points to the
   second sheet (~370), weighted toward what failed here: slots 3 and 6 as destinations, slot-6 sources,
   same-rack left moves, and scenes with other vials in the racks. If A passes, A is the model.

## Data and model

- The model: [`sari-abdan/vial-sort-pi05-ws220-b-16000`](https://huggingface.co/sari-abdan/vial-sort-pi05-ws220-b-16000) (Mango Pudding on the Results page)
- What it trained on: [`sari-abdan/vial-sort-slots-220`](https://huggingface.co/datasets/sari-abdan/vial-sort-slots-220)
- The recordings: [`rollout_pi05_016000_20261108_235412`](https://huggingface.co/datasets/sari-abdan/rollout_pi05_016000_20261108_235412) and [`rollout_pi05_016000_20261109_000538`](https://huggingface.co/datasets/sari-abdan/rollout_pi05_016000_20261109_000538)

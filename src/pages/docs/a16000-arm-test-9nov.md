---
layout: ../../layouts/Doc.astro
title: "Arm test, 9 Nov: π0.5 A at 16000 steps, against B"
date: "2026-11-09"
description: "A, trained from the pi05 base, on the same 31 moves as B: 21 placed correctly and it meets the 12-move gate narrowly. Also the probes and the camera check."
---

- Checkpoint: `outputs/pi05_full_vial-sort-ws220_canon_base16k/checkpoints/016000` (from `lerobot/pi05_base`,
  LR 2.5e-5, 16000 steps, pinned quantiles; trained on the cluster 7 Nov). Sync, 15 actions per replan.
- Session the session log (started 00:50). 37 rollout starts for
  31 moves, the same count as B's 37. Repeats: L6→R1, L6→R3 and R1→L3 were restarted after 8–13 s;
  L3→R6, L2→R6 and R2→bin are the retries in the operator's notes. **L3→R3's first try ran 39 s** before the
  reset, and the note says "success". If that first try failed, block 2 below is 3/4 on first tries.
- B's rollouts and the grasp analysis: `ee/ROLLOUT_ws220_B16000_8nov.md`.

## Rollouts, as recorded at the robot (the operator's words), next to B

| # | move | A 16000 (the operator's words) | A | B 16000 |
|---|---|---|---|---|
| 1 | R3 → L1 | put in slot 2 | 1 off | ✓ |
| 2 | R3 → L3 | put in slot 2 | 1 off | drop missed |
| 3 | R3 → L6 | success | ✓ | 1 off (5) |
| 4 | R3 → bin | success | ✓ | ✓ |
| 5 | L3 → R1 | success | ✓ | drop missed |
| 6 | L3 → R3 | success | ✓ | 1 off (2) |
| 7 | L3 → R6 | success | ✓ | wrong (3) |
| 8 | L3 → R6 | didnt grasp it at first but then grasp and success | ✓ (2nd grasp) | wrong (3) |
| 9 | L3 → bin | success | ✓ | ✓ |
| 10 | R6 → R1 | placed in front of slot 1 | drop missed | ✓ |
| 11 | R1 → R6 | put behind slot 6 | drop missed | ✓ |
| 12 | L1 → L6 (0 training eps) | didnt grasp it | no grasp | no grasp |
| 13 | L6 → L1 | success | ✓ | no grasp |
| 14 | L1 → R1 | put in front of slot 1 of right rack | drop missed | drop missed |
| 15 | L1 → R3 | put in slot 2 | 1 off | 1 off (2) |
| 16 | L1 → R6 | success | ✓ | ✓ |
| 17 | L6 → R1 | success | ✓ | no grasp |
| 18 | L6 → R3 | stuck between slot 3 and 4 and didnt put the vial in any | drop missed (never let go) | wrong (1) |
| 19 | L6 → R6 | success | ✓ | wrong (3) |
| 20 | R1 → L1 | success | ✓ | drop missed |
| 21 | R1 → L3 | success | ✓ | 1 off (2) |
| 22 | R1 → L6 | success | ✓ | ✓ |
| 24 | R6 → L1 | success | ✓ | no grasp |
| 25 | R6 → L3 | success | ✓ | ✓ |
| 26 | R6 → L6 | success | ✓ | no grasp |
| 25b | R5 → L1 (source 5 held out) | success | ✓ | ✓ |
| 26b | L2 → R6 (source 2 held out) | picked the wrong vial (4th slot one), then i retried when putting the other vial in 5th slot then it carried teh one in 2nd slot but missed drop behind the 6th slot of right rack | wrong vial, then drop missed | no grasp |
| 27 | R3 → L5 (dest 5 held out) | was going to 5th slot but dropped it in front of the rack | drop missed, at slot 5 | 1 off (4) |
| 28 | L3 → R4 (dest 4 never trained) | success | ✓ | no grasp |
| 29 | L5 → bin (source 5 held out) | success | ✓ | ✓ |
| 30 | R2 → bin (source 2 held out) | was going to slot 3 or 4 (missed grasp) but i retried with removing one of teh neighboring vials from the dest vial, and then it succeeded | ✓ (after a retry) | ✓ |

## Tally, A vs B

| outcome | A 16000 | B 16000 |
|---|---|---|
| **placed right** | **21 of 31 (68%)**: 19 on the first try, 8 and 30 after a retry | 11 of 31 (35%) |
| right slot, drop missed (in front / behind / never let go) | 6 (10 11 14 18 26b 27) | 4 |
| one slot off | 3 (1 2 15), all "slot 2" | 5 |
| wrong slot (2+ away) | **0** | 4 |
| no grasp | **1** (12, the untrained L1→L6) | 7 |
| wrong vial at first | 2, both held-out source slot 2 (26b took L4; 30 went for R3/R4) | 0 |

Move by move (ranking ✓ > drop missed at the right slot > one off > wrong slot > no grasp): A is better
on 16, B on 5 (1, 2, 10, 11, and 30 where A needed a retry), and 10 are the same.

## The 12-take gate: A meets it, narrowly

| block | A | B |
|---|---|---|
| 1, vial at R3 | L1 → slot 2 · L3 → slot 2 · L6 ✓ · bin ✓ | L1 ✓ · L3 drop missed · L6 → 5 · bin ✓ |
| 2, vial at L3 | R1 ✓ · R3 ✓ · R6 ✓ · bin ✓ | R1 drop missed · R3 → 2 · R6 → 3 · bin ✓ |
| 3, same rack | R6→R1 drop missed at 1 · R1→R6 drop missed at 6 · L1→L6 no grasp · L6→L1 ✓ | ✓ · ✓ · no grasp · no grasp |
| placed right | 7 / 12 | 5 / 12 |
| right slot (counting missed drops); pass ≥ 9 | **9 / 12** | 7 / 12 |
| right vial picked; pass ≥ 11 | **11 / 12** | 10 / 12 |

A passes both arm criteria, with no margin, and only 7 of the 12 were actually placed. What's left is
mostly the drop, not the destination.

## The destination, by digit

| asked for | A: where the carried vial went | B |
|---|---|---|
| slot 1 | slot 1 in **7 of 8** (5 placed, 2 dropped in front), slot 2 once | 6 of 6 at slot 1 (3 placed) |
| slot 3 | slot 3 in 3 of 6 (+1 stuck between 3 and 4), slot 2 in 2 | slot 3 in 1, slot 2 in 3, slot 1 in 1 |
| slot 6 | slot 6 in **9 of 9** (7 placed, 2 dropped behind) | slot 6 in 3 of 7, slot 3 in 3 |
| bin | 4 of 4 | 4 of 4 |
| slot 5 (never trained) | **slot 5** (dropped in front) | slot 4 |
| slot 4 (never a destination) | **placed in R4** | no grasp |

**B's squeeze is gone in A.** Slot 6 is reached every time, and A even lands on slots 4 and 5, which never
appear as destinations in training. It has learned where each number is, not 1/3/6 as three memorised
moves. Slot 3 is A's weak one (twice slot 2, both times with the vial from rack position 3 or 1).

**Grasps:** 1 failure in 31 (the one move that isn't in the training data), against B's 7. B's
L6/R6 source problem doesn't happen in A: L6 and R6 were picked up in all 8 of those moves. (Caveat:
L6→R1 and L6→R3 were restarted after 8 and 13 s. If those were failed grasps, the recordings will show
it. They can be read once the session is closed.)

**Held-out source slot 2:** twice A went for a neighbouring vial first (L4, R3/R4). Slot 2 is never a
source in training, so this tests generalisation, not the gate. B didn't grasp L2 at all, and did
R2→bin on the first try.

## Probes (cluster, 9 Nov 00:43–; checkpoints 8000, 10000–16000 of both runs)

**probe_go (does it leave home?):** both runs pass at every checkpoint. All 9 real start frames move
72–88°, on 4 of 4 seeds. Error against the recorded demonstrations: B 2.0–3.7°, A 2.8–4.7° (A
improves steadily to 16000).

**probe_digits:**

| check | B (every checkpoint 8000–16000) | A |
|---|---|---|
| 1 SOURCE (R1 > R3 > R6, spread ≥ 15) | PASS, pan +33 / +25 / +12 | PASS, pan +32 / +23 / +2 (wider) |
| 2 ROLES (digits bound to source/destination) | PASS | PASS |
| 3 DEST (slot 1/3/6 ordered, spread ≥ 10, on ≥ 4 of 7 frames) | fail, **0 of 7** at every checkpoint | fail, **1–2 of 7** (2 at 8000, 13000, 14000, 15000; 1 at 10000, 12000, 16000) |

- DEST predicts the carry 1 s after the grasp, so the spreads are small for both. But A's is bigger on
  the same frames, e.g. episode 77: A +31 / +27 / +16 vs B +11 / +9 / +7. That matches the arm.
- **Is 16000 the best for B?** On these probes B is flat: 8000 through 16000 give the same numbers
  within 1–3°. No other B checkpoint is better, and on the arm B is clearly behind A anyway.
- A's 13000–15000 score one frame more than 16000 (2/7 vs 1/7). That's one frame crossing the 10° line
  (episode 50: 33/30/22 at 13000 vs 32/29/22 at 16000): noise, not a reason to switch.

**probe_shortcut (destination from the prompt or from the cameras), checkpoints 8000 and 10000–16000**
(jobs 37843/37844 finished 02:00–02:03, 1 h 17–20 min each):

| condition, 1 s after the grasp | B, % follows the swapped episode | A |
|---|---|---|
| prompt → other destination | 12–21 | 12–21 |
| no prompt | 31–33 | 21–42 |
| 4 scene cameras swapped | 62–65 | 46–58 |
| all 5 cameras swapped | 75–83 | 71–79 |
| source: other vial named (start frame) | 81–94 | 88–94 |

Flat across checkpoints for both runs, so it doesn't pick a checkpoint either. Neither model passes the
old "prompt swap ≥ 80%" line, base12k's 19% is in the same range, and A leans less on the scene cameras
than B. But this probe asks the model to change destination *mid-carry*: the frame is 1 s after the
grasp, when the arm is already moving toward the recorded one. On the arm, with the prompt there from the
start, A went where the digit said within one unchanged scene (blocks 1 and 2). The probe was built for
ws100's failure, where the scene named the destination. On the contrastive data it doesn't separate A from
B. A cleaner version would compare the three rollouts of one triplet at the start frame.

## Checked from the recordings after the session (9 Nov, 01:45–02:00)

**First tries.** Some repeats in the log weren't in the notes:
- **L3 → R3, first try:** A grasped (jaws 8.1°) and carried the vial for 28 s **without ever letting go**.
  The "success" was the second try. So the gate's block 2 is 3/4 on first tries, and **the gate on strict
  first tries is 8/12 right slot: one short.**
- L6 → R3, first try: the gripper never closed in 11 s (hovering, B's failure mode). R1 → L3, first try:
  no close within 6 s, too short to call. L6 → R1, first try: it had the vial when you reset at 6 s.
- Strict first-try count: A placed about **17–18 of 31**, B 11.

**Release poses: the missed drops are a last-centimetre problem.** Follower joints [pan lift elbow wflex]
at the moment the gripper opened, right rack:

| slot | A placed | A missed |
|---|---|---|
| R1 | 38.3 −15.6 60.1 −34.9 · 41.7 −11.5 53.3 −35.6 | 42.0 −11.8 56.8 −34.4 (in front of slot 1) |
| R6 | 9.9 −4.8 55.1 −41.0 · 9.3 −2.6 48.3 −39.3 · 9.6 −1.2 47.2 −38.8 | 8.9 −2.8 47.2 −44.2 (behind) · 10.3 −0.4 51.0 −41.5 (behind) |

The misses opened within 3–5° per joint of the successes at the same slot. A wasn't aiming somewhere else.
A few degrees at the wrist and elbow is ~1–2 cm at the gripper, the size of "in front of / behind the
slot". The demos' pan per slot is the same in all three batches (within 2–3°), so the racks haven't moved
sideways. (Release *style* did change: the old 70 released with a flatter wrist, wflex −28 to −43, than
batches 1–2, −42 to −61.)

## The left_top camera moved on 4 Nov (and it's still off)

Phase correlation of the first frames' edges, table area only, against batch 2 (3 Nov), at 640×480.
+ = picture lower / further right:

| when | left_top shift | the other 3 scene cameras |
|---|---|---|
| batch 1, 28 Oct | +0.4, −0.6 | ≤ 1 px |
| 4 Nov rollouts until 18:31 (5 sessions) | 0.0 to +0.3, −0.2 to +0.1 | |
| **4 Nov from 18:33** (B 4000, q37, q37g) | **−5.3, +12.4** | |
| 8–9 Nov (B 16000, A 16000) | **−5.7, +12.2** | ≤ 1 px |
| old ws100, mid-Oct | different again (whole frame: −11, −2; the table area doesn't match the 3 Nov layout) | ≤ 1 px |

So left_top was bumped on **4 Nov between 18:31 and 18:33**, during the B 4000 tests: ~12 px down and ~6 px
left, about 6 px at the model's 224×224 input. **Every arm test since then ran with left_top away from where
150 of the 220 training episodes were recorded.** the operator's "moved before the 2nd batch" matches the old 70
being in another position again.

Whether it matters isn't proven. A reaches the right slot most of the time with the camera off, so it isn't
breaking the task. But the failures left are last-centimetre drops, and that's where the cameras guide the
arm. Test: put it back (`.venv/bin/python tools/cam_align.py` prints the live offset and which way to move
the camera until ALIGNED), then repeat the near-miss moves on A 16000 with a few controls.

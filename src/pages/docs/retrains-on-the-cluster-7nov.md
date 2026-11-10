---
layout: ../../layouts/Doc.astro
title: "Retraining π0.5 on a university cluster, 6–7 Nov"
date: "2026-11-07"
description: "Two full fine-tunes on the 220 contrastive demonstrations, one from the earlier checkpoint and one from the pi05 base, trained side by side on two 80 GB A100 GPUs in 12-hour jobs."
---

## The two runs

Both train every weight of π0.5 on the same 220 demonstrations (113,010 frames after the idle start and end are trimmed), with the operator-free starts, batch 16, 16,000 steps (2.3 passes over the data) and a checkpoint every 1,000 steps. The image colour and shift augmentations are the same as before.

| run | starts from | learning rate | started | finished |
|---|---|---|---|---|
| **B** | the 12k checkpoint of the earlier 100-demonstration run | 1e-5 | Fri 6 Nov, 13:41 | Sat 7 Nov, 11:18 |
| **A** | the public `pi05_base` | 2.5e-5 | Sat 7 Nov, 01:34 | Sat 7 Nov, 23:10 |

Both finished at a loss of about 0.009 (0.085 and 0.099 after 100 steps). Loss says how well the model fits the recorded actions, not how it behaves on the arm; the arm tests are on the other pages in this section.

## The normalisation fix

B had first been trained for 4,000 steps on the merged dataset and lost its grasp on the arm. State and action are scaled by the 1st and 99th percentile of the training data, and merging datasets had widened the gripper range from 37.4° to 50.8°. A fine-tune inherits the scale of the model it starts from, so every gripper command came out about 36% too wide. Both runs here use the original percentiles, pinned in the dataset before training, for all six joints. The details are in the 4 Nov arm test.

## Running it on the cluster

- **GPUs:** the account may use only the A100 nodes, two 80 GB cards. Both were used at once, one per run. A pi05 full fine-tune peaks at about 38 GiB at batch 16, so it fits with room to spare.
- **12-hour jobs:** each job saves a checkpoint, works out whether the next one would still fit in its time limit, and if not stops and hands over to a job it queued beforehand, which resumes from the last checkpoint. B took two jobs (steps 0 to 8,000, then 8,000 to 16,000) and so did A. A chained test with 40 steps was run first.
- **Speed:** 4.8 seconds per step on one A100, limited by the GPU rather than by loading data, so the two runs did not slow each other down.
- **Memory:** the default AdamW update briefly needs an extra copy of the weights (about 37 GiB at any batch size). The fused AdamW implementation does the same arithmetic without it, which is why it was switched on.
- **Video decoding:** the cluster has no FFmpeg libraries for torchcodec, so frames are decoded with PyAV. The frames are the same.
- **Offline checks:** after training, three probes ran on checkpoints 8,000 and 10,000 to 16,000 of both runs, on the cluster, in about 80 minutes each. They were flat across checkpoints, so none beat the final one.

## Reading list

- [Arm test, 4 Nov: B at 4000 steps](../b4000-arm-test-4nov/)
- [Arm test, 8–9 Nov: B at 16000 steps](../b16000-arm-test-8nov/)
- [Arm test, 9 Nov: A at 16000 steps, against B](../a16000-arm-test-9nov/)

// Every word the October pages use in a narrower sense than everyday English, defined once. <Term k="…">
// shows the definition on hover or focus; the Experiments page prints the whole list.

export interface Entry { term: string; def: string }

export const GLOSSARY: Record<string, Entry> = {
  rollout: { term: 'Rollout', def: 'One autonomous attempt by the robot at one command, from the moment it is started until it stops or the session ends.' },
  session: { term: 'Session', def: 'One launch of the rollout program. A session holds several rollouts, all with the same checkpoint, the same mode and the same lighting.' },
  checkpoint: { term: 'Checkpoint', def: 'The model’s weights saved at one training step. “12k” is the checkpoint after 12,000 steps. Results are never pooled across checkpoints.' },
  step: { term: 'Step', def: 'One update of the model’s weights, made from one batch of frames.' },
  pass: { term: 'Pass over the data', def: 'Every frame of the training data seen once. Steps × batch size ÷ number of frames.' },
  command: { term: 'Command (prompt)', def: 'The sentence typed to the robot, for example “Move the vial from position 3 of the right rack to slot 6 of the left rack.” It names a source and a destination by position, never by colour.' },
  wording: { term: 'Wording', def: 'One way of phrasing a command. The 100 demonstrations use 100 different wordings of 32 moves.' },
  move: { term: 'Move', def: 'One source slot and one destination, written R3 → L6: take the vial from slot 3 of the right rack and put it in slot 6 of the left rack. A destination can also be the bin.' },
  slot: { term: 'Slot', def: 'One of the six holes of a rack, numbered 1 to 6. Slot 1 is nearest the follower arm.' },
  rack: { term: 'Left and right rack', def: 'Read from the follower arm’s point of view: the left rack is the rack to the left of the arm, which is the top rack in the overhead camera. The bin sits between the racks.' },
  source: { term: 'Source and destination', def: 'The source is the slot the vial starts in. The destination is the slot (or the bin) it must end in.' },
  heldout: { term: 'Held out', def: 'Never recorded on purpose: slots 2 and 5 are never a source, and slots 2, 4 and 5 never a destination. They test whether a model can reach slots no demonstration used.' },
  demonstration: { term: 'Demonstration', def: 'One move recorded by a person driving the leader arm while the follower arm copied it, with all cameras and joint positions logged.' },
  scorer: { term: 'Scorer', def: 'A script (assess_rollouts) that reads the arm’s joint angles during a rollout, finds each grasp and release, and works out which slot the arm was at by matching its pose to the same moment in the demonstrations. It is accurate to about half a slot and cannot see the vial.' },
  eyecheck: { term: 'Eye check', def: 'A person watching the cameras to see where the vial actually ended. Done for only some rollouts, so it is reported beside the scores, never inside them.' },
  grasp: { term: 'Grasped', def: 'The gripper closed on the vial in the slot the command asked to take it from. It does not mean the vial was lifted.' },
  lifted: { term: 'Lifted (picked up)', def: 'After a grasp, the arm raised the vial out of its slot.' },
  letgo: { term: 'Let go at the asked slot', def: 'The arm opened the gripper at the destination slot the command asked for, within half a slot. It does not prove the vial ended in the hole.' },
  sync: { term: 'Sync mode', def: 'The robot pauses while the model computes its next chunk of actions, then runs the chunk. Smooth enough, but it stalls at every replan.' },
  rtc: { term: 'RTC', def: 'Real-time chunking: the model computes the next chunk while the arm is still running the last one. π0.5 supports it; FLUX 3 Action does not, so FLUX is always sync.' },
  ema: { term: 'EMA weights', def: 'A slowly moving average of the weights over training, saved next to the raw weights. A rollout is run with one or the other.' },
  lora: { term: 'LoRA', def: 'Low-rank adaptation: the large base model stays frozen and small added matrices are trained instead.' },
  finetune: { term: 'Full fine-tune', def: 'Every weight of the model is trained, with no frozen part and no adapters.' },
  gate: { term: 'Offline gate', def: 'A test of a saved checkpoint without the robot. It is shown recorded frames and commands and asked what motion it would predict.' },
  loss: { term: 'Loss', def: 'The training error: how far the model’s predicted actions are from the recorded ones. It falls as the model fits the data and says nothing about how it behaves on the robot.' },
  n: { term: 'n', def: 'The number of rollouts behind a number. Small n means one more good or bad rollout moves the result a long way.' },
  operator: { term: 'Operator-free start', def: 'Training frames from the start of a demonstration, where the person leaned over the robot, replaced by views of the arm with nobody near it.' },
};

/** The order the glossary is printed in: what a reader meets first. */
export const GLOSSARY_ORDER = [
  'rollout', 'session', 'checkpoint', 'step', 'pass', 'demonstration', 'command', 'wording', 'move', 'slot', 'rack', 'source', 'heldout',
  'scorer', 'grasp', 'lifted', 'letgo', 'eyecheck', 'n', 'sync', 'rtc', 'ema', 'lora', 'finetune', 'loss', 'gate', 'operator',
];

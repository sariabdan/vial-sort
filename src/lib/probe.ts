// The probe of 21 October on training frames: 24 pairs of demonstrations with the same source and different
// destinations, for the model the site calls Mango Rice. One place for its numbers: Training shows the whole
// table, the home page draws the three rows marked `short` as bars.
export interface ProbeRow { test: string; at12k: number; at2k: number; short?: string }

export const PROBE: ProbeRow[] = [
  { test: 'Replays its own demonstration’s destination', at12k: 100, at2k: 88 },
  { test: 'The command names another source vial: it goes there', at12k: 94, at2k: 94, short: 'The command names another vial: the arm goes to it' },
  { test: 'The command names another destination: it follows it', at12k: 19, at2k: 31, short: 'The command names another destination: the arm follows it' },
  { test: 'No command at all: it follows the other destination', at12k: 19, at2k: 27 },
  { test: 'Same command, all five camera images from the other demonstration: it follows the cameras', at12k: 81, at2k: 75, short: 'Same command, camera images swapped: the arm follows the cameras' },
  { test: 'Same command, joint positions from the other demonstration', at12k: 10, at2k: 15 },
];

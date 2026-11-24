// The score of one run (one model at one checkpoint in one mode), as agreed with the supervisor on 24 Nov 2026.
// For each of the 12 rack slots as the destination: the share of its rollouts that ended in the asked slot. The total
// is the plain mean of those 12 shares, so every place on the table counts the same however many rollouts went there.
// The bin is left out: it is an easy target and would lift the score. Trained and held-out accuracy are the same mean
// over slots 1, 3, 6 (the demonstrations' destinations) and 2, 4, 5 (never a destination in training) of both racks.
// A run passes only with at least 10 rollouts at every slot and a total of at least 70%. Fewer than 10 at any slot
// disqualifies it; its numbers are still shown, over the slots it was tried at. Explained on Experiments (#score).

export const RACK_SLOTS = ['L', 'R'].flatMap((r) => [1, 2, 3, 4, 5, 6].map((n) => `${r}${n}`));
export const HELD_OUT_SLOTS = RACK_SLOTS.filter((s) => '245'.includes(s[1]));
export const TRAINED_SLOTS = RACK_SLOTS.filter((s) => !HELD_OUT_SLOTS.includes(s));
export const MIN_PER_SLOT = 10;
export const PASS_MARK = 0.7;

type ByDestination = Record<string, { rollouts: number; released: number }>;
export interface RunScore {
  total: number | null;
  trained: number | null;
  held: number | null;
  tried: number;   // slots with at least one rollout
  short: number;   // slots with fewer than MIN_PER_SLOT rollouts
  verdict: 'passed' | 'below' | 'disqualified';
}

const mean = (v: number[]) => (v.length ? v.reduce((a, b) => a + b, 0) / v.length : null);

export function scoreRun(by: ByDestination): RunScore {
  const share = (s: string) => (by[s]?.rollouts ? by[s].released / by[s].rollouts : null);
  const over = (slots: string[]) => mean(slots.map(share).filter((x): x is number => x !== null));
  const total = over(RACK_SLOTS);
  const short = RACK_SLOTS.filter((s) => (by[s]?.rollouts ?? 0) < MIN_PER_SLOT).length;
  return {
    total, trained: over(TRAINED_SLOTS), held: over(HELD_OUT_SLOTS),
    tried: RACK_SLOTS.filter((s) => by[s]?.rollouts).length, short,
    verdict: short ? 'disqualified' : total !== null && total >= PASS_MARK ? 'passed' : 'below',
  };
}

export const pctOf = (x: number | null) => (x === null ? '–' : `${Math.round(x * 100)}%`);

/** "Disqualified: fewer than 10 rollouts at 12 of 12 slots", "Passed", "Below 70%" */
export const verdictText = (s: RunScore) =>
  s.verdict === 'passed' ? 'Passed' : s.verdict === 'below' ? `Below ${PASS_MARK * 100}%`
    : `Disqualified: fewer than ${MIN_PER_SLOT} rollouts at ${s.short} of 12 slots`;

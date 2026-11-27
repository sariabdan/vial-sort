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
export const WEAK_AT = 0.5;   // a slot at half or less in the asked slot is listed as weak

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

// ── the score worked out with a run's own numbers (Results: "How the score is calculated") ──
// In machine-learning words, a slot's share is its recall (true positives over all rollouts asked for it), and the
// total is the mean of the recalls: balanced accuracy, which weighs every slot the same however often it was tried.

/** 412.698 -> "412.7", 550 -> "550": one decimal, none when it is whole. */
export const num1 = (x: number) => String(Math.round(x * 10) / 10);

export interface WorkedPart {
  slots: { s: string; got: number; n: number; pct: number }[];  // the slots tried, with their share in percent
  missing: string[];                                             // the slots of this part never tried
  sum: number;                                                   // sum of the shares, in percent
  count: number;
  mean: number | null;                                           // in percent
}

/** The mean over `slots`, step by step: what scoreRun computes, kept apart so it can be written out. */
export function workedPart(by: ByDestination, slots: string[]): WorkedPart {
  const tried = slots.filter((s) => by[s]?.rollouts);
  const parts = tried.map((s) => ({ s, got: by[s].released, n: by[s].rollouts, pct: (100 * by[s].released) / by[s].rollouts }));
  const sum = parts.reduce((a, p) => a + p.pct, 0);
  return { slots: parts, missing: slots.filter((s) => !by[s]?.rollouts), sum, count: parts.length,
           mean: parts.length ? sum / parts.length : null };
}

/** "(L1 2/2 = 100 + R3 1/2 = 50) ÷ 2 = 150 ÷ 2 = 75%" */
export const workedLine = (p: WorkedPart) =>
  p.count ? `(${p.slots.map((x) => `${x.s} ${x.got}/${x.n} = ${num1(x.pct)}`).join(' + ')}) ÷ ${p.count} = ` +
            `${num1(p.sum)} ÷ ${p.count} = ${num1(p.mean!)}%` : 'no slot tried';

/** The same, as TeX for <TeX> (the shares are percentages, so % is written once, on the result): every share labelled with its slot and count under a brace, then the mean.
 *  null when no slot of the part was tried. */
export function workedTex(name: string, p: WorkedPart): string | null {
  if (!p.count) return null;
  const terms = p.slots.map((x) => `\\underbrace{${num1(x.pct)}}_{\\text{${x.s} ${x.got}/${x.n}}}`).join(' + ');
  return `\\text{${name}} = \\frac{${terms}}{${p.count}} = \\frac{${num1(p.sum)}}{${p.count}} = ${num1(p.mean!)}\\,\\%`;
}

/** The total as TeX: the parts' sums over the number of slots tried, then the rounded score of the Score table. */
export function totalTex(parts: WorkedPart[], total: number | null): string | null {
  const used = parts.filter((p) => p.count);
  const n = used.reduce((a, p) => a + p.count, 0);
  if (!n || total === null) return null;
  const sum = used.reduce((a, p) => a + p.sum, 0);
  return `\\text{Total} = \\frac{${used.map((p) => num1(p.sum)).join(' + ')}}{${n}} = ${num1(sum / n)}\\,\\% ` +
         `\\approx ${Math.round(total * 100)}\\,\\%`;
}

/** The median of a run's slot shares (in percent), to show what the mean is chosen over. */
export function medianShare(by: ByDestination): number | null {
  const v = RACK_SLOTS.filter((s) => by[s]?.rollouts).map((s) => (100 * by[s].released) / by[s].rollouts).sort((a, b) => a - b);
  if (!v.length) return null;
  const h = Math.floor(v.length / 2);
  return v.length % 2 ? v[h] : (v[h - 1] + v[h]) / 2;
}

/** Plain accuracy over the rack slots: every rollout pooled, which lets a slot tried often count more. */
export function pooled(by: ByDestination): { got: number; n: number } {
  return RACK_SLOTS.reduce((a, s) => ({ got: a.got + (by[s]?.released ?? 0), n: a.n + (by[s]?.rollouts ?? 0) }), { got: 0, n: 0 });
}

/** "Disqualified: under 10 rollouts at 12 of 12 slots", "Passed", "Below 70%" */
export const verdictText = (s: RunScore) =>
  s.verdict === 'passed' ? 'Passed' : s.verdict === 'below' ? `Below ${PASS_MARK * 100}%`
    : `Disqualified: under ${MIN_PER_SLOT} rollouts at ${s.short} of 12 slots`;

/** The slots at half or less in the asked slot, worst first ("R2 0/3"); slots never tried are not listed. */
export function weakSlots(by: ByDestination): string[] {
  const share = (s: string) => by[s].released / by[s].rollouts;
  return RACK_SLOTS.filter((s) => by[s]?.rollouts && share(s) <= WEAK_AT)
    .sort((a, b) => share(a) - share(b) || by[b].rollouts - by[a].rollouts)
    .map((s) => `${s} ${by[s].released}/${by[s].rollouts}`);
}

// Cells for the rack maps: the left rack, the bin and the right rack, slots 1–6 of each from left to right.
// A cell's class picks a step of a validated ramp; null leaves the slot empty.

export type Cell = { code: string; cls: number | null; text: string; title: string };
export type RackMap = { caption: string; ramp: 'd' | 'st'; cells: Cell[] };

export const PLACES = [...['L', 'R'].flatMap((r) => [1, 2, 3, 4, 5, 6].map((n) => `${r}${n}`)), 'bin'];
const name = (c: string) => (c === 'bin' ? 'The bin' : c);

/** class 1–5 by four ascending upper bounds: value ≤ bounds[0] → 1 … above bounds[3] → 5 */
export const byBounds = (v: number, bounds: number[]) => 1 + bounds.filter((b) => v > b).length;

/** Demonstrations per slot; `role` reads "as the source" or "as the destination". */
export function demoCells(counts: Record<string, number>, role: string, bounds: number[]): Cell[] {
  return PLACES.map((c) => {
    if (c === 'bin' && role === 'as the source') return { code: c, cls: null, text: '', title: 'The bin is never a source' };
    const v = counts[c] ?? 0;
    return { code: c, cls: v ? byBounds(v, bounds) : null, text: String(v),
      title: `${name(c)} ${role}: ${v} demonstration${v === 1 ? '' : 's'}` };
  });
}

/** Share of rollouts per slot that reached `what`: four classes (up to 25%, 50%, 75%, over), none for zero.
 *  Uses the stage colours, so a darker slot is a better outcome, as everywhere else on the site. */
export function rateCells(by: Record<string, { n: number; ok: number }>, role: string, what: string): Cell[] {
  return PLACES.map((c) => {
    if (c === 'bin' && role === 'as the source') return { code: c, cls: null, text: '', title: 'The bin is never a source' };
    const b = by[c];
    if (!b) return { code: c, cls: null, text: '–', title: `${name(c)} ${role}: no rollouts` };
    return { code: c, cls: b.ok === 0 ? null : Math.min(4, Math.ceil((b.ok / b.n) * 4)), text: `${b.ok}/${b.n}`,
      title: `${name(c)} ${role}: ${b.ok} of ${b.n} rollouts ${what}` };
  });
}

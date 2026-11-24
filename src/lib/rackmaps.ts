// Cells for the rack maps: the left rack, the bin and the right rack, slots 1–6 of each from left to right.
// A cell's class picks a step of a validated ramp; null leaves the slot empty.

export type Cell = { code: string; cls: number | null; text: string; title: string };
export type RackMap = { caption: string; ramp: 'd' | 'ob'; cells: Cell[] };  // ramps: demonstrations (violet), the August π0.5 blue

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
 *  Only the August page draws these (in its blue ramp); Results uses slotDemos / slotGot below. */
export function rateCells(by: Record<string, { n: number; ok: number }>, role: string, what: string): Cell[] {
  return PLACES.map((c) => {
    if (c === 'bin' && role === 'as the source') return { code: c, cls: null, text: '', title: 'The bin is never a source' };
    const b = by[c];
    if (!b) return { code: c, cls: null, text: '–', title: `${name(c)} ${role}: no rollouts` };
    return { code: c, cls: b.ok === 0 ? null : Math.min(4, Math.ceil((b.ok / b.n) * 4)), text: `${b.ok}/${b.n}`,
      title: `${name(c)} ${role}: ${b.ok} of ${b.n} rollouts ${what}` };
  });
}

// ── Results' slot maps (SlotMaps.astro): one solid colour per map, the number under each slot is the value ──
export type SlotCell = { code: string; on: boolean; text: string; title: string };
export type SlotMap = { caption: string; kind: 'demo' | 'got'; role: 'source' | 'destination'; cells: SlotCell[] };
const NEVER: SlotCell = { code: 'bin', on: false, text: '', title: 'The bin is never a source' };

/** Demonstrations per slot of a row's training set: a slot is filled when it has any. */
export function slotDemos(counts: Record<string, number>, role: SlotMap['role'], set: string): SlotMap {
  return { caption: `Demonstrations in ${set}, by ${role === 'source' ? 'source slot' : 'destination'}`, kind: 'demo', role,
    cells: PLACES.map((c) => {
      if (c === 'bin' && role === 'source') return NEVER;
      const v = counts[c] ?? 0;
      return { code: c, on: v > 0, text: String(v), title: `${name(c)} as the ${role}: ${v} demonstration${v === 1 ? '' : 's'}` };
    }) };
}

/** Rollouts per slot: filled when any rollout started (source) or ended (destination) there; the text is got/tried. */
export function slotGot(got: Record<string, { n: number; ok: number }>, role: SlotMap['role'], caption: string, verb: string): SlotMap {
  return { caption, kind: 'got', role,
    cells: PLACES.map((c) => {
      if (c === 'bin' && role === 'source') return NEVER;
      const g = got[c];
      if (!g || !g.n) return { code: c, on: false, text: '–', title: `${name(c)} as the ${role}: no rollouts` };
      return { code: c, on: true, text: `${g.ok}/${g.n}`, title: `${name(c)} as the ${role}: ${g.ok} of ${g.n} rollouts ${verb}` };
    }) };
}

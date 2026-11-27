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
// untr: the row's training set has no demonstration with this slot in this role (an untrained slot), drawn ringed
// level: how full the slot's colour is, 0 to 1. Rollouts: the share that got through (0 of 5 is an empty ring in the
// map's colour, 5 of 5 is solid). Demonstrations: the count against the largest count on that map.
export type SlotCell = { code: string; on: boolean; text: string; title: string; untr?: boolean; level?: number };
export type SlotMap = { caption: string; kind: 'demo' | 'got'; role: 'source' | 'destination'; cells: SlotCell[] };
const NEVER: SlotCell = { code: 'bin', on: false, text: '', title: 'The bin is never a source' };

/** Demonstrations per slot of a row's training set: a slot is filled when it has any. */
export function slotDemos(counts: Record<string, number>, role: SlotMap['role'], set: string): SlotMap {
  // the caption stays one line in a narrow column; the set's name is in the tooltip of each slot and beside the map
  return { caption: `Demonstrations, by ${role === 'source' ? 'source slot' : 'destination'}`, kind: 'demo', role,
    cells: PLACES.map((c) => {
      if (c === 'bin' && role === 'source') return NEVER;
      const v = counts[c] ?? 0;
      const most = Math.max(1, ...Object.values(counts));
      return { code: c, on: v > 0, text: String(v), untr: v === 0, level: v / most,
        title: `${name(c)} as the ${role}: ${v} demonstration${v === 1 ? '' : 's'} in ${set}${v ? '' : ' (untrained)'}` };
    }) };
}

/** Rollouts per slot: filled when any rollout started (source) or ended (destination) there; the text is got/tried.
 *  `untrained` names the slots its training set never used in this role; they are ringed like on the demonstration maps. */
export function slotGot(got: Record<string, { n: number; ok: number }>, role: SlotMap['role'], caption: string, verb: string,
                        untrained: Set<string> = new Set()): SlotMap {
  return { caption, kind: 'got', role,
    cells: PLACES.map((c) => {
      if (c === 'bin' && role === 'source') return NEVER;
      const g = got[c], untr = untrained.has(c), tag = untr ? ' (untrained)' : '';
      if (!g || !g.n) return { code: c, on: false, text: '–', untr, title: `${name(c)} as the ${role}${tag}: no rollouts` };
      return { code: c, on: true, text: `${g.ok}/${g.n}`, untr, level: g.ok / g.n, title: `${name(c)} as the ${role}${tag}: ${g.ok} of ${g.n} rollouts ${verb}` };
    }) };
}

/** The slots a training set never used in a role (0 demonstrations there), the bin as a source left out. */
export const untrainedSlots = (counts: Record<string, number>, role: SlotMap['role']) =>
  new Set(PLACES.filter((c) => !(c === 'bin' && role === 'source') && !(counts[c] ?? 0)));

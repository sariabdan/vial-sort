// Results page: success per command (chart 3), how far each command got (chart 4), and the
// player that shows a command's recorded trials. Clicking a command in either chart opens it.
import * as Plot from '@observablehq/plot';
import evals from '../data/evals.json';
import media from '../data/media.json';
import { mount, plotBase, tip, moveLabel, pct } from './common';

type Scenario = (typeof evals.scenarios)[number];
const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');
const STAGES = evals.stages;
const FILL = STAGES.map((_, i) => `var(--o4-${i + 1})`);
const INK = STAGES.map((_, i) => `var(--o4t-${i + 1})`);

// one order for both charts: best first, then more rollouts, then the evaluation's task order
const scen: Scenario[] = [...evals.scenarios].sort((a, b) => b.rate - a.rate || b.n - a.n || a.task - b.task);
const order = scen.map((s) => moveLabel(s.move));
const rowH = 30;

function onPick(plot: Element & { value?: unknown }) {
  plot.addEventListener('click', () => {
    const d = plot.value as { move?: string } | undefined;
    if (d?.move) select(d.move, true);
  });
  (plot as HTMLElement).style.cursor = 'pointer';
}

mount('per-move', (width) => {
  const plot = Plot.plot({
    ...plotBase,
    width,
    height: order.length * rowH + 44,
    marginLeft: 76,
    marginRight: 70,
    marginTop: 8,
    marginBottom: 36,
    x: { domain: [0, 100], percent: true, label: 'Completed (% of rollouts)', labelAnchor: 'left', labelOffset: 32, ticks: width < 520 ? 3 : 5 },
    y: { domain: order, label: null, tickSize: 0, tickPadding: 10 },
    marks: [
      Plot.gridX({ stroke: 'var(--grid)', strokeOpacity: 1, ticks: width < 520 ? 3 : 5 }),
      Plot.ruleX([0], { stroke: 'var(--rack)' }),
      Plot.ruleY(scen, { y: (d) => moveLabel(d.move), x1: 'lo', x2: 'hi', stroke: 'var(--m-pi05)', strokeOpacity: 0.45, strokeWidth: 2.5 }),
      Plot.dot(scen, {
        y: (d) => moveLabel(d.move), x: 'rate', r: 5.5, strokeWidth: 2, stroke: 'var(--m-pi05)',
        fill: (d) => (d.trained ? 'var(--m-pi05)' : 'var(--page)'),
        channels: { move: 'move' },
        title: (d) => `${moveLabel(d.move)}\n${d.complete} of ${d.n} completed (${pct(d.rate)})\n95% interval ${pct(d.lo)}–${pct(d.hi)}` +
          (d.trained ? '' : '\nSource slot held out of training') + '\nClick to watch the trials',
        tip,
      }),
      Plot.text(scen, { y: (d) => moveLabel(d.move), x: () => 1, dx: 12, textAnchor: 'start', text: (d) => `${d.complete} of ${d.n}`, fill: 'var(--ink-2)' }),
    ],
  });
  onPick(plot);
  return plot;
});

mount('per-move-pooled', (width) => {
  const rows = [
    { label: 'Trained source', ...evals.trained },
    { label: 'Held-out source', ...evals.held_out },
  ].map((r) => ({ ...r, rate: r.complete / r.rollouts }));
  return Plot.plot({
    ...plotBase,
    width,
    height: 2 * rowH + 16,
    marginLeft: 76, marginRight: 70, marginTop: 8, marginBottom: 8,
    x: { domain: [0, 100], percent: true, axis: null },
    y: { domain: rows.map((r) => r.label), label: null, tickSize: 0, tickPadding: 10, tickFormat: (t: string) => t },
    marks: [
      Plot.gridX({ stroke: 'var(--grid)', strokeOpacity: 1, ticks: width < 520 ? 3 : 5 }),
      Plot.ruleX([0], { stroke: 'var(--rack)' }),
      Plot.ruleY(rows, { y: 'label', x1: 'lo', x2: 'hi', stroke: 'var(--m-pi05)', strokeOpacity: 0.45, strokeWidth: 2.5 }),
      Plot.dot(rows, {
        y: 'label', x: 'rate', r: 6.5, strokeWidth: 2, stroke: 'var(--m-pi05)',
        fill: (d) => (d.label === 'Trained source' ? 'var(--m-pi05)' : 'var(--page)'),
        title: (d) => `${d.label}: ${d.complete} of ${d.rollouts} completed (${pct(d.rate)})\n${d.scenarios} commands\n95% interval ${pct(d.lo)}–${pct(d.hi)}`,
        tip,
      }),
      Plot.text(rows, { y: 'label', x: () => 1, dx: 12, textAnchor: 'start', text: (d) => `${d.complete} of ${d.rollouts}`, fill: 'var(--ink)', fontWeight: 600 }),
    ],
  });
});

mount('composition', (width) => {
  const rows = scen.flatMap((s) =>
    STAGES.map((st, i) => ({ move: s.move, row: moveLabel(s.move), stage: st.key, label: st.label, i, count: s.stages[st.key as keyof typeof s.stages], n: s.n }))
      .filter((r) => r.count > 0));
  const stack = { y: 'row', x: 'count', z: 'stage', order: STAGES.map((s) => s.key), offset: 'normalize' as const };
  const plot = Plot.plot({
    ...plotBase,
    width,
    height: order.length * rowH + 44,
    marginLeft: 76, marginRight: 8, marginTop: 8, marginBottom: 36,
    x: { domain: [0, 100], percent: true, label: 'Share of the command’s rollouts (%)', labelAnchor: 'left', labelOffset: 32, ticks: width < 520 ? 3 : 5 },
    y: { domain: order, label: null, tickSize: 0, tickPadding: 10, padding: 0.22 },
    marks: [
      Plot.barX(rows, Plot.stackX({
        ...stack, fill: (d) => FILL[d.i], insetLeft: 1, insetRight: 1,
        channels: { move: 'move' },
        title: (d) => `${d.row}\n${d.label}: ${d.count} of ${d.n}\nClick to watch the trials`,
        tip,
      })),
      Plot.text(rows, Plot.stackX({ ...stack, text: (d) => String(d.count), fill: (d) => INK[d.i], fontWeight: 600 })),
    ],
  });
  onPick(plot);
  return plot;
});

// ── the trial player ────────────────────────────────────────────────────────────────────────
const pick = document.getElementById('watch-move') as HTMLSelectElement;
const trialsEl = document.getElementById('watch-trials') as HTMLElement;
const video = document.getElementById('watch-video') as HTMLVideoElement;
const caption = document.getElementById('watch-caption') as HTMLElement;
const stageLabel = Object.fromEntries(STAGES.map((s) => [s.key, s.label]));
const captures = media.captures as Record<string, { src: string; poster: string }>;

function play(s: Scenario, k: number) {
  const cap = s.captures[k];
  const c = captures[cap.id];
  video.poster = `${BASE}/${c.poster}`;
  video.src = `${BASE}/${c.src}`;
  const trial = s.matched ? evals.trials.find((t) => t.move === s.move && t.i === k) : undefined;
  caption.textContent = trial
    ? `${moveLabel(s.move)}, trial ${k + 1} of ${s.n}: ${stageLabel[trial.stage]}${trial.collision ? ', with a collision' : ''}.` +
      (trial.note ? ` Scorer’s note: “${trial.note}”.` : '')
    : `${moveLabel(s.move)}, run ${k + 1} of ${s.captures.length} recorded in this command’s session. ` +
      `The session has ${s.captures.length} full runs for ${s.n} scored trials, so runs are not matched to scores.`;
  trialsEl.querySelectorAll('button').forEach((b, i) => b.setAttribute('aria-pressed', String(i === k)));
}

function select(move: string, scroll = false) {
  const s = scen.find((x) => x.move === move);
  if (!s) return;
  pick.value = move;
  trialsEl.replaceChildren(...s.captures.map((_, k) => {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'quiet-btn';
    const trial = s.matched ? evals.trials.find((t) => t.move === s.move && t.i === k) : undefined;
    b.textContent = trial ? `${k + 1}: ${stageLabel[trial.stage]}` : `Run ${k + 1}`;
    b.addEventListener('click', () => play(s, k));
    return b;
  }));
  play(s, 0);
  const smooth = !matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (scroll) document.getElementById('watch')?.scrollIntoView({ behavior: smooth ? 'smooth' : 'auto', block: 'nearest' });
}

pick.addEventListener('change', () => select(pick.value));
select(scen[0].move);

// Training page: each run's loss, and under it on the same step axis one square per scored rollout
// at each checkpoint that went on the robot, coloured by how far the rollout got.
import * as Plot from '@observablehq/plot';
import training from '../data/training.json';
import rollouts from '../data/rollouts.json';
import gate from '../data/gate.json';
import { mount, plotBase, tip } from './common';

type Run = (typeof training.runs)[number];
type RobotRow = Run['robot'][number];
const STAGES = rollouts.stages;
const color = (model: string) => `var(--m-${model})`;
const ramp = (_model: string, i: number) => `var(--st-${i + 1})`; // one set of stage colours for every model
const kStep = (s: number) => (s >= 1000 ? `${s / 1000}k` : String(s));
const UNIT = 11; // px per rollout square, gap included
const M = { marginLeft: 58, marginRight: 20 };

// one loss domain per model: the runs of a model share a y scale, different models do not
const lossDomain: Record<string, [number, number]> = {};
for (const r of training.runs) {
  const ys = r.points.map((p) => p.loss);
  const [lo, hi] = lossDomain[r.model] ?? [Infinity, 0];
  lossDomain[r.model] = [Math.min(lo, ...ys), Math.max(hi, ...ys)];
}

function summary(row: RobotRow) {
  const parts = [...STAGES].reverse().map((s) => [s.label, row.stages[s.key as keyof typeof row.stages]] as const)
    .filter(([, n]) => n > 0).map(([label, n]) => `${label}: ${n}`);
  return `${kStep(row.step)} steps, ${row.mode === 'rtc' ? 'RTC' : 'sync'}${row.ema ? ', EMA weights' : ''}\n${row.takes} rollout${row.takes === 1 ? '' : 's'}\n${parts.join('\n')}`;
}

/** One square per rollout, worst stage at the bottom; columns side by side where a checkpoint ran in several modes. */
function units(rows: RobotRow[], x: (r: RobotRow) => number | string) {
  const out: { x: number | string; i: number; col: number; stage: number; title: string }[] = [];
  const groups = new Map<number | string, RobotRow[]>();
  for (const r of rows) groups.set(x(r), [...(groups.get(x(r)) ?? []), r]);
  for (const [gx, rs] of groups) {
    rs.forEach((r, k) => {
      let i = 0;
      STAGES.forEach((s, si) => {
        for (let n = 0; n < r.stages[s.key as keyof typeof r.stages]; n++) {
          out.push({ x: gx, i: i++, col: k - (rs.length - 1) / 2, stage: si, title: summary(r) });
        }
      });
    });
  }
  return out;
}

// The loss curves: the runs ticked in the page's list, one chart per kind of model (each kind measures its loss
// differently, so only runs of one kind share an axis). A run keeps one colour, its place in a fixed order, the same
// as its swatch in the list and the table (src/pages/training.astro).
const SERIES = ['pi05', 'flux', 'groot', 'pi0', 'act', 'isaac'];
const seriesColor = (id: string) => `var(--m-${SERIES[training.runs.findIndex((r) => r.id === id) % SERIES.length]})`;
const LOSS_NAME: Record<string, string> = { flux: 'loss (video + action)', isaac: 'flow loss (action expert)' };
const KIND: Record<string, string> = { pi05: 'π0.5', flux: 'FLUX 3 Action', isaac: 'Isaac 0.5' };
const lossHost = document.querySelector<HTMLElement>('[data-loss]');
const runBoxes = [...document.querySelectorAll<HTMLInputElement>('[data-run-box]')];
function drawLoss() {
  if (!lossHost) return;
  const on = new Set(runBoxes.filter((b) => b.checked).map((b) => b.dataset.runBox));
  const picked = training.runs.filter((r) => on.has(r.id));
  document.querySelectorAll<HTMLElement>('[data-run-row]').forEach((tr) => (tr.hidden = !on.has(tr.dataset.runRow)));
  document.querySelector<HTMLElement>('[data-loss-empty]')!.hidden = picked.length > 0;
  const width = Math.round(lossHost.clientWidth);
  if (!width) return;  // the tab is closed: it is drawn when it opens (the observer below)
  const kinds = [...new Set(picked.map((r) => r.model))];
  lossHost.style.minHeight = '';
  lossHost.replaceChildren(...kinds.map((kind) => {
    const mine = picked.filter((r) => r.model === kind);
    const points = mine.flatMap((r) => r.points.map((p) => ({ ...p, run: r.id })));
    const names = Object.fromEntries(mine.map((r) => [r.id, document.querySelector(`[data-run-row="${r.id}"] th`)?.textContent ?? r.id]));
    const box = document.createElement('div');
    const head = document.createElement('h3');
    head.innerHTML = `${KIND[kind] ?? kind} <span>${LOSS_NAME[kind] ?? 'loss'}, ${mine.length} run${mine.length === 1 ? '' : 's'}</span>`;
    box.append(head, Plot.plot({
      ...plotBase,
      ...M,
      width,
      height: kinds.length > 2 ? 150 : kinds.length === 2 ? 190 : 260,
      marginTop: 10,
      marginBottom: 24,
      x: { domain: [0, Math.max(...mine.map((r) => r.steps))], tickFormat: kStep, ticks: width < 500 ? 3 : 6, label: null },
      y: { type: 'log', domain: lossDomain[kind], label: null, ticks: 3, tickFormat: '~g' },
      marks: [
        Plot.gridY({ stroke: 'var(--grid)', strokeOpacity: 1, ticks: 3 }),
        Plot.lineY(points, { x: 'step', y: 'loss', z: 'run', stroke: (d) => seriesColor(d.run), strokeWidth: 2 }),
        Plot.dot(points, Plot.pointer({ x: 'step', y: 'loss', r: 4, fill: (d) => seriesColor(d.run), stroke: 'var(--page)', strokeWidth: 2 })),
        Plot.tip(points, Plot.pointer({ x: 'step', y: 'loss', ...tip,
          title: (d) => `${names[d.run]}\n${kStep(d.step)} steps\nloss ${d.loss.toPrecision(3)}${d.action_mse ? `\naction error ${d.action_mse.toPrecision(3)}` : ''}` })),
      ],
    }));
    return box;
  }));
}
if (lossHost) {
  runBoxes.forEach((b) => b.addEventListener('change', drawLoss));
  document.querySelectorAll<HTMLElement>('[data-runs]').forEach((b) => b.addEventListener('click', () => {
    runBoxes.forEach((x) => (x.checked = b.dataset.runs === 'all'));
    drawLoss();
  }));
  let lastWidth = 0;
  new ResizeObserver(() => { const w = Math.round(lossHost.clientWidth); if (w !== lastWidth) { lastWidth = w; drawLoss(); } }).observe(lossHost);
  drawLoss();
}

for (const run of training.runs) {
  if (!run.robot.length) continue;
  const data = units(run.robot, (r) => r.step);
  const tall = Math.max(...data.map((d) => d.i)) + 1;
  mount(`robot-${run.id}`, (width) => {
    // columns of one checkpoint sit side by side: a column is UNIT px, in steps at this width
    const perPx = run.steps / (width - M.marginLeft - M.marginRight);
    return Plot.plot({
      ...plotBase,
      ...M,
      width,
      height: tall * UNIT + 34,
      marginTop: 6,
      marginBottom: 26,
      x: { domain: [0, run.steps], ticks: run.robot.map((r) => r.step), tickFormat: kStep, label: null, tickSize: 0 },
      y: { domain: [-0.6, tall - 0.4], axis: null },
      marks: [
        Plot.dot(data, { x: (d) => (d.x as number) + d.col * UNIT * perPx, y: 'i', symbol: 'square', r: 5.1,
                         fill: (d) => ramp(run.model, d.stage), title: 'title', tip }),
      ],
    });
  });
}

mount('gate-error', (width) => {
  const rows = gate.checkpoints.flatMap((g) => [
    { step: g.step, series: 'Insertion error', value: g.insertion_err },
    { step: g.step, series: 'Gripper error', value: g.gripper_err },
  ]);
  const stroke = (s: string) => (s === 'Insertion error' ? 'var(--m-pi05)' : 'var(--steel)');
  const end = rows.filter((r) => r.step === gate.checkpoints[gate.checkpoints.length - 1].step);
  return Plot.plot({
    ...plotBase,
    width,
    height: 240,
    marginLeft: 44, marginRight: width < 520 ? 90 : 120, marginTop: 30, marginBottom: 30,
    x: { domain: [1000, 12000], tickFormat: kStep, ticks: width < 520 ? 4 : 6, label: null },
    y: { domain: [0, 8], label: 'Degrees', labelAnchor: 'top', ticks: 4 },
    marks: [
      Plot.gridY({ stroke: 'var(--grid)', strokeOpacity: 1, ticks: 4 }),
      Plot.ruleY([0], { stroke: 'var(--rack)' }),
      Plot.lineY(rows, { x: 'step', y: 'value', z: 'series', stroke: (d) => stroke(d.series), strokeWidth: 2 }),
      Plot.dot(rows, Plot.pointerX({ x: 'step', y: 'value', z: 'series', r: 4, fill: (d) => stroke(d.series), stroke: 'var(--page)', strokeWidth: 2 })),
      // the two lines end 0.3° apart: put the upper label above its line and the lower below
      Plot.text(end.filter((d) => d.series === 'Gripper error'), { x: 'step', y: 'value', text: 'series', dx: 8, dy: -7, textAnchor: 'start', fill: 'var(--ink)' }),
      Plot.text(end.filter((d) => d.series !== 'Gripper error'), { x: 'step', y: 'value', text: 'series', dx: 8, dy: 7, textAnchor: 'start', fill: 'var(--ink)' }),
      Plot.tip(rows, Plot.pointerX({ x: 'step', y: 'value', z: 'series', ...tip,
        title: (d) => `${kStep(d.step)} steps\n${d.series}: ${d.value}°` })),
    ],
  });
});

mount('robot-probes', (width) => {
  const rows = training.probes.flatMap((p) => p.robot.map((r) => ({ ...r, probe: p.name })));
  const labels = rows.map((r) => `${r.probe} (${r.step} steps)`);
  const data = units(rows as unknown as RobotRow[], (r) => `${(r as unknown as { probe: string }).probe} (${r.step} steps)`);
  const tall = Math.max(...data.map((d) => d.i)) + 1;
  return Plot.plot({
    ...plotBase,
    width,
    height: tall * UNIT + 40,
    marginLeft: 18, marginRight: 18, marginTop: 6, marginBottom: 30,
    x: { domain: labels, label: null, tickSize: 0, padding: 0.3 },
    y: { domain: [-0.6, tall - 0.4], axis: null },
    marks: [Plot.dot(data, { x: 'x', y: 'i', symbol: 'square', r: 5.1, fill: (d) => ramp('pi05', d.stage), title: 'title', tip })],
  });
});

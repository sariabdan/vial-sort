// Results page: the compare rail drives everything. The page is rendered with every row; this script
// shows the ticked ones, redraws the axis, and keeps the selection in the URL (?r=key,key).
import results from '../data/results.json';

const rows = results.rows;
const byKey = new Map(rows.map((r) => [r.key, r]));
const all = (sel: string, root: ParentNode = document) => [...root.querySelectorAll<HTMLElement>(sel)];
const rowBoxes = all('[data-row-box]') as HTMLInputElement[];
const modelBoxes = all('[data-model-box]') as HTMLInputElement[];
const MAX_MAPS = 4;

const fromUrl = () => {
  const r = new URLSearchParams(location.search).get('r');
  return r === null ? null : r.split(',').filter((k) => byKey.has(k));
};
const state = new Set<string>(fromUrl() ?? results.defaults);
let scale: 'share' | 'count' = 'share';
const stageOn = new Set(results.stages.map((s) => s.key));

function ticks(mode: 'share' | 'count', max: number) {
  const step = mode === 'share' ? 25 : max <= 6 ? 1 : max <= 12 ? 2 : max <= 30 ? 5 : 10;
  const end = mode === 'share' ? 100 : Math.ceil(max / step) * step;
  const out: string[] = [];
  for (let v = 0; v <= end; v += step) {
    out.push(`<span style="left:${(v / end) * 100}%">${v}${mode === 'share' ? '%' : ''}</span>`);
  }
  return { html: `<div class="ticks">${out.join('')}</div>`, end };
}

function draw() {
  const chosen = rows.filter((r) => state.has(r.key));
  // rail
  rowBoxes.forEach((b) => (b.checked = state.has(b.dataset.rowBox!)));
  modelBoxes.forEach((b) => {
    const mine = rowBoxes.filter((x) => x.dataset.of === b.dataset.modelBox);
    const on = mine.filter((x) => x.checked).length;
    b.checked = on === mine.length;
    b.indeterminate = on > 0 && on < mine.length;
  });
  document.getElementById('rail-count')!.textContent = `${chosen.length} of ${rows.length} ticked`;

  // bars and table
  const max = Math.max(1, ...chosen.map((r) => r.rollouts));
  const bars = document.getElementById('bars')!;
  bars.dataset.mode = scale;
  const t = ticks(scale, max);
  // in count mode the longest bar is `end` wide so the axis and the segments agree
  bars.style.setProperty('--max', String(scale === 'count' ? t.end : 1));
  document.getElementById('axis')!.innerHTML = chosen.length ? t.html : '';
  all('.bar-row, .twin tr[data-row]').forEach((el) => (el.hidden = !state.has(el.dataset.row!)));
  document.getElementById('bars-empty')!.hidden = chosen.length > 0;

  // slot maps: the first four ticked
  let shown = 0;
  all('.slot-row').forEach((el) => {
    const on = state.has(el.dataset.row!) && shown < MAX_MAPS;
    el.hidden = !on;
    if (on) shown++;
  });
  document.getElementById('slots-empty')!.hidden = chosen.length > 0;
  document.getElementById('slots-more')!.hidden = chosen.length <= MAX_MAPS;

  // rollouts to watch
  let clips = 0;
  all('.clip-wrap').forEach((el) => {
    const on = state.has(el.dataset.row!) && stageOn.has(el.dataset.stage!);
    el.hidden = !on;
    if (on) clips++;
  });
  document.getElementById('clips-empty')!.hidden = clips > 0;

  // url
  const q = new URLSearchParams(location.search);
  const same = [...state].sort().join() === [...results.defaults].sort().join();
  if (same) q.delete('r'); else q.set('r', rows.filter((r) => state.has(r.key)).map((r) => r.key).join(','));
  try { history.replaceState(null, '', `${location.pathname}${q.toString() ? `?${q}` : ''}`); } catch (e) {}
}

rowBoxes.forEach((b) => b.addEventListener('change', () => {
  if (b.checked) state.add(b.dataset.rowBox!); else state.delete(b.dataset.rowBox!);
  draw();
}));
modelBoxes.forEach((b) => b.addEventListener('change', () => {
  for (const r of rows.filter((x) => x.model === b.dataset.modelBox)) {
    if (b.checked) state.add(r.key); else state.delete(r.key);
  }
  draw();
}));
document.getElementById('pick-none')!.addEventListener('click', () => { state.clear(); draw(); });
document.getElementById('pick-all')!.addEventListener('click', () => { rows.forEach((r) => state.add(r.key)); draw(); });
document.getElementById('pick-newest')!.addEventListener('click', () => { state.clear(); results.defaults.forEach((k) => state.add(k)); draw(); });
all('[data-scale]').forEach((b) => b.addEventListener('click', () => {
  scale = b.dataset.scale as 'share' | 'count';
  all('[data-scale]').forEach((x) => x.setAttribute('aria-pressed', String(x === b)));
  draw();
}));
all('[data-stage]').forEach((b) => {
  if (b.tagName !== 'BUTTON') return;
  b.addEventListener('click', () => {
    const k = b.dataset.stage!;
    if (stageOn.has(k)) stageOn.delete(k); else stageOn.add(k);
    b.setAttribute('aria-pressed', String(stageOn.has(k)));
    draw();
  });
});
draw();

// on a phone the compare list is long: start it closed (the count still shows which rows are ticked)
if (matchMedia('(max-width: 62rem)').matches) document.querySelector('.rail-box')?.removeAttribute('open');

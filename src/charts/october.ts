// Results page. The list of runs on the left is the picker: a ticked run joins the comparison. The right side holds
// one row (or one block) per run in every tab, all of them in the page; this script shows the ticked ones in the
// order they were ticked, letters them A, B, C and so on, switches the tabs, and keeps the
// selection, the tab and the demonstrations switch in the URL (?r=key,key&v=tab&d=0).
import results from '../data/results.json';

const rows = results.rows;
const MAX = rows.length;  // the runs are rows now, so any number can be ticked
const byKey = new Map(rows.map((r) => [r.key, r]));
const all = (sel: string, root: ParentNode = document) => [...root.querySelectorAll<HTMLElement>(sel)];
const boxes = all('[data-row-box]') as HTMLInputElement[];
const modelBoxes = all('[data-model-box]') as HTMLInputElement[];
const note = document.getElementById('pick-note')!;
const LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const TABS = all('[data-tab]').map((b) => b.dataset.tab!);
// addresses the old page layout used, and which tab they are on now
const FROM_HASH: Record<string, string> = { '#h-score': 'compare', '#h-slot': 'compare', '#h-far': 'compare', '#h-watch': 'compare', '#h-said': 'notes', '#h-moves': 'detail' };
const startHash = location.hash;

const params = new URLSearchParams(location.search);
const fromUrl = params.get('r');
// ordered: the order of ticking is the order of the columns
let state: string[] = (fromUrl === null ? results.defaults : fromUrl.split(',').filter((k) => byKey.has(k))).slice(0, MAX);
let tab = FROM_HASH[location.hash] ?? (TABS.includes(params.get('v') ?? '') ? params.get('v')! : TABS[0]);
let stage = 'released';
const demoBox = document.getElementById('show-demos') as HTMLInputElement;
let demosOn = params.get('d') !== '0';
let noteTimer = 0;
function say(text: string) {
  note.textContent = text;
  clearTimeout(noteTimer);
  if (text) noteTimer = window.setTimeout(() => (note.textContent = ''), 4000);
}

function draw() {
  const at = (key?: string) => (key ? state.indexOf(key) : -1);

  // the list: ticks, letters, and a folded group opens when one of its runs is ticked
  boxes.forEach((b) => {
    const i = at(b.dataset.rowBox);
    b.checked = i >= 0;
    const line = b.closest('.run')!;
    line.querySelector('.letter')!.textContent = i < 0 ? '' : LETTERS[i];
  });
  // a branch of the tree: its box is ticked when all its checkpoints are, half-ticked when some are
  modelBoxes.forEach((b) => {
    const mine = boxes.filter((x) => x.dataset.of === b.dataset.modelBox);
    const on = mine.filter((x) => x.checked).length;
    b.checked = on > 0 && on === mine.length;
    b.indeterminate = on > 0 && on < mine.length;
  });
  document.getElementById('runs-count')!.textContent = `${state.length} of ${rows.length} ticked`;

  // the columns and the full-width blocks: shown when ticked, in ticking order, with their letter
  all('.col, .wide-row').forEach((el) => {
    const i = at(el.dataset.row);
    el.hidden = i < 0;
    el.style.order = String(Math.max(i, 0));
    const letter = el.querySelector('.letter');
    if (letter) letter.textContent = i < 0 ? '' : LETTERS[i];
  });
  all('.cols').forEach((el) => el.style.setProperty('--n', String(Math.max(state.length, 1))));
  // each run's training demonstrations, under its vials: shown or hidden by the switch in the legend
  demoBox.checked = demosOn;
  document.querySelector<HTMLElement>('.runs-table')!.dataset.demos = demosOn ? 'on' : 'off';

  // one tab at a time
  all('[data-tab]').forEach((b) => b.setAttribute('aria-selected', String(b.dataset.tab === tab)));
  all('[data-panel]').forEach((p) => (p.hidden = p.dataset.panel !== tab || !state.length));
  document.getElementById('none-picked')!.hidden = state.length > 0;

  // video: one rollout per run, of the outcome chosen
  all('[data-stage]').forEach((b) => { if (b.tagName === 'BUTTON') b.setAttribute('aria-pressed', String(b.dataset.stage === stage)); });
  all('.vids .col').forEach((col) => {
    let shown = 0;
    all('.clip-wrap', col).forEach((el) => { el.hidden = el.dataset.stage !== stage || shown > 0; if (!el.hidden) shown++; });
    (col.querySelector('.no-clip') as HTMLElement).hidden = shown > 0;
  });

  // everything is now shown or hidden by this script: drop what kept the first paint clean (src/layouts/Base.astro)
  all('[data-init-off]').forEach((el) => el.removeAttribute('data-init-off'));
  document.querySelector('.view')?.removeAttribute('data-await');

  // url
  const q = new URLSearchParams(location.search);
  if (state.join() === results.defaults.slice(0, MAX).join()) q.delete('r'); else q.set('r', state.join(','));
  if (tab === TABS[0]) q.delete('v'); else q.set('v', tab);
  if (demosOn) q.delete('d'); else q.set('d', '0');
  try { history.replaceState(null, '', `${location.pathname}${q.toString() ? `?${q}` : ''}`); } catch (e) {}
}

function toggle(key: string, on: boolean) {
  if (!on) state = state.filter((k) => k !== key);
  else if (state.includes(key)) return;
  else if (state.length >= MAX) say(`${MAX} at most side by side: untick one first.`);
  else state = [...state, key];
  draw();
}

boxes.forEach((b) => b.addEventListener('change', () => toggle(b.dataset.rowBox!, b.checked)));
modelBoxes.forEach((b) => b.addEventListener('change', () => {
  const mine = rows.filter((r) => r.model === b.dataset.modelBox).map((r) => r.key);
  state = b.checked ? [...state, ...mine.filter((k) => !state.includes(k))] : state.filter((k) => !mine.includes(k));
  draw();
}));
all('[data-preset]').forEach((b) => b.addEventListener('click', () => {
  state = b.dataset.preset!.split(',').filter((k) => byKey.has(k)).slice(0, MAX);
  say('');
  draw();
}));
all('[data-tab]').forEach((b) => b.addEventListener('click', () => { tab = b.dataset.tab!; draw(); }));
demoBox.addEventListener('change', () => { demosOn = demoBox.checked; draw(); });

// Reordering: a row is dragged by its handle and dropped above or below another row; with the keyboard, the up and
// down arrow keys on the handle move it one place. The order is the order of ticking, so it holds in every tab and
// in the URL.
const runRows = all('.runs-table .rt-row.col');
let dragging: string | null = null;
const unmark = () => runRows.forEach((r) => r.classList.remove('drop-before', 'drop-after', 'dragging'));
function place(key: string, target: string, after: boolean) {
  if (key === target || !state.includes(key) || !state.includes(target)) return;
  const rest = state.filter((k) => k !== key);
  rest.splice(rest.indexOf(target) + (after ? 1 : 0), 0, key);
  state = rest;
  draw();
}
runRows.forEach((row) => {
  const key = row.dataset.row!;
  const grip = row.querySelector<HTMLElement>('.grip')!;
  // only the handle starts a drag, so text in the row can still be selected
  grip.addEventListener('pointerdown', () => (row.draggable = true));
  grip.addEventListener('pointerup', () => (row.draggable = false));
  row.addEventListener('dragstart', (e) => {
    dragging = key;
    e.dataTransfer!.effectAllowed = 'move';
    e.dataTransfer!.setData('text/plain', key);
    requestAnimationFrame(() => row.classList.add('dragging'));
  });
  row.addEventListener('dragend', () => { row.draggable = false; dragging = null; unmark(); });
  row.addEventListener('dragover', (e) => {
    if (!dragging || dragging === key) return;
    e.preventDefault();
    const box = row.getBoundingClientRect();
    const after = e.clientY > box.top + box.height / 2;
    row.classList.toggle('drop-after', after);
    row.classList.toggle('drop-before', !after);
  });
  row.addEventListener('dragleave', () => row.classList.remove('drop-before', 'drop-after'));
  row.addEventListener('drop', (e) => {
    if (!dragging) return;
    e.preventDefault();
    const after = row.classList.contains('drop-after');
    const moved = dragging;
    unmark();
    place(moved, key, after);
  });
  grip.addEventListener('keydown', (e) => {
    const step = e.key === 'ArrowUp' ? -1 : e.key === 'ArrowDown' ? 1 : 0;
    const i = state.indexOf(key), j = i + step;
    if (!step || j < 0 || j >= state.length) return;
    e.preventDefault();
    [state[i], state[j]] = [state[j], state[i]];
    draw();
    grip.focus();
  });
});
all('[data-stage]').forEach((b) => {
  if (b.tagName === 'BUTTON') b.addEventListener('click', () => { stage = b.dataset.stage!; draw(); });
});
draw();
// a link to the rollouts lands on them (they sit under the slot maps of the first tab)
if (startHash === '#h-watch') document.getElementById('h-watch')?.scrollIntoView();

// below a small laptop's width the list sits above the comparison: start it closed there (the count stays visible)
if (matchMedia('(max-width: 56rem)').matches) document.querySelector('.runs-box')?.removeAttribute('open');

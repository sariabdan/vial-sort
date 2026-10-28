// Datasets page: every training dataset on the Hub by date and size (chart 6). Uploads of the same
// recordings in two formats (equal episode and frame counts) share one dot.
import * as Plot from '@observablehq/plot';
import datasets from '../data/datasets.json';
import { mount, plotBase, tip } from './common';

const groups = new Map<string, { date: Date; episodes: number; frames: number; names: string[] }>();
for (const d of datasets.datasets.filter((d) => d.kind === 'training' && d.episodes)) {
  const key = `${d.episodes}-${d.frames}`;
  const g = groups.get(key);
  const date = new Date(`${d.updated}T12:00:00Z`);
  if (g) {
    g.names.push(d.name);
    if (date < g.date) g.date = date;
  } else groups.set(key, { date, episodes: d.episodes!, frames: d.frames!, names: [d.name] });
}
const data = [...groups.values()].map((g) => ({
  ...g,
  label: g.names.map((n) => n.replace(/^vial-sort-/, '')).join(' and '),
  minutes: Math.round(g.frames / 30 / 60),
}));

mount('dataset-versions', (width) =>
  Plot.plot({
    ...plotBase,
    width,
    height: 240,
    marginLeft: 44,
    marginRight: width < 520 ? 70 : 120,
    marginTop: 18,
    marginBottom: 30,
    x: { type: 'utc', label: null, ticks: width < 520 ? 3 : 5, tickFormat: '%b' },
    y: { domain: [0, 170], label: 'Demonstrations', labelAnchor: 'top', ticks: 4 },
    marks: [
      Plot.gridY({ stroke: 'var(--grid)', strokeOpacity: 1, ticks: 4 }),
      Plot.ruleY([0], { stroke: 'var(--rack)' }),
      Plot.dot(data, {
        x: 'date', y: 'episodes', r: 6, fill: 'var(--d-3)', stroke: 'var(--page)', strokeWidth: 2,
        title: (d) => `${d.names.join('\n')}\n${d.episodes} demonstrations, about ${d.minutes} minutes of recording`,
        tip,
      }),
      Plot.text(data, { x: 'date', y: 'episodes', text: 'label', dx: 10, textAnchor: 'start', fill: 'var(--ink)', lineWidth: 12 }),
    ],
  }));

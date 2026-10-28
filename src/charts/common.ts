// Shared by every chart script. Colours are CSS variables, so a chart follows the light/dark
// theme without re-rendering; it re-renders only when its figure changes width.

/** Draw a chart into its figure (the [data-chart] element) at the figure's width. */
export function mount(id: string, draw: (width: number) => Element) {
  const el = document.querySelector<HTMLElement>(`[data-chart="${id}"]`);
  if (!el) return;
  let last = 0;
  const render = () => {
    const width = Math.round(el.clientWidth);
    if (!width || width === last) return;
    last = width;
    el.replaceChildren(draw(width));
    el.style.minHeight = '';
  };
  render();
  new ResizeObserver(render).observe(el);
}

/** Options every Plot shares: the site's font and ink, colours passed through as written. */
export const plotBase = {
  style: { fontFamily: 'var(--font)', fontSize: '13px', color: 'var(--ink-2)', background: 'transparent', overflow: 'visible' },
  color: { type: 'identity' as const },
};

export const tip = { fill: 'var(--raise)', stroke: 'var(--rule)', fontSize: 13 };

export const moveLabel = (m: string) => m.replace('->', ' → ');

export const pct = (x: number) => `${Math.round(x * 100)}%`;

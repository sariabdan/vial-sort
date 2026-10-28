// Paths and formatters shared by pages, components and chart scripts.

const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');

/** A path inside the site, with the GitHub Pages base in front. */
export const url = (p: string) => `${BASE}/${p.replace(/^\//, '')}`;

export const pct = (x: number, digits = 0) => `${(x * 100).toFixed(digits)}%`;

/** 'R3->L3' → 'R3 → L3', the project's notation. */
export const moveLabel = (m: string | null | undefined) => (m ? m.replace('->', ' → ') : '');

/** The five cameras of the October rig, in the order every page lists them. */
export const CAMERA_NAMES: Record<string, string> = {
  top_down: 'Overhead',
  left_top: 'Across the table',
  left_bottom: 'Near eye level',
  right: 'From the side',
  wrist: 'On the gripper',
};

export const HF = 'https://huggingface.co';
export const CODE = 'https://github.com/Cognitive-Software-Labs/lerebot';

/** One episode of a public LeRobot dataset in the Hugging Face visualizer. */
export const visualizer = (repo: string, episode = 0) =>
  `${HF}/spaces/lerobot/visualize_dataset?path=/${repo}/episode_${episode}`;

export const MODELS: Record<string, { label: string; color: string }> = {
  pi05: { label: 'π0.5', color: 'var(--m-pi05)' },
  flux: { label: 'FLUX 3 Action', color: 'var(--m-flux)' },
  groot: { label: 'GR00T N1.5', color: 'var(--m-groot)' },
  pi0: { label: 'π0', color: 'var(--m-pi0)' },
  act: { label: 'ACT', color: 'var(--m-act)' },
};

/** CSS colours of a model's 5-stage "how far the take got" ramp (worst → best). */
export const stageRamp = (model: string) =>
  [1, 2, 3, 4, 5].map((k) => `var(--${model === 'flux' ? 'oo' : 'ob'}-${k})`);

export const V5_RAMP = [1, 2, 3, 4].map((k) => `var(--o4-${k})`);
export const DEMO_RAMP = [1, 2, 3, 4, 5].map((k) => `var(--d-${k})`);

/** '20261021' or '2026-10-21' → '21 Oct 2026'. */
export const date = (s: string) => {
  const iso = /^\d{8}$/.test(s) ? `${s.slice(0, 4)}-${s.slice(4, 6)}-${s.slice(6, 8)}` : s.slice(0, 10);
  return new Date(`${iso}T12:00:00Z`).toLocaleDateString('en-GB', {
    day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC',
  });
};

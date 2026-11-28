// @ts-check
import { defineConfig } from 'astro/config';

// Served from GitHub Pages at https://cognitive-software-labs.github.io/vial-sort/
export default defineConfig({
  site: 'https://cognitive-software-labs.github.io',
  base: '/vial-sort',
  devToolbar: { enabled: false },
});

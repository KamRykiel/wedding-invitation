import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5174,
  },
  // Build to repo root so Vercel serves /index.html correctly
  build: {
    outDir: '../dist',
    emptyOutDir: true,
  },
})

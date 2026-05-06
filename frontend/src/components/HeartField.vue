<template>
  <div class="field" aria-hidden="true">
    <span v-for="h in hearts" :key="h.id" class="heart" :style="h.style">♥</span>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

type Heart = { id: number; style: Record<string, string> }

const props = defineProps<{ density?: number }>()

const hearts = computed<Heart[]>(() => {
  const n = Math.max(12, Math.min(64, props.density ?? 28))
  const out: Heart[] = []
  for (let i = 0; i < n; i++) {
    const x = `${Math.random() * 100}%`
    const delay = `${Math.random() * 14}s`
    const dur = `${12 + Math.random() * 16}s`
    const fs = `${6 + Math.random() * 10}px`
    const drift = `${Math.random() * 90 - 45}px`
    const op = `${0.45 + Math.random() * 0.45}`
    out.push({
      id: i,
      style: {
        '--x': x,
        '--delay': delay,
        '--dur': dur,
        '--fs': fs,
        '--drift': drift,
        '--op': op,
      } as any,
    })
  }
  return out
})
</script>

<style scoped>
.field {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 1;
  overflow: hidden;
}
.heart {
  position: absolute;
  bottom: -8%;
  left: var(--x, 50%);
  font-size: var(--fs, 12px);
  opacity: var(--op, 0.7);
  color: rgba(255, 255, 255, 0.92);
  text-shadow:
    0 0 10px rgba(255, 255, 255, 0.55),
    0 1px 3px rgba(75, 58, 53, 0.25);
  animation: floatUp var(--dur, 16s) linear infinite;
  animation-delay: var(--delay, 0s);
}
@keyframes floatUp {
  0% {
    transform: translate3d(0, 0, 0) rotate(0deg);
    opacity: 0;
  }
  8% {
    opacity: var(--op, 0.7);
  }
  92% {
    opacity: calc(var(--op, 0.7) * 0.9);
  }
  100% {
    transform: translate3d(var(--drift, 40px), -112vh, 0) rotate(18deg);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .heart {
    animation: none !important;
  }
}
</style>


<template>
  <section class="finale" data-reveal="block" :style="bg">
    <div class="inner">
      <h2 class="t" data-reveal="line">Nous avons hâte de partager ce moment unique avec vous</h2>
      <p class="sig" data-reveal="line">{{ event?.couple_name ?? 'Wilfried & Ornella' }}</p>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { EventDto } from '../stores/event'

const props = defineProps<{ event: EventDto | null; heroImageUrl: string }>()

const bg = computed(() => {
  const url = props.heroImageUrl ? `url("${props.heroImageUrl}")` : 'none'
  return {
    backgroundImage: `
      linear-gradient(180deg, rgba(20,14,13,0.54) 0%, rgba(20,14,13,0.16) 42%, rgba(255,255,255,0.0) 70%, rgba(255,255,255,0.96) 100%),
      ${url}
    `,
  } as any
})
</script>

<style scoped>
.finale {
  margin-top: var(--space-y);
  border-radius: clamp(1.25rem, 4vw, 2rem);
  overflow: hidden;
  position: relative;
  min-height: min(72vh, 620px);
  display: grid;
  align-items: end;
  box-shadow: var(--shadow-lift);
  border: 1px solid rgba(211, 187, 161, 0.35);
  background-size: cover;
  background-position: center;
}
.inner {
  padding: clamp(1.5rem, 5vw, 2.25rem);
  text-align: center;
}
.t {
  font-family: "Playfair Display", Georgia, serif;
  font-size: clamp(1.95rem, 6.5vw, 3.1rem);
  font-weight: 650;
  color: rgba(255, 255, 255, 0.96);
  text-shadow: 0 18px 70px rgba(0, 0, 0, 0.28);
  line-height: 1.15;
  margin: 0;
}
.sig {
  margin: 0.85rem 0 0;
  font-family: "Playfair Display", Georgia, serif;
  font-size: 1.1rem;
  font-style: italic;
  color: rgba(255, 255, 255, 0.9);
  letter-spacing: 0.02em;
  text-shadow: 0 12px 50px rgba(0, 0, 0, 0.25);
}
</style>


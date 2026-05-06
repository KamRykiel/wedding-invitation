<template>
  <header class="topbar" data-reveal="block">
    <div class="brand">{{ coupleName }}</div>
    <nav class="nav" aria-label="Navigation">
      <a v-for="s in sections" :key="s.id" class="link" :href="`#${s.id}`">{{ s.label }}</a>
    </nav>
  </header>
</template>

<script setup lang="ts">
export type NavSection = { id: string; label: string }

defineProps<{
  sections: NavSection[]
  coupleName: string
}>()
</script>

<style scoped>
.topbar {
  position: sticky;
  top: 0;
  z-index: 50;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  flex-wrap: wrap;
  padding: 0.9rem clamp(1.15rem, 4vw, 2.4rem);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.7);
  border-bottom: 1px solid rgba(211, 187, 161, 0.35);
}

.brand {
  font-family: "Playfair Display", Georgia, serif;
  font-size: 1.02rem;
  font-weight: 500;
  font-style: italic;
  color: var(--c-primary);
  letter-spacing: 0.03em;
}

.nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.15rem;
  justify-content: flex-end;
}

.link {
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--c-ink);
  text-decoration: none;
  padding: 0.45rem 0.5rem;
  border-radius: var(--radius-sm);
  transition: background 0.2s, transform 0.2s var(--ease-out);
}

.link:hover {
  background: rgba(255, 255, 255, 0.85);
  transform: translateY(-1px);
}

.link:focus-visible {
  outline: 2px solid var(--c-primary);
  outline-offset: 2px;
}
</style>


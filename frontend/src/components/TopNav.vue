<template>
  <header class="topbar" data-reveal="block">
    <div class="brand">{{ coupleName }}</div>
    <button class="burger" type="button" aria-label="Menu" :aria-expanded="open ? 'true' : 'false'" @click="toggle">
      <span></span><span></span><span></span>
    </button>

    <nav class="nav" aria-label="Navigation">
      <a v-for="s in sections" :key="s.id" class="link" :href="`#${s.id}`">{{ s.label }}</a>
    </nav>

    <div v-if="open" class="sheet" role="dialog" aria-label="Menu de navigation" @click.self="close">
      <div class="panel">
        <div class="panelHead">
          <div class="panelBrand">{{ coupleName }}</div>
          <button class="closeBtn" type="button" aria-label="Fermer" @click="close">×</button>
        </div>
        <a v-for="s in sections" :key="s.id" class="sheetLink" :href="`#${s.id}`" @click="close">
          {{ s.label }}
        </a>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'

export type NavSection = { id: string; label: string }

defineProps<{
  sections: NavSection[]
  coupleName: string
}>()

const open = ref(false)
function toggle() {
  open.value = !open.value
}
function close() {
  open.value = false
}
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

.burger {
  display: none;
  width: 44px;
  height: 44px;
  border-radius: 999px;
  border: 1px solid rgba(211, 187, 161, 0.55);
  background: rgba(255, 255, 255, 0.85);
  box-shadow: var(--shadow-soft);
  align-items: center;
  justify-content: center;
  gap: 4px;
  padding: 0;
}
.burger span {
  display: block;
  width: 18px;
  height: 2px;
  background: var(--c-ink);
  border-radius: 2px;
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

/* Mobile */
@media (max-width: 720px) {
  .nav {
    display: none;
  }
  .burger {
    display: inline-flex;
  }
}

.sheet {
  position: fixed;
  inset: 0;
  background: rgba(15, 10, 9, 0.45);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  display: grid;
  justify-items: end;
  z-index: 80;
}

.panel {
  width: min(92vw, 360px);
  height: 100%;
  background: rgba(255, 255, 255, 0.92);
  border-left: 1px solid rgba(211, 187, 161, 0.35);
  box-shadow: var(--shadow-lift);
  padding: 1rem 1rem 1.25rem;
}

.panelHead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid rgba(211, 187, 161, 0.35);
}

.panelBrand {
  font-family: "Playfair Display", Georgia, serif;
  font-style: italic;
  color: var(--c-primary);
  font-weight: 600;
}

.closeBtn {
  width: 44px;
  height: 44px;
  border-radius: 999px;
  border: 1px solid rgba(211, 187, 161, 0.55);
  background: rgba(255, 255, 255, 0.85);
  box-shadow: var(--shadow-soft);
  font-size: 1.6rem;
  line-height: 1;
  cursor: pointer;
  color: var(--c-ink);
}

.sheetLink {
  display: block;
  padding: 0.95rem 0.75rem;
  margin-top: 0.35rem;
  border-radius: 0.9rem;
  text-decoration: none;
  color: var(--c-ink);
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-size: 0.72rem;
  border: 1px solid rgba(211, 187, 161, 0.25);
  background: rgba(255, 255, 255, 0.7);
}
.sheetLink:active {
  transform: scale(0.99);
}
</style>


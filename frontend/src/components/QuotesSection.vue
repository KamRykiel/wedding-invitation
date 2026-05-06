<template>
  <section class="section" :id="id">
    <header class="head" data-reveal="block">
      <p class="kicker" data-reveal="line">Quelques mots</p>
      <h2 class="title" data-reveal="line">Amour, famille, <em>lumière</em></h2>
    </header>

    <div v-if="loading" class="quote" data-reveal="block">
      <p>Chargement…</p>
    </div>

    <div v-else>
      <div v-for="m in items.slice(0, 3)" :key="m.id" class="quote" data-reveal="block">
        <p data-reveal="line">« {{ m.content }} »</p>
        <small v-if="m.author">— {{ m.author }}</small>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import type { MessageDto } from '../stores/messages'

defineProps<{ id: string; items: MessageDto[]; loading: boolean }>()
</script>

<style scoped>
.section {
  margin-top: var(--space-y);
}
.head {
  text-align: center;
  margin-bottom: clamp(1.75rem, 4vw, 2.5rem);
}
.kicker {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--c-primary);
  margin-bottom: 0.5rem;
}
.title {
  font-family: "Playfair Display", Georgia, serif;
  font-size: clamp(1.85rem, 5vw, 2.5rem);
  font-weight: 600;
  color: var(--c-ink);
  line-height: 1.15;
  margin: 0;
}
.title em {
  font-style: italic;
  font-weight: 500;
  color: var(--c-primary);
}
.quote {
  text-align: center;
  padding: clamp(2.25rem, 6vw, 3.25rem) 1.5rem;
  margin: 1.1rem 0;
}
.quote p {
  font-family: "Playfair Display", Georgia, serif;
  font-size: clamp(1.25rem, 3.5vw, 1.65rem);
  font-style: italic;
  font-weight: 400;
  color: var(--c-ink);
  max-width: 34rem;
  margin: 0 auto;
  line-height: 1.45;
}
.quote small {
  display: block;
  margin-top: 0.65rem;
  color: var(--c-primary);
  letter-spacing: 0.06em;
}
</style>


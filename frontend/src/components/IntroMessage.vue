<template>
  <section class="section" :id="id">
    <header class="head" data-reveal="block">
      <p class="kicker" data-reveal="line">Un mot du cœur</p>
      <h2 class="title" data-reveal="line">Notre invitation, <em>pour vous</em></h2>
    </header>

    <div class="card" data-reveal="block">
      <p v-if="loading" class="prose">Chargement…</p>
      <div v-else class="prose">
        <p>
          C’est avec une immense joie, beaucoup de tendresse et une gratitude profonde que nous vous invitons à partager le
          début de notre vie à deux.
        </p>
        <p>{{ event?.description ?? "Ce jour-là, tout aura le goût des choses simples et précieuses." }}</p>
        <p>
          Votre présence est un cadeau. Et si vous ne pouvez pas être là, sachez que vos pensées nous accompagneront.
        </p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import type { EventDto } from '../stores/event'

defineProps<{
  id: string
  event: EventDto | null
  loading: boolean
}>()
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
.card {
  background: linear-gradient(165deg, rgba(255, 255, 255, 0.92) 0%, rgba(227, 209, 195, 0.26) 100%);
  border: 1px solid rgba(211, 187, 161, 0.35);
  border-radius: var(--radius-lg);
  padding: clamp(1.75rem, 4vw, 2.5rem);
  box-shadow: var(--shadow-soft);
}
.prose {
  color: var(--c-ink-soft);
  font-weight: 320;
  max-width: 46rem;
  margin: 0 auto;
  text-align: center;
}
.prose p + p {
  margin-top: 1rem;
}
</style>


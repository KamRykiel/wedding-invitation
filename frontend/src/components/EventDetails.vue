<template>
  <section class="section" :id="id">
    <header class="head" data-reveal="block">
      <p class="kicker" data-reveal="line">Les détails</p>
      <h2 class="title" data-reveal="line">Tout ce qu’il faut savoir, <em>avec élégance</em></h2>
    </header>

    <div class="grid">
      <article class="card" data-reveal="block">
        <span class="badge">Date</span>
        <p class="big">{{ dateLabel }}</p>
        <p class="small">Cérémonie &amp; réception — <strong>samedi</strong>, à partir de <strong>14h</strong></p>
      </article>

      <article class="card" data-reveal="block">
        <span class="badge">Lieu</span>
        <p class="big">{{ event?.location ?? 'Faya Hotel, Akwa — Douala, Cameroun' }}</p>
        <p class="small">Un cadre lumineux pour vous accueillir et vous laisser vivre la journée au même rythme.</p>
      </article>
    </div>

    <div class="map" data-reveal="block" aria-label="Carte du lieu">
      <div>
        <h3 class="mapTitle">Faya Hotel — Akwa</h3>
        <p class="mapCopy">
          Pour arriver sereinement, ouvrir l’itinéraire et repérer l’entrée. (La carte ci-dessous sert de prévisualisation.)
        </p>
      </div>
      <a class="mapBtn" :href="mapsUrl" target="_blank" rel="noopener noreferrer">Ouvrir Google Maps</a>
    </div>

    <div class="embedWrap" data-reveal="block">
      <iframe
        class="embed"
        :src="embedUrl"
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        title="Carte — Faya Hotel Douala"
      ></iframe>
    </div>

    <p v-if="loading" class="note" data-reveal="block">Chargement…</p>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { MAPS_EMBED_URL, MAPS_PLACE_URL } from '../config/constants'
import type { EventDto } from '../stores/event'

const props = defineProps<{ id: string; event: EventDto | null; loading: boolean }>()

const mapsUrl = MAPS_PLACE_URL
const embedUrl = MAPS_EMBED_URL

const dateLabel = computed(() => {
  if (!props.event?.date) return '[Date]'
  const d = new Date(props.event.date)
  return d.toLocaleDateString('fr-FR', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
})
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
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.15rem;
}
@media (min-width: 640px) {
  .grid {
    grid-template-columns: 1fr 1fr;
  }
}
.card {
  border-radius: var(--radius-lg);
  padding: clamp(1.35rem, 3vw, 1.75rem);
  overflow: hidden;
  border: 1px solid rgba(211, 187, 161, 0.35);
  background: linear-gradient(150deg, #ffffff 0%, rgba(227, 209, 195, 0.28) 100%);
  box-shadow: var(--shadow-soft);
}
.badge {
  display: inline-block;
  font-size: 0.58rem;
  font-weight: 800;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--c-white);
  background: linear-gradient(135deg, var(--c-primary), rgba(175, 150, 128, 0.78));
  padding: 0.38rem 0.7rem;
  border-radius: 999px;
  margin-bottom: 0.85rem;
}
.big {
  font-family: "Playfair Display", Georgia, serif;
  font-size: 1.35rem;
  font-weight: 650;
  color: var(--c-ink);
  margin: 0;
}
.small {
  margin: 0.45rem 0 0;
  color: var(--c-ink-soft);
}
.map {
  margin-top: 1.15rem;
  position: relative;
  border-radius: var(--radius-lg);
  padding: clamp(1.35rem, 3vw, 1.75rem);
  display: grid;
  gap: 1rem;
  align-items: center;
  overflow: hidden;
  border: 1px solid rgba(211, 187, 161, 0.35);
  background: linear-gradient(135deg, #ffffff 0%, rgba(227, 209, 195, 0.45) 100%);
  box-shadow: var(--shadow-soft);
}
@media (min-width: 768px) {
  .map {
    grid-template-columns: 1fr auto;
  }
}
.mapTitle {
  font-family: "Playfair Display", Georgia, serif;
  font-size: 1.4rem;
  margin: 0 0 0.35rem;
  color: var(--c-ink);
}
.mapCopy {
  margin: 0;
  color: var(--c-ink-soft);
}
.mapBtn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.85rem 1.1rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.95);
  color: var(--c-ink);
  border: 1px solid rgba(175, 150, 128, 0.28);
  text-decoration: none;
  font-size: 0.78rem;
  font-weight: 750;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  transition: transform 0.2s var(--ease-out);
}
.mapBtn:hover {
  transform: translateY(-2px);
}

.embedWrap {
  margin-top: 0.95rem;
  border-radius: var(--radius-lg);
  overflow: hidden;
  border: 1px solid rgba(211, 187, 161, 0.35);
  box-shadow: var(--shadow-soft);
  background: rgba(255, 255, 255, 0.6);
}

.embed {
  width: 100%;
  height: min(52vh, 420px);
  border: 0;
  display: block;
}
.note {
  margin-top: 0.85rem;
  text-align: center;
  color: var(--c-primary);
}
</style>


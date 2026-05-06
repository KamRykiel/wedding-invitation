<template>
  <section class="section" :id="id">
    <header class="head" data-reveal="block">
      <p class="kicker" data-reveal="line">Notre histoire</p>
      <h2 class="title" data-reveal="line">Trois chapitres, <em>un même battement</em></h2>
    </header>

    <div class="grid">
      <article class="step" data-reveal="block">
        <div class="media" data-parallax="slow">
          <img :src="img(0)" alt="" loading="lazy" decoding="async" />
        </div>
        <div class="content">
          <p class="sk" data-reveal="line">Rencontre</p>
          <h3 class="st" data-reveal="line">L’évidence, sans bruit</h3>
          <p class="copy" data-reveal="line">
            Au début, il y a eu une conversation de plus… puis celle qu’on n’oublie plus. Des détails minuscules, et déjà
            cette sensation : « je me sens bien, ici ».
          </p>
        </div>
      </article>

      <article class="step rev" data-reveal="block">
        <div class="media" data-parallax="slow">
          <img :src="img(1)" alt="" loading="lazy" decoding="async" />
        </div>
        <div class="content">
          <p class="sk" data-reveal="line">Parcours</p>
          <h3 class="st" data-reveal="line">Grandir, l’un avec l’autre</h3>
          <p class="copy" data-reveal="line">
            Nous avons appris nos silences, nos forces, nos fragilités. Nous avons choisi l’écoute, la patience, et l’élan.
            L’amour s’est installé : calme, fidèle, présent.
          </p>
        </div>
      </article>

      <article class="step" data-reveal="block">
        <div class="media" data-parallax="slow">
          <img :src="img(2)" alt="" loading="lazy" decoding="async" />
        </div>
        <div class="content">
          <p class="sk" data-reveal="line">Décision</p>
          <h3 class="st" data-reveal="line">Se choisir, pour longtemps</h3>
          <p class="copy" data-reveal="line">
            Dire « oui », ce n’est pas seulement une phrase — c’est une manière de se promettre la paix, la joie, la maison.
          </p>
        </div>
      </article>
    </div>

    <p v-if="loading" class="note" data-reveal="block">Chargement des images…</p>
  </section>
</template>

<script setup lang="ts">
import type { GalleryItemDto } from '../stores/gallery'

const props = defineProps<{
  id: string
  gallery: GalleryItemDto[]
  loading: boolean
}>()

function img(idx: number) {
  const picks = props.gallery.filter((x) => x.image_url)
  return picks[idx]?.image_url ?? picks[0]?.image_url ?? ''
}
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
  gap: 1.25rem;
}

.step {
  display: grid;
  gap: 1rem;
  align-items: center;
  background: rgba(255, 255, 255, 0.7);
  border: 1px solid rgba(211, 187, 161, 0.38);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(40, 27, 23, 0.08);
}

@media (min-width: 860px) {
  .step {
    grid-template-columns: 1.05fr 1fr;
  }
  .step.rev {
    grid-template-columns: 1fr 1.05fr;
  }
  .step.rev .media {
    order: 2;
  }
}

.media {
  position: relative;
  min-height: 14.5rem;
  background: linear-gradient(135deg, rgba(227, 209, 195, 0.4), rgba(211, 187, 161, 0.25));
}
.media img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform: scale(1.04);
  filter: saturate(1.03) contrast(1.02);
}
.media::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0), rgba(255, 255, 255, 0.55));
  opacity: 0.75;
  mix-blend-mode: screen;
  pointer-events: none;
}
.content {
  padding: 1.25rem 1.25rem 1.35rem;
}
@media (min-width: 860px) {
  .content {
    padding: 1.6rem 1.6rem 1.75rem;
  }
}
.sk {
  font-size: 0.66rem;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  font-weight: 800;
  color: var(--c-primary);
  margin: 0;
}
.st {
  margin: 0.35rem 0 0;
  font-family: "Playfair Display", Georgia, serif;
  font-size: 1.55rem;
  font-weight: 600;
  color: var(--c-ink);
  line-height: 1.2;
}
.copy {
  margin: 0.7rem 0 0;
  color: var(--c-ink-soft);
  font-weight: 320;
  font-size: 0.98rem;
}
.note {
  margin-top: 1rem;
  text-align: center;
  color: var(--c-primary);
  font-size: 0.9rem;
}
</style>


<template>
  <section class="section" :id="id">
    <header class="head" data-reveal="block">
      <p class="kicker" data-reveal="line">Galerie</p>
      <h2 class="title" data-reveal="line">Des instants, <em>comme des promesses</em></h2>
    </header>

    <div v-if="loading" class="grid">
      <div v-for="i in 5" :key="i" class="frame sk" data-reveal="block"></div>
    </div>

    <div v-else class="grid" aria-label="Galerie de photos">
      <button
        v-for="(img, idx) in mosaic"
        :key="img.id ?? idx"
        class="frame"
        type="button"
        data-reveal="block"
        @click="open(img.image_url)"
        :aria-label="`Agrandir : photo ${idx + 1}`"
        :class="{ feat: idx === 0 }"
      >
        <img :src="img.image_url" :alt="img.category ?? ''" loading="lazy" decoding="async" />
      </button>
    </div>

    <p class="hint" data-reveal="block">Touchez une photo pour l’ouvrir en plein écran</p>

    <div class="cards" data-reveal="block" aria-label="Cartes éditoriales">
      <article v-for="(c, i) in editorialCards" :key="i" class="card" :style="c.style" data-reveal="block">
        <div class="cardGlow" aria-hidden="true"></div>
        <div class="cardTop">
          <span class="pill">{{ c.kicker }}</span>
          <span class="dot" aria-hidden="true">♥</span>
        </div>
        <h3 class="cardTitle">{{ c.title }}</h3>
        <p class="cardCopy">{{ c.copy }}</p>
      </article>
    </div>

    <dialog ref="dlg" class="lightbox" aria-label="Photo en grand format">
      <div class="inner" @click="onBackdrop">
        <button type="button" class="close" @click="close" aria-label="Fermer la photo">×</button>
        <img v-if="active" :src="active" alt="" />
      </div>
    </dialog>
  </section>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import type { GalleryItemDto } from '../stores/gallery'

const props = defineProps<{ id: string; items: GalleryItemDto[]; loading: boolean }>()

const dlg = ref<HTMLDialogElement | null>(null)
const active = ref<string>('')

const mosaic = computed(() => {
  const imgs = props.items.filter((x) => x.image_url)
  if (imgs.length === 0) return []
  const out: GalleryItemDto[] = []
  while (out.length < 5) out.push(imgs[out.length % imgs.length]!)
  return out
})

const editorialCards = computed(() => {
  const imgs = props.items.filter((x) => x.image_url)
  const img = (n: number) => imgs[n % Math.max(1, imgs.length)]?.image_url ?? '/uploads/tsaf001.png'
  return [
    {
      kicker: 'Cérémonie',
      title: 'Un “oui” qui rassemble',
      copy: 'Un moment de famille, de promesse et de lumière — à vivre ensemble, doucement.',
      style: {
        '--bg': `url("${img(0)}")`,
      },
    },
    {
      kicker: 'Réception',
      title: 'La douceur d’une fête',
      copy: 'Rires, photos, musique — et ces instants suspendus qu’on n’oublie pas.',
      style: {
        '--bg': `url("${img(1)}")`,
      },
    },
    {
      kicker: 'Souvenirs',
      title: 'Des images comme des promesses',
      copy: 'Chaque regard devient un récit. Chaque sourire, une page de plus.',
      style: {
        '--bg': `url("${img(2)}")`,
      },
    },
  ] as Array<{ kicker: string; title: string; copy: string; style: Record<string, string> }>
})

function open(url: string) {
  active.value = url
  dlg.value?.showModal()
}
function close() {
  dlg.value?.close()
  active.value = ''
}
function onBackdrop(e: MouseEvent) {
  if (e.target === e.currentTarget) close()
}
</script>

<style scoped>
.section {
  margin-top: var(--space-y);
}
.head {
  text-align: center;
  margin-bottom: clamp(1.25rem, 3vw, 1.75rem);
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
  gap: 0.7rem;
}
@media (min-width: 720px) {
  .grid {
    grid-template-columns: 1.12fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 0.85rem;
    min-height: min(54vh, 540px);
  }
  .frame.feat {
    grid-row: 1 / -1;
  }
}
.frame {
  display: block;
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
  border: none;
  cursor: zoom-in;
  border-radius: var(--radius-lg);
  overflow: hidden;
  background: linear-gradient(145deg, #ece6e2, #f5f0ec);
  box-shadow: var(--shadow-soft);
  border: 1px solid rgba(255, 255, 255, 0.85);
  transition: transform 0.4s var(--ease-spring), box-shadow 0.4s;
}
.frame:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lift);
}
.frame img {
  width: 100%;
  height: 100%;
  display: block;
  object-fit: cover;
  object-position: center 28%;
  aspect-ratio: 4 / 5;
}
@media (min-width: 720px) {
  .frame.feat img {
    aspect-ratio: auto;
    min-height: 100%;
  }
}
.hint {
  text-align: center;
  font-size: 0.78rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--c-primary);
  margin-top: 1.1rem;
  opacity: 0.9;
}
.sk {
  min-height: 14rem;
  cursor: default;
}

.lightbox {
  padding: 0;
  border: none;
  max-width: none;
  max-height: none;
  width: 100%;
  height: 100%;
  background: transparent;
}
.lightbox::backdrop {
  background: rgba(45, 32, 28, 0.72);
  backdrop-filter: blur(6px);
}
.inner {
  position: fixed;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(1rem, 4vw, 2.5rem);
}
.inner img {
  max-width: min(96vw, 1100px);
  max-height: min(88vh, 900px);
  width: auto;
  height: auto;
  object-fit: contain;
  border-radius: 0.35rem;
  box-shadow: 0 24px 80px rgba(0, 0, 0, 0.35);
}
.close {
  position: fixed;
  top: 1rem;
  right: 1rem;
  z-index: 2;
  width: 3rem;
  height: 3rem;
  border: none;
  border-radius: 50%;
  font-size: 1.75rem;
  line-height: 1;
  cursor: pointer;
  color: var(--c-ink);
  background: rgba(255, 255, 255, 0.95);
  box-shadow: var(--shadow-soft);
}

.cards {
  margin-top: 1.25rem;
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.85rem;
}

@media (min-width: 760px) {
  .cards {
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
  }
}

.card {
  position: relative;
  border-radius: 1.15rem;
  overflow: hidden;
  border: 1px solid rgba(211, 187, 161, 0.35);
  box-shadow: var(--shadow-soft);
  background-image:
    linear-gradient(180deg, rgba(20, 14, 13, 0.62) 0%, rgba(20, 14, 13, 0.22) 52%, rgba(255, 255, 255, 0.0) 78%, rgba(255, 255, 255, 0.92) 100%),
    linear-gradient(120deg, rgba(175, 150, 128, 0.18), rgba(227, 209, 195, 0.12)),
    var(--bg);
  background-size: cover;
  background-position: center;
  padding: 1.1rem 1.05rem 1.15rem;
  min-height: 190px;
  display: grid;
  align-content: end;
  transition: transform 0.5s var(--ease-spring), box-shadow 0.5s;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lift);
}

.cardGlow {
  position: absolute;
  inset: -40%;
  background: radial-gradient(circle at 30% 30%, rgba(255, 255, 255, 0.16), transparent 55%);
  transform: rotate(10deg);
  pointer-events: none;
  animation: glowDrift 10s ease-in-out infinite;
}
@keyframes glowDrift {
  0%,
  100% {
    transform: rotate(10deg) translate3d(0, 0, 0);
    opacity: 0.9;
  }
  50% {
    transform: rotate(10deg) translate3d(22px, -14px, 0);
    opacity: 1;
  }
}

.cardTop {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
}

.pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.45rem 0.7rem;
  border-radius: 999px;
  font-size: 0.62rem;
  font-weight: 850;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.92);
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.24);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.dot {
  color: rgba(255, 255, 255, 0.92);
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.55);
  animation: dotPulse 2.2s ease-in-out infinite;
}
@keyframes dotPulse {
  0%,
  100% {
    transform: scale(1);
    opacity: 0.85;
  }
  50% {
    transform: scale(1.35);
    opacity: 1;
  }
}

.cardTitle {
  margin: 0.7rem 0 0.35rem;
  font-family: "Playfair Display", Georgia, serif;
  font-weight: 650;
  color: rgba(255, 255, 255, 0.96);
  text-shadow: 0 14px 60px rgba(0, 0, 0, 0.28);
  font-size: 1.22rem;
  line-height: 1.2;
}
.cardCopy {
  margin: 0;
  color: rgba(255, 255, 255, 0.88);
  font-weight: 330;
  text-shadow: 0 10px 50px rgba(0, 0, 0, 0.24);
  font-size: 0.95rem;
}

@media (prefers-reduced-motion: reduce) {
  .cardGlow,
  .dot {
    animation: none !important;
  }
}
</style>


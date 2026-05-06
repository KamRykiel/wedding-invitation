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
</style>


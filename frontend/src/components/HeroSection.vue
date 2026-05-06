<template>
  <section class="hero" :style="heroStyle">
    <div class="inner">
      <p class="eyebrow" data-reveal="line">Nous avons le plaisir de vous inviter</p>

      <div v-if="loading" class="skeleton" data-reveal="block" aria-label="Chargement…">
        <div class="sk-title"></div>
        <div class="sk-sub"></div>
        <div class="sk-pill"></div>
      </div>

      <template v-else-if="event">
        <h1 class="title" data-reveal="line">{{ event.couple_name }}</h1>
        <p class="subtitle" data-reveal="line">
          Nous avons le plaisir de vous inviter à célébrer notre union — un moment de famille, de promesse et de lumière.
        </p>
        <p class="pill" data-reveal="block">
          <span>{{ dateLabel }}</span> · <span>{{ event.location }}</span>
        </p>

        <div class="cta" data-reveal="block">
          <a class="btn primary" href="#rsvp">Confirmer</a>
          <a class="btn ghost" href="#details">Voir les infos</a>
        </div>
      </template>

      <p v-else class="error" data-reveal="block">{{ error ?? 'Impossible de charger l’événement.' }}</p>

      <a class="scroll" href="#intro" aria-label="Défiler pour découvrir l’invitation" data-reveal="block">
        <span class="mouse" aria-hidden="true"></span>
        <span class="scroll-label">Défiler</span>
      </a>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { EventDto } from '../stores/event'

const props = defineProps<{
  event: EventDto | null
  loading: boolean
  error: string | null
  heroImageUrl: string
}>()

const heroStyle = computed(() => {
  const url = props.heroImageUrl ? `url("${props.heroImageUrl}")` : 'none'
  return {
    backgroundImage: `
      linear-gradient(180deg, rgba(20,14,13,0.58) 0%, rgba(20,14,13,0.20) 42%, rgba(255,255,255,0.0) 70%, rgba(255,255,255,0.96) 100%),
      radial-gradient(circle at 20% 10%, rgba(255,255,255,0.35) 0%, transparent 50%),
      linear-gradient(120deg, rgba(175,150,128,0.18), rgba(227,209,195,0.12)),
      ${url}
    `,
  } as any
})

const dateLabel = computed(() => {
  if (!props.event?.date) return ''
  const d = new Date(props.event.date)
  return d.toLocaleDateString('fr-FR', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
})
</script>

<style scoped>
.hero {
  position: relative;
  min-height: 100dvh;
  border-radius: clamp(1.25rem, 4vw, 2rem);
  overflow: hidden;
  isolation: isolate;
  box-shadow: var(--shadow-soft);
  border: 1px solid rgba(211, 187, 161, 0.35);
  background-size: cover;
  background-position: center;
  margin-top: 1.05rem;
}

.inner {
  min-height: 100dvh;
  display: grid;
  align-content: end;
  padding: clamp(1.1rem, 4vw, 2rem);
  padding-bottom: clamp(2rem, 8vw, 4rem);
  text-align: center;
}

.eyebrow {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.65rem;
  font-size: 0.65rem;
  font-weight: 650;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.86);
  margin-bottom: 1rem;
}

.eyebrow::before,
.eyebrow::after {
  content: "";
  width: 2rem;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.7));
}

.eyebrow::after {
  background: linear-gradient(90deg, rgba(255, 255, 255, 0.7), transparent);
}

.title {
  font-family: "Playfair Display", Georgia, serif;
  font-weight: 600;
  font-size: clamp(2.35rem, 10vw, 4.25rem);
  line-height: 1.02;
  letter-spacing: 0.01em;
  color: rgba(255, 255, 255, 0.96);
  text-shadow: 0 16px 60px rgba(0, 0, 0, 0.26);
  margin: 0.25rem 0 0.85rem;
}

.subtitle {
  max-width: 34rem;
  margin: 0 auto;
  font-size: 1.05rem;
  font-weight: 320;
  color: rgba(255, 255, 255, 0.9);
  text-shadow: 0 10px 40px rgba(0, 0, 0, 0.24);
}

.pill {
  margin: 1.1rem auto 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.55rem;
  padding: 0.55rem 0.9rem;
  border-radius: 999px;
  border: 1px solid rgba(255, 255, 255, 0.38);
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  box-shadow: 0 18px 60px rgba(0, 0, 0, 0.18);
  color: rgba(255, 255, 255, 0.92);
  font-size: 0.82rem;
  font-weight: 650;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.cta {
  margin-top: 1.35rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  justify-content: center;
}

.btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  text-decoration: none;
  padding: 0.85rem 1.25rem;
  border-radius: 999px;
  border: none;
  cursor: pointer;
  overflow: hidden;
  transition: transform 0.3s var(--ease-spring), box-shadow 0.3s;
}

.primary {
  background: linear-gradient(135deg, rgba(175, 150, 128, 1), rgba(211, 187, 161, 1));
  color: var(--c-white);
  box-shadow: var(--shadow-soft);
}

.primary:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lift);
}

.ghost {
  background: rgba(255, 255, 255, 0.85);
  color: var(--c-ink);
  border: 1px solid rgba(211, 187, 161, 0.8);
}

.ghost:hover {
  transform: translateY(-2px);
  background: var(--c-white);
}

.scroll {
  margin-top: 1.45rem;
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 0.55rem;
  color: rgba(255, 255, 255, 0.86);
  text-decoration: none;
  font-size: 0.72rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  opacity: 0.92;
}

.mouse {
  width: 28px;
  height: 44px;
  border-radius: 999px;
  border: 1px solid rgba(255, 255, 255, 0.6);
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  position: relative;
  overflow: hidden;
}

.mouse::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 10px;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  transform: translateX(-50%);
  background: rgba(255, 255, 255, 0.92);
  animation: dot 1.65s var(--ease-out) infinite;
}

@keyframes dot {
  0% {
    transform: translate(-50%, 0);
    opacity: 0.2;
  }
  35% {
    opacity: 1;
  }
  70% {
    transform: translate(-50%, 18px);
    opacity: 0.35;
  }
  100% {
    opacity: 0.2;
  }
}

.error {
  margin: 1.1rem auto 0;
  max-width: 36rem;
  color: rgba(255, 255, 255, 0.92);
}

.skeleton {
  max-width: 42rem;
  margin: 0 auto;
}
.sk-title,
.sk-sub,
.sk-pill {
  background: rgba(255, 255, 255, 0.22);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 999px;
  height: 20px;
  margin: 0 auto 0.9rem;
}
.sk-title {
  height: 44px;
  width: min(92%, 520px);
  border-radius: 16px;
}
.sk-sub {
  width: min(90%, 560px);
}
.sk-pill {
  width: min(74%, 420px);
}

@media (prefers-reduced-motion: reduce) {
  .mouse::after {
    animation: none !important;
  }
}
</style>


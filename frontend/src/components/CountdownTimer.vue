<template>
  <section class="section" :id="id" data-reveal="block">
    <p class="kicker" data-reveal="line">Compte à rebours</p>
    <h2 class="title" data-reveal="line">{{ title }}</h2>
    <p class="sub" data-reveal="line">Chaque seconde nous rapproche d’un moment unique.</p>

    <div v-if="loading" class="row" aria-label="Chargement…">
      <div v-for="i in 4" :key="i" class="box sk"></div>
    </div>

    <div v-else class="row" role="timer" aria-live="polite" aria-atomic="true">
      <div class="box" style="--ci: 0"><span>{{ parts.days }}</span><small>Jours</small></div>
      <div class="box" style="--ci: 1"><span>{{ parts.hours }}</span><small>Heures</small></div>
      <div class="box" style="--ci: 2"><span>{{ parts.mins }}</span><small>Minutes</small></div>
      <div class="box" style="--ci: 3"><span>{{ parts.secs }}</span><small>Secondes</small></div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue'

const props = defineProps<{
  id: string
  eventDate?: string
  loading: boolean
}>()

const parts = ref({ days: '0', hours: '00', mins: '00', secs: '00' })
let t: number | undefined

const title = computed(() => {
  if (!props.eventDate) return '[Date]'
  const d = new Date(props.eventDate)
  return d.toLocaleDateString('fr-FR', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
})

function pad2(n: number) {
  return n < 10 ? `0${n}` : `${n}`
}

function tick() {
  if (!props.eventDate) return
  const target = new Date(props.eventDate).getTime()
  const diff = target - Date.now()
  if (diff <= 0) {
    parts.value = { days: '0', hours: '00', mins: '00', secs: '00' }
    return
  }
  let sec = Math.floor(diff / 1000)
  const d = Math.floor(sec / 86400)
  sec -= d * 86400
  const h = Math.floor(sec / 3600)
  sec -= h * 3600
  const m = Math.floor(sec / 60)
  sec -= m * 60
  parts.value = { days: `${d}`, hours: pad2(h), mins: pad2(m), secs: pad2(sec) }
}

onMounted(() => {
  tick()
  t = window.setInterval(tick, 1000)
})
onUnmounted(() => {
  if (t) window.clearInterval(t)
})
</script>

<style scoped>
.section {
  margin-top: var(--space-y);
  text-align: center;
  padding: clamp(2rem, 5vw, 2.75rem);
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.92), rgba(227, 209, 195, 0.35));
  border-radius: var(--radius-lg);
  border: 1px solid rgba(211, 187, 161, 0.35);
  box-shadow: var(--shadow-soft);
}
.kicker {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--c-primary);
  margin: 0 0 0.5rem;
}
.title {
  margin: 0 0 0.35rem;
  font-family: "Playfair Display", Georgia, serif;
  font-size: clamp(1.85rem, 5vw, 2.35rem);
  font-weight: 650;
  color: var(--c-ink);
  line-height: 1.1;
}
.sub {
  font-size: 0.95rem;
  color: var(--c-primary);
  margin: 0 0 1.5rem;
}
.row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.65rem;
}
.box {
  min-width: 4.5rem;
  padding: 0.85rem 0.65rem;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 0.75rem;
  border: 1px solid rgba(211, 187, 161, 0.55);
  box-shadow: 0 4px 16px rgba(40, 27, 23, 0.06);
}
.box span {
  display: block;
  font-family: "Playfair Display", Georgia, serif;
  font-size: clamp(1.85rem, 5vw, 2.35rem);
  font-weight: 700;
  color: var(--c-ink);
  line-height: 1;
  font-variant-numeric: tabular-nums;
}
.box small {
  display: block;
  margin-top: 0.35rem;
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--c-primary);
}
.sk {
  height: 5.25rem;
  background: rgba(255, 255, 255, 0.65);
}
</style>


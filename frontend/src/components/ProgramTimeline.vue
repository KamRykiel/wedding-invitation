<template>
  <section class="section" :id="id">
    <header class="head" data-reveal="block">
      <p class="kicker" data-reveal="line">Le programme</p>
      <h2 class="title" data-reveal="line">La journée, <em>pas à pas</em></h2>
    </header>

    <div class="list">
      <div class="item" data-reveal="block">
        <div class="time">14h</div>
        <div>
          <div class="itTitle" data-reveal="line">Cérémonie</div>
          <div class="itCopy" data-reveal="line">Accueil, installation, entrée, vœux.</div>
        </div>
      </div>
      <div class="item" data-reveal="block">
        <div class="time">16h</div>
        <div>
          <div class="itTitle" data-reveal="line">Photos</div>
          <div class="itCopy" data-reveal="line">Moments de famille, sourires, souvenirs.</div>
        </div>
      </div>
      <div class="item" data-reveal="block">
        <div class="time">18h</div>
        <div>
          <div class="itTitle" data-reveal="line">Réception</div>
          <div class="itCopy" data-reveal="line">Cocktail, repas, discours, ouverture, danse.</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
defineProps<{ id: string }>()
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
.list {
  display: grid;
  gap: 0.85rem;
  margin: 0 auto;
  max-width: 46rem;
}
.item {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 0.9rem;
  align-items: start;
  padding: 1.1rem;
  border-radius: 1rem;
  background: rgba(255, 255, 255, 0.78);
  border: 1px solid rgba(211, 187, 161, 0.35);
  box-shadow: 0 10px 40px rgba(40, 27, 23, 0.08);
}
.time {
  font-family: "Playfair Display", Georgia, serif;
  font-size: 1.15rem;
  font-weight: 750;
  color: var(--c-ink);
  min-width: 3.5rem;
}
.itTitle {
  font-weight: 750;
  color: var(--c-ink);
}
.itCopy {
  color: var(--c-ink-soft);
  font-weight: 320;
  margin-top: 0.15rem;
  font-size: 0.98rem;
}
</style>


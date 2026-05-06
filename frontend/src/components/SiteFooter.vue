<template>
  <footer class="footer" data-reveal="block">
    <p class="up" data-reveal="line">Avec toute notre affection</p>
    <p class="down" data-reveal="line">{{ coupleName }} — merci d’être dans l’histoire</p>
  </footer>
</template>

<script setup lang="ts">
defineProps<{ coupleName: string }>()
</script>

<style scoped>
.footer {
  text-align: center;
  margin-top: var(--space-y);
  padding: 0 0 3.5rem;
  border-top: 1px solid rgba(211, 187, 161, 0.35);
}
.up {
  margin-top: 2rem;
  font-size: 0.72rem;
  font-weight: 750;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--c-primary);
}
.down {
  margin-top: 0.45rem;
  font-size: 0.92rem;
  font-weight: 320;
  letter-spacing: 0.02em;
  color: var(--c-ink-soft);
}
</style>


<template>
  <div class="sparkles" aria-hidden="true">
    <span v-for="s in 18" :key="s" class="sparkle" :style="styleFor(s)"></span>
  </div>
</template>

<script setup lang="ts">
function styleFor(_i: number) {
  const top = `${Math.random() * 100}%`
  const left = `${Math.random() * 100}%`
  const delay = `${Math.random() * 4}s`
  const dur = `${3.8 + Math.random() * 3.6}s`
  const size = `${5 + Math.random() * 7}px`
  return {
    top,
    left,
    width: size,
    height: size,
    animationDelay: delay,
    animationDuration: dur,
  } as any
}
</script>

<style scoped>
.sparkles {
  position: fixed;
  inset: 0;
  z-index: 1;
  pointer-events: none;
}
.sparkle {
  position: absolute;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.98) 0%, transparent 72%);
  border-radius: 50%;
  opacity: 0;
  animation-name: twinkle;
  animation-timing-function: ease-in-out;
  animation-iteration-count: infinite;
}
@keyframes twinkle {
  0%,
  100% {
    opacity: 0;
    transform: scale(0.35);
  }
  40% {
    opacity: 0.85;
    transform: scale(1);
  }
  60% {
    opacity: 0.2;
    transform: scale(0.75);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sparkle {
    animation: none !important;
    opacity: 0.25;
  }
}
</style>


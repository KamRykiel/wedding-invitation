<template>
  <div class="bg" aria-hidden="true">
    <div class="aurora"></div>
    <div class="mesh">
      <div class="blob b1"></div>
      <div class="blob b2"></div>
      <div class="blob b3"></div>
    </div>
    <div class="grain"></div>
  </div>
</template>

<style scoped>
.bg {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
}

.aurora {
  position: absolute;
  inset: 0;
  opacity: 0.48;
  background: linear-gradient(
    118deg,
    #ffffff 0%,
    rgba(227, 209, 195, 0.6) 18%,
    rgba(211, 187, 161, 0.55) 40%,
    rgba(227, 209, 195, 0.42) 58%,
    rgba(211, 187, 161, 0.28) 78%,
    #ffffff 100%
  );
  background-size: 320% 320%;
  animation: auroraShift 22s ease-in-out infinite;
}

@keyframes auroraShift {
  0%,
  100% {
    background-position: 0% 40%;
  }
  50% {
    background-position: 100% 60%;
  }
}

.mesh {
  position: absolute;
  inset: 0;
  overflow: hidden;
}

.blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.42;
  mix-blend-mode: multiply;
}

.b1 {
  width: min(90vw, 560px);
  height: min(90vw, 560px);
  background: radial-gradient(circle at 35% 35%, #ffffff 0%, #e3d1c3 50%, #d3bba1 100%);
  top: -15%;
  left: -20%;
  animation: drift1 24s ease-in-out infinite;
}

.b2 {
  width: min(100vw, 620px);
  height: min(100vw, 620px);
  background: radial-gradient(circle at 65% 35%, #ffffff 0%, rgba(227, 209, 195, 0.75) 45%, rgba(211, 187, 161, 0.75) 100%);
  bottom: -28%;
  right: -25%;
  animation: drift2 28s ease-in-out infinite;
}

.b3 {
  width: min(75vw, 480px);
  height: min(75vw, 480px);
  background: radial-gradient(circle, rgba(255, 255, 255, 0.95) 0%, rgba(211, 187, 161, 0.35) 55%, transparent 72%);
  top: 42%;
  left: 50%;
  transform: translateX(-50%);
  opacity: 0.38;
  mix-blend-mode: soft-light;
  animation: pulse 16s ease-in-out infinite;
}

@keyframes drift1 {
  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }
  33% {
    transform: translate(10%, 5%) scale(1.05);
  }
  66% {
    transform: translate(3%, -6%) scale(0.97);
  }
}

@keyframes drift2 {
  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }
  40% {
    transform: translate(-12%, -6%) scale(1.06);
  }
  70% {
    transform: translate(-5%, 6%) scale(0.95);
  }
}

@keyframes pulse {
  0%,
  100% {
    transform: translateX(-50%) scale(1);
    opacity: 0.32;
  }
  50% {
    transform: translateX(-50%) scale(1.12);
    opacity: 0.48;
  }
}

.grain {
  position: absolute;
  inset: 0;
  opacity: 0.028;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

@media (prefers-reduced-motion: reduce) {
  .aurora,
  .blob {
    animation: none !important;
  }
}
</style>


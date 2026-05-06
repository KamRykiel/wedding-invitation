<template>
  <div class="toast" :class="{ on: toast.isOn }" role="status" aria-live="polite" aria-atomic="true">
    {{ toast.message }}
  </div>
</template>

<script setup lang="ts">
export type ToastState = { isOn: boolean; message: string }
defineProps<{ toast: ToastState }>()
</script>

<style scoped>
.toast {
  position: fixed;
  left: 50%;
  bottom: 1.1rem;
  transform: translateX(-50%);
  z-index: 9999;
  padding: 0.85rem 1.1rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid rgba(211, 187, 161, 0.55);
  box-shadow: var(--shadow-lift);
  color: var(--c-ink);
  font-weight: 750;
  font-size: 0.9rem;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.35s var(--ease-out), transform 0.35s var(--ease-out);
}
.toast.on {
  opacity: 1;
  transform: translateX(-50%) translateY(-6px);
}
</style>


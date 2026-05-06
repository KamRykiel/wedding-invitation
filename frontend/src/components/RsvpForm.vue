<template>
  <section class="section" :id="id">
    <header class="head" data-reveal="block">
      <p class="kicker" data-reveal="line">RSVP</p>
      <h2 class="title" data-reveal="line">Votre présence, <em>notre joie</em></h2>
    </header>

    <div class="card" data-reveal="block">
      <p class="prose" data-reveal="line">
        Merci de confirmer votre présence. Votre réponse est enregistrée et transmise au comité d’organisation.
      </p>

      <form class="grid" @submit.prevent="submit">
        <div class="full">
          <label for="name">Nom</label>
          <input id="name" v-model.trim="name" type="text" placeholder="Votre nom" required />
        </div>

        <div>
          <label for="attend">Présence</label>
          <select id="attend" v-model="attending">
            <option :value="true">Oui, avec joie</option>
            <option :value="false">Non, avec regret</option>
          </select>
        </div>

        <div>
          <label for="count">Nombre de personnes</label>
          <input id="count" v-model.number="guestsCount" type="number" min="1" max="20" required />
        </div>

        <div class="full">
          <label for="msg">Message (optionnel)</label>
          <input id="msg" v-model.trim="message" type="text" placeholder="Un mot pour les mariés…" />
        </div>

        <div class="actions full">
          <button class="btn primary" type="submit" :disabled="submitting">
            {{ submitting ? 'Envoi…' : 'Envoyer' }}
          </button>
          <button class="btn ghost" type="button" @click="reset" :disabled="submitting">Réinitialiser</button>
        </div>
      </form>

      <p v-if="error" class="err" role="alert">{{ error }}</p>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRsvpStore } from '../stores/rsvp'

defineProps<{ id: string; submitting: boolean; error: string | null }>()
const emit = defineEmits<{ submitted: [name: string] }>()

const rsvp = useRsvpStore()

const name = ref('')
const attending = ref(true)
const guestsCount = ref(1)
const message = ref('')

async function submit() {
  const n = name.value.trim()
  if (!n) return
  const res = await rsvp.submit({
    name: n,
    attending: attending.value,
    guests_count: guestsCount.value,
    message: message.value.trim() || null,
  })
  emit('submitted', res.name)
}

function reset() {
  name.value = ''
  attending.value = true
  guestsCount.value = 1
  message.value = ''
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
.card {
  max-width: 46rem;
  margin: 0 auto;
  padding: clamp(1.75rem, 4vw, 2.25rem);
  border-radius: var(--radius-lg);
  background: rgba(255, 255, 255, 0.72);
  border: 1px solid rgba(211, 187, 161, 0.38);
  box-shadow: var(--shadow-soft);
}
.prose {
  color: var(--c-ink-soft);
  font-weight: 320;
  text-align: center;
  margin: 0;
}
.grid {
  display: grid;
  gap: 0.85rem;
  margin-top: 1.25rem;
}
@media (min-width: 680px) {
  .grid {
    grid-template-columns: 1.2fr 0.9fr;
  }
  .full {
    grid-column: 1 / -1;
  }
}
label {
  display: block;
  font-size: 0.72rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--c-primary);
  font-weight: 800;
  margin-bottom: 0.35rem;
}
input,
select {
  width: 100%;
  padding: 0.9rem 1rem;
  border-radius: 0.95rem;
  border: 1px solid rgba(211, 187, 161, 0.6);
  background: rgba(255, 255, 255, 0.9);
  color: var(--c-ink);
  font-size: 1rem;
  outline: none;
}
input:focus,
select:focus {
  border-color: rgba(175, 150, 128, 0.85);
  box-shadow: 0 0 0 4px rgba(175, 150, 128, 0.18);
}
.actions {
  margin-top: 0.3rem;
  display: flex;
  gap: 0.65rem;
  flex-wrap: wrap;
  justify-content: center;
}
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.78rem;
  font-weight: 750;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  text-decoration: none;
  padding: 0.85rem 1.25rem;
  border-radius: 999px;
  border: none;
  cursor: pointer;
  transition: transform 0.3s var(--ease-spring), box-shadow 0.3s;
}
.primary {
  background: linear-gradient(135deg, rgba(175, 150, 128, 1), rgba(211, 187, 161, 1));
  color: var(--c-white);
  box-shadow: var(--shadow-soft);
}
.ghost {
  background: rgba(255, 255, 255, 0.85);
  color: var(--c-ink);
  border: 1px solid rgba(211, 187, 161, 0.8);
}
.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}
.err {
  margin-top: 0.9rem;
  text-align: center;
  color: #7a2c2c;
  font-weight: 650;
}
</style>


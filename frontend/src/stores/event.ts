import { defineStore } from 'pinia'
import { getJson, type ApiError } from '../services/api'

export type EventDto = {
  id: number
  couple_name: string
  date: string
  location: string
  description: string
}

export const useEventStore = defineStore('event', {
  state: () => ({
    event: null as EventDto | null,
    loading: false,
    error: null as string | null,
  }),
  actions: {
    async fetchEvent() {
      this.loading = true
      this.error = null
      try {
        this.event = await getJson<EventDto>('/api/event')
      } catch (e) {
        const err = e as ApiError
        this.error = err.message ?? 'Impossible de charger l’événement.'
        // Fallback so the UI (countdown) still works even if DB/API isn't ready yet.
        this.event = {
          id: 1,
          couple_name: 'Wilfried & Ornella',
          date: '2026-06-06T15:00:00+01:00',
          location: 'Faya Hotel, Akwa — Douala, Cameroun',
          description: 'C’est avec une immense joie et beaucoup d’amour que nous vous invitons à célébrer notre union.',
        }
      } finally {
        this.loading = false
      }
    },
  },
})


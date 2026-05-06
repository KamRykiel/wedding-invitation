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
      } finally {
        this.loading = false
      }
    },
  },
})


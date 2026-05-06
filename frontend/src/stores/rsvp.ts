import { defineStore } from 'pinia'
import { postJson, type ApiError } from '../services/api'

export type RsvpIn = {
  name: string
  attending: boolean
  guests_count: number
  message?: string | null
}

export type RsvpOut = {
  id: number
  name: string
  attending: boolean
  guests_count: number
  message?: string | null
}

export const useRsvpStore = defineStore('rsvp', {
  state: () => ({
    submitting: false,
    error: null as string | null,
  }),
  actions: {
    async submit(payload: RsvpIn) {
      this.submitting = true
      this.error = null
      try {
        return await postJson<RsvpIn, RsvpOut>('/api/rsvp', payload)
      } catch (e) {
        const err = e as ApiError
        this.error = err.message ?? 'Impossible d’envoyer votre réponse.'
        throw e
      } finally {
        this.submitting = false
      }
    },
  },
})


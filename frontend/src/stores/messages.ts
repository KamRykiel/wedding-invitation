import { defineStore } from 'pinia'
import { getJson, type ApiError } from '../services/api'

export type MessageDto = {
  id: number
  content: string
  author?: string | null
  created_at: string
}

export const useMessagesStore = defineStore('messages', {
  state: () => ({
    items: [] as MessageDto[],
    loading: false,
    error: null as string | null,
  }),
  actions: {
    async fetchMessages() {
      this.loading = true
      this.error = null
      try {
        this.items = await getJson<MessageDto[]>('/api/messages')
      } catch (e) {
        const err = e as ApiError
        this.error = err.message ?? 'Impossible de charger les messages.'
        this.items = [
          { id: 1, content: 'Aimer, c’est choisir chaque jour — et se retrouver, encore.', author: null, created_at: new Date().toISOString() },
          { id: 2, content: 'La famille, c’est là où l’amour devient un foyer.', author: null, created_at: new Date().toISOString() },
        ]
      } finally {
        this.loading = false
      }
    },
  },
})


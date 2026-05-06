import { defineStore } from 'pinia'
import { getJson, type ApiError } from '../services/api'

export type GalleryItemDto = {
  id: number
  image_url: string
  category?: string | null
  sort_order?: number
}

export const useGalleryStore = defineStore('gallery', {
  state: () => ({
    items: [] as GalleryItemDto[],
    loading: false,
    error: null as string | null,
  }),
  actions: {
    async fetchGallery() {
      this.loading = true
      this.error = null
      try {
        this.items = await getJson<GalleryItemDto[]>('/api/gallery')
      } catch (e) {
        const err = e as ApiError
        this.error = err.message ?? 'Impossible de charger la galerie.'
      } finally {
        this.loading = false
      }
    },
  },
})


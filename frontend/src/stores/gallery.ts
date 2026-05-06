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
        // Fallback to static assets so images show on first deploy.
        this.items = [
          { id: 1, image_url: '/uploads/tsaf001.png', category: 'hero', sort_order: 0 },
          { id: 2, image_url: '/uploads/tsaf002.jpeg', category: 'story', sort_order: 1 },
          { id: 3, image_url: '/uploads/tsaf003.jpeg', category: 'story', sort_order: 2 },
        ]
      } finally {
        this.loading = false
      }
    },
  },
})


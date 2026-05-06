<template>
  <div class="app">
    <BackgroundAurora />
    <TopNav :sections="sections" :couple-name="eventStore.event?.couple_name ?? '...'"/>

    <main class="wrap">
      <HeroSection
        :event="eventStore.event"
        :loading="eventStore.loading"
        :error="eventStore.error"
        :hero-image-url="heroImageUrl"
      />

      <IntroMessage
        id="intro"
        :event="eventStore.event"
        :loading="eventStore.loading"
      />

      <LoveStory id="story" :gallery="galleryStore.items" :loading="galleryStore.loading" />

      <EventDetails id="details" :event="eventStore.event" :loading="eventStore.loading" />

      <CountdownTimer
        id="countdown"
        :event-date="eventStore.event?.date"
        :loading="eventStore.loading"
      />

      <GalleryMasonry id="gallery" :items="galleryStore.items" :loading="galleryStore.loading" />

      <ProgramTimeline id="program" />

      <RsvpForm
        id="rsvp"
        :submitting="rsvpStore.submitting"
        :error="rsvpStore.error"
        @submitted="onRsvpSubmitted"
      />

      <QuotesSection id="quotes" :items="messagesStore.items" :loading="messagesStore.loading" />

      <FinalSection :event="eventStore.event" :hero-image-url="heroImageUrl" />
    </main>

    <SiteFooter :couple-name="eventStore.event?.couple_name ?? 'Wilfried & [Partner Name]'" />

    <ToastHost :toast="toast" />
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import BackgroundAurora from './components/BackgroundAurora.vue'
import CountdownTimer from './components/CountdownTimer.vue'
import EventDetails from './components/EventDetails.vue'
import FinalSection from './components/FinalSection.vue'
import GalleryMasonry from './components/GalleryMasonry.vue'
import HeroSection from './components/HeroSection.vue'
import IntroMessage from './components/IntroMessage.vue'
import LoveStory from './components/LoveStory.vue'
import ProgramTimeline from './components/ProgramTimeline.vue'
import QuotesSection from './components/QuotesSection.vue'
import RsvpForm from './components/RsvpForm.vue'
import SiteFooter from './components/SiteFooter.vue'
import ToastHost, { type ToastState } from './components/ToastHost.vue'
import TopNav, { type NavSection } from './components/TopNav.vue'
import { useReveal } from './composables/useReveal'
import { useEventStore } from './stores/event'
import { useGalleryStore } from './stores/gallery'
import { useMessagesStore } from './stores/messages'
import { useRsvpStore } from './stores/rsvp'

const sections: NavSection[] = [
  { id: 'intro', label: 'Message' },
  { id: 'story', label: 'Histoire' },
  { id: 'details', label: 'Infos' },
  { id: 'countdown', label: 'Compte' },
  { id: 'gallery', label: 'Galerie' },
  { id: 'program', label: 'Programme' },
  { id: 'rsvp', label: 'RSVP' },
]

const eventStore = useEventStore()
const galleryStore = useGalleryStore()
const messagesStore = useMessagesStore()
const rsvpStore = useRsvpStore()

const toast = ref<ToastState>({ isOn: false, message: '' })

const heroImageUrl = computed(() => {
  const hero = galleryStore.items.find((x) => x.category === 'hero') ?? galleryStore.items[0]
  return hero?.image_url ?? ''
})

function showToast(message: string) {
  toast.value = { isOn: true, message }
  window.clearTimeout((showToast as any)._t)
  ;(showToast as any)._t = window.setTimeout(() => {
    toast.value = { isOn: false, message: '' }
  }, 2600)
}

function onRsvpSubmitted(name: string) {
  showToast(`Réponse enregistrée. Merci ${name} !`)
}

onMounted(async () => {
  const stopReveal = useReveal()
  try {
    await Promise.all([eventStore.fetchEvent(), galleryStore.fetchGallery(), messagesStore.fetchMessages()])
  } finally {
    // keep observer running; stopReveal is here if we ever want to unmount
    void stopReveal
  }
})
</script>

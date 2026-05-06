export function useReveal() {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  const selectors = ['[data-reveal="block"]', '[data-reveal="line"]']

  function revealNow(el: Element) {
    el.classList.add('is-visible')
  }

  if (reduceMotion) {
    document.querySelectorAll(selectors.join(',')).forEach(revealNow)
    return () => {}
  }

  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue
        revealNow(entry.target)
        io.unobserve(entry.target)
      }
    },
    { root: null, rootMargin: '0px 0px 18% 0px', threshold: 0 },
  )

  document.querySelectorAll(selectors.join(',')).forEach((el) => io.observe(el))
  return () => io.disconnect()
}


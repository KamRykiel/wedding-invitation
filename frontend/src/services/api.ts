export type ApiError = {
  status: number
  message: string
  details?: unknown
}

// If not set, default to same-origin (nginx can proxy /api).
const baseUrl = (import.meta.env.VITE_API_BASE_URL as string | undefined) ?? ''

async function parseError(res: Response): Promise<ApiError> {
  let details: unknown = undefined
  try {
    details = await res.json()
  } catch {
    // ignore
  }
  const message =
    (details as any)?.detail?.toString?.() ??
    (typeof details === 'string' ? details : '') ??
    res.statusText ??
    'Erreur'
  return { status: res.status, message, details }
}

export async function getJson<T>(path: string): Promise<T> {
  const res = await fetch(`${baseUrl}${path}`, { headers: { Accept: 'application/json' } })
  if (!res.ok) throw await parseError(res)
  return (await res.json()) as T
}

export async function postJson<TIn, TOut>(path: string, body: TIn): Promise<TOut> {
  const res = await fetch(`${baseUrl}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
    body: JSON.stringify(body),
  })
  if (!res.ok) throw await parseError(res)
  return (await res.json()) as TOut
}


const CACHE = 'food-tracker-v7';
const STATIC = [
  '/Calorie-tracker/manifest.json',
  '/Calorie-tracker/icons/icon-192.png',
  '/Calorie-tracker/icons/icon-512.png',
];

// Install — only cache static assets, NOT index.html
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(cache => cache.addAll(STATIC))
  );
  self.skipWaiting();
});

// Activate — clear old caches
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch — index.html always fetched fresh from network
// Static assets served from cache
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);

  // Always fetch index.html fresh — never cache it
  if (url.pathname.endsWith('/') || url.pathname.endsWith('index.html')) {
    e.respondWith(
      fetch(e.request).catch(() => caches.match(e.request))
    );
    return;
  }

  // Static assets: cache first
  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(res => {
        if (!res || res.status !== 200) return res;
        const clone = res.clone();
        caches.open(CACHE).then(cache => cache.put(e.request, clone));
        return res;
      });
    })
  );
});

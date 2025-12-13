// Service Worker for SnapCode
const CACHE_NAME = 'snapcode-v2';
const CACHE_URLS = [
  '/',
  '/index.html',
  '/static/favicon.ico'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(CACHE_URLS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((names) => Promise.all(
        names.filter((n) => n !== CACHE_NAME).map((n) => caches.delete(n))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  // Skip non-GET and chrome-extension requests
  if (event.request.method !== 'GET' || event.request.url.startsWith('chrome-extension')) {
    return;
  }
  
  // Network-first for external CDN, cache-first for local
  const isExternal = !event.request.url.startsWith(self.location.origin);
  
  event.respondWith(
    isExternal
      ? fetch(event.request).catch(() => caches.match(event.request))
      : caches.match(event.request).then((r) => r || fetch(event.request))
  );
});

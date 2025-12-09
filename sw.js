// Service Worker for SnapCode
const CACHE_NAME = 'snapcode-v1';
const CACHE_URLS = [
  '/',
  '/index.html',
  '/static/favicon.ico',
  // CDN resources
  'https://cdn.tailwindcss.com',
  'https://cdn.jsdelivr.net/npm/alpinejs@3.13.3/dist/cdn.min.js',
  'https://cdn.jsdelivr.net/npm/marked@11.1.1/marked.min.js',
  'https://cdn.jsdelivr.net/npm/dompurify@3.0.8/dist/purify.min.js',
  'https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js',
  'https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500;600;700&display=swap'
];

// Install - cache resources
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(CACHE_URLS))
      .then(() => self.skipWaiting())
  );
});

// Activate - clean old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((cacheNames) => {
        return Promise.all(
          cacheNames
            .filter((name) => name !== CACHE_NAME)
            .map((name) => caches.delete(name))
        );
      })
      .then(() => self.clients.claim())
  );
});

// Fetch - serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        if (response) {
          return response;
        }
        
        return fetch(event.request).then((response) => {
          // Cache successful responses
          if (response && response.status === 200) {
            const responseClone = response.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, responseClone);
            });
          }
          return response;
        });
      })
      .catch(() => {
        // Offline fallback
        if (event.request.destination === 'document') {
          return caches.match('/index.html');
        }
      })
  );
});

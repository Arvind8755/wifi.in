{% comment %} // templates/service-worker.js
// Reset SW: take control, then unregister any old service worker.

self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (event) => {
  event.waitUntil(self.clients.claim());
});

// No fetch handler => no caching or redirects.

// Unregister on first run, then refresh clients
self.registration.unregister().then(() => {
  return self.clients.matchAll().then((clients) => {
    clients.forEach((client) => client.navigate(client.url));
  });
}); {% endcomment %}

/* Zkouška A2 — service worker. Сайт працює лише онлайн; без інтернету показуємо сторінку offline.html.
   Нічого з завдань не кешується, тому статистика й оновлення завжди актуальні. */
const CACHE = 'a2-shell-v3';
const SHELL = ['/offline.html', '/img/app/icon-192.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.mode !== 'navigate') return; // усе інше — звичайна мережа браузера
  e.respondWith(fetch(e.request).catch(() => caches.match('/offline.html')));
});

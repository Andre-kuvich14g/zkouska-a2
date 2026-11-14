// Мультяшні сцени всередині уроків дня 8 (720x720 бокові, 16:9 панелі для Mluvení 3).
const fs = require('fs'); const K = require('./kit.js'); const S2 = require('./scenes2.js');
const { P, MIA, EXA, DAN, KID, person, bubble, room, outdoor, night, city, txt, svg, SK, INK, T } = K;
const OUT = '/home/claude/yt/ab2/day8/';
const cal = (x, y, s, l1, l2) => T(x, y, s, 0, `<rect width="220" height="230" rx="18" fill="#fff" stroke="${INK}" stroke-width="6"/><rect width="220" height="64" rx="18" fill="#e63946"/><rect y="40" width="220" height="24" fill="#e63946"/>${[50, 110, 170].map(cx => `<circle cx="${cx}" cy="6" r="10" fill="${INK}"/>`).join('')}${txt(110, 48, l1, 30, '#fff')}${txt(110, 160, l2, 44, INK)}`);
const flower = (x, y, s, c) => T(x, y, s, 0, `<path d="M0 0 v120" stroke="#22b14c" stroke-width="10"/>${[0, 72, 144, 216, 288].map(a => `<circle cx="${Math.cos(a / 57.3) * 28}" cy="${Math.sin(a / 57.3) * 28}" r="22" fill="${c}"/>`).join('')}<circle r="18" fill="#ffd93b"/>`);
const pollen = (x, y) => [0, 1, 2, 3, 4, 5, 6, 7].map(i => `<circle cx="${x + (i * 47) % 160}" cy="${y + (i * 31) % 110}" r="7" fill="#ffd93b" stroke="#c99a00" stroke-width="2"/>`).join('');
const tv = (x, y, s, inner = '') => T(x, y, s, 0, `<rect width="300" height="190" rx="14" fill="${INK}"/><rect x="14" y="14" width="272" height="162" rx="8" fill="#3fb6f2"/>${inner}<rect x="120" y="190" width="60" height="30" fill="${INK}"/><rect x="80" y="216" width="140" height="12" rx="6" fill="${INK}"/>`);
const mat = (x, y, s, c = '#6d3fc0') => T(x, y, s, 0, `<rect width="360" height="44" rx="20" fill="${c}"/>`);
const bowl = (x, y, s) => T(x, y, s, 0, `<path d="M-110 0 h220 q-10 90 -110 90 q-100 0 -110 -90z" fill="#fff" stroke="${INK}" stroke-width="6"/><circle cx="-50" cy="-10" r="26" fill="#22b14c"/><circle cx="0" cy="-20" r="28" fill="#6fcf57"/><circle cx="50" cy="-8" r="24" fill="#e63946"/><circle cx="20" cy="-2" r="16" fill="#ffb020"/>`);
const soup = (x, y, s) => T(x, y, s, 0, `<ellipse cx="0" cy="0" rx="90" ry="26" fill="#ffb020" stroke="${INK}" stroke-width="5"/><path d="M-90 0 q0 70 90 70 q90 0 90 -70" fill="#fff" stroke="${INK}" stroke-width="5"/><path d="M-30 -40 q10 -30 0 -60 M20 -40 q10 -30 0 -60" stroke="#9aa4b8" stroke-width="6" fill="none"/>`);
const coffee = (x, y, s) => T(x, y, s, 0, `<rect x="-40" y="0" width="80" height="90" rx="12" fill="#fff" stroke="${INK}" stroke-width="5"/><path d="M40 20 q34 0 34 30 q0 30 -34 30" stroke="${INK}" stroke-width="6" fill="none"/><rect x="-32" y="8" width="64" height="20" fill="#6b3d1f"/><path d="M-10 -10 q10 -20 0 -40 M14 -10 q10 -20 0 -40" stroke="#9aa4b8" stroke-width="5" fill="none"/>`);
const alarm = (x, y, s) => P.clock(x, y, s, 4, 0) + T(x, y, s, 0, `<path d="M-70 -70 l-30 -20 M70 -70 l30 -20" stroke="${INK}" stroke-width="8" stroke-linecap="round"/>`);
const lorry = (x, y, s) => T(x, y, s, 0, `<rect x="0" y="0" width="360" height="200" rx="10" fill="#e9edf4" stroke="${INK}" stroke-width="6"/><rect x="360" y="70" width="120" height="130" rx="16" fill="#1f5fbf" stroke="${INK}" stroke-width="6"/><rect x="385" y="88" width="70" height="50" rx="8" fill="#bfeaff"/><circle cx="80" cy="210" r="34" fill="${INK}"/><circle cx="280" cy="210" r="34" fill="${INK}"/><circle cx="420" cy="210" r="34" fill="${INK}"/>${txt(180, 115, 'SKLAD', 44, '#1f5fbf')}`);
const SC = {
 // f08 — zápis k lékaři: 1 proč nový lékař (stěhování), 2 alergie, 3 kdy (ráno / pátek)
 f08_1: ['560 0 720 720', () => S2.f08()],
 f08_2: ['260 0 720 720', () => svg(outdoor('#5cc4ff', '#d4f3ff', '#6fcf57', { hills: false }) + flower(420, 420, 1.1, '#ff5a5f') + flower(520, 470, .9, '#6d3fc0') + flower(900, 440, 1.0, '#ff7a3d') + pollen(560, 200) + DAN(700, 420, { mouth: 'open', arms: 'down', shirt: '#2bb673' }) + bubble(740, 90, 300, 'Hapčí!', 50, 'l') + P.pills(900, 600, .7))],
 f08_3: ['260 0 720 720', () => svg(room('#fff3d6', '#ffe1a6', '#9c6435', { window: [860, 60] }) + K.sun(940, 140, .7) + cal(340, 110, 1.0, 'PÁTEK', '14:00') + P.clock(720, 220, 1.1, 7, 0) + DAN(560, 450, { arms: 'wave', mouth: 'open', shirt: '#2bb673', s: .9 }) + P.briefcase(820, 560, .7))],
 // p08 — dětská oslava
 p08_1: ['560 0 720 720', () => S2.p08()],
 // m08 — čeština
 m08_1: ['560 0 720 720', () => S2.m08()],
 m08_2: ['260 0 720 720', () => svg(room('#e8f0ff', '#cfdcff', '#c98b55') + tv(640, 120, 1.0, txt(150, 110, 'Zprávy', 40, '#fff')) + P.sofa(470, 470, .9) + DAN(520, 430, { arms: 'hold', mouth: 'open', s: .85 }) + P.phone(560, 520, .6, -10) + P.books(860, 560, .5))],
 m08_3: ['260 0 720 720', () => svg(room('#e7ebf2', '#cfd6e4', '#8a8f9c') + P.box(320, 470, .9) + P.box(320, 350, .9, 4) + DAN(560, 430, { arms: 'wave', mouth: 'open', shirt: '#ff7a3d', s: .9 }) + person({ x: 830, y: 430, s: .9, hs: 'short', hair: '#c9a26b', shirt: '#1f5fbf', flip: true, mouth: 'open', arms: 'wave' }) + bubble(330, 80, 360, 'Ahoj, jak se máš?', 38, 'r') + bubble(640, 200, 260, 'Dobře!', 40, 'l'))],
 // d08 — půjčovna kol
 d08_1: ['560 0 720 720', () => S2.d08()],
 d08_2: ['260 0 720 720', () => svg(outdoor('#4fb8ff', '#d4f3ff', '#6fcf57') + P.counter(640, 520, 560, '#22b14c', '') + EXA(780, 360, { hs: 'long', hair: '#7a3b12', shirt: '#22b14c', flip: true, mouth: 'open', glasses: false }) + P.helmet(470, 430, .9) + P.clock(900, 140, .8, 19, 0) + P.bike(380, 560, .6, 0) + KID(560, 560, { arms: 'up', mouth: 'open', s: .8 }))],
 // r08 — něco pro zdraví
 r08_s: ['560 0 720 720', () => S2.r08()],
 r08_joga: ['260 0 720 720', () => svg(room('#f3e8ff', '#e2ccff', '#c98b55', { window: [880, 60] }) + mat(440, 600, 1.1) + MIA(620, 420, { arms: 'up', shirt: '#6d3fc0', mouth: 'smile' }) + P.plant(380, 480, .8) + txt(640, 120, '🧘', 90))],
 r08_proch: ['260 0 720 720', () => svg(outdoor('#4fb8ff', '#d4f3ff', '#6fcf57') + `<path d="M260 720 Q600 560 980 520" stroke="#d9c39a" stroke-width="120" fill="none"/>` + P.tree(380, 500, .9) + P.tree(900, 470, .8) + DAN(560, 440, { arms: 'wave', s: .8 }) + MIA(720, 440, { arms: 'wave', s: .8, shirt: '#ff5a5f' }) + K.sun(900, 120, .7))],
 r08_jidlo: ['260 0 720 720', () => svg(room('#e6fbef', '#c2f0d5', '#9c6435') + P.table(340, 520, 600) + bowl(520, 470, 1.2) + bowl(780, 480, .9) + T(660, 300, 1, 0, `<circle r="40" fill="#e63946"/><path d="M0 -40 q10 -30 30 -30" stroke="#22b14c" stroke-width="8" fill="none"/>`) + T(400, 330, 1, 20, `<path d="M0 0 l26 120 l-52 0z" fill="#ff7a3d"/><path d="M0 0 l-12 -30 M0 0 l12 -30" stroke="#22b14c" stroke-width="8"/>`))],
 outro: ['560 0 720 720', () => S2.promo()],
};
// Mluvení 3 · v08 — Ivanův pracovní den (16:9 panelі)
const VB = '100 30 1080 608';
const PN = {
 v08_1: () => svg(night() + K.win(820, 80, 300, 220) + P.bed(560, 470, 1.0) + alarm(380, 230, .9) + DAN(760, 430, { arms: 'hold', mouth: 'open', shirt: '#9aa4b8', s: .95 }) + coffee(900, 470, .9)),
 v08_2: () => svg(room('#e7ebf2', '#cfd6e4', '#8a8f9c') + P.box(300, 470, 1.0) + P.box(300, 330, 1.0, 4) + P.box(420, 470, 1.0, -3) + lorry(760, 330, .95) + DAN(620, 430, { arms: 'hold', shirt: '#ff7a3d', hat: 'cap', hatc: '#ffd500', mouth: 'open', extra: `<rect x="-36" y="110" width="72" height="16" fill="#ffd500"/>` }) + P.box(620, 520, .55)),
 v08_3: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435') + DAN(470, 400, { mouth: 'open', shirt: '#ff7a3d' }) + person({ x: 800, y: 400, hs: 'short', hair: '#c9a26b', shirt: '#1f5fbf', flip: true, mouth: 'open' }) + P.table(300, 540, 760) + soup(470, 500, .9) + soup(800, 500, .9) + P.ball(640, 200, .8) + bubble(560, 90, 260, 'Gól!', 46, 'l')),
 v08_4: () => svg(room('#e8f0ff', '#cfdcff', '#c98b55') + tv(820, 150, 1.0, txt(150, 110, '⚽', 70)) + P.sofa(520, 470, 1.0) + DAN(560, 430, { arms: 'down', mouth: 'sad', s: .95 }) + P.zzz(660, 220, .9, '#1f5fbf')),
 v08_t: () => svg(room('#e7ebf2', '#cfd6e4', '#8a8f9c') + P.box(300, 470, 1.0) + P.box(420, 470, 1.0, -3) + DAN(620, 430, { arms: 'wave', shirt: '#ff7a3d', hat: 'cap', hatc: '#ffd500', mouth: 'open', extra: `<rect x="-36" y="110" width="72" height="16" fill="#ffd500"/>` }) + bubble(700, 120, 380, 'Co dělal Ivan?', 40, 'l') + P.clock(960, 360, .9, 4, 0)),
};
fs.mkdirSync(OUT, { recursive: true });
for (const [k, [vb, f]] of Object.entries(SC)) fs.writeFileSync(`${OUT}${k}.svg`, f().replace('viewBox="0 0 1280 720" width="1280" height="720"', `viewBox="${vb}" width="720" height="720"`));
for (const [k, f] of Object.entries(PN)) fs.writeFileSync(`${OUT}${k}.svg`, f().replace('viewBox="0 0 1280 720" width="1280" height="720"', `viewBox="${VB}" width="1080" height="608"`));
console.log(Object.keys(SC).concat(Object.keys(PN)).join(' '));

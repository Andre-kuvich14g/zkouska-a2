// Сцени дня 20: f20 cestovní kancelář · p20 zkouška (e-mail učitelce) · m20 cestování · d20 zoo · v20 den zkoušky · r20 oslava
const K = require('../../thumb3/kit.js'); const S2 = require('../../thumb3/scenes2.js');
const { P, DAN, MIA, EXA, KID, person, bubble, room, outdoor, night, city, txt, svg, INK, T } = K;

const sea = (y = 470) => `<rect y="${y}" width="1280" height="${720 - y}" fill="#2fa8e0"/>${[0, 1, 2].map(i => `<path d="M${i * 430} ${y + 40} q50 -24 100 0 t100 0 t100 0 t100 0" stroke="#bfe9ff" stroke-width="8" fill="none"/>`).join('')}<rect y="${y + 140}" width="1280" height="${580 - y}" fill="#f3d19b"/>`;
const sun = (x, y, s = 1) => T(x, y, s, 0, `<circle r="60" fill="#ffd500"/>${Array.from({ length: 10 }, (_, i) => `<path d="M0 -78 V-104" stroke="#ffd500" stroke-width="10" stroke-linecap="round" transform="rotate(${i * 36})"/>`).join('')}`);
const umbrella = (x, y, s = 1) => T(x, y, s, 0, `<path d="M0 0 V200" stroke="${INK}" stroke-width="8"/><path d="M-130 10 Q0 -120 130 10Z" fill="#e63946"/><path d="M-130 10 Q-65 -30 0 10 Q65 -30 130 10" fill="#fff" opacity=".35"/>`);
const boat = (x, y, s = 1, c = '#ff7a3d') => T(x, y, s, 0, `<path d="M-120 0 H120 L90 50 H-90Z" fill="${c}"/><path d="M0 0 V-150" stroke="${INK}" stroke-width="7"/><path d="M6 -140 L90 -20 H6Z" fill="#fff"/>`);
const passport = (x, y, s = 1, r = -10) => T(x, y, s, r, `<rect width="120" height="160" rx="12" fill="#1f3f7a"/><circle cx="60" cy="70" r="26" fill="none" stroke="#ffd500" stroke-width="5"/>${txt(60, 135, 'PAS', 26, '#ffd500')}`);
const cert = (x, y, s = 1, r = -6) => T(x, y, s, r, `<rect width="300" height="210" rx="10" fill="#fffbe8" stroke="#c9a800" stroke-width="8"/>${txt(150, 50, 'CERTIFIKÁT', 30, '#1f3f7a')}${txt(150, 100, 'A2', 52, '#e63946')}<path d="M40 140 H260 M60 165 H240" stroke="#9aa4b8" stroke-width="6"/><circle cx="250" cy="180" r="26" fill="#e63946"/>`);
const cup = (x, y, s = 1) => T(x, y, s, 0, `<path d="M0 0 H90 L80 90 H10Z" fill="#fff" stroke="${INK}" stroke-width="5"/><path d="M90 20 q34 0 30 30 q-4 24 -34 22" fill="none" stroke="${INK}" stroke-width="6"/><path d="M25 -20 q10 -20 0 -40 M55 -20 q10 -20 0 -40" stroke="#9aa4b8" stroke-width="5" fill="none"/>`);
const giraffe = (x, y, s = 1) => T(x, y, s, 0, `<rect x="-60" y="-40" width="150" height="90" rx="40" fill="#ffc928"/>${[[-20, 0], [30, -10], [60, 20], [-40, 30]].map(([a, b]) => `<circle cx="${a}" cy="${b}" r="12" fill="#c98b55"/>`).join('')}<rect x="50" y="-260" width="34" height="240" rx="16" fill="#ffc928"/><ellipse cx="80" cy="-270" rx="46" ry="30" fill="#ffc928"/><circle cx="94" cy="-278" r="6" fill="${INK}"/>${[-50, -10, 40, 70].map(a => `<rect x="${a}" y="40" width="16" height="120" fill="#ffc928"/>`).join('')}`);
const elephant = (x, y, s = 1) => T(x, y, s, 0, `<ellipse cx="0" cy="0" rx="130" ry="90" fill="#9aa4b8"/><circle cx="-120" cy="-50" r="60" fill="#9aa4b8"/><ellipse cx="-80" cy="-60" rx="40" ry="55" fill="#b8c1d4"/><path d="M-165 -30 q-40 60 -10 120" stroke="#9aa4b8" stroke-width="30" fill="none" stroke-linecap="round"/><circle cx="-135" cy="-62" r="7" fill="${INK}"/>${[-80, -20, 40, 90].map(a => `<rect x="${a}" y="60" width="34" height="80" fill="#9aa4b8"/>`).join('')}`);
const pin = (x, y, s = 1) => T(x, y, s, 0, `<path d="M0 -120 q-26 0 -22 34 q4 30 -16 70 q-10 30 10 60 h56 q20 -30 10 -60 q-20 -40 -16 -70 q4 -34 -22 -34Z" fill="#fff" stroke="${INK}" stroke-width="4"/><rect x="-22" y="-80" width="44" height="10" fill="#e63946"/><rect x="-26" y="-64" width="52" height="10" fill="#e63946"/>`);
const bball = (x, y, s = 1) => T(x, y, s, 0, `<circle r="60" fill="#2f2f6d"/><circle cx="-16" cy="-22" r="8" fill="#ccc"/><circle cx="8" cy="-28" r="8" fill="#ccc"/><circle cx="-6" cy="-4" r="8" fill="#ccc"/>`);
const desk = (x, y, w) => `<rect x="${x}" y="${y}" width="${w}" height="24" rx="6" fill="#c98b55"/><rect x="${x + 20}" y="${y + 24}" width="18" height="${700 - y}" fill="#a4703f"/><rect x="${x + w - 38}" y="${y + 24}" width="18" height="${700 - y}" fill="#a4703f"/>`;

exports.SC = {
  f20: () => svg(outdoor('#5cc4ff', '#d4f3ff', '#f3d19b', { hills: false }) + sea(430) + sun(1150, 110, .9) + umbrella(1130, 420, .9) + P.form(600, 90, .75, -6, 'OBJEDNÁVKA') + P.suitcase(640, 470, .9, '#e63946') + DAN(940, 400, { arms: 'wave', shirt: '#2f80ed', mouth: 'open' })),
  p20: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435', { window: [1000, 70] }) + cert(600, 110, .9) + P.envelope(640, 420, .7, 8) + cup(1150, 520, .9) + MIA(980, 420, { arms: 'up', mouth: 'open', shirt: '#22b14c' })),
  m20: () => svg(outdoor('#5cc4ff', '#d4f3ff', '#6fcf57') + sea(520) + P.car(600, 400, .9, '#ffb020') + passport(1100, 110, .8) + P.suitcase(1160, 470, .7, '#2f80ed') + DAN(950, 410, { arms: 'hold', s: .9, mouth: 'open' })),
  d20: () => svg(outdoor('#5cc4ff', '#d4f3ff', '#6fcf57', { hills: false }) + P.counter(560, 460, 300, '#8a5a2b', 'POKLADNA') + EXA(700, 360, { s: .8, mouth: 'open', shirt: '#be185d' }) + giraffe(1100, 420, .9) + DAN(950, 420, { arms: 'point', s: .85 }) + KID(1040, 470, { s: .8, arms: 'up', mouth: 'open' })),
  v20: () => svg(room('#eef3ff', '#cfdcff', '#9aa4b8') + P.board(600, 70, .8, ['ZKOUŠKA A2']) + desk(620, 470, 560) + P.form(700, 400, .55, -4, 'TEST') + DAN(980, 400, { arms: 'hold', mouth: 'smile' }) + P.clock(1180, 120, .6, 9, 0)),
  r20: () => svg(room('#eee6fb', '#d9c8f8', '#9c6435') + cert(600, 100, .7) + P.pizza(700, 470, .9) + pin(860, 560, .8) + boat(1180, 640, .6) + DAN(980, 410, { arms: 'up', shirt: '#22b14c', mouth: 'open' }) + MIA(1160, 410, { arms: 'wave', shirt: '#e63946' }) + P.qmark(1080, 120, .7)),
  outro: () => S2.promo(),
};
const ROOM = () => room('#eef3ff', '#cfdcff', '#9aa4b8');
exports.PN = {
  v20_1: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435', { window: [900, 60] }) + P.clock(330, 200, 1.4, 6, 0) + cup(520, 480, 1.3) + DAN(800, 360, { mouth: 'open', arms: 'hold', s: 1.1 }) + P.table(420, 560, 520)),
  v20_2: () => svg(outdoor('#5cc4ff', '#d4f3ff', '#6fcf57') + P.train(150, 260, 1.3, '#1f5fbf') + DAN(1020, 380, { s: 1.05, arms: 'phone' })),
  v20_3: () => svg(ROOM() + P.board(200, 80, 1.0, ['ČTENÍ · PSANÍ', 'POSLECH']) + desk(240, 470, 900) + P.form(560, 380, .8, -4, 'TEST') + P.pen(740, 420, .9) + DAN(980, 360, { arms: 'hold', s: 1.1 })),
  v20_4: () => svg(ROOM() + desk(380, 500, 640) + EXA(880, 360, { s: 1.1, mouth: 'smile', arms: 'hold' }) + DAN(460, 360, { s: 1.1, mouth: 'open', arms: 'point' }) + bubble(320, 80, 260, 'Pracuju…', 40, 'l') + P.check(1100, 140, 1.2)),
};
exports.OPT = {
  r20_o1: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435') + P.table(380, 520, 520) + P.pizza(640, 470, 1.6) + P.sign(400, 50, 480, 'RESTAURACE', '#e63946', '#fff', 50)),
  r20_o2: () => svg(room('#2f2f6d', '#1f1f4d', '#c98b55') + `<rect x="300" y="470" width="680" height="250" fill="#e0b070"/>` + [520, 600, 680, 560, 640].map((x, i) => pin(x, i < 3 ? 560 : 500, .8)).join('') + bball(800, 620, .9)),
  r20_o3: () => svg(outdoor('#5cc4ff', '#d4f3ff', '#6fcf57', { hills: false }) + `<rect y="380" width="1280" height="340" fill="#2fa8e0"/>` + boat(560, 500, 1.4) + boat(820, 560, 1.0, '#22b14c') + sun(900, 120, .9)),
};
exports.TH = [
  { id: 'f20', sec: 'f', lab: 'PSANÍ 1', hook: ['ZÁJEZD', 'K MOŘI'], ua: 'Замовлення туру в турагенції', badge: 'FORMULÁŘ · 8 BODŮ', num: '20/40' },
  { id: 'p20', sec: 'p', lab: 'PSANÍ 2', hook: ['ZKOUŠKU', 'MÁM!'], ua: 'E-mail учительці після іспиту', badge: 'E-MAIL · 12 BODŮ', num: '20/40' },
  { id: 'm20', sec: 'm', lab: 'MLUVENÍ 1', hook: ['CESTOVÁNÍ', 'A DOVOLENÁ'], ua: 'Подорожі й відпустка', badge: '10 OTÁZEK + VZORY', num: '20/40' },
  { id: 'd20', sec: 'd', lab: 'MLUVENÍ 2', hook: ['V ZOO'], ua: 'У зоопарку з дітьми', badge: '4 OTÁZKY · 12 BODŮ', num: '20/40' },
  { id: 'v20', sec: 'v', lab: 'MLUVENÍ 3', hook: ['DEN', 'ZKOUŠKY'], ua: 'День іспиту', badge: 'PŘÍBĚH · 10 BODŮ', num: '20/40' },
  { id: 'r20', sec: 'r', lab: 'MLUVENÍ 4', hook: ['JAK TO', 'OSLAVÍME?'], ua: 'Як відсвяткуємо іспит?', badge: 'DIALOG · 7 BODŮ', num: '20/40' },
];

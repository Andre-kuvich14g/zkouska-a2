// Сцени дня 21: f21 mateřská škola (přihláška) · p21 výměna směny · m21 svátky a oslavy · d21 jazyková škola (zkouška) · v21 na poště · r21 vaříme večeři
const K = require('../../thumb3/kit.js'); const S2 = require('../../thumb3/scenes2.js');
const { P, DAN, MIA, EXA, KID, bubble, room, outdoor, txt, svg, INK, T } = K;

const sun = (x, y, s = 1) => T(x, y, s, 0, `<circle r="60" fill="#ffd500"/>${Array.from({ length: 10 }, (_, i) => `<path d="M0 -78 V-104" stroke="#ffd500" stroke-width="10" stroke-linecap="round" transform="rotate(${i * 36})"/>`).join('')}<circle cx="-20" cy="-10" r="7" fill="${INK}"/><circle cx="20" cy="-10" r="7" fill="${INK}"/><path d="M-24 18 Q0 40 24 18" stroke="${INK}" stroke-width="6" fill="none" stroke-linecap="round"/>`);
const xmas = (x, y, s = 1) => T(x, y, s, 0, `<path d="M0 -260 L-120 -40 H-60 L-150 120 H150 L60 -40 H120Z" fill="#1f8a4c"/><rect x="-22" y="120" width="44" height="60" fill="#8a5a2b"/><path d="M0 -300 l14 30 h32 l-26 20 l10 32 l-30 -20 l-30 20 l10 -32 l-26 -20 h32Z" fill="#ffd500"/>${[[-50, -60, '#e63946'], [40, -10, '#2f80ed'], [-80, 60, '#ffd500'], [70, 80, '#e63946'], [0, 30, '#fff']].map(([a, b, c]) => `<circle cx="${a}" cy="${b}" r="14" fill="${c}"/>`).join('')}`);
const firework = (x, y, s = 1, c = '#ff5a5f') => T(x, y, s, 0, Array.from({ length: 12 }, (_, i) => `<path d="M0 -26 V-80" stroke="${c}" stroke-width="9" stroke-linecap="round" transform="rotate(${i * 30})"/>`).join('') + `<circle r="14" fill="#ffd500"/>`);
const soup = (x, y, s = 1) => T(x, y, s, 0, `<path d="M-120 0 H120 Q110 110 0 110 Q-110 110 -120 0Z" fill="#fff" stroke="${INK}" stroke-width="6"/><ellipse cx="0" cy="0" rx="120" ry="24" fill="#f4a340"/>${[-50, 0, 50].map(a => `<path d="M${a} -24 q14 -30 0 -60 q-14 -30 0 -60" stroke="#9aa4b8" stroke-width="7" fill="none"/>`).join('')}`);
const salad = (x, y, s = 1) => T(x, y, s, 0, `<path d="M-130 0 H130 Q120 100 0 100 Q-120 100 -130 0Z" fill="#fff" stroke="${INK}" stroke-width="6"/>${[[-70, -14, '#6fcf57'], [-20, -26, '#3fa63a'], [40, -20, '#6fcf57'], [80, -8, '#3fa63a'], [-40, -4, '#e63946'], [20, -6, '#e63946'], [60, -30, '#ffd500']].map(([a, b, c]) => `<circle cx="${a}" cy="${b}" r="${c === '#e63946' ? 18 : 30}" fill="${c}"/>`).join('')}`);
const cal = (x, y, s = 1, a = 'SO', b = 'NE') => T(x, y, s, 0, `<rect width="300" height="210" rx="16" fill="#fff" stroke="${INK}" stroke-width="6"/><rect width="300" height="54" rx="16" fill="#e63946"/>${txt(150, 40, 'SMĚNA', 32, '#fff')}${txt(80, 150, a, 64, INK)}${txt(220, 150, b, 64, '#22b14c')}<path d="M130 130 H170 M160 118 l12 12 l-12 12" stroke="${INK}" stroke-width="7" fill="none" stroke-linecap="round"/>`);
const scale = (x, y, s = 1) => T(x, y, s, 0, `<rect x="-90" y="0" width="180" height="40" rx="8" fill="#9aa4b8"/><rect x="-60" y="40" width="120" height="30" fill="#6b7590"/>${txt(0, 30, '2,5 kg', 26, '#fff')}`);
const uaflag = (x, y, s = 1) => T(x, y, s, 0, `<path d="M0 0 V260" stroke="${INK}" stroke-width="8"/><rect x="4" y="0" width="180" height="60" fill="#2f80ed"/><rect x="4" y="60" width="180" height="60" fill="#ffd500"/>`);
const OLD = (x, y, o = {}) => MIA(x, y, Object.assign({ hair: '#c9c9c9', shirt: '#9b59b6' }, o));

exports.SC = {
  f21: () => svg(outdoor('#5cc4ff', '#d4f3ff', '#6fcf57') + P.school(560, 200, .8) + P.sign(560, 40, 400, 'ŠKOLKA SLUNÍČKO', '#ffd500', INK, 40) + sun(1150, 110, .8) + P.form(980, 120, .5, -8, 'PŘIHLÁŠKA') + DAN(960, 420, { arms: 'hold', mouth: 'smile', s: .85 }) + KID(1120, 470, { s: .75, arms: 'wave', mouth: 'open' })),
  p21: () => svg(room('#eef3ff', '#cfdcff', '#9aa4b8', { window: [1020, 70] }) + cal(620, 110, .95) + P.envelope(660, 420, .7, -8) + P.clock(1160, 470, .6, 6, 0) + DAN(960, 410, { arms: 'phone', shirt: '#2f80ed', mouth: 'open' })),
  m21: () => svg(room('#fdecef', '#f9c9d2', '#9c6435') + xmas(700, 380, .9) + P.gift(560, 560, .8, '#e63946') + P.cake(1150, 560, .7) + firework(1120, 140, .9) + DAN(940, 410, { arms: 'up', mouth: 'open', shirt: '#e63946' }) + MIA(1110, 420, { arms: 'wave', s: .9, shirt: '#22b14c' })),
  d21: () => svg(room('#eef3ff', '#cfdcff', '#9aa4b8') + P.board(580, 60, .7, ['ZKOUŠKA A2']) + P.counter(560, 460, 330, '#2f80ed', 'RECEPCE') + EXA(720, 360, { s: .8, mouth: 'open', shirt: '#be185d' }) + P.tag(1100, 120, .9, '3 200 Kč') + DAN(1000, 410, { arms: 'point', s: .9, mouth: 'open' })),
  v21: () => svg(room('#fff6dd', '#ffe7a8', '#9c6435') + P.sign(560, 60, 420, 'POŠTA', '#ffd500', INK, 56) + P.counter(560, 470, 330, '#ff9f00', '') + EXA(720, 370, { s: .8, shirt: '#2f80ed' }) + P.parcel(640, 380, .8) + OLD(1000, 420, { arms: 'hold', mouth: 'smile', s: .9 })),
  r21: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435', { window: [600, 70] }) + P.table(560, 540, 380) + soup(680, 480, .55) + P.pizza(840, 480, .6) + P.qmark(1080, 110, .7) + DAN(980, 410, { arms: 'point', mouth: 'open', shirt: '#2f80ed' }) + MIA(1160, 420, { arms: 'hold', s: .9, shirt: '#e63946' })),
  outro: () => S2.promo(),
};
exports.PN = {
  v21_1: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435', { window: [900, 60] }) + P.table(360, 560, 560) + P.box(470, 380, 1.3, 0, '') + P.gift(760, 470, .9, '#2f80ed') + P.books(400, 470, .7) + OLD(1000, 360, { arms: 'hold', s: 1.1, mouth: 'smile' })),
  v21_2: () => svg(room('#fff6dd', '#ffe7a8', '#9c6435') + P.sign(200, 50, 400, 'POŠTA', '#ffd500', INK, 56) + P.counter(140, 460, 300, '#ff9f00', '') + EXA(290, 360, { s: .9 }) + DAN(620, 380, { s: .9, shirt: '#e63946' }) + MIA(800, 380, { s: .9, shirt: '#2f80ed' }) + OLD(1000, 380, { s: .95, arms: 'down' }) + P.clock(1150, 90, .6, 10, 20)),
  v21_3: () => svg(room('#fff6dd', '#ffe7a8', '#9c6435') + P.counter(260, 460, 760, '#ff9f00', '') + EXA(420, 350, { s: 1.0, mouth: 'open' }) + scale(560, 410, 1) + P.parcel(560, 330, .7) + P.card(760, 380, 1.0, -12) + bubble(120, 70, 300, '600 Kč', 48, 'r') + OLD(960, 360, { arms: 'point', s: 1.05 })),
  v21_4: () => svg(room('#eaf6e2', '#cdebbd', '#9c6435') + P.box(480, 420, 1.2, 0, '') + P.gift(560, 330, .8, '#e63946') + KID(800, 420, { s: 1.1, arms: 'up', mouth: 'open' }) + OLD(1020, 380, { s: 1.0, arms: 'wave', mouth: 'smile' }) + uaflag(250, 120, 1.0)),
};
exports.OPT = {
  r21_o1: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435') + P.table(380, 540, 520) + P.pizza(640, 470, 1.6)),
  r21_o2: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435') + P.table(380, 540, 520) + soup(640, 420, 1.3)),
  r21_o3: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435') + P.table(380, 540, 520) + salad(640, 430, 1.3)),
};
exports.TH = [
  { id: 'f21', sec: 'f', lab: 'PSANÍ 1', hook: ['PŘIHLÁŠKA', 'DO ŠKOLKY'], ua: 'Заявка в дитячий садок', badge: 'FORMULÁŘ · 8 BODŮ', num: '21/40' },
  { id: 'p21', sec: 'p', lab: 'PSANÍ 2', hook: ['VÝMĚNA', 'SMĚNY'], ua: 'E-mail колезі: обмін змінами', badge: 'E-MAIL · 12 BODŮ', num: '21/40' },
  { id: 'm21', sec: 'm', lab: 'MLUVENÍ 1', hook: ['SVÁTKY', 'A OSLAVY'], ua: 'Свята й урочистості', badge: '10 OTÁZEK + VZORY', num: '21/40' },
  { id: 'd21', sec: 'd', lab: 'MLUVENÍ 2', hook: ['PŘIHLÁŠKA', 'NA ZKOUŠKU'], ua: 'У мовній школі: запис на іспит', badge: '4 OTÁZKY · 12 BODŮ', num: '21/40' },
  { id: 'v21', sec: 'v', lab: 'MLUVENÍ 3', hook: ['NA', 'POŠTĚ'], ua: 'На пошті', badge: 'PŘÍBĚH · 10 BODŮ', num: '21/40' },
  { id: 'r21', sec: 'r', lab: 'MLUVENÍ 4', hook: ['CO', 'UVAŘÍME?'], ua: 'Що приготуємо на вечерю?', badge: 'DIALOG · 7 BODŮ', num: '21/40' },
];

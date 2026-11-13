// 20 мультяшних сцен для Velké opakování Mluvení 3 (příběhy 1–5) — 4 картинки на історію, 16:9.
const fs = require('fs'); const K = require('./kit.js');
const { P, MIA, EXA, DAN, KID, person, bubble, room, outdoor, mountains, city, txt, svg, SK, INK, T, cloud } = K;
const OUT = '/home/claude/yt/ab2/om3/'; fs.mkdirSync(OUT, { recursive: true });
const VB = '100 30 1080 608';
// --- додаткові предмети ---
const dog = (x, y, s = 1, flip) => T(x, y, s, 0, `<g transform="scale(${flip ? -1 : 1},1)"><ellipse cx="0" cy="0" rx="90" ry="46" fill="#c98b55"/><circle cx="90" cy="-40" r="44" fill="#c98b55"/><ellipse cx="112" cy="-70" rx="16" ry="30" fill="#8a5a2b" transform="rotate(20 112 -70)"/><circle cx="104" cy="-46" r="7" fill="${INK}"/><circle cx="132" cy="-30" r="9" fill="${INK}"/><path d="M-90 -10 q-40 -30 -30 -60" stroke="#c98b55" stroke-width="16" fill="none" stroke-linecap="round"/>${[-60, -20, 30, 70].map(lx => `<rect x="${lx}" y="30" width="18" height="50" rx="8" fill="#c98b55"/>`).join('')}<path d="M110 -12 q14 14 30 4" stroke="#e63946" stroke-width="8" fill="none"/></g>`);
const bus = (x, y, s = 1) => T(x, y, s, 0, `<rect width="620" height="230" rx="34" fill="#e63946"/><rect y="150" width="620" height="22" fill="#ffd93b"/>${[30, 150, 270, 390].map(wx => `<rect x="${wx}" y="30" width="100" height="90" rx="12" fill="#bfe6ff"/>`).join('')}<rect x="510" y="30" width="80" height="170" rx="10" fill="#bfe6ff"/>${[110, 500].map(cx => `<circle cx="${cx}" cy="232" r="38" fill="${INK}"/><circle cx="${cx}" cy="232" r="15" fill="#9aa4b8"/>`).join('')}${txt(560, 22, '14', 26, '#fff')}`);
const ambulance = (x, y, s = 1) => T(x, y, s, 0, `<rect x="0" y="0" width="380" height="190" rx="18" fill="#fff" stroke="${INK}" stroke-width="5"/><path d="M380 60 h80 l50 60 v70 h-130Z" fill="#fff" stroke="${INK}" stroke-width="5"/><rect x="400" y="74" width="66" height="46" rx="6" fill="#bfe6ff"/><rect x="0" y="120" width="510" height="18" fill="#e63946"/><path d="M190 30 v80 M150 70 h80" stroke="#e63946" stroke-width="26"/><rect x="150" y="-26" width="80" height="26" rx="8" fill="#2f80ed"/>${[90, 420].map(cx => `<circle cx="${cx}" cy="196" r="38" fill="${INK}"/><circle cx="${cx}" cy="196" r="15" fill="#9aa4b8"/>`).join('')}`);
const rain = (x0 = 0, x1 = 1280) => `<g stroke="#5b8bd6" stroke-width="6" stroke-linecap="round" opacity=".8">${Array.from({ length: 46 }, (_, i) => { const x = x0 + (i * 97) % (x1 - x0), y = (i * 53) % 560; return `<path d="M${x} ${y} l-12 34"/>`; }).join('')}</g>`;
const darkCloud = (x, y, s = 1) => T(x, y, s, 0, `<g fill="#8a94a8"><ellipse cx="0" cy="0" rx="120" ry="44"/><ellipse cx="60" cy="-26" rx="80" ry="54"/><ellipse cx="-60" cy="-12" rx="60" ry="40"/></g>`);
const cup = (x, y, s = 1, c = '#e63946') => T(x, y, s, 0, `<path d="M0 0 h70 l-8 70 h-54Z" fill="${c}"/><path d="M70 14 q30 0 26 26 q-4 22 -30 20" stroke="${c}" stroke-width="8" fill="none"/><path d="M20 -14 q10 -16 0 -30 M42 -14 q10 -16 0 -30" stroke="#9aa4b8" stroke-width="5" fill="none"/>`);
const policeCap = `<path d="M-52 -26 Q-50 -70 0 -72 Q50 -70 52 -26Z" fill="#1d3b78"/><rect x="-56" y="-30" width="112" height="12" rx="4" fill="${INK}"/><circle cy="-50" r="9" fill="#ffd93b"/>`;
const cast = `<rect x="70" y="80" width="56" height="70" rx="20" fill="#fff" stroke="#d6dcea" stroke-width="4"/>`;
const plate2 = (x, y) => T(x, y, 1, 0, `<ellipse rx="60" ry="18" fill="#fff" stroke="#d6dcea" stroke-width="4"/>`);
const kitchen = () => room('#fff7e6', '#ffe9c2', '#c98b55') + `<rect x="100" y="380" width="1080" height="160" fill="#f3e2c2"/><rect x="100" y="370" width="1080" height="22" fill="#8a5a2b"/>${[160, 420, 680, 940].map(x => `<rect x="${x}" y="410" width="220" height="110" rx="10" fill="#e8d3ae"/><circle cx="${x + 200}" cy="465" r="7" fill="#8a5a2b"/>`).join('')}<rect x="200" y="90" width="300" height="150" rx="12" fill="#e8d3ae"/><rect x="560" y="90" width="300" height="150" rx="12" fill="#e8d3ae"/>`;
const doorF = (x, y) => `<rect x="${x}" y="${y}" width="200" height="400" rx="10" fill="#8a5a2b"/><circle cx="${x + 170}" cy="${y + 220}" r="10" fill="#ffd93b"/>`;
// персонажі історій
const NOVAK = (x, y, o = {}) => DAN(x, y, { shirt: '#2bb673', ...o });
const NOVAKOVA = (x, y, o = {}) => MIA(x, y, { shirt: '#ff7a3d', ...o });
const PETR = (x, y, o = {}) => DAN(x, y, { shirt: '#2f80ed', hat: 'cap', hatc: '#22b14c', ...o });
const JANA = (x, y, o = {}) => MIA(x, y, { shirt: '#ff5a5f', ...o });
const TICHY = (x, y, o = {}) => person({ x, y, skin: SK[3], hair: '#7a3b12', hs: 'short', shirt: '#6d3fc0', glasses: true, ...o });
const DVORAK = (x, y, o = {}) => person({ x, y, skin: SK[1], hair: '#4a3426', hs: 'short', shirt: '#1f5fbf', beard: true, tie: '#e63946', ...o });
const MARIE = (x, y, o = {}) => person({ x, y, skin: SK[0], hair: '#e0a84a', hs: 'long', shirt: '#ff8fb8', ...o });
const FRIEND = (x, y, o = {}) => person({ x, y, skin: SK[2], hair: INK, hs: 'curly', shirt: '#ffb020', ...o });

const S = {
 // ===== 1 Stěhování =====
 v01_1: () => svg(room('#eef7ff', '#d6eaff', '#c98b55', { window: [900, 70] }) + P.box(200, 420, 1.1, -4, 'NÁDOBÍ') + P.box(420, 460, 1.0, 3) + P.box(300, 330, .8, 6, 'HRAČKY') +
  NOVAKOVA(720, 400, { arms: 'hold', mouth: 'open' }) + plate2(720, 540) + KID(940, 470, { arms: 'up', mouth: 'open', extra: `<circle cx="100" cy="0" r="30" fill="#ffd93b"/>` })),
 v01_2: () => svg(outdoor('#4fb8ff', '#d4f3ff', '#8a8f9c', { hills: false, gy: 600 }) + P.truck(560, 300, 1.15) +
  person({ x: 300, y: 380, skin: SK[2], hair: INK, hs: 'short', shirt: '#ffb020', hat: 'cap', hatc: '#1f5fbf', arms: 'hold' }) + P.box(210, 450, .9) +
  person({ x: 470, y: 400, s: .95, skin: SK[1], hair: '#5b3a1e', hs: 'short', shirt: '#ffb020', hat: 'cap', hatc: '#1f5fbf', arms: 'up', mouth: 'open' }) + P.box(990, 250, .5) ),
 v01_3: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435', { window: [880, 60] }) + P.sofa(170, 440, 1.0, '#6d3fc0') + P.table(700, 520, 360) +
  NOVAK(640, 380, { arms: 'up', mouth: 'open' }) + NOVAKOVA(1000, 400, { arms: 'point', flip: true }) + P.plant(1120, 560, .6) + bubble(700, 140, 280, 'Tady!', 48, 'r')),
 v01_4: () => svg(room('#2a2f6e', '#3b4a8f', '#7a5233', { window: [880, 60, '#1b2559'] }) + P.box(130, 380, .9) + P.box(1000, 400, 1.0) + P.box(1050, 300, .6) +
  NOVAK(360, 440, { arms: 'up', mouth: 'open' }) + NOVAKOVA(560, 450, { arms: 'down', mouth: 'open' }) + KID(760, 500, { arms: 'up', mouth: 'open' }) + P.pizza(560, 650, .9) + txt(640, 150, 'ha ha!', 54, '#ffd93b')),
 // ===== 2 Výlet na hory =====
 v02_1: () => svg(room('#e7e3ff', '#cfc7ff', '#7d8fb8') + `<rect x="180" y="90" width="920" height="320" rx="30" fill="#5cc4ff"/>` + `<g clip-path="inset(0)">${mountains().replace('M520 560', 'M180 410').replace('V720 H520Z', 'V410Z')}</g>` +
  `<rect x="160" y="70" width="960" height="360" rx="34" fill="none" stroke="#9aa4b8" stroke-width="40"/><rect x="630" y="70" width="20" height="360" fill="#9aa4b8"/>` +
  PETR(450, 450, { arms: 'point', mouth: 'open' }) + JANA(830, 460, { arms: 'down', mouth: 'smile', flip: true }) + `<rect x="100" y="560" width="1080" height="160" fill="#2f80ed"/>` + txt(640, 612, 'VLAK', 40, '#fff')),
 v02_2: () => svg(outdoor('#4fb8ff', '#d4f3ff', '#6fcf57', { hills: false }) + mountains().replace('M520 560', 'M100 560') + `<path d="M150 720 Q500 600 700 470 T1100 300" stroke="#c9a36b" stroke-width="70" fill="none" stroke-linecap="round"/>` +
  PETR(520, 440, { arms: 'wave', s: .9, extra: `<rect x="-62" y="70" width="40" height="90" rx="12" fill="#ff7a3d"/>` }) + JANA(720, 380, { arms: 'up', s: .8, mouth: 'open' }) + P.tree(220, 520, .7) + P.tree(1050, 520, .6)),
 v02_3: () => svg(outdoor('#8a94a8', '#c9d0dc', '#5aa34a', { hills: false, noSun: true }) + darkCloud(400, 120, 1.2) + darkCloud(850, 100, 1.4) + rain() +
  PETR(520, 420, { arms: 'up', mouth: 'o' }) + JANA(760, 430, { arms: 'up', mouth: 'sad' }) + bubble(260, 220, 340, 'Deštník?', 46, 'r') + P.tree(1080, 520, .7, '#3f8a3a')),
 v02_4: () => svg(room('#ffe9c7', '#ffd59a', '#8a5a2b', { window: [180, 70, '#8a94a8'] }) + darkCloud(290, 140, .5) + P.table(380, 520, 560, '#6b4421') +
  PETR(500, 410, { arms: 'hold', mouth: 'smile' }) + JANA(820, 410, { arms: 'hold', mouth: 'smile', flip: true }) + cup(470, 450, .9) + cup(790, 450, .9, '#2f80ed') + txt(1000, 160, 'CHATA', 46, '#8a5a2b')),
 // ===== 3 Nehoda na kole =====
 v03_1: () => svg(outdoor('#4fb8ff', '#d4f3ff', '#6fcf57', { hills: false, gy: 560 }) + `<path d="M100 640 H1180" stroke="#8a8f9c" stroke-width="120"/>` + city(520, ['#b7c9e8', '#a3bbe3', '#c3d3ee', '#aec2e6']).replace(/x="(\d+)"/g, (m, v) => `x="${+v - 300}"`) +
  P.bike(470, 610, 1.0) + TICHY(600, 380, { arms: 'up', mouth: 'smile', extra: P.helmet(0, -46, .9) }) + txt(1000, 200, '7:30', 54, INK)),
 v03_2: () => svg(outdoor('#4fb8ff', '#d4f3ff', '#6fcf57', { hills: false, gy: 560 }) + `<path d="M100 640 H1180" stroke="#8a8f9c" stroke-width="120"/>` +
  P.bike(360, 600, .9, 40) + TICHY(600, 470, { arms: 'up', mouth: 'o' }) + dog(880, 560, 1.1, true) + P.bang(640, 230, 1, '!') + bubble(860, 300, 240, 'Haf!', 46, 'l')),
 v03_3: () => svg(outdoor('#4fb8ff', '#d4f3ff', '#8a8f9c', { hills: false, gy: 600 }) + `<rect x="760" y="140" width="400" height="460" fill="#eef1f7"/>${txt(960, 200, 'NEMOCNICE', 40, '#e63946')}` + `<rect x="900" y="230" width="120" height="120" rx="20" fill="#fff"/><path d="M960 250 v80 M920 290 h80" stroke="#e63946" stroke-width="24"/>` +
  ambulance(180, 380, 1.05) + T(520, 300, 1, 0, `<path d="M-40 0 l20 -20 M0 -30 v-26 M40 0 l-20 -20" stroke="#2f80ed" stroke-width="10" stroke-linecap="round"/>`)),
 v03_4: () => svg(room('#e9f6ff', '#d0ecff', '#9aa4b8') + P.cross(1000, 60, .9) + TICHY(420, 400, { arms: 'wave', mouth: 'sad', extra: cast }) +
  EXA(800, 400, { hs: 'short', hair: '#9aa4b8', glasses: true, shirt: '#fff', collar: false, flip: true, arms: 'point' }) + T(940, 300, 1, 6, `<rect width="160" height="110" rx="10" fill="#fff" stroke="${INK}" stroke-width="4"/>${txt(80, 44, '6 týdnů', 28, '#e63946')}`)),
 // ===== 4 Ztracená peněženka =====
 v04_1: () => svg(outdoor('#4fb8ff', '#d4f3ff', '#8a8f9c', { hills: false, gy: 600 }) + city(600, ['#b7c9e8', '#a3bbe3', '#c3d3ee', '#aec2e6']).replace(/x="(\d+)"/g, (m, v) => `x="${+v - 380}"`) +
  bus(300, 300, 1.05) + DVORAK(560, 370, { s: .5, arms: 'down' })),
 v04_2: () => svg(room('#eef1f7', '#d6dcea', '#7d8fb8') + `<rect x="840" y="200" width="180" height="300" rx="16" fill="${INK}"/><rect x="870" y="240" width="120" height="80" rx="8" fill="#bfe6ff"/>${txt(930, 290, 'KÁVA', 26, INK)}` + cup(895, 420, .8, '#8a5a2b') +
  DVORAK(560, 400, { arms: 'up', mouth: 'o' }) + P.qmark(300, 200, 1.0) + T(300, 440, 1, 0, `<path d="M-60 0 h120 v80 q-60 30 -120 0Z" fill="#1f5fbf" stroke="${INK}" stroke-width="4"/>${txt(0, 54, 'prázdno', 22, '#fff')}`)),
 v04_3: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435') + DVORAK(420, 400, { arms: 'phone', mouth: 'open' }) + bubble(560, 120, 520, 'Zablokujte kartu, prosím!', 38, 'l') +
  P.card(820, 380, 1.0, -8) + T(900, 400, 1, 0, `<rect x="0" y="0" width="70" height="60" rx="10" fill="#e63946"/><path d="M14 0 v-24 q21 -30 42 0 v24" stroke="#e63946" stroke-width="12" fill="none"/>`) + P.bank(760, 560, .35)),
 v04_4: () => svg(room('#e6efff', '#c9dbff', '#7d8fb8') + P.sign(440, 30, 400, 'POLICIE', '#1d3b78', '#fff', 54) +
  person({ x: 820, y: 360, skin: SK[1], hair: INK, hs: 'short', shirt: '#1d3b78', collar: true, flip: true, extra: policeCap }) + P.counter(640, 520, 540, '#1d3b78', '') +
  DVORAK(360, 400, { arms: 'point', mouth: 'open' }) + T(700, 440, 1, -4, `<rect width="170" height="110" rx="8" fill="#fff" stroke="${INK}" stroke-width="4"/>${txt(85, 40, 'PROTOKOL', 24, '#1d3b78')}<path d="M24 66 h120 M24 88 h90" stroke="#b8c2d6" stroke-width="8"/>`)),
 // ===== 5 Narozeniny =====
 v05_1: () => svg(kitchen() + MARIE(620, 330, { arms: 'hold', mouth: 'smile', extra: `<rect x="-54" y="-74" width="108" height="40" rx="14" fill="#fff"/>` }) + P.cake(520, 520, .8) + T(980, 200, 1, 0, `${txt(0, 0, '☀', 90, '#ffb020')}`)),
 v05_2: () => svg(room('#ffe8f1', '#ffd0e2', '#c98b55', { window: [900, 70] }) + P.balloon(240, 180, 1.1, '#ff5a5f') + P.balloon(340, 140, 1, '#2f80ed') + P.balloon(1100, 160, 1, '#ffd93b') + P.balloon(1000, 200, .9, '#22b14c') +
  MARIE(640, 420, { arms: 'up', mouth: 'open' }) + P.balloon(760, 240, .8, '#6d3fc0') + `<path d="M260 120 Q640 40 1080 130" stroke="#ff5a5f" stroke-width="6" fill="none"/>${[340, 480, 620, 760, 900].map((x, i) => `<path d="M${x} ${92 - (i % 2) * 6} l20 40 l20 -40z" fill="${['#ffd93b', '#2f80ed', '#22b14c', '#ff7a3d', '#6d3fc0'][i]}"/>`).join('')}`),
 v05_3: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435') + doorF(160, 140) + FRIEND(420, 400, { arms: 'hold', mouth: 'open' }) + P.gift(360, 450, .7, '#2f80ed') +
  person({ x: 600, y: 410, skin: SK[1], hair: '#5b3a1e', hs: 'long', shirt: '#22b14c', arms: 'hold', mouth: 'open' }) + T(560, 470, 1, 0, `<g fill="#ff5a5f">${[0, 30, 60].map(dx => `<circle cx="${dx}" cy="0" r="20"/>`).join('')}</g><path d="M30 20 v70" stroke="#22b14c" stroke-width="8"/>`) +
  MARIE(900, 400, { arms: 'up', mouth: 'open', flip: true }) + bubble(640, 110, 420, 'Všechno nejlepší!', 40, 'l')),
 v05_4: () => svg(room('#2a2f6e', '#4b3b8f', '#7a5233') + P.balloon(200, 160, .9, '#ff5a5f') + P.balloon(1100, 150, .9, '#ffd93b') + P.notes(380, 170, .9) + P.notes(820, 140, .8, '#ff8fb8') +
  FRIEND(300, 420, { arms: 'up', mouth: 'open', hat: 'party' }) + MARIE(560, 400, { arms: 'up', mouth: 'open', hat: 'party' }) + person({ x: 820, y: 420, skin: SK[1], hair: '#5b3a1e', hs: 'long', shirt: '#22b14c', arms: 'up', mouth: 'open', hat: 'party' }) +
  DAN(1040, 440, { arms: 'up', mouth: 'open', s: .9 }) + P.cake(560, 600, .5) + txt(1040, 230, '0:00', 40, '#fff')),
 // титульні сцени підсумку
 om3_t: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435') + DAN(420, 400, { arms: 'wave', mouth: 'open' }) + bubble(500, 110, 380, 'Včera jsem…', 48, 'l') +
  T(700, 220, .38, -4, `<rect width="1100" height="700" rx="40" fill="#fff" stroke="${INK}" stroke-width="12"/><g transform="translate(40,40)"><rect width="500" height="300" rx="20" fill="#bfe6ff"/><rect x="520" width="500" height="300" rx="20" fill="#ffd6a5"/><rect y="320" width="500" height="300" rx="20" fill="#c2f0d5"/><rect x="520" y="320" width="500" height="300" rx="20" fill="#ffd0e2"/></g>${[['1', 90, 120], ['2', 610, 120], ['3', 90, 440], ['4', 610, 440]].map(([n, x, y]) => `<circle cx="${x}" cy="${y}" r="50" fill="#c2410c"/>${txt(x, y + 22, n, 64, '#fff')}`).join('')}`)),
};
for (const [k, f] of Object.entries(S)) fs.writeFileSync(`${OUT}${k}.svg`, f().replace('viewBox="0 0 1280 720"', `viewBox="${VB}" preserveAspectRatio="xMidYMid slice"`));
console.log(Object.keys(S).length);

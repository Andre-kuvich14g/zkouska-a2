// Пілот: мультяшні сцени для уроку Mluvení 3 · Příběh 7 «U lékaře» (Olga = MIA).
const fs = require('fs'); const K = require('./kit.js'); const { P, MIA, EXA, DAN, person, bubble, room, outdoor, txt, svg, SK, INK, T } = K;
const OLGA = (x, y, o = {}) => MIA(x, y, { shirt: '#ff7a3d', ...o });
const VB = { v07_1: '120 40 1100 619', v07_2: '220 90 1040 585', v07_3: '180 30 1040 585', v07_4: '100 20 1120 630', v07_t: '280 90 900 506' };
const S = {
 // 1. Ráno je jí špatně: ліжко, термометр, будильник 7:00
 v07_1: () => svg(room('#e6f0ff', '#cddcff', '#9c6435', { window: [900, 70, '#ffd6a5'] }) +
  P.bed(330, 360, 1.25) + person({ x: 470, y: 400, s: .85, skin: SK[0], hair: '#7a3b12', hs: 'long', shirt: '#6aa8ff', mouth: 'sad' }) +
  P.thermo(560, 420, .75, 40) + `<rect x="330" y="520" width="560" height="130" rx="24" fill="#6aa8ff"/>` +
  P.clock(1080, 470, .8, 210, 0) + `<rect x="1010" y="550" width="140" height="120" rx="12" fill="#8a5a2b"/>` +
  txt(700, 200, '38,5 °C', 64, '#e63946') + P.zzz(240, 300, .8, '#9aa4b8')),
 // 2. Volá do ordinace
 v07_2: () => svg(room('#fff3d6', '#ffe1a6', '#9c6435') + P.sofa(260, 470, 1.2, '#2f80ed') +
  OLGA(520, 380, { arms: 'phone', mouth: 'open', shirt: '#6aa8ff' }) +
  bubble(640, 150, 520, 'Dobrý den, mohu přijít?', 40, 'l') +
  T(1010, 360, 1, 0, `<rect width="180" height="300" rx="20" fill="#fff" stroke="${INK}" stroke-width="6"/>${txt(90, 60, 'ORDINACE', 26, '#e63946')}<path d="M90 90 v60 M60 120 h60" stroke="#e63946" stroke-width="18"/>${txt(90, 220, '10:00', 44, INK)}`)),
 // 3. Lékařka ji vyšetřuje
 v07_3: () => svg(room('#e9f6ff', '#d0ecff', '#9aa4b8') + P.cross(1040, 60, 1) +
  `<rect x="260" y="470" width="420" height="60" rx="16" fill="#fff" stroke="#d6dcea" stroke-width="6"/><rect x="290" y="530" width="20" height="190" fill="#9aa4b8"/><rect x="630" y="530" width="20" height="190" fill="#9aa4b8"/>` +
  OLGA(440, 330, { arms: 'down', mouth: 'o', shirt: '#6aa8ff' }) +
  EXA(820, 360, { hs: 'bun', hair: '#4a3426', glasses: true, shirt: '#ffffff', collar: false, flip: true, arms: 'point',
   extra: `<path d="M-28 70 q-26 50 4 92" stroke="${INK}" stroke-width="6" fill="none"/><circle cx="-22" cy="166" r="15" fill="#9aa4b8"/>` }) +
  T(560, 250, .8, -8, `<rect width="200" height="150" rx="10" fill="#fff" stroke="${INK}" stroke-width="5"/>${txt(100, 46, 'RECEPT', 30, '#1f5fbf')}<path d="M30 80 h140 M30 110 h100" stroke="#b8c2d6" stroke-width="10" stroke-linecap="round"/>`)),
 // 4. V lékárně kupuje léky
 v07_4: () => svg(room('#e8fbef', '#c6f2d6', '#9aa4b8') + P.sign(560, 30, 400, 'LÉKÁRNA', '#15803d', '#fff', 54) +
  `<rect x="980" y="140" width="110" height="110" rx="18" fill="#22b14c"/><path d="M1035 160 v70 M1000 195 h70" stroke="#fff" stroke-width="22"/>` +
  P.shelf(140, 230, 300) + P.pills(160, 130, .8) + P.pills(250, 130, .8) + P.pills(340, 130, .8) +
  person({ x: 760, y: 360, skin: SK[1], hair: INK, hs: 'short', shirt: '#fff', collar: true, flip: true }) +
  P.counter(560, 500, 520, '#15803d', '') + OLGA(330, 420, { arms: 'hold', mouth: 'smile', shirt: '#6aa8ff' }) +
  P.pills(700, 420, .8) + T(860, 440, 1, 0, `<rect width="70" height="70" rx="10" fill="#fff" stroke="${INK}" stroke-width="4"/><path d="M70 20 q30 0 30 25 q0 25 -30 25" stroke="${INK}" stroke-width="6" fill="none"/>${txt(35, 48, 'čaj', 22, '#15803d')}`)),
 // Титульна сцена уроку
 v07_t: () => svg(room('#e9f6ff', '#d0ecff', '#9aa4b8') + P.cross(1040, 60, 1) + OLGA(420, 380, { arms: 'down', mouth: 'sad', shirt: '#6aa8ff' }) + P.thermo(560, 360, .8, 30) +
  EXA(860, 380, { hs: 'bun', glasses: true, shirt: '#fff', collar: false, flip: true, arms: 'wave' }) + P.pills(1000, 560, .8) + bubble(560, 120, 300, 'Co vás bolí?', 40, 'r')),
};
for (const [k, f] of Object.entries(S)) fs.writeFileSync(`/home/claude/yt/ab2/pilot/${k}.svg`, f().replace('viewBox="0 0 1280 720"', `viewBox="${VB[k]}" preserveAspectRatio="xMidYMid slice"`));
console.log('ok');

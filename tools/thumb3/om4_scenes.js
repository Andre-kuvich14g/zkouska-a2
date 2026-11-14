// Сцени для підсумку Mluvení 4 (om4_1): ситуації r01–r05 + титульна сцена.
const fs = require('fs'); const K = require('./kit.js'); const S2 = require('./scenes2.js');
const { P, MIA, DAN, bubble, room, outdoor, svg } = K;
const OUT = '/home/claude/yt/ab2/om4/';
const SC = {
 r01: ['560 0 720 720', () => S2.r01()], r02: ['560 0 720 720', () => S2.r02()], r03: ['560 0 720 720', () => S2.r03()],
 r04: ['560 0 720 720', () => S2.r04()], r05: ['560 0 720 720', () => S2.r05()],
 om4_t: ['280 0 720 720', () => svg(room('#fff3d6', '#ffe1a6', '#9c6435') + P.table(320, 560, 680) + DAN(470, 430, { arms: 'point', mouth: 'open' }) + MIA(820, 430, { arms: 'wave', flip: true, glasses: true, shirt: '#6d3fc0' }) + bubble(300, 90, 400, 'Co kdybychom…?', 40, 'l') + bubble(640, 220, 320, 'Proč?', 44, 'r'))],
 om4_q: ['280 0 720 720', () => svg(outdoor('#4fb8ff', '#d4f3ff', '#6fcf57') + DAN(500, 430, { arms: 'up', mouth: 'open' }) + MIA(800, 430, { arms: 'wave', flip: true, shirt: '#ff5a5f' }) + bubble(300, 90, 300, 'Souhlasím!', 40, 'l') + P.check(840, 160, .9))],
};
fs.mkdirSync(OUT, { recursive: true });
for (const [k, [vb, f]] of Object.entries(SC)) fs.writeFileSync(`${OUT}${k}.svg`, f().replace('viewBox="0 0 1280 720" width="1280" height="720"', `viewBox="${vb}" width="720" height="720"`));
console.log(Object.keys(SC).join(' '));

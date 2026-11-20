// Ілюстрація для головної сторінки сайту (img/home/hero.svg): екзаменаторка, кандидат Daniel, картка результату.
const { T, txt, INK, EXA, DAN, P, bubble } = require('./kit.js');
const W = 640, H = 560;
const card = (x, y) => T(x, y, 1, -4, `
 <rect x="6" y="10" width="250" height="168" rx="22" fill="rgba(13,30,70,.25)"/>
 <rect width="250" height="168" rx="22" fill="#fff" stroke="${INK}" stroke-width="5"/>
 ${txt(26, 42, 'VÝSLEDEK', 22, '#59647a', 800, 'start')}
 ${txt(26, 98, '92', 56, INK, 900, 'start')}${txt(100, 98, '/ 110', 30, '#59647a', 800, 'start')}
 <rect x="26" y="116" width="198" height="14" rx="7" fill="#e3ebf8"/><rect x="26" y="116" width="166" height="14" rx="7" fill="#22b14c"/>
 <g transform="translate(206,58)"><circle r="30" fill="#22b14c"/><path d="M-13 0 l9 10 l17 -20" stroke="#fff" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>
 ${txt(26, 158, 'PROSPĚL ✓', 22, '#15803d', 900, 'start')}`);
const inner = `
 <defs><radialGradient id="hb" cx=".5" cy=".55" r=".55"><stop offset="0" stop-color="#ffffff" stop-opacity=".22"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient></defs>
 <circle cx="330" cy="300" r="260" fill="url(#hb)"/>
 <circle cx="330" cy="310" r="205" fill="#2b63c4" opacity=".55"/>
 ${P.flag(60, 50, .55)}
 ${EXA(190, 236, { s: .95, arms: 'hold', mouth: 'smile' })}
 ${DAN(455, 236, { s: .95, arms: 'wave', mouth: 'open', flip: true })}
 <rect x="70" y="400" width="500" height="30" rx="12" fill="#8a5a2b"/><rect x="100" y="430" width="22" height="110" fill="#8a5a2b"/><rect x="518" y="430" width="22" height="110" fill="#8a5a2b"/>
 ${P.nameplate(70, 400, 'ZKOUŠKA A2')}
 ${bubble(330, 40, 250, 'Dobrý den!', 34, 'r')}
 ${card(360, 400 - 250)}
`;
// картку ставимо праворуч знизу поверх столу
const out = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="">${inner.replace(card(360, 150), '')}${T(0, 0, 1, 0, card(360, 392))}</svg>`;
require('fs').writeFileSync(process.argv[2] || '../../img/home/hero.svg', out);
console.log('ok', out.length);

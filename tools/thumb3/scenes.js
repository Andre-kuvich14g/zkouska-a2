// Мультяшні сцени (власні SVG-ілюстрації) для обкладинок.
const person = (x, y, s, skin, hair, shirt, flip, mouth = 'smile') => `
<g transform="translate(${x},${y}) scale(${flip ? -s : s},${s})">
 <ellipse cx="0" cy="190" rx="70" ry="14" fill="rgba(0,0,0,.18)"/>
 <path d="M-55 180 Q-60 70 0 62 Q60 70 55 180 Z" fill="${shirt}"/>
 <path d="M-55 120 Q-90 140 -78 175" stroke="${shirt}" stroke-width="26" stroke-linecap="round" fill="none"/>
 <path d="M52 110 Q95 80 100 40" stroke="${shirt}" stroke-width="26" stroke-linecap="round" fill="none"/>
 <circle cx="100" cy="34" r="16" fill="${skin}"/>
 <rect x="-14" y="38" width="28" height="30" rx="10" fill="${skin}"/>
 <circle cx="0" cy="0" r="52" fill="${skin}"/>
 <path d="M-54 -6 Q-56 -62 0 -60 Q58 -62 54 -8 Q40 -40 0 -38 Q-38 -40 -54 -6Z" fill="${hair}"/>
 <circle cx="-18" cy="2" r="6.5" fill="#1d2433"/><circle cx="18" cy="2" r="6.5" fill="#1d2433"/>
 <circle cx="-16" cy="0" r="2.2" fill="#fff"/><circle cx="20" cy="0" r="2.2" fill="#fff"/>
 <circle cx="-32" cy="18" r="8" fill="#ff8a8a" opacity=".55"/><circle cx="32" cy="18" r="8" fill="#ff8a8a" opacity=".55"/>
 ${mouth === 'open' ? '<path d="M-14 24 Q0 44 14 24 Z" fill="#7a1f2b"/>' : '<path d="M-14 24 Q0 36 14 24" stroke="#7a1f2b" stroke-width="5" fill="none" stroke-linecap="round"/>'}
</g>`;
const bubble = (x, y, w, txt, fs = 40, tail = 'l') => `
<g transform="translate(${x},${y})"><rect x="0" y="0" width="${w}" height="${fs + 40}" rx="${(fs + 40) / 2}" fill="#fff" stroke="#1d2433" stroke-width="5"/>
<path d="M${tail === 'l' ? 40 : w - 70} ${fs + 37} l${tail === 'l' ? -18 : 48} 34 l${tail === 'l' ? 48 : -18} -34" fill="#fff" stroke="#1d2433" stroke-width="5" stroke-linejoin="round"/>
<rect x="${tail === 'l' ? 26 : w - 84}" y="${fs + 30}" width="58" height="10" fill="#fff"/>
<text x="${w / 2}" y="${fs + 8}" text-anchor="middle" font-family="Inter,sans-serif" font-weight="900" font-size="${fs}" fill="#1d2433">${txt}</text></g>`;

const beach = () => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#39b6ff"/><stop offset="1" stop-color="#bdeaff"/></linearGradient>
<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14a3d6"/><stop offset="1" stop-color="#0b7fb5"/></linearGradient>
<linearGradient id="sand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe08a"/><stop offset="1" stop-color="#f5c451"/></linearGradient></defs>
<rect width="1280" height="720" fill="url(#sky)"/>
<g transform="translate(1110,120)"><circle r="70" fill="#ffd93b"/><circle r="96" fill="#ffd93b" opacity=".25"/></g>
<g fill="#fff" opacity=".95"><ellipse cx="560" cy="110" rx="90" ry="34"/><ellipse cx="620" cy="92" rx="60" ry="38"/><ellipse cx="880" cy="170" rx="70" ry="26"/><ellipse cx="925" cy="156" rx="46" ry="30"/></g>
<path d="M0 360 Q160 340 320 360 T640 360 T960 360 T1280 360 V470 H0Z" fill="url(#sea)"/>
<path d="M0 395 Q80 385 160 395 T320 395 T480 395 T640 395 T800 395 T960 395 T1120 395 T1280 395" stroke="#fff" stroke-width="6" fill="none" opacity=".6"/>
<path d="M0 440 Q90 430 180 440 T360 440 T540 440 T720 440 T900 440 T1080 440 T1280 440" stroke="#fff" stroke-width="5" fill="none" opacity=".45"/>
<path d="M0 470 Q300 430 640 455 Q980 480 1280 445 V720 H0Z" fill="url(#sand)"/>
<g transform="translate(1200,470)"><path d="M0 0 Q-20 -160 10 -300" stroke="#8a5a2b" stroke-width="26" fill="none" stroke-linecap="round"/>
<g fill="#22b14c"><path d="M10 -300 Q-90 -340 -160 -280 Q-80 -300 10 -300Z"/><path d="M10 -300 Q100 -350 170 -290 Q90 -305 10 -300Z"/><path d="M10 -300 Q-40 -390 -110 -400 Q-30 -360 10 -300Z"/><path d="M10 -300 Q70 -400 140 -390 Q60 -360 10 -300Z"/><path d="M10 -300 Q-120 -260 -150 -190 Q-80 -260 10 -300Z" fill="#1a9a40"/></g>
<circle cx="-4" cy="-292" r="13" fill="#7a4a1d"/><circle cx="18" cy="-288" r="13" fill="#7a4a1d"/></g>
<g transform="translate(850,560)"><path d="M0 0 L-12 -250" stroke="#5a4636" stroke-width="10"/>
<path d="M-180 -230 Q-12 -360 160 -250 Z" fill="#ff5a5f"/><path d="M-130 -258 Q-80 -320 -12 -340 Q-60 -300 -70 -245Z" fill="#fff"/><path d="M40 -248 Q60 -310 -12 -340 Q80 -320 110 -255Z" fill="#fff"/></g>
<rect x="680" y="585" width="230" height="22" rx="11" fill="#2f80ed" transform="rotate(-4 790 596)"/>
<g transform="translate(1000,630)"><circle r="34" fill="#fff"/><path d="M-34 0 A34 34 0 0 1 34 0Z" fill="#ff5a5f"/><circle r="8" fill="#ffd93b"/></g>
${person(660, 430, 1.05, '#f6c7a1', '#5b3a1e', '#ff7a3d', false, 'open')}
${person(1050, 440, 1.0, '#e9b48f', '#1d2433', '#2bb673', true)}
${bubble(560, 200, 240, 'Kam?', 54, 'r')}
${bubble(930, 225, 250, 'K moři!', 46, 'l')}
</svg>`;

const listen = () => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720">
<defs><radialGradient id="g" cx=".7" cy=".4" r=".8"><stop offset="0" stop-color="#ff7ab6"/><stop offset="1" stop-color="#7a0f45"/></radialGradient></defs>
<rect width="1280" height="720" fill="url(#g)"/>
<g fill="none" stroke="#ffd93b" stroke-width="14" stroke-linecap="round" opacity=".9">
<path d="M1120 250 Q1170 330 1120 410"/><path d="M1160 210 Q1240 330 1160 450"/><path d="M640 250 Q590 330 640 410"/><path d="M600 210 Q520 330 600 450"/></g>
<g fill="#fff" opacity=".9"><text x="560" y="170" font-size="90" font-family="Inter" font-weight="900">♪</text><text x="1160" y="150" font-size="70" font-family="Inter" font-weight="900">♫</text><text x="1190" y="560" font-size="80" font-family="Inter" font-weight="900">♪</text></g>
<rect x="640" y="560" width="520" height="40" rx="14" fill="#5a2b14"/><rect x="680" y="600" width="26" height="120" fill="#5a2b14"/><rect x="1094" y="600" width="26" height="120" fill="#5a2b14"/>
<g transform="translate(900,330)">
 <ellipse cx="0" cy="230" rx="120" ry="18" fill="rgba(0,0,0,.2)"/>
 <path d="M-110 230 Q-120 90 0 80 Q120 90 110 230 Z" fill="#2f80ed"/>
 <rect x="-18" y="50" width="36" height="40" rx="12" fill="#f6c7a1"/>
 <circle cx="0" cy="0" r="74" fill="#f6c7a1"/>
 <path d="M-76 -8 Q-78 -88 0 -86 Q80 -88 76 -10 Q56 -54 0 -52 Q-54 -54 -76 -8Z" fill="#7a3b12"/>
 <path d="M-92 0 Q-96 -120 0 -118 Q96 -120 92 0" stroke="#1d2433" stroke-width="18" fill="none"/>
 <rect x="-118" y="-22" width="42" height="72" rx="18" fill="#1d2433"/><rect x="76" y="-22" width="42" height="72" rx="18" fill="#1d2433"/>
 <rect x="-110" y="-12" width="26" height="52" rx="12" fill="#ffd93b"/><rect x="84" y="-12" width="26" height="52" rx="12" fill="#ffd93b"/>
 <path d="M-26 0 Q-18 -10 -10 0" stroke="#1d2433" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M10 0 Q18 -10 26 0" stroke="#1d2433" stroke-width="6" fill="none" stroke-linecap="round"/>
 <circle cx="-42" cy="22" r="11" fill="#ff8a8a" opacity=".55"/><circle cx="42" cy="22" r="11" fill="#ff8a8a" opacity=".55"/>
 <path d="M-18 30 Q0 46 18 30" stroke="#7a1f2b" stroke-width="6" fill="none" stroke-linecap="round"/>
 <rect x="-150" y="180" width="160" height="56" rx="8" fill="#fff" transform="rotate(-6)"/><path d="M-130 196 h110 M-130 214 h80" stroke="#9aa4b8" stroke-width="6" transform="rotate(-6)"/>
 <path d="M60 150 L160 210" stroke="#ffd93b" stroke-width="14" stroke-linecap="round"/>
</g></svg>`;

const mail = () => `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720">
<defs><linearGradient id="w" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9f7e6"/><stop offset="1" stop-color="#9fe3bd"/></linearGradient></defs>
<rect width="1280" height="720" fill="url(#w)"/>
<rect x="980" y="70" width="220" height="170" rx="12" fill="#fff" stroke="#1d2433" stroke-width="6"/><path d="M1090 70 V240 M980 155 H1200" stroke="#1d2433" stroke-width="6"/>
<g transform="translate(640,110) rotate(-10)"><rect width="250" height="170" rx="16" fill="#fff" stroke="#1d2433" stroke-width="6"/><path d="M0 8 L125 100 L250 8" stroke="#1d2433" stroke-width="6" fill="none"/><circle cx="235" cy="10" r="34" fill="#ff5a5f"/><text x="235" y="23" text-anchor="middle" font-family="Inter" font-weight="900" font-size="38" fill="#fff">1</text></g>
<rect x="600" y="560" width="680" height="40" rx="12" fill="#8a5a2b"/><rect x="640" y="600" width="26" height="120" fill="#8a5a2b"/><rect x="1210" y="600" width="26" height="120" fill="#8a5a2b"/>
<g transform="translate(910,250)">
 <path d="M-110 210 Q-120 70 0 60 Q120 70 110 210 Z" fill="#ff7a3d"/>
 <rect x="-18" y="30" width="36" height="40" rx="12" fill="#e9b48f"/><circle cx="0" cy="-20" r="72" fill="#e9b48f"/>
 <path d="M-74 -26 Q-76 -104 0 -102 Q78 -104 74 -28 Q56 -70 0 -68 Q-54 -70 -74 -26Z" fill="#1d2433"/>
 <circle cx="-24" cy="-14" r="8" fill="#1d2433"/><circle cx="24" cy="-14" r="8" fill="#1d2433"/><circle cx="-21" cy="-17" r="3" fill="#fff"/><circle cx="27" cy="-17" r="3" fill="#fff"/>
 <circle cx="-44" cy="8" r="11" fill="#ff8a8a" opacity=".55"/><circle cx="44" cy="8" r="11" fill="#ff8a8a" opacity=".55"/>
 <path d="M-20 14 Q0 34 20 14 Z" fill="#7a1f2b"/></g>
<g transform="translate(700,330)"><rect x="0" y="0" width="420" height="250" rx="18" fill="#1d2433"/><rect x="16" y="16" width="388" height="200" rx="10" fill="#fff"/>
<text x="36" y="62" font-family="Inter" font-weight="900" font-size="34" fill="#0f8a43">Dobrý den,</text>
<path d="M36 100 h300 M36 136 h250 M36 172 h280" stroke="#b8c2d6" stroke-width="12" stroke-linecap="round"/>
<rect x="290" y="160" width="100" height="44" rx="22" fill="#0f8a43"/><text x="340" y="191" text-anchor="middle" font-family="Inter" font-weight="900" font-size="24" fill="#fff">Odeslat</text>
<path d="M150 250 h120 l30 30 h-180 Z" fill="#3a4256"/></g>
<g transform="translate(1180,420)"><circle r="56" fill="#22b14c"/><path d="M-26 0 l18 20 l34 -40" stroke="#fff" stroke-width="14" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>
</svg>`;
module.exports = { beach, listen, mail };

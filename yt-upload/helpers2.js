window.__R=window.__R||'https://raw.githubusercontent.com/Andre-kuvich14g/zkouska-a2/main/yt-upload/';
window.__sleep=ms=>new Promise(r=>setTimeout(r,ms));
window.__set=(el,text)=>{ el.textContent=text; el.dispatchEvent(new InputEvent('input',{bubbles:true,inputType:'insertText',data:text})); el.dispatchEvent(new Event('change',{bubbles:true})); el.dispatchEvent(new Event('blur',{bubbles:true})); };
window.__A=async(id)=>{ const R=window.__R, m=window.__M[id];
  for(let i=0;i<20 && !document.querySelector('input[name=Filedata]');i++) await window.__sleep(500);
  const b=await (await fetch(R+id+'.mp4')).blob(); const el=document.querySelector('input[name=Filedata]'); const dt=new DataTransfer(); dt.items.add(new File([b],id+'.mp4',{type:'video/mp4'})); el.files=dt.files; el.dispatchEvent(new Event('change',{bubbles:true}));
  for(let i=0;i<30 && document.querySelectorAll('ytcp-uploads-dialog #textbox').length<2;i++) await window.__sleep(500);
  await window.__sleep(3000);
  let tb=[...document.querySelectorAll('ytcp-uploads-dialog #textbox')]; window.__set(tb[0], m.title); await window.__sleep(400); window.__set(tb[1], m.desc); await window.__sleep(800);
  const ti=[...document.querySelectorAll('ytcp-uploads-dialog input[type=file]')].find(e=>/image/.test(e.accept)); let ir=await fetch(R+id+'.jpg'); if(!ir.ok) ir=await fetch(R+'thumb3/'+id+'.jpg'); if(!ir.ok) throw 'NO THUMBNAIL '+id+' — add yt-upload/'+id+'.jpg (style: ab2/out3)'; const ib=await ir.blob(); if(ib.size<20000) throw 'BAD THUMBNAIL '+id; const d2=new DataTransfer(); d2.items.add(new File([ib],id+'.jpg',{type:'image/jpeg'})); ti.files=d2.files; ti.dispatchEvent(new Event('change',{bubbles:true})); await window.__sleep(1500);
  const d=document.querySelector('ytcp-uploads-dialog'); d.querySelector('#toggle-button')?.click(); await window.__sleep(1200);
  for (const n of ['VIDEO_HAS_ALTERED_CONTENT_NO','VIDEO_MADE_FOR_KIDS_NOT_MFK','VIDEO_PAID_PRODUCT_PLACEMENT_NO']) { const x=d.querySelector(`tp-yt-paper-radio-button[name=${n}]`); if(x && x.offsetParent && x.getAttribute('aria-checked')!=='true') x.click(); }
  tb=[...document.querySelectorAll('ytcp-uploads-dialog #textbox')]; return [tb[0].innerText.slice(0,45), tb[1].innerText.length]; };
window.__tags=async(txt)=>{ const i=document.querySelector('ytcp-uploads-dialog input[aria-label="Теги"]'); for (const t of txt.split(',').map(s=>s.trim()).filter(Boolean)) { i.value=t; i.dispatchEvent(new Event('input',{bubbles:true})); i.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',code:'Enter',keyCode:13,which:13,bubbles:true})); await window.__sleep(150);} return [...document.querySelectorAll('ytcp-uploads-dialog ytcp-chip')].length; };
window.__B=async(id)=>{ const d=document.querySelector('ytcp-uploads-dialog'); const trg=d.querySelector('ytcp-video-metadata-playlists ytcp-text-dropdown-trigger'); trg.scrollIntoView({block:'center'}); trg.click(); await window.__sleep(2500); const r=await window.__plOnly(id); const n=await window.__tags(window.__M[id].tags); return [r, n]; };
window.__C=async()=>{ const d=document.querySelector('ytcp-uploads-dialog'); for(let i=0;i<3 && !d.querySelector('tp-yt-paper-radio-button[name=PUBLIC]')?.offsetParent;i++){ d.querySelector('#next-button').click(); await window.__sleep(2500); } const pub=d.querySelector('tp-yt-paper-radio-button[name=PUBLIC]'); pub.click(); await window.__sleep(800); return [pub.getAttribute('aria-checked'), d.querySelector('.progress-label, ytcp-video-upload-progress')?.innerText?.trim(), (d.innerText.match(/https:\/\/youtu\.be\/[\w-]+/)||[''])[0]]; };
window.__D=async()=>{ const d=document.querySelector('ytcp-uploads-dialog'); d.querySelector('#done-button').click(); await window.__sleep(5000); const sd=[...document.querySelectorAll('ytcp-video-share-dialog')].find(x=>x.offsetParent); return sd?.innerText.slice(0,80).replace(/\n/g,' | '); };

// 06.11: 6 playlists, one per úloha. Pick by checkbox test-id (= playlist id), read state via .checked
window.__PL={f:'PLUQqjJU0hPfs',p:'PLEbZM6bcfLsA',m:'PLMPSqjkk5Axw',d:'PLZ9QkvIdNGFg',v:'PLQZcneUaebBI',r:'PLK-4mNG0zlrk'};
window.__plOnly=async(id)=>{ const pid=window.__PL[id[0]]; const cbs=[...document.querySelectorAll('ytcp-checkbox-lit[test-id^="PL"]')].filter(c=>c.offsetParent); for(const c of cbs){ const want=c.getAttribute('test-id').startsWith(pid); if(!!c.checked!==want){ c.click(); await window.__sleep(600);} } const host=cbs[0]?.closest('ytcp-playlist-dialog'); [...(host?.querySelectorAll('ytcp-button')||[])].find(x=>x.offsetParent && x.innerText.trim()==='Готово')?.click(); await window.__sleep(1200); return document.querySelector('ytcp-video-metadata-playlists')?.innerText.trim(); };

window.__PL.o='PLROyJEw4bAqA';

// NOTE 13.11: #done-button JS click leaves video as DRAFT. Publish via real click (find 'Опублікувати' ref) or __pubPrep + click.

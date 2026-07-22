
const nav=document.getElementById('nav');
addEventListener('scroll',()=>nav.classList.toggle('scrolled',scrollY>20),{passive:true});
const mnav=document.getElementById('mnav');
document.getElementById('burger').onclick=()=>mnav.classList.add('open');
document.getElementById('mclose').onclick=()=>mnav.classList.remove('open');
mnav.querySelectorAll('a').forEach(a=>a.onclick=()=>mnav.classList.remove('open'));
const io=new IntersectionObserver((es)=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}}),{threshold:.12});
document.querySelectorAll('.rev,.cards,.values,.reasons,.team-grid,.stats,.approach,.tst').forEach(el=>io.observe(el));
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const cio=new IntersectionObserver((es)=>es.forEach(e=>{if(e.isIntersecting){count(e.target);cio.unobserve(e.target);}}),{threshold:.5});
document.querySelectorAll('.stat .n,.wstat .n[data-to]').forEach(n=>cio.observe(n));
function count(el){const to=+el.dataset.to;if(isNaN(to))return;const v=el.querySelector('.v')||el;const suf=el.querySelector('.v')?'':(el.dataset.suf||'');
  if(reduce){v.textContent=to+suf;return;}const dur=1200,t0=performance.now();
  (function tick(t){const p=Math.min(1,(t-t0)/dur);const e=1-Math.pow(1-p,3);v.textContent=Math.round(to*e)+suf;if(p<1)requestAnimationFrame(tick);})(performance.now());}
/* hero parallax */
(function(){const c=document.getElementById('heroCar');if(!c)return;
const im=Array.from(c.querySelectorAll('img'));
let i=Math.floor(Math.random()*im.length);
im.forEach(x=>x.classList.remove('on'));im[i].classList.add('on');
setInterval(()=>{let n;do{n=Math.floor(Math.random()*im.length)}while(n===i&&im.length>1);
im[i].classList.remove('on');i=n;im[i].classList.add('on');},5200);
addEventListener('scroll',()=>{c.style.transform='translateY('+(Math.min(scrollY,700)*0.2)+'px)';},{passive:true});})();

/* scroll progress */
(function(){const sb=document.getElementById('scrollbar');if(!sb)return;addEventListener('scroll',()=>{const h=document.documentElement;sb.style.transform='scaleX('+(h.scrollTop/((h.scrollHeight-h.clientHeight)||1))+')';},{passive:true});})();
/* gallery lightbox */
(function(){
  const tiles=[...document.querySelectorAll('.galtile')];if(!tiles.length)return;
  const lb=document.getElementById('lightbox'),img=document.getElementById('lbImg'),prev=document.getElementById('lbPrev'),next=document.getElementById('lbNext'),cl=document.getElementById('lbClose');
  const urls=tiles.map(t=>t.querySelector('img').getAttribute('src'));let i=0;const show=()=>img.src=urls[i];
  tiles.forEach((t,k)=>t.onclick=()=>{i=k;show();lb.classList.add('open');});
  prev.onclick=e=>{e.stopPropagation();i=(i-1+urls.length)%urls.length;show();};
  next.onclick=e=>{e.stopPropagation();i=(i+1)%urls.length;show();};
  cl.onclick=()=>lb.classList.remove('open');lb.onclick=e=>{if(e.target===lb)lb.classList.remove('open');};
  addEventListener('keydown',e=>{if(!lb.classList.contains('open'))return;if(e.key==='Escape')lb.classList.remove('open');if(e.key==='ArrowLeft')prev.click();if(e.key==='ArrowRight')next.click();});
})();

/* ===== FORM SENDING — Netlify Forms (no backend script, no Google) =====
   The site deploys from your GitHub repo to Netlify. Netlify detects the
   hidden form definition below in the HTML and handles submissions natively:
   notifications go to ANY email (Gmail now, Outlook later) – set it once in
   Netlify: Site → Forms → Notifications. Photos arrive as download links.
   See NETLIFY-OPPSETT.md. */
function validEmail(e){return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e);}
async function sendForm(o){
  if(location.protocol==='file:'){o.set('Skjemaet fungerer når siden er publisert – ikke når filen åpnes lokalt.','err');return;}
  const files=o.fileInput&&o.fileInput.files?[...o.fileInput.files]:[];
  if(!o.name||!o.email){o.set('Fyll inn navn og e-post.','err');return;}
  if(!validEmail(o.email)){o.set('Skriv inn en gyldig e-post.','err');return;}
  if(files.length>10){o.set('Du kan legge ved maks 10 bilder.','err');return;}
  let tot=0;files.forEach(f=>tot+=f.size);
  if(tot>9*1024*1024){o.set('Bildene er for store til sammen (maks ca. 9 MB).','err');return;}
  const fd=new FormData();
  fd.append('form-name','tilbud');
  fd.append('kundetype',o.ptype||'-');
  fd.append('navn',o.name);
  fd.append('epost',o.email);
  fd.append('telefon',o.phone||'-');
  fd.append('adresse',o.addr||'-');
  fd.append('melding',o.msg||'-');
  files.forEach((f,i)=>fd.append('bilde'+(i+1),f,f.name));
  try{
    o.btn.disabled=true;o.set(files.length?'Laster opp bilder …':'Sender …');
    const r=await fetch('/',{method:'POST',body:fd});
    if(r.ok){o.set('Takk! Meldingen er sendt. Vi svarer raskt.','ok');o.clear&&o.clear();}
    else{o.set('Noe gikk galt ('+r.status+'). Prøv igjen, eller ring +47 915 76 447.','err');}
  }catch(e){o.set('Fikk ikke kontakt. Sjekk nettforbindelsen og prøv igjen.','err');}
  finally{o.btn.disabled=false;}
}
function fileHint(input,hint){if(!input||!hint)return;input.onchange=()=>{const n=input.files.length;hint.textContent=n?(n+' bilde'+(n>1?'r':'')+' valgt'+(n>10?' – maks 10!':'')):'';};}

/* contact page form */
(function(){
  const send=document.getElementById('fsend');if(!send)return;
  const g=id=>(document.getElementById(id)||{value:''}).value.trim();
  const st=document.getElementById('fstatus');const set=(m,t)=>{st.textContent=m;st.className='fstatus '+(t||'');};
  const fi=document.getElementById('f-files');fileHint(fi,document.getElementById('f-hint'));
  send.onclick=()=>sendForm({name:g('f-name'),email:g('f-email'),phone:g('f-phone'),addr:g('f-addr'),msg:g('f-msg'),fileInput:fi,btn:send,set,
    clear:()=>{['f-name','f-email','f-phone','f-addr','f-msg'].forEach(i=>{const e=document.getElementById(i);if(e)e.value='';});if(fi)fi.value='';const h=document.getElementById('f-hint');if(h)h.textContent='';}});
})();

/* floating Be om tilbud pod */
(function(){
  const pod=document.getElementById('pod'),btn=document.getElementById('podBtn');if(!pod||!btn)return;
  const open=()=>{pod.classList.add('open');btn.setAttribute('aria-expanded','true');const n=document.getElementById('pf-name');if(n)setTimeout(()=>n.focus(),60);};
  const close=()=>{pod.classList.remove('open');btn.setAttribute('aria-expanded','false');};
  btn.onclick=()=>pod.classList.contains('open')?close():open();
  document.addEventListener('click',e=>{if(pod.classList.contains('open')&&!pod.contains(e.target))close();});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&pod.classList.contains('open'))close();});
  const pseg=document.getElementById('pseg');let ptype='privat';
  if(pseg)[...pseg.children].forEach(bb=>bb.onclick=()=>{ptype=bb.dataset.type;[...pseg.children].forEach(x=>x.classList.toggle('on',x===bb));});
  const st=document.getElementById('pf-status');const set=(m,t)=>{if(st){st.textContent=m;st.className='pstatus '+(t||'');}};
  const g=id=>(document.getElementById(id)||{value:''}).value.trim();
  const pf=document.getElementById('pf-files');fileHint(pf,document.getElementById('pf-hint'));
  const send=document.getElementById('pf-send');
  if(send)send.onclick=()=>sendForm({name:g('pf-name'),email:g('pf-email'),phone:g('pf-phone'),addr:g('pf-addr'),msg:g('pf-msg'),ptype:ptype==='bedrift'?'Bedrift':'Privat',fileInput:pf,btn:send,set,
    clear:()=>{['pf-name','pf-email','pf-phone','pf-addr','pf-msg'].forEach(i=>{const e=document.getElementById(i);if(e)e.value='';});if(pf)pf.value='';const h=document.getElementById('pf-hint');if(h)h.textContent='';}});
})();

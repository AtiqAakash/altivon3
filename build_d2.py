#!/usr/bin/env python3
# Altivon Design 2 (DroneTjek-style, green/white) — clean multi-page build.
import os, re
OUT='/home/claude/design2'
os.makedirs(OUT+'/assets',exist_ok=True)
for f in os.listdir(OUT):
    if f.endswith('.html'): os.remove(os.path.join(OUT,f))

CSS=r'''
:root{
  --bg:#ffffff;--bg-alt:#f3f9f5;--line:#e6efe9;--line2:#d6e5dc;
  --ink:#0c1f17;--muted:#586f66;--faint:#8a9a92;
  --green:#12b06a;--green-d:#0d9c5e;--green-dd:#0a3527;--green-soft:#e7f6ee;--green-glow:rgba(18,176,106,.22);
  --r:16px;--r-lg:24px;--ease:cubic-bezier(.4,0,.15,1);
  --disp:'Space Grotesk',sans-serif;--body:'Inter',sans-serif;--wrap:1180px;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:var(--body);background:var(--bg);color:var(--ink);line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
h1,h2,h3,h4{font-family:var(--disp);font-weight:600;line-height:1.12;letter-spacing:-.02em;color:var(--ink)}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 28px}
.btn{display:inline-flex;align-items:center;gap:9px;font-family:var(--disp);font-weight:600;font-size:.96rem;padding:.85rem 1.5rem;border-radius:100px;transition:.3s var(--ease);cursor:pointer;border:1px solid transparent;white-space:nowrap;position:relative;overflow:hidden}
.btn svg{width:16px;height:16px}
.btn-primary{background:var(--green);color:#fff}
.btn-primary:hover{background:var(--green-d);transform:translateY(-2px);box-shadow:0 14px 30px -12px var(--green)}
.btn-primary::after{content:"";position:absolute;top:0;left:-130%;width:55%;height:100%;background:linear-gradient(120deg,transparent,rgba(255,255,255,.35),transparent);transform:skewX(-20deg);transition:left .7s var(--ease)}
.btn-primary:hover::after{left:150%}
.btn-ghost{background:transparent;color:var(--ink);border-color:var(--line2)}
.btn-ghost:hover{background:var(--green-soft);border-color:var(--green);color:var(--green-dd)}
.btn-white{background:#fff;color:var(--green-dd)}.btn-white:hover{transform:translateY(-2px);box-shadow:0 16px 34px -16px rgba(0,0,0,.4)}
.eyebrow{display:inline-flex;align-items:center;gap:9px;font-family:var(--disp);font-weight:600;font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--green)}
.eyebrow::before{content:"";width:24px;height:2px;background:var(--green);border-radius:2px}
.eyebrow.c{justify-content:center}

/* nav */
.nav{position:fixed;top:0;left:0;right:0;z-index:100;transition:.4s var(--ease);background:rgba(255,255,255,.93);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.nav-in{max-width:var(--wrap);margin:0 auto;padding:20px 28px;display:flex;align-items:center;justify-content:space-between;transition:.4s var(--ease)}
.nav.scrolled{background:rgba(255,255,255,.9);backdrop-filter:blur(14px);border-bottom:1px solid var(--line);box-shadow:0 8px 26px -22px rgba(10,53,39,.5)}
.nav.scrolled .nav-in{padding-top:13px;padding-bottom:13px}
.brand img{height:26px;width:auto}
.nav-links{display:flex;gap:4px;align-items:center}
.nav-links a{font-size:.94rem;color:var(--muted);padding:.5rem .9rem;border-radius:9px;transition:.25s}
.nav-links a:hover,.nav-links a.on{color:var(--ink);background:var(--green-soft)}
.nav-cta{display:flex;align-items:center;gap:12px}
.burger{display:none;background:none;border:0;width:40px;height:40px;color:var(--ink);cursor:pointer}
.burger svg{width:26px;height:26px}
@media(max-width:960px){.nav-links,.nav-cta .btn{display:none}.burger{display:flex;align-items:center;justify-content:center}}
.mnav{position:fixed;inset:0;z-index:120;background:#fff;display:flex;flex-direction:column;justify-content:center;gap:6px;padding:40px;transform:translateY(-100%);transition:.45s var(--ease);opacity:0}
.mnav.open{transform:none;opacity:1}
.mnav a{font-family:var(--disp);font-size:1.5rem;font-weight:600;color:var(--ink);padding:.5rem 0;border-bottom:1px solid var(--line)}
.mnav .btn{margin-top:22px;justify-content:center}
.mnav-close{position:absolute;top:26px;right:26px;background:none;border:0;color:var(--ink);font-size:2rem;cursor:pointer;line-height:1}

/* hero — photo fading into white */
.hero{padding:170px 0 130px;overflow:hidden;position:relative;background:#fff}
.hero-bg{position:absolute;inset:0;z-index:0;overflow:hidden}
.hero-bg img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.05);transition:opacity 1.5s var(--ease),transform 7s linear}
.hero-bg img.on{opacity:1;transform:scale(1.12)}
.hero-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,53,39,.62) 0%,rgba(10,53,39,.4) 36%,rgba(255,255,255,.25) 76%,#ffffff 97%)}
.hero-inner{position:relative;z-index:1;text-align:center;max-width:940px;margin:0 auto}
.hero .eyebrow{color:#a9f5cf}.hero .eyebrow::before{background:#a9f5cf}
.hero h1{font-size:clamp(2.4rem,6vw,4.8rem);letter-spacing:-.03em;margin:22px 0 0;color:#fff;text-shadow:0 2px 26px rgba(10,53,39,.5)}
.hero h1 .g{color:#7df0b6}
.hero .sub{color:rgba(255,255,255,.96);font-size:1.14rem;max-width:58ch;margin:26px auto 36px;text-shadow:0 1px 16px rgba(10,53,39,.55)}
.hero-actions{display:flex;gap:14px;flex-wrap:wrap;justify-content:center}
.hero .btn-ghost{color:#fff;border-color:rgba(255,255,255,.55)}
.hero .btn-ghost:hover{background:rgba(255,255,255,.16);border-color:#fff;color:#fff}
.hero-inner>*{opacity:0;transform:translateY(22px);animation:heroup .8s var(--ease) forwards}
.hero-inner>*:nth-child(2){animation-delay:.12s}.hero-inner>*:nth-child(3){animation-delay:.24s}.hero-inner>*:nth-child(4){animation-delay:.36s}
@keyframes heroup{to{opacity:1;transform:none}}
@media(max-width:700px){.hero{padding:128px 0 84px}}

/* page hero */
.page-hero{background:var(--green-soft);padding:150px 0 56px;text-align:center;position:relative;overflow:hidden}
.page-hero::before{content:"";position:absolute;top:-30%;left:50%;transform:translateX(-50%);width:700px;height:460px;background:radial-gradient(ellipse,var(--green-glow),transparent 62%);pointer-events:none}
.page-hero .wrap{position:relative;z-index:1}
.page-hero .ph-bg{position:absolute;inset:0;z-index:0;overflow:hidden}
.page-hero .ph-bg img{width:100%;height:100%;object-fit:cover;opacity:.5}
.page-hero .ph-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(231,246,238,.3),rgba(243,249,245,.72))}
.page-hero h1{font-size:clamp(2.3rem,5.4vw,3.9rem)}
.page-hero h1 .g{color:var(--green)}
.page-hero p{color:var(--muted);font-size:1.14rem;max-width:56ch;margin:20px auto 0}
.crumb{display:inline-flex;gap:8px;align-items:center;font-family:var(--disp);font-size:.74rem;letter-spacing:.1em;text-transform:uppercase;color:var(--faint);margin-top:24px}
.crumb a{color:var(--green)}

/* sections */
.sec{padding:100px 0}
.sec-head{max-width:660px;margin-bottom:56px}
.sec-head.c{margin-left:auto;margin-right:auto;text-align:center}
.sec-head h2{font-size:clamp(1.9rem,4vw,3rem);margin:18px 0 0}
.sec-head p{color:var(--muted);font-size:1.1rem;margin-top:16px}
.alt{background:var(--bg-alt)}

/* cards */
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
@media(max-width:840px){.cards{grid-template-columns:1fr}}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:34px 30px;transition:.35s var(--ease)}
.card:hover{transform:translateY(-6px);box-shadow:0 34px 66px -38px rgba(18,176,106,.45);border-color:var(--green)}
.card .ico{width:54px;height:54px;border-radius:14px;background:var(--green-soft);display:flex;align-items:center;justify-content:center;margin-bottom:22px;transition:.35s var(--ease)}
.card .ico svg{width:26px;height:26px;color:var(--green);transition:.35s var(--ease)}
.card:hover .ico{background:var(--green);transform:scale(1.06) rotate(-3deg)}
.card:hover .ico svg{color:#fff}
.card .num{font-family:var(--disp);font-size:.8rem;color:var(--green);font-weight:700;letter-spacing:.1em;margin-bottom:8px}
.card h3{font-size:1.28rem;margin-bottom:12px}
.card p{color:var(--muted);font-size:.98rem}
.card .sub2{color:var(--ink);font-weight:600;margin-bottom:8px;font-size:.95rem}

/* comparison + hover */
.cmp{border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;margin-top:10px;background:#fff}
.cmp-row{display:grid;grid-template-columns:1fr 1fr;border-bottom:1px solid var(--line)}
.cmp-row:last-child{border-bottom:0}
.cmp-row.head .c{padding:22px 26px;font-family:var(--disp);font-weight:600;font-size:.98rem}
.cmp-row.head .c.us{color:var(--green-dd)}.cmp-row.head .c.them{color:var(--faint)}
.cmp .c{padding:18px 26px;display:flex;align-items:center;gap:12px;font-size:.98rem;transition:.28s var(--ease)}
.cmp .c.us{background:var(--green-soft);color:var(--ink)}.cmp .c.them{color:var(--muted)}
.cmp .c .ic{width:22px;height:22px;border-radius:50%;flex:0 0 auto;display:flex;align-items:center;justify-content:center;transition:.28s var(--ease)}
.cmp .c.us .ic{background:var(--green)}.cmp .c.them .ic{background:#dfe6e2}
.cmp .c .ic svg{width:13px;height:13px;color:#fff}.cmp .c.them .ic svg{color:#9aa8a1}
.cmp-row:not(.head):hover .c.us{background:var(--green);color:#fff;transform:translateX(2px)}
.cmp-row:not(.head):hover .c.us .ic{background:#fff}
.cmp-row:not(.head):hover .c.us .ic svg{color:var(--green)}
.cmp-row:not(.head):hover .c.them{background:#fbfdfc;color:var(--ink)}
@media(max-width:700px){
.cmp-row{grid-template-columns:1fr 1fr}
.cmp .c{padding:12px 10px;font-size:.82rem;line-height:1.35;gap:8px;align-items:flex-start}
.cmp .c svg{width:15px;height:15px;flex:none;margin-top:2px}
.cmp-row.head .c{padding:10px;font-size:.72rem}
}
.cmp-note{color:var(--muted);text-align:center;margin-top:26px;font-size:1.05rem}.cmp-note b{color:var(--green-dd)}

/* split rows */
.split{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;margin-top:70px}
.split.flip .split-media{order:2}
@media(max-width:840px){.split{grid-template-columns:1fr;gap:30px}.split.flip .split-media{order:0}}
.split-media{border-radius:var(--r-lg);overflow:hidden;aspect-ratio:4/3;max-height:420px;box-shadow:0 30px 60px -44px rgba(10,53,39,.4);border:1px solid var(--line)}
.split-media img,.split-media video{width:100%;height:100%;object-fit:cover;transition:transform .6s var(--ease)}
.split:hover .split-media img{transform:scale(1.05)}
.split h3{font-size:clamp(1.4rem,3vw,2rem);margin:14px 0 14px}
.split p{color:var(--muted);margin-bottom:18px}
.checks{list-style:none;display:grid;gap:12px}
.checks li{display:grid;grid-template-columns:auto 1fr;gap:12px;color:var(--ink);font-size:.98rem}
.checks li::before{content:"";width:22px;height:22px;border-radius:50%;background:var(--green);margin-top:1px;-webkit-mask:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3'><path d='M20 6 9 17l-5-5'/></svg>") center/13px no-repeat;mask:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3'><path d='M20 6 9 17l-5-5'/></svg>") center/13px no-repeat}

/* values */
.values{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;margin-top:50px}
@media(max-width:900px){.values{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.values{grid-template-columns:1fr}}
.value{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:28px;transition:.3s var(--ease)}
.value:hover{border-color:var(--green);transform:translateY(-4px);box-shadow:0 30px 60px -40px rgba(18,176,106,.4)}
.value .vn{font-family:var(--disp);font-weight:700;font-size:1.6rem;color:var(--green);opacity:.5}
.value h3{margin:12px 0 10px;font-size:1.16rem}
.value p{color:var(--muted);font-size:.94rem}

/* reasons */
.reasons{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;margin-top:44px}
@media(max-width:800px){.reasons{grid-template-columns:1fr}}
.reason{transition:.3s var(--ease)}
.reason .ico{width:52px;height:52px;border-radius:13px;background:var(--green-soft);display:flex;align-items:center;justify-content:center;margin-bottom:18px;transition:.35s var(--ease)}
.reason .ico svg{width:25px;height:25px;color:var(--green);transition:.35s var(--ease)}
.reason:hover .ico{background:var(--green);transform:scale(1.06) rotate(-3deg)}
.reason:hover .ico svg{color:#fff}
.reason h3{font-size:1.2rem;margin-bottom:8px}.reason p{color:var(--muted);font-size:.96rem}

/* who-we-are stats */
.wstats{display:grid;grid-template-columns:repeat(2,1fr);gap:26px 20px;margin-top:30px}
.wstat .n{font-family:var(--disp);font-weight:700;font-size:1.9rem;color:var(--green)}
.wstat .l{color:var(--muted);font-size:.92rem}

/* team */
.team-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:50px}
@media(max-width:800px){.team-grid{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.team-grid{grid-template-columns:1fr}}
.tcard{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;transition:.35s var(--ease)}
.tcard:hover{transform:translateY(-6px);box-shadow:0 30px 60px -42px rgba(10,53,39,.3)}
.tcard .ph{aspect-ratio:1/1;position:relative;background:var(--green-dd);overflow:hidden}
.tcard .ph .ini{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-family:var(--disp);font-weight:700;font-size:2.4rem;color:#fff}
.tcard .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:grayscale(1);transition:transform .55s var(--ease)}
.tcard:hover .ph img{transform:scale(1.06)}
.tcard .tb{padding:22px}
.tcard .role{font-family:var(--disp);font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;color:var(--green);margin-bottom:8px}
.tcard h3{font-size:1.16rem;margin-bottom:6px}
.tcard p{color:var(--muted);font-size:.9rem}
.tcard .tc{display:flex;gap:9px;margin-top:16px;padding-top:15px;border-top:1px solid var(--line)}
.tcard .tc a{width:34px;height:34px;border-radius:9px;background:var(--green-soft);display:flex;align-items:center;justify-content:center;color:var(--green);transition:.25s}
.tcard .tc a:hover{background:var(--green);color:#fff;transform:translateY(-2px)}
.tcard .tc svg{width:16px;height:16px}

/* cases */
.cases{display:grid;gap:26px;margin-top:50px}
.case{display:grid;grid-template-columns:1.05fr 1fr;border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;background:#fff;transition:.35s var(--ease)}
.case:hover{box-shadow:0 34px 70px -48px rgba(10,53,39,.4)}
.case:nth-child(even){grid-template-columns:1fr 1.05fr}
.case:nth-child(even) .ci{order:2}
@media(max-width:800px){.case,.case:nth-child(even){grid-template-columns:1fr}.case:nth-child(even) .ci{order:0}}
.case .ci{overflow:hidden;min-height:240px;max-height:360px;background:var(--green-dd);position:relative}
.case .ci img{width:100%;height:100%;max-height:360px;object-fit:cover;transition:transform .6s var(--ease)}
.case:hover .ci img{transform:scale(1.05)}
.case .ci::after{content:"";position:absolute;inset:0;background:linear-gradient(120deg,rgba(10,53,39,.32),transparent 60%);opacity:0;transition:.4s}
.case:hover .ci::after{opacity:1}
.case .cb{padding:38px}
.case .cat{font-family:var(--disp);font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--green);font-weight:600}
.case h3{font-size:1.5rem;margin:10px 0 12px}
.case>.cb>p{color:var(--muted)}
.metrics{display:flex;flex-wrap:wrap;gap:9px;margin:20px 0 22px}
.metric{background:var(--green-soft);color:var(--green-dd);border-radius:100px;padding:.4rem .85rem;font-size:.78rem;font-weight:600;font-family:var(--disp)}

/* gallery + lightbox */
.galgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:44px}
@media(max-width:900px){.galgrid{grid-template-columns:repeat(3,1fr)}}
@media(max-width:560px){.galgrid{grid-template-columns:repeat(2,1fr);gap:10px}}
.galtile{position:relative;aspect-ratio:1/1;overflow:hidden;border-radius:var(--r);cursor:pointer;background:var(--bg-alt);border:1px solid var(--line)}
.galtile img{width:100%;height:100%;object-fit:cover;transition:transform .5s var(--ease)}
.galtile:hover img{transform:scale(1.08)}
.galtile::after{content:"";position:absolute;inset:0;background:rgba(10,53,39,0);transition:.3s}
.galtile:hover::after{background:rgba(10,53,39,.16)}
.galtile .zoom{position:absolute;top:12px;right:12px;color:#fff;opacity:0;transition:.3s;z-index:2;filter:drop-shadow(0 1px 3px rgba(0,0,0,.5))}
.galtile:hover .zoom{opacity:1}
.galtile .cap{position:absolute;left:0;right:0;bottom:0;padding:14px;color:#fff;font-family:var(--disp);font-weight:600;font-size:.9rem;background:linear-gradient(transparent,rgba(10,53,39,.85));transform:translateY(100%);transition:.35s var(--ease);z-index:2}
.galtile:hover .cap{transform:none}
.lightbox{position:fixed;inset:0;z-index:500;background:rgba(8,20,15,.93);backdrop-filter:blur(6px);display:flex;align-items:center;justify-content:center;opacity:0;visibility:hidden;transition:.3s}
.lightbox.open{opacity:1;visibility:visible}
.lb-stage{position:relative;max-width:92vw;max-height:86vh;animation:pop .35s var(--ease)}
@keyframes pop{from{opacity:0;transform:scale(.96)}to{opacity:1;transform:none}}
.lb-stage img{max-width:92vw;max-height:86vh;border-radius:14px;box-shadow:0 30px 80px rgba(0,0,0,.6);display:block}
.lb-close{position:fixed;top:22px;right:26px;background:none;border:0;color:#fff;font-size:2.4rem;cursor:pointer;line-height:1;z-index:2}
.lb-nav{position:absolute;top:50%;transform:translateY(-50%);width:48px;height:48px;border-radius:50%;border:0;background:rgba(255,255,255,.15);color:#fff;font-size:1.7rem;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:.25s;line-height:1}
.lb-nav:hover{background:var(--green)}.lb-nav.prev{left:-64px}.lb-nav.next{right:-64px}
@media(max-width:760px){.lb-nav.prev{left:8px}.lb-nav.next{right:8px}.lb-nav{background:rgba(0,0,0,.45)}}

/* approach + platform */
.approach{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:44px}
@media(max-width:800px){.approach{grid-template-columns:1fr}}
.astep{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:32px;transition:.3s var(--ease)}
.astep:hover{border-color:var(--green);transform:translateY(-4px)}
.astep .an{font-family:var(--disp);font-weight:700;font-size:2.4rem;color:var(--green);opacity:.35;line-height:1}
.astep h3{margin:12px 0 8px;font-size:1.2rem}.astep p{color:var(--muted);font-size:.96rem}
.platform{background:linear-gradient(135deg,rgba(10,53,39,.66),rgba(14,92,64,.6)),url('../media/gallery-4.jpg') center/cover;color:#fff;border-radius:var(--r-lg);padding:clamp(40px,6vw,64px);text-align:center;margin-top:30px;position:relative;overflow:hidden}
.platform h2,.platform p{color:#fff;position:relative}
.platform .eyebrow{color:#7ff0b8;justify-content:center}.platform .eyebrow::before{background:#7ff0b8}
.platform h2{font-size:clamp(1.6rem,3.4vw,2.4rem);max-width:20ch;margin:16px auto 14px}
.platform p{color:rgba(255,255,255,.85);max-width:54ch;margin:0 auto 26px}

/* promise / testimonials / cta / footer */
.promise{background:radial-gradient(ellipse at 50% -20%,rgba(94,230,160,.22),transparent 60%),linear-gradient(135deg,rgba(16,150,92,.6),rgba(10,53,39,.7)),url('../media/about.jpg') center/cover;text-align:center}
.promise .q,.promise .by,.promise .mark{color:#fff}
.promise .q{font-family:var(--disp);font-weight:500;font-size:clamp(1.5rem,3.4vw,2.5rem);line-height:1.3;max-width:22ch;margin:18px auto 0;letter-spacing:-.02em}
.promise .q .g{color:#a9f5cf}.promise .mark{font-family:var(--disp);font-size:4rem;line-height:.5;height:34px;opacity:.55}
.promise .by{margin-top:28px;font-family:var(--disp);letter-spacing:.14em;text-transform:uppercase;font-size:.76rem;opacity:.85}
.tst{display:grid;grid-template-columns:1fr 1fr;gap:24px}
@media(max-width:760px){.tst{grid-template-columns:1fr}}
.tst-card{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:34px;transition:.3s var(--ease)}
.tst-card:hover{box-shadow:0 30px 60px -44px rgba(10,53,39,.3)}
.tst-card p{font-size:1.12rem;color:var(--ink);line-height:1.55}
.tst-card .who{margin-top:22px;display:flex;align-items:center;gap:12px;color:var(--muted);font-size:.9rem}
.tst-card .who .av{width:40px;height:40px;border-radius:50%;background:var(--green-soft);display:flex;align-items:center;justify-content:center;font-family:var(--disp);font-weight:700;color:var(--green)}
.tst-card .stars{color:var(--green);letter-spacing:3px;margin-bottom:14px;font-size:.9rem}
.cta{background:radial-gradient(ellipse at 50% 0,var(--green-glow),transparent 60%),linear-gradient(rgba(10,53,39,.55),rgba(10,53,39,.72)),url('../media/gallery-7.jpg') center/cover;text-align:center;padding:110px 0;color:#fff}
.cta h2{color:#fff;font-size:clamp(2rem,4.5vw,3.2rem);max-width:20ch;margin:0 auto 18px}
.cta p{color:rgba(255,255,255,.82);max-width:52ch;margin:0 auto 32px;font-size:1.1rem}
.cta .eyebrow{color:#7ff0b8;justify-content:center}.cta .eyebrow::before{background:#7ff0b8}
@media(min-width:900px){.promise,.cta{background-attachment:fixed}}
.foot{background:var(--green-dd);color:#cfe0d8;padding:70px 0 34px}
.foot-top{display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:40px;padding-bottom:44px;border-bottom:1px solid rgba(255,255,255,.12)}
@media(max-width:760px){.foot-top{grid-template-columns:1fr;gap:32px}}
.foot .brand img{height:28px;filter:brightness(0) invert(1)}
.foot p.tag{color:rgba(255,255,255,.7);font-size:.94rem;max-width:38ch;margin:18px 0 20px}
.foot .socials{display:flex;gap:10px}
.foot .socials a{width:38px;height:38px;border-radius:10px;border:1px solid rgba(255,255,255,.18);display:flex;align-items:center;justify-content:center;color:#cfe0d8;transition:.25s}
.foot .socials a:hover{color:#fff;border-color:var(--green);background:rgba(18,176,106,.25)}
.foot .socials svg{width:17px;height:17px}
.foot h5{font-family:var(--disp);font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.5);margin-bottom:16px}
.foot ul{list-style:none}.foot li{margin-bottom:10px}
.foot li a,.foot li span{color:rgba(255,255,255,.72);font-size:.94rem;transition:.2s}.foot li a:hover{color:#fff}
.foot-bot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding-top:26px;color:rgba(255,255,255,.5);font-size:.84rem}

/* praksis grid (responsive) */
.praksis-grid{display:grid;grid-template-columns:1fr 1.1fr;gap:54px;align-items:center}
@media(max-width:860px){.praksis-grid{grid-template-columns:1fr;gap:30px}}
/* video frame */
.video-frame{position:relative;border-radius:var(--r-lg);overflow:hidden;border:1px solid var(--line);aspect-ratio:16/11;background:var(--bg-alt);box-shadow:0 40px 80px -50px rgba(10,53,39,.4)}
.video-frame video,.video-frame img{width:100%;height:100%;object-fit:cover}

/* forms */
.form-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:54px;align-items:start}
@media(max-width:860px){.form-grid{grid-template-columns:1fr;gap:38px}}
.form{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);padding:clamp(26px,4vw,40px);box-shadow:0 30px 70px -50px rgba(10,53,39,.35)}
.form .row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:520px){.form .row{grid-template-columns:1fr}}
.field{margin-bottom:16px}
.field label{display:block;font-family:var(--disp);font-weight:500;font-size:.82rem;color:var(--ink);margin-bottom:7px}
.field input,.field textarea{width:100%;background:var(--bg-alt);border:1px solid var(--line);border-radius:11px;padding:.72rem .85rem;font-family:var(--body);font-size:.95rem;color:var(--ink)}
.field input:focus,.field textarea:focus{outline:none;border-color:var(--green);background:#fff}
.field textarea{min-height:120px;resize:vertical}
.field input[type=file]{padding:.55rem .6rem;cursor:pointer}
.filehint{font-size:.78rem;color:var(--faint);margin-top:6px}
.form .note{font-size:.8rem;color:var(--faint);margin-top:6px}.form .note a{color:var(--green)}
.fstatus{font-size:.9rem;margin-top:12px;min-height:1.1em}.fstatus.ok{color:var(--green-d)}.fstatus.err{color:#d9534f}
.contact-alt{background:var(--green-soft);border-radius:var(--r-lg);padding:36px}
.contact-alt h3{font-size:1.35rem;margin:14px 0 12px}.contact-alt p{color:var(--muted);margin-bottom:22px}
.contact-line{display:flex;align-items:center;gap:13px;padding:14px 0;border-top:1px solid var(--line2)}
.contact-line svg{width:20px;height:20px;color:var(--green);flex:0 0 auto}
.contact-line b{font-family:var(--disp);font-size:.95rem}.contact-line span{display:block;color:var(--muted);font-size:.86rem}
.office-map{margin-top:20px;border-radius:16px;overflow:hidden;border:1px solid var(--line2);height:200px}
.office-map iframe{width:100%;height:100%;border:0;display:block;filter:grayscale(.35) contrast(1.05)}

/* floating pod */
.scrollbar{position:fixed;top:0;left:0;right:0;height:3px;background:var(--green);transform:scaleX(0);transform-origin:left;z-index:200;transition:transform .1s linear}
.pod{position:fixed;right:22px;bottom:22px;z-index:400}
.pod-btn{display:inline-flex;align-items:center;gap:10px;height:54px;padding:0 22px;border-radius:100px;background:var(--green);color:#fff;border:0;cursor:pointer;font-family:var(--disp);font-weight:600;font-size:.98rem;box-shadow:0 16px 34px -14px var(--green);transition:.3s var(--ease)}
.pod-btn:hover{background:var(--green-d);transform:translateY(-2px)}
.pod-btn svg{width:20px;height:20px}
.pod-panel{position:absolute;right:0;bottom:70px;width:360px;max-width:calc(100vw - 36px);max-height:calc(100vh - 130px);overflow:auto;background:#fff;border:1px solid var(--line);border-radius:20px;padding:24px;box-shadow:0 40px 80px -28px rgba(10,53,39,.45);opacity:0;visibility:hidden;transform:translateY(12px);transition:.3s var(--ease)}
.pod.open .pod-panel{opacity:1;visibility:visible;transform:none}
.pod-panel .ph{font-family:var(--disp);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:var(--green);font-weight:700}
.pod-panel h5{font-family:var(--disp);font-size:1.14rem;margin:6px 0 16px;color:var(--ink)}
.pseg{display:inline-flex;background:var(--bg-alt);border-radius:100px;padding:4px;margin-bottom:14px}
.pseg button{border:0;background:none;font-family:var(--disp);font-weight:600;font-size:.85rem;padding:.42rem 1.05rem;border-radius:100px;cursor:pointer;color:var(--muted);transition:.25s}
.pseg button.on{background:var(--green);color:#fff}
.pod-panel input:not([type=file]),.pod-panel textarea{width:100%;background:var(--bg-alt);border:1px solid var(--line);border-radius:11px;padding:.6rem .8rem;font-family:var(--body);font-size:.9rem;color:var(--ink);margin-bottom:9px}
.pod-panel input:focus,.pod-panel textarea:focus{outline:none;border-color:var(--green);background:#fff}
.pod-panel textarea{min-height:66px;resize:vertical}
.podfile{display:inline-flex;align-items:center;gap:8px;font-family:var(--disp);font-weight:600;font-size:.84rem;color:var(--green);cursor:pointer;padding:.35rem 0;margin-bottom:6px}
.podfile svg{width:16px;height:16px}
.pstatus{font-size:.82rem;margin-top:8px;min-height:1em}.pstatus.ok{color:var(--green-d)}.pstatus.err{color:#d9534f}

/* mobile spacing + symmetry */
@media(max-width:700px){
.wrap{padding:0 18px}
.sec{padding:60px 0}
.sec-head{margin-bottom:34px}
.page-hero{padding:118px 0 44px}
.split{gap:22px;margin-top:44px}
.case .cb{padding:24px}
.case h3{font-size:1.28rem}
.platform{padding:30px 20px}
.cta{padding:72px 0}
.foot{padding:48px 0 24px}
.pod{right:14px;bottom:14px}
.pod-btn{height:48px;padding:0 16px;font-size:.9rem}
.btn{padding:.78rem 1.2rem;font-size:.92rem}
.tst-card{padding:24px}
.contact-alt{padding:24px}
.form{padding:20px}
.video-frame{aspect-ratio:16/10}
h1,h2,h3,p{overflow-wrap:break-word}
body{-webkit-text-size-adjust:100%}
}
/* galleri */
.vgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:44px}
@media(max-width:900px){.vgrid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){.vgrid{grid-template-columns:repeat(2,1fr);gap:10px}}
.vtile{position:relative;aspect-ratio:9/16;overflow:hidden;border-radius:var(--r);background:var(--green-dd);border:1px solid var(--line);transition:transform .35s var(--ease),box-shadow .35s var(--ease)}
.vtile:hover{transform:translateY(-6px);box-shadow:0 26px 50px -34px rgba(10,53,39,.45)}
.vtile video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.vtile .cap{position:absolute;left:0;right:0;bottom:0;padding:26px 12px 10px;color:#fff;font-size:.8rem;font-family:var(--disp);font-weight:600;background:linear-gradient(0deg,rgba(10,53,39,.75),transparent);pointer-events:none}
/* service grid (numbered, Design1-style) */
.svc-grid{display:grid;grid-template-columns:repeat(3,1fr);background:var(--line);gap:1px;border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden}
.svc{background:#fff;padding:34px 30px 38px;position:relative;transition:.3s var(--ease)}
.svc:hover{background:var(--green-soft)}
.svc .num{position:absolute;top:24px;right:26px;font-family:var(--disp);font-size:.8rem;letter-spacing:.12em;color:var(--faint)}
.svc .sico{width:44px;height:44px;color:var(--green);margin-bottom:18px}
.svc .sico svg{width:100%;height:100%}
.svc h3{font-size:1.18rem;margin-bottom:10px}
.svc p{color:var(--muted);font-size:.94rem}
@media(max-width:900px){.svc-grid{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.svc-grid{grid-template-columns:1fr}.svc{padding:26px 22px}}
/* FAQ */
.faq-h{font-size:1.4rem;margin:44px 0 16px}
.qa{background:#fff;border:1px solid var(--line);border-radius:16px;margin-bottom:12px;overflow:hidden;transition:.3s var(--ease)}
.qa[open]{border-color:var(--green);box-shadow:0 18px 40px -30px rgba(18,176,106,.4)}
.qa summary{list-style:none;cursor:pointer;padding:17px 52px 17px 20px;font-family:var(--disp);font-weight:600;font-size:1rem;position:relative;color:var(--ink)}
.qa summary::-webkit-details-marker{display:none}
.qa summary::after{content:"+";position:absolute;right:16px;top:50%;transform:translateY(-50%);width:28px;height:28px;border-radius:50%;background:var(--green-soft);color:var(--green);display:flex;align-items:center;justify-content:center;font-size:1.2rem;transition:.3s var(--ease)}
.qa[open] summary::after{content:"–";background:var(--green);color:#fff}
.qa-a{padding:0 20px 18px;color:var(--muted)}
.qa-a p{margin:0;font-size:.96rem;line-height:1.65}
/* reveal */
.rev{opacity:0;transform:translateY(26px);transition:.7s var(--ease)}
.rev.in{opacity:1;transform:none}
.cards.in>*,.values.in>*,.reasons.in>*,.team-grid.in>*,.stats.in>*,.approach.in>*,.tst.in>*{animation:up .55s var(--ease) both}
.in>*:nth-child(2){animation-delay:.08s}.in>*:nth-child(3){animation-delay:.16s}.in>*:nth-child(4){animation-delay:.24s}
.in>*:nth-child(5){animation-delay:.32s}.in>*:nth-child(6){animation-delay:.4s}
@keyframes up{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.rev{opacity:1;transform:none}}
'''
open(OUT+'/assets/style.css','w',encoding='utf-8').write(CSS)

JS=r'''
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
'''
open(OUT+'/assets/app.js','w',encoding='utf-8').write(JS)

FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
AR='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17 17 7M9 7h8v8"/></svg>'
NAVI=[('index.html','Hjem'),('losninger.html','Løsninger'),('prosjekter.html','Prosjekter'),('galleri.html','Galleri'),('om-oss.html','Om oss'),('faq.html','FAQ'),('kontakt.html','Kontakt')]
def nav(active):
    links=''.join(f'<a href="{h}"{" class=\"on\"" if h==active else ""}>{t}</a>' for h,t in NAVI)
    m=''.join(f'<a href="{h}">{t}</a>' for h,t in NAVI)
    return (f'<header class="nav" id="nav"><div class="nav-in"><a href="index.html" class="brand"><img src="media/altivon-logo.png?v=2" alt="Altivon"></a>'
      f'<nav class="nav-links">{links}</nav><div class="nav-cta"><a href="kontakt.html" class="btn btn-primary">Be om tilbud {AR}</a>'
      f'<button class="burger" id="burger" aria-label="Meny"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button></div></div></header>'
      f'<div class="mnav" id="mnav"><button class="mnav-close" id="mclose" aria-label="Lukk">&times;</button>{m}<a href="kontakt.html" class="btn btn-primary">Be om tilbud</a></div>')

FOOT='''<footer class="foot"><div class="wrap"><div class="foot-top">
  <div><a href="index.html" class="brand"><img src="media/altivon-logo.png?v=2" alt="Altivon"></a>
    <p class="tag">Fra data til beslutninger. Altivon kombinerer dronebasert vedlikehold og inspeksjon med strukturert dokumentasjon som gjør eiendom enklere å drifte.</p>
    <div class="socials"><a href="https://www.instagram.com/altivon_as/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="2" width="20" height="20" rx="5.5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.6" cy="6.4" r="1.1" fill="currentColor" stroke="none"/></svg></a>
      <a href="mailto:mathias@altivon.no" aria-label="E-post"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg></a></div></div>
  <div><h5>Utforsk</h5><ul><li><a href="losninger.html">Løsninger</a></li><li><a href="prosjekter.html">Prosjekter</a></li><li><a href="om-oss.html">Om oss</a></li><li><a href="galleri.html">Galleri</a></li><li><a href="om-oss.html#team">Team</a></li><li><a href="faq.html">FAQ</a></li><li><a href="kontakt.html">Kontakt</a></li></ul></div>
  <div><h5>Ta kontakt</h5><ul><li><span>Madserud allé 2, 0274 Oslo</span></li><li><a href="mailto:mathias@altivon.no">mathias@altivon.no</a></li><li><a href="tel:+4791576447">+47 915 76 447</a></li></ul></div>
</div><div class="foot-bot"><span>&copy; 2026 Altivon AS. Alle rettigheter reservert.</span><span>Org.nr 937 206 879</span></div></div></footer>'''

TAIL='''<form name="tilbud" method="POST" data-netlify="true" netlify-honeypot="bot-field" enctype="multipart/form-data" hidden><input type="hidden" name="form-name" value="tilbud"><input name="bot-field"><input name="kundetype"><input name="navn"><input name="epost"><input name="telefon"><input name="adresse"><textarea name="melding"></textarea><input type="file" name="bilde1"><input type="file" name="bilde2"><input type="file" name="bilde3"><input type="file" name="bilde4"><input type="file" name="bilde5"><input type="file" name="bilde6"><input type="file" name="bilde7"><input type="file" name="bilde8"><input type="file" name="bilde9"><input type="file" name="bilde10"></form>
<div class="scrollbar" id="scrollbar"></div>
<div class="pod" id="pod"><div class="pod-panel" id="podPanel" role="dialog" aria-label="Be om tilbud">
  <div class="ph">Be om tilbud</div><h5>Fortell oss kort om oppdraget</h5>
  <div class="pseg" id="pseg"><button type="button" data-type="privat" class="on">Privat</button><button type="button" data-type="bedrift">Bedrift</button></div>
  <input id="pf-name" type="text" placeholder="Navn" autocomplete="name"><input id="pf-email" type="email" placeholder="E-post" autocomplete="email"><input id="pf-phone" type="tel" placeholder="Telefon" autocomplete="tel"><input id="pf-addr" type="text" placeholder="Adresse på bygg"><textarea id="pf-msg" placeholder="Hva trenger du hjelp til?"></textarea>
  <label class="podfile" for="pf-files"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m17 8-5-5-5 5M12 3v12"/></svg> Legg ved bilder (maks 10)</label>
  <input id="pf-files" type="file" accept="image/*" multiple hidden><div class="filehint" id="pf-hint"></div>
  <button class="btn btn-primary" id="pf-send" style="width:100%;justify-content:center;margin-top:8px">Send forespørsel</button>
  <div class="pstatus" id="pf-status" role="status"></div></div>
  <button class="pod-btn" id="podBtn" aria-label="Be om tilbud" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>Be om tilbud</button></div>
<div class="lightbox" id="lightbox"><button class="lb-close" id="lbClose" aria-label="Lukk">&times;</button><div class="lb-stage"><button class="lb-nav prev" id="lbPrev" aria-label="Forrige">&#8249;</button><img id="lbImg" src="" alt=""><button class="lb-nav next" id="lbNext" aria-label="Neste">&#8250;</button></div></div>'''

def head(title,desc):
    return (f'<!DOCTYPE html><html lang="no"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">'
      f'<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#ffffff">'
      f'<link rel="icon" type="image/png" href="media/altivon-icon.png?v=2">{FONTS}<link rel="stylesheet" href="assets/style.css"></head><body>')
def page(fn,active,title,desc,body):
    open(OUT+'/'+fn,'w',encoding='utf-8').write(head(title,desc)+nav(active)+body+FOOT+TAIL+'<script src="assets/app.js"></script></body></html>')
def cta(h,p):
    return f'<section class="cta"><div class="wrap rev"><span class="eyebrow c">La oss snakke</span><h2 style="margin-top:16px">{h}</h2><p>{p}</p><div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap"><a href="kontakt.html" class="btn btn-white">Be om tilbud {AR}</a><a href="tel:+4791576447" class="btn btn-ghost" style="color:#fff;border-color:rgba(255,255,255,.3)">Ring +47 915 76 447</a></div></div></section>'

CMP=[('Uten stillas eller lift','Krever stillas og rigg'),('Rask dronetilkomst til hele bygget','Tidkrevende opprigging'),('Foto, termografi og 3D-data','Kun bilder'),('Personell trygt på bakken','Arbeid i høyden'),('Strukturert dokumentasjon','Manuell rapportering'),('Proaktiv vedlikeholdsplan','Reaktiv inspeksjon')]
def cmprows():
    return ''.join(f'<div class="cmp-row"><div class="c us"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg></span>{u}</div><div class="c them"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M18 6 6 18M6 6l12 12"/></svg></span>{t}</div></div>' for u,t in CMP)

# HOME
home=f'''<section class="hero" id="top"><div class="hero-bg" id="heroCar"><img src="media/about.jpg" alt="" class="on"><img src="media/gallery-1.jpg" alt=""><img src="media/gallery-7.jpg" alt=""><img src="media/gallery-2.jpg" alt=""><img src="media/gallery-4.jpg" alt=""><img src="media/gallery-5.jpg" alt=""><img src="media/gallery-8.jpg" alt=""></div><div class="wrap hero-inner">
  <span class="eyebrow c">Dronebasert vedlikehold &amp; inspeksjon</span>
  <h1>Ekte data.<br><span class="g">Ekte innsikt.</span><br>Riktige beslutninger.</h1>
  <p class="sub">Altivon vasker og inspiserer bygg i Oslo-området. Drone der det gir best resultat – lift, stang eller manuelt arbeid der det passer bedre. Alltid dokumentert, alltid uten stillas der det er mulig.</p>
  <div class="hero-actions"><a href="kontakt.html" class="btn btn-primary">Be om tilbud {AR}</a><a href="losninger.html" class="btn btn-ghost">Se løsninger</a></div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head rev"><span class="eyebrow">Hva vi løser</span><h2>Rent bygg. Full oversikt.</h2><p>Vi gjør bygget rent og dokumenterer tilstanden samtidig. Drone der det lønner seg – lift, stang eller manuelt arbeid der det passer bygget best. Metoden velges etter bygget, ikke omvendt.</p></div>
  <div class="cards">
    <div class="card"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg></div><div class="num">01</div><h3>Forutsigbart vedlikehold</h3><p>Vi kartlegger byggets faktiske tilstand og leverer en strukturert oversikt, slik at du kan prioritere tiltak og estimere kostnader med trygghet.</p></div>
    <div class="card"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2a10 10 0 1 0 10 10"/><path d="M12 6v6l4 2"/></svg></div><div class="num">02</div><h3>Proaktivt og prioritert</h3><p>Vi oppdager og strukturerer byggets tilstand tidlig, og prioriterer etter risiko – slik at du kan handle før små avvik blir dyre skader.</p></div>
    <div class="card"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div><div class="num">03</div><h3>Strukturert dokumentasjon</h3><p>Foto, termografi og 3D-modeller samlet ett sted – klart for rapportering, styremøte og en langsiktig vedlikeholdsplan.</p></div>
  </div></div></section>

<section class="sec alt"><div class="wrap">
  <div class="sec-head rev"><span class="eyebrow">Hvorfor Altivon</span><h2>Mer verdi enn tradisjonelle metoder</h2><p>Tradisjonelle løsninger samler bilder. Altivon leverer rene bygg og et grunnlag du kan ta beslutninger på.</p></div>
  <div class="cmp rev"><div class="cmp-row head"><div class="c us">Altivon</div><div class="c them">Tradisjonelle metoder</div></div>{cmprows()}</div>
  <p class="cmp-note rev">Tradisjonelle løsninger samler data. <b>Altivon gjør data om til beslutninger.</b></p>
</div></section>

<section class="sec"><div class="wrap praksis-grid">
  <div class="rev"><span class="eyebrow">Altivon i praksis</span><h2 style="font-size:clamp(1.9rem,4vw,3rem);margin:18px 0 16px">Ekte oppdrag.<br>Ekte bygg.</h2>
    <p style="color:var(--muted);font-size:1.1rem;margin-bottom:28px">Se hvordan et droneoppdrag ser ut – hva operatøren ser, hva dronen fanger, og hvordan hver flyvning blir til strukturert dokumentasjon for eiendommen din.</p>
    <a href="kontakt.html" class="btn btn-primary">Be om tilbud {AR}</a></div>
  <div class="video-frame rev"><video autoplay muted loop playsinline poster="media/hero-poster.jpg"><source src="media/hero.mp4" type="video/mp4"></video></div>
</div></section>

<section class="sec promise"><div class="wrap rev"><div class="mark">&ldquo;</div><div class="q">Rene bygg – og <span class="g">dokumentasjon du kan bruke</span>. Det er det vi leverer, med den metoden som passer bygget best.</div><div class="by">Altivon</div></div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head c rev"><span class="eyebrow c">Kundene våre</span><h2>Det kundene sier</h2><p>Eksempelsitater – erstattes med reelle tilbakemeldinger etter hvert.</p></div>
  <div class="tst rev">
    <div class="tst-card"><div class="stars">★★★★★</div><p>&ldquo;Vi kunne gå til styret med dokumentasjon i stedet for magefølelse. Det gjorde en stor forskjell.&rdquo;</p><div class="who"><span class="av">BS</span><div><b>Boligsameie</b><br>Oslo</div></div></div>
    <div class="tst-card"><div class="stars">★★★★★</div><p>&ldquo;Fasaden ble ren uten stillas, og rapporten var klar rett etterpå. Ryddig og profesjonelt.&rdquo;</p><div class="who"><span class="av">EF</span><div><b>Eiendomsforvalter</b><br>Næringsbygg</div></div></div>
  </div></div></section>
{cta("Klar for renere bygg og bedre beslutninger?","Be om en uforpliktende vurdering, så anbefaler vi metoden som passer eiendommen eller virksomheten din best.")}'''
page('index.html','index.html','Altivon | Dronebasert vedlikehold, inspeksjon og data for bygg','Altivon kombinerer dronebasert fasadevask, vindusvask og takrens med inspeksjon, termografi og 3D-dokumentasjon for eiendom og næring i Oslo-området.',home)

# LØSNINGER
def splitrow(flip,img,label,h,p,bullets):
    return f'''<div class="split{' flip' if flip else ''} rev"><div class="split-media"><img src="media/{img}" alt="{h}"></div><div><span class="eyebrow">{label}</span><h3>{h}</h3><p>{p}</p><ul class="checks">{''.join(f'<li>{b}</li>' for b in bullets)}</ul></div></div>'''
los=f'''<section class="page-hero"><div class="ph-bg"><img src="media/gallery-1.jpg" alt=""></div><div class="wrap"><span class="eyebrow c">Løsninger</span><h1>Fra observasjon til <span class="g">beslutning</span></h1><p>Vedlikehold, inspeksjon og datagrunnlag for fasade, tak og eiendom – med drone der det gir fordeler, tradisjonelt der det passer best.</p><div class="crumb"><a href="index.html">Hjem</a> → Løsninger</div></div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head rev"><span class="eyebrow">Tjenester</span><h2>Hva vi leverer</h2><p>Åtte kjernetjenester for utvendig vedlikehold og inspeksjon. Vi bruker drone der det gir best resultat – og lift, stang eller manuelt arbeid der det passer bygget bedre. Metoden velges alltid ut fra byggets høyde, tilkomst og overflate.</p></div>
  <div class="svc-grid"><div class="svc rev"><span class="num">01</span><div class="sico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M3 21V8l7-5 7 5v13"/><path d="M13 21v-6h-4v6M21 21H3"/></svg></div><h3>Fasadevask</h3><p>Skånsom og effektiv fjerning av smuss, alger og forurensning fra betong, tegl, glass, metall og tre.</p></div><div class="svc rev"><span class="num">02</span><div class="sico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="4" y="4" width="16" height="16" rx="1"/><path d="M12 4v16M4 12h16"/></svg></div><h3>Vindusvask</h3><p>Presisjonsrengjøring med rent, avionisert vann for et stripefritt resultat – også ved krevende tilkomst.</p></div><div class="svc rev"><span class="num">03</span><div class="sico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M2 12 12 4l10 8"/><path d="M5 10v9h14v-9"/></svg></div><h3>Takrens</h3><p>Fjerning av mose og skitt som forringer takets levetid – med metode tilpasset taktype og tilkomst.</p></div><div class="svc rev"><span class="num">04</span><div class="sico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="8" width="18" height="10" rx="1"/><path d="M8 8v10M16 8v10M3 13h18M12 2v3"/></svg></div><h3>Solcellevask</h3><p>Regelmessig, skånsom vask opprettholder anleggets effekt – uten å gå på taket og uten skade på panelene.</p></div><div class="svc rev"><span class="num">05</span><div class="sico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg></div><h3>Inspeksjon &amp; dokumentasjon</h3><p>Høyoppløselig visuell dokumentasjon for tilstandsanalyse – fuktskader, sprekker, beslag og avvik.</p></div><div class="svc rev"><span class="num">06</span><div class="sico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 3v10"/><circle cx="12" cy="17" r="4"/><path d="M12 3a2 2 0 0 1 2 2"/></svg></div><h3>Termografisk inspeksjon</h3><p>Kartlegging av varmetap og isolasjonsfeil med termisk kamera. Avdekker kuldebroer, fukt og avvik.</p></div><div class="svc rev"><span class="num">07</span><div class="sico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="3" width="18" height="18" rx="1"/><path d="M3 9h18M3 15h18M9 3v18M15 3v18"/></svg></div><h3>Ortofoto &amp; 2D-kartlegging</h3><p>Geo-refererte, målriktige ortofoto av eiendommen – grunnlag for planlegging og forvaltning.</p></div><div class="svc rev"><span class="num">08</span><div class="sico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 2 2 7l10 5 10-5-10-5z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/></svg></div><h3>3D-modeller &amp; geodata</h3><p>Centimeter-nøyaktige 3D-modeller og punktskyer for måling, prosjektering og dokumentasjon.</p></div><div class="svc rev"><span class="num">09</span><div class="sico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M15 10l4.55-2.28A1 1 0 0 1 21 8.62v6.76a1 1 0 0 1-1.45.9L15 14"/><rect x="3" y="6" width="12" height="12" rx="2"/></svg></div><h3>FPV-film for eiendom</h3><p>Cinematiske FPV-flyvninger i én sammenhengende tagning – innvendig og utvendig. Viser frem eiendommer, hoteller og restauranter slik stillbilder ikke kan.</p></div></div>
  <div class="platform rev"><span class="eyebrow c">Metoden bak</span><h2>Fra observasjon til beslutning – i én prosess</h2><p>Vi kombinerer sertifisert droneflyging med strukturert dokumentasjon, slik at hvert oppdrag ender i noe du faktisk kan bruke: en oversikt over tilstand, tiltak og prioritering.</p><a href="prosjekter.html" class="btn btn-white">Se prosjekter {AR}</a></div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head rev"><span class="eyebrow">Nærmere blikk</span><h2>Slik henger det sammen</h2><p>Hver del har en jobb. Her er hva du faktisk får igjen som kunde.</p></div>
  {splitrow(False,'gallery-1.jpg','Fasadevask','Ren fasade uten stillas','Vi vasker fasader skånsomt og effektivt – med drone der det gir tilgang og fart, og tradisjonelle metoder der det passer bedre.',['Skånsom vask tilpasset overflaten','Når høye fasader uten stillas','Foto før og etter på hvert oppdrag'])}
  {splitrow(True,'gallery-2.jpg','Vindusvask','Stripefrie vinduer, også i høyden','Rent, avionisert vann gir et stripefritt resultat. For krevende tilkomst bruker vi tilkomstteknikk eller drone.',['Avionisert vann, stripefritt resultat','Tilkomstteknikk for høyder','Egnet for næringsbygg og boliger'])}
  {splitrow(False,'gallery-6.jpg','Takrens','Forleng takets levetid','Mose og skitt holder på fuktighet og forkorter takets levetid. Vi fjerner begroning før den gjør skade.',['Fjerner mose og begroning','Metode tilpasset taktype','Reduserer fuktskader over tid'])}
  {splitrow(True,'about.jpg','Inspeksjon &amp; termografi','Se det øyet ikke ser','Termiske og høyoppløselige kameraer avdekker fukt, varmetap og skader som ikke er synlige i et vanlig bilde.',['Høyoppløselig bildedokumentasjon','Termografi for fukt og varmetap','Grunnlag for vedlikeholdsplan'])}
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head c rev"><span class="eyebrow c">Hvorfor Altivon</span><h2>Én partner, tre grunner</h2></div>
  <div class="reasons rev">
    <div class="reason"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="m12 15 2 2 4-4"/><path d="M12 2 4 6v6c0 5 3.5 8 8 10 4.5-2 8-5 8-10V6z"/></svg></div><h3>Erfaring og sertifisering</h3><p>Sertifiserte droneoperatører og lang erfaring med fasade- og vindusarbeid – riktig verktøy for riktig jobb.</p></div>
    <div class="reason"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 12h4l3 8 4-16 3 8h4"/></svg></div><h3>Skalerbart</h3><p>Fra ett bygg til hele porteføljer – vi tilpasser metode og omfang etter behovet.</p></div>
    <div class="reason"><div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 3v18h18"/><path d="m7 14 4-4 3 3 5-6"/></svg></div><h3>Datadrevet</h3><p>Tydelig, handlingsrettet dokumentasjon som støtter bedre beslutninger og planlegging.</p></div>
  </div>
</div></section>
{cta("Skal vi ta en titt på bygget ditt?","Send oss adresse og noen bilder, eller ring. Du får et ærlig svar på hva bygget trenger – og hva det ikke trenger.")}'''
page('losninger.html','losninger.html','Løsninger – vask, inspeksjon, termografi og 3D | Altivon','Altivons løsninger: fasadevask, vindusvask, takrens, inspeksjon, termografi, ortofoto og 3D-modeller for eiendom og næring.',los)

# PROSJEKTER
def casecard(img,cat,title,desc,metrics):
    return f'<div class="case rev"><div class="ci"><img src="media/{img}" alt="{title}"></div><div class="cb"><span class="cat">{cat}</span><h3>{title}</h3><p>{desc}</p><div class="metrics">{"".join(f"<span class=\"metric\">{m}</span>" for m in metrics)}</div><a href="kontakt.html" class="btn btn-ghost">Be om lignende {AR}</a></div></div>'
caps={1:'Fasadevask med drone',2:'Vindusvask · tilkomst',3:'Vindusvask · bolig',4:'Fasadevask',5:'Utvendig vedlikehold',6:'Takrens',7:'Fasadevask med drone',8:'Vindusvask'}
gtiles=''.join(f'<div class="galtile"><img src="media/gallery-{i}.jpg" alt="Altivon prosjekt {i}" loading="lazy"><span class="zoom"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M14 10l7-7M9 21H3v-6M10 14l-7 7"/></svg></span><span class="cap">{caps[i]}</span></div>' for i in range(1,9))
pro=f'''<section class="page-hero"><div class="ph-bg"><img src="media/gallery-6.jpg" alt=""></div><div class="wrap"><span class="eyebrow c">Prosjekter</span><h1>Ekte bygg. <span class="g">Ekte verdi.</span></h1><p>Se hvordan eiendomsbesittere og næringskunder bruker Altivon til renere bygg, bedre dokumentasjon og tryggere vedlikeholdsplaner.</p><div class="crumb"><a href="index.html">Hjem</a> → Prosjekter</div></div></section>
<section class="sec"><div class="wrap"><div class="cases">
  {casecard('gallery-1.jpg','Boligsameie','Fasadevask med drone','Hele fasaden rengjort uten stillas eller sperret fortau – med foto før og etter som dokumentasjon til styret.',['Uten stillas','Foto før/etter','Minimal forstyrrelse'])}
  {casecard('gallery-2.jpg','Næringsbygg','Vindusvask i høyden','Stripefri vindusvask på glassfasade med tilkomstteknikk, gjennomført trygt og effektivt utenom åpningstid.',['Glassfasade','Tilkomstteknikk','Trygt i høyden'])}
  {casecard('gallery-6.jpg','Bolig','Takrens og inspeksjon','Fjerning av mose kombinert med droneinspeksjon av takflaten – tilstand dokumentert og tiltak prioritert.',['Mose fjernet','Droneinspeksjon','Tilstandsrapport'])}
  {casecard('about.jpg','Eiendom','Inspeksjon &amp; termografi','Høyoppløselig inspeksjon og termografi som avdekket fukt og varmetap – grunnlag for en konkret vedlikeholdsplan.',['Termografi','Fukt avdekket','Vedlikeholdsplan'])}
</div></div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head c rev"><span class="eyebrow c">Vår tilnærming</span><h2>Fra befaring til dokumentasjon</h2><p>Tre steg – fra vurdering til et resultat du kan handle på.</p></div>
  <div class="approach rev">
    <div class="astep"><div class="an">01</div><h3>Befaring &amp; metode</h3><p>Vi vurderer bygg, tilkomst og velger riktig metode – drone eller tradisjonelt.</p></div>
    <div class="astep"><div class="an">02</div><h3>Utførelse</h3><p>Vi gjennomfører oppdraget fagmessig, trygt og med minimal forstyrrelse.</p></div>
    <div class="astep"><div class="an">03</div><h3>Dokumentasjon</h3><p>Du får strukturert dokumentasjon: foto, eventuelt termografi og en klar oversikt.</p></div>
  </div>
</div></section>
{cta("Klar for å se hva bygget ditt avslører?","Hvert prosjekt starter med én befaring. Ta kontakt, så finner vi ut hva som passer eiendommen din.")}'''
page('prosjekter.html','prosjekter.html','Prosjekter – ekte bygg, ekte verdi | Altivon','Se hvordan Altivon hjelper boligsameier, næringsbygg og eiendom med fasadevask, vindusvask, takrens og inspeksjon.',pro)

# OM OSS
PH='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'
MLs='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>'
WB='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20"/></svg>'
TEAM=[('Mathias Loe','Daglig leder','team-mathias.jpg','ML','Strategi, vekst og forretningsutvikling – med bakgrunn innen kommunikasjon og rådgivning (Zynk, PR-operatørene).','+4791576447','mathias@altivon.no',None),
      ('Kristoff Stepinski','Driftssjef','team-kristoff.jpg','KS','13+ års erfaring med vindusvask og fasadearbeid (Elite Vinduspuss). Sikrer kvalitet på hvert oppdrag.','+4745843356','kristoff@altivon.no',None),
      ('Atiqur Rahman','Droneoperatør &amp; teknisk ansvarlig','team-atiqur.jpg','AR','Sertifikatene A1, A2, A3 og STS. Ekspert på bygging og flyging av droner – militært og sivilt – med bakgrunn i informatikk, programmering og robotikk.','+4745808855','atiqur@altivon.no','https://atiq.no')]
def tcard(m):
    name,role,ph,ini,bio,tel,mail,web=m
    wl=f'<a href="{web}" target="_blank" rel="noopener" aria-label="Nettside">{WB}</a>' if web else ''
    return f'<div class="tcard"><div class="ph"><div class="ini">{ini}</div><img src="media/{ph}" alt="{name}" loading="lazy" onerror="this.remove()"></div><div class="tb"><div class="role">{role}</div><h3>{name}</h3><p>{bio}</p><div class="tc"><a href="tel:{tel}" aria-label="Ring">{PH}</a><a href="mailto:{mail}" aria-label="E-post">{MLs}</a>{wl}</div></div></div>'
about=f'''<section class="page-hero"><div class="ph-bg"><img src="media/about.jpg" alt=""></div><div class="wrap"><span class="eyebrow c">Om oss</span><h1>Dette er <span class="g">Altivon</span></h1><p>Vi gjør drone- og inspeksjonsdata om til strategisk innsikt for eiendomsbesittere og forvaltere i Oslo-området.</p><div class="crumb"><a href="index.html">Hjem</a> → Om oss</div></div></section>
<section class="sec"><div class="wrap">
  <div class="split rev"><div class="split-media"><img src="media/about.jpg" alt="Altivon drone ved fasade"></div><div><span class="eyebrow">Vår visjon</span><h3>Et beslutningsgrunnlag for hvert bygg</h3><p>Enhver eiendomsbesitter fortjener å ta beslutninger på data – ikke antakelser. Vi gjør teknologien, bildene og analysen enkel nok til at enhver forvalter kan handle på den.</p><ul class="checks"><li>Erstatt antakelser med dokumentert grunnlag</li><li>Kortere vei fra befaring til beslutning</li><li>Rene bygg og trygge, prioriterte tiltak</li></ul></div></div>
  <div class="split flip rev"><div class="split-media"><img src="media/gallery-3.jpg" alt="Altivon i arbeid"></div><div><span class="eyebrow">Vårt oppdrag</span><h3>Fra observasjon til beslutning</h3><p>Vi kombinerer sertifiserte droneoperatører med praktisk fagkunnskap innen fasade og vindusvask, og leverer resultater og dokumentasjon som eiere, styrer og forvaltere kan stole på.</p><ul class="checks"><li>Rene bygg med skånsomme metoder</li><li>Strukturert dokumentasjon på hvert oppdrag</li><li>Samme standard, hvert prosjekt</li></ul></div></div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="split rev"><div><span class="eyebrow">Hvem vi er</span><h3>Fagkunnskap møter teknologi</h3><p>Altivon ble startet for å modernisere utvendig vedlikehold og inspeksjon av bygg. Vi kombinerer tradisjonelt håndverk med droneteknologi og strukturert dokumentasjon – slik at kundene får både et rent bygg og et grunnlag for gode beslutninger.</p><p>I dag jobber vi for boligselskaper, næringsbygg og eiendomsforvaltere som trenger dokumentasjon de kan bruke – ikke bare bilder.</p>
    <div class="wstats"><div class="wstat"><div class="n">2026</div><div class="l">Grunnlagt</div></div><div class="wstat"><div class="n">A1–STS</div><div class="l">Sertifiserte operatører</div></div><div class="wstat"><div class="n">Oslo</div><div class="l">Dekningsområde</div></div><div class="wstat"><div class="n">Forsikret</div><div class="l">Registrert operatør</div></div></div>
  </div><div class="split-media"><img src="media/gallery-4.jpg" alt="Altivon på oppdrag"></div></div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head rev"><span class="eyebrow">Det vi står for</span><h2>Fire verdier som styrer hvert prosjekt</h2><p>Prinsippene bak hver inspeksjon, hver rapport og hver samtale med en byggeier.</p></div>
  <div class="values rev">
    <div class="value"><div class="vn">01</div><h3>Dokumentasjon, ikke synsing</h3><p>Hver anbefaling er forankret i dokumenterte data. Ingen gjetning.</p></div>
    <div class="value"><div class="vn">02</div><h3>Fart med standard</h3><p>Dager, ikke måneder – aldri på bekostning av kvalitet.</p></div>
    <div class="value"><div class="vn">03</div><h3>Eier først</h3><p>Vi jobber for byggeieren. Rapporter bygges så et styremedlem kan handle på dem.</p></div>
    <div class="value"><div class="vn">04</div><h3>Tryggere og renere</h3><p>Dronemetoder reduserer risiko og rigg – og gir et bedre resultat.</p></div>
  </div>
</div></section>
<section class="sec alt" id="team"><div class="wrap">
  <div class="sec-head rev"><span class="eyebrow">Teamet</span><h2>Folkene bak Altivon</h2><p>Fagkunnskap innen fasade og vindusvask, kombinert med spisskompetanse på droneteknologi.</p></div>
  <div class="team-grid rev">{''.join(tcard(m) for m in TEAM)}</div>
</div></section>
{cta("Ta en prat med oss","Ring eller send noen linjer om bygget ditt. Vi svarer raskt og ærlig.")}'''
page('om-oss.html','om-oss.html','Om Altivon – fagkunnskap og droneekspertise','Altivon kombinerer sertifiserte droneoperatører med erfaring fra fasade og vindusvask. Møt teamet og verdiene våre.',about)

# KONTAKT
kont=f'''<section class="page-hero"><div class="ph-bg"><img src="media/gallery-2.jpg" alt=""></div><div class="wrap"><span class="eyebrow c">Kontakt</span><h1>La oss <span class="g">snakke</span></h1><p>Fortell oss hva som skal vaskes eller inspiseres, så svarer vi raskt med omfang, tidspunkt og et tydelig tilbud.</p><div class="crumb"><a href="index.html">Hjem</a> → Kontakt</div></div></section>
<section class="sec"><div class="wrap form-grid">
  <div class="rev"><span class="eyebrow">Be om tilbud</span><h2 style="font-size:clamp(1.7rem,3.4vw,2.4rem);margin:16px 0 14px">Fortell oss om bygget</h2><p style="color:var(--muted);margin-bottom:24px">Hvert bygg er forskjellig. Del oppdraget ditt og legg gjerne ved bilder, så anbefaler vi den best egnede metoden.</p>
    <div class="form">
      <div class="row"><div class="field"><label>Navn *</label><input id="f-name" type="text" placeholder="Ditt navn" autocomplete="name"></div><div class="field"><label>Telefon</label><input id="f-phone" type="tel" placeholder="Telefonnummer" autocomplete="tel"></div></div>
      <div class="field"><label>E-post *</label><input id="f-email" type="email" placeholder="din@epost.no" autocomplete="email"></div>
      <div class="field"><label>Adresse på bygg</label><input id="f-addr" type="text" placeholder="Gateadresse, sted"></div>
      <div class="field"><label>Beskrivelse</label><textarea id="f-msg" placeholder="Hva trenger du hjelp til? Type bygg, ønsket tidspunkt …"></textarea></div>
      <div class="field"><label>Bilder av bygget (valgfritt – inntil 10)</label><input id="f-files" type="file" accept="image/*" multiple><div class="filehint" id="f-hint">JPG/PNG, maks 10 bilder (ca. 9 MB til sammen).</div></div>
      <button class="btn btn-primary" id="fsend" style="width:100%;justify-content:center">Send forespørsel {AR}</button>
      <div class="fstatus" id="fstatus" role="status"></div>
      <p class="note">Ved å sende samtykker du til å bli kontaktet om henvendelsen. Vi deler ikke dine data.</p>
    </div>
  </div>
  <div class="rev"><div class="contact-alt"><span class="eyebrow">Snakk direkte</span><h3>Vil du heller snakke med noen direkte?</h3><p>Ikke alt starter med et skjema. Vil du diskutere behovet, er vi tilgjengelige på telefon eller e-post.</p>
    <a href="tel:+4791576447" class="contact-line"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg><span><b>+47 915 76 447</b><span>Man–fre 08–16</span></span></a>
    <a href="mailto:mathias@altivon.no" class="contact-line"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg><span><b>mathias@altivon.no</b><span>Svar innen én virkedag</span></span></a>
    <div class="contact-line"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg><span><b>Madserud allé 2</b><span>0274 Oslo</span></span></div>
    <div class="office-map"><iframe title="Kart – Altivon" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Madserud%20all%C3%A9%202,%200274%20Oslo&output=embed"></iframe></div>
  </div></div>
</div></section>'''
page('kontakt.html','kontakt.html','Kontakt Altivon – be om tilbud','Fortell oss hva som skal vaskes eller inspiseres. Legg ved bilder. Vi svarer raskt. Madserud allé 2, Oslo.',kont)

takk=f'''<section class="page-hero" style="min-height:60vh;display:flex;align-items:center"><div class="wrap">
  <div style="width:74px;height:74px;border-radius:50%;background:var(--green);display:flex;align-items:center;justify-content:center;margin:0 auto 22px;box-shadow:0 20px 44px -18px var(--green)"><svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg></div>
  <h1>Takk! <span class="g">Meldingen er sendt.</span></h1>
  <p>Vi har mottatt henvendelsen din og svarer så raskt vi kan – normalt innen én virkedag. Haster det? Ring oss på <a href="tel:+4791576447" style="color:var(--green);font-weight:600">+47 915 76 447</a>.</p>
  <div style="margin-top:30px;display:flex;gap:14px;justify-content:center;flex-wrap:wrap"><a href="index.html" class="btn btn-primary">Til forsiden {AR}</a><a href="prosjekter.html" class="btn btn-ghost">Se prosjekter</a></div>
</div></section>'''
page('takk.html','','Takk – meldingen er sendt | Altivon','Vi har mottatt henvendelsen din og svarer så raskt vi kan.',takk)


# ============ FAQ (fra kundens dokument) ============
import json as _json
_FAQ=_json.loads(r'''[["Metode og gjennomføring", [["Hvordan foregår en fasadevask med drone -- steg for steg?", "Et oppdrag starter med en befaring, enten fysisk eller ut fra bilder og kartmål, der vi vurderer materiale, tilstand og tilkomst og velger metode. På vaskedagen rigges pumpe og vanntilførsel på bakken, og området sikres. En sertifisert operatør styrer dronen systematisk over fasaden – som regel fra topp til bunn – og påfører vann og et skånsomt, biologisk nedbrytbart middel gjennom en spesialdyse. På ømfintlige flater brukes softwash med lavt trykk. Til slutt dokumenteres resultatet med foto før og etter. Hele tiden står personellet trygt på bakken."], ["Hvorfor drone i stedet for stillas, lift eller tauarbeid?", "Fordi det for vask og inspeksjon som regel er raskere, rimeligere og tryggere. Det er ingen rigg som skal opp og ned, ingen sperring av fortau, og ingen jobber i høyden. En jobb som ville tatt uker med stillas, gjøres ofte på én til to dager. Begrensningen er oppgaver som krever fysisk berøring – reparasjon, fuging, maling – der stillas, lift eller tau fortsatt trengs. Ofte lønner det seg å kombinere: en droneinspeksjon først viser nøyaktig hvor fysisk utbedring trengs, slik at riggen står kortest mulig."], ["Fungerer dronevask på alle fasadematerialer?", "Ja. Metoden brukes på betong, tegl, mur, naturstein, trepanel, fasadeplater, metallkledning og glass. Det som endrer seg er trykket og middelet: ømfintlige flater som puss, malt tre og eldre tegl vaskes skånsomt med softwash og lavt trykk, mens mer robuste flater tåler mer. Riktig tilpasning til materialet er nettopp det som skiller en fagmessig vask fra en som kan gjøre skade."], ["Hvor rene blir egentlig fasaden og vinduene?", "Målet er et synlig og varig resultat. På vinduer gir rent (avionisert) vann et stripefritt resultat uten såperester, fordi det er mineraler og såpe som lager striper. På fasade fjerner softwash både det synlige belegget og selve begroingen, slik at algene og soppen dør og flaten holder seg ren lenger. På kraftig begrodde flater fortsetter effekten å utvikle seg i ukene etter vask, når nedbøren skyller bort døde sporer."], ["Kan dere vaske solcellepaneler og tak også?", "Ja. Solcellepaneler vaskes skånsomt med rent vann og lavt trykk for å hente tilbake produksjon uten å skade antirefleksbelegg eller pakninger – og uten at noen går på taket. Tak renses for mose og begroing med skånsom metode og mosemiddel, slik at fukt og frost ikke bryter ned takflaten. Begge deler kan kombineres med droneinspeksjon i samme oppdrag."], ["Hvor lang tid tar et oppdrag?", "Det avhenger av byggets størrelse, tilstand og kompleksitet, men de fleste bygg vaskes på én til to dager – mot flere uker med stillas, fordi det ikke er noe rigg som skal opp og ned. Et mindre bygg kan være ferdig på noen timer. Du får alltid et konkret tidsestimat i tilbudet."]]], ["Trygghet, skader og miljø", [["Skader dronevask fasaden?", "Nei – riktig utført er dronevask skånsommere enn ukyndig høytrykksspyling. Trykk, avstand og middel tilpasses materialet, og på ømfintlige flater brukes softwash med lavt trykk som løser opp begroing i stedet for å blåse den bort. Det er feil bruk av høytrykk – uansett tilkomstmetode – som skader fasader, ikke dronen. Er du usikker på hva flaten tåler, tester vi gjerne en liten flate først på befaringen."], ["Er det trygt for beboere og folk rundt bygget mens dere jobber?", "Ja. Beboerne kan være hjemme og ferdes normalt; vi anbefaler bare at vinduer holdes lukket og at biler flyttes bort fra flaten som vaskes. Arbeidsområdet sikres, operasjonen risikovurderes før dronen letter, og vi varsler beboere når det er relevant. Fordi ingen jobber i høyden og det ikke settes opp stillas, fjernes flere av de vanligste risikoene helt."], ["Hvilke vaskemidler bruker dere -- er de miljøvennlige?", "Vi bruker biologisk nedbrytbare midler uten skadelige kjemikalier, og på vinduer ofte bare rent vann helt uten middel. Avrenning håndteres bevisst, med hensyn til beplantning, husdyr og avløp. Målet er et effektivt resultat med minst mulig miljøavtrykk."], ["Hva skjer hvis dere oppdager en skade under vask eller inspeksjon?", "Da dokumenterer vi den med daterte, stedfestede bilder og tar den med i rapporten, gradert etter alvorlighet (akutt, bør utbedres, observeres) og med en anbefaling om tiltak. Slik blir en tilfeldig observasjon til noe du kan handle på – ofte oppdages små ting (løse beslag, begynnende riss, tett takrenne) i tide, mens de er billige å utbedre."], ["Er dere forsikret hvis noe skulle gå galt?", "Ja. Ansvarsforsikring for droneoperasjoner er lovpålagt, og vi opererer med gyldig forsikring. Sammen med registrering hos Luftfartstilsynet, gyldige sertifikater og risikovurdering av hvert oppdrag betyr det at ansvaret er ivaretatt – noe du alltid bør kreve dokumentert av enhver droneleverandør."]]], ["Pris og bestilling", [["Hva koster fasadevask med drone?", "Prisen avhenger av areal, tilstand, materiale, tilkomst og høyde. Areal er den viktigste driveren, og tilstand nummer to: en fasade som vaskes jevnlig krever mindre tid og middel enn en som ikke er vedlikeholdt på mange år. Nettopp derfor gir de fleste seriøse aktører ikke en fast pris uten befaring – forholdene varierer for mye fra bygg til bygg. Send oss adresse, noen bilder og en kort beskrivelse, så gir vi et estimat raskt og et bindende tilbud etter en kostnadsfri befaring."], ["Hvorfor kan jeg ikke få en fast kvadratmeterpris med en gang?", "Fordi to bygg med samme areal kan kreve svært ulik innsats. Grad av begroing, fasadematerial, antall detaljer, tilgang til vann og fri flyplass påvirker alle tidsbruken. En fast «per m²»-pris uten å ha sett bygget ville enten vært for høy (for å ta høyde for det verste) eller for lav. Et raskt estimat basert på bilder, bekreftet med befaring, gir deg en riktigere pris."], ["Er dronevask billigere enn stillas?", "På høye bygg som regel ja, når du regner totalkostnad. Med stillas betaler du for montering, leie i hele perioden og demontering – ofte over uker – pluss eventuell leie for å sperre fortau. Disse kostnadene kan overstige selve vasken. Med drone er riggen nede på timer. Sammenlign derfor totalkostnaden for hele jobben, ikke bare «vaskeprisen»."], ["Hva bør jeg sende for å få et raskt tilbud?", "Adresse (så vi kan se bygget på kart), noen bilder av fasaden eller taket, og en kort beskrivelse av hva du ønsker gjort. Jo mer vi vet om tilstand og tilkomst, desto mer presist blir estimatet. Deretter bekrefter vi med en kostnadsfri, uforpliktende befaring."], ["Tilbyr dere faste vedlikeholdsavtaler?", "Ja. Mange kunder foretrekker en årsavtale der vi følger opp intervallene for vask, takrens og inspeksjon automatisk – da slipper du å huske på det selv, og bygget holder jevn standard. Vi tilpasser omfang og hyppighet etter bygget og behovet, og du får forutsigbar økonomi."], ["Hvilke områder dekker dere?", "Vi holder til på Madserud allé 2 i Oslo og betjener Oslo-området. Ta kontakt med adressen din, så bekrefter vi at vi kan ta oppdraget – eller hjelper deg videre."]]], ["Dokumentasjon, inspeksjon og termografi", [["Hva slags dokumentasjon får jeg etter et oppdrag?", "Som minimum foto før og etter. Ved inspeksjon får du en strukturert tilstandsrapport: funn som er stedfestet på bygget, gradert etter alvorlighet og fulgt av anbefalte tiltak, samt oversiktsbilder som viser omfang. Rapporten er laget for å kunne legges rett inn i styrepapirer, vedlikeholdsplan eller en forsikringssak."], ["Hva er forskjellen på vanlig (RGB) inspeksjon og termografi?", "En visuell RGB-inspeksjon bruker et høyoppløselig fargekamera og viser synlige forhold – riss, avskalling, skadde fuger, knekt takstein, korrosjon. Termografi bruker et termisk kamera og viser skjulte forhold – varmetap, kuldebroer og fukt – ved å måle temperaturforskjeller på overflatene. De utfyller hverandre, og kombineres ofte i samme oppdrag for å fange både det synlige og det skjulte."], ["Hva kan termografi avdekke?", "Dårlig eller manglende isolasjon og kuldebroer (varme felt som lekker ut på en kald dag), skjult fukt og lekkasjer (fuktige materialer holder en annen temperatur enn tørre), luftlekkasjer ved vinduer og dører, og defekte solceller (som går varmere enn friske). Det gir et konkret grunnlag for å prioritere etterisolering, tetting eller utbedring der det faktisk monner."], ["Når på året bør termografi gjøres?", "Bygningstermografi krever temperaturforskjell mellom inne og ute, så kalde, gjerne overskyede dager i fyringssesongen (vinter og tidlig vår) gir de tydeligste resultatene. Solcelleinspeksjon er motsatt – der trengs sol på panelene for at defekte celler skal skille seg ut. Vi planlegger tidspunktet etter hva som skal måles."], ["Hvor nøyaktige er 3D-modellene og målingene?", "Med riktig flyplan, kalibrering og bakkekontrollpunkter oppnås centimeternøyaktighet, og vi dokumenterer oppnådd nøyaktighet i leveransen. Modeller og punktskyer leveres i standardformater for CAD, GIS og BIM (som GeoTIFF, LAS/LAZ og E57), eller som nettbasert visning du kan måle i via en lenke – uten spesialprogramvare."], ["Kan droneinspeksjon erstatte en tradisjonell takst eller tilstandsvurdering?", "Droneinspeksjon gir svært god dekning av synlig tilstand på tak, fasade og detaljer i høyden – ofte bedre enn en manuell befaring, og helt uten arbeid i høyden. Enkelte forhold krever likevel fysisk kontroll eller en autorisert takstmann. Vi er tydelige på hva metoden dekker, og inspeksjonen er et sterkt supplement til – og noen ganger et godt førstesteg før – en full tilstandsvurdering."]]], ["Borettslag, sameier og forvaltere", [["Hvem i borettslaget eller sameiet kan bestille?", "Styreleder eller forretningsfører bestiller normalt på vegne av fellesskapet. Enkeltoppdrag innenfor ordinær vedlikeholdsramme kan styret bestille direkte, uten vedtak i generalforsamling/sameiermøte. Flerårige avtaler som binder laget over tid, eller som påvirker felleskostnadene, bør derimot forankres i budsjettet som vedtas av eierne. Vi bistår gjerne med saksunderlag."], ["Kan dere levere ferdig saksunderlag til styret?", "Ja. Vi kan levere et kort underlag tilpasset styremøtet: beskrivelse av metoden, sammenligning mot stillas og lift, prisestimat for byggets areal, en enkel HMS-vurdering og forslag til vedtak. Det gjør det enklere for styret å fatte en beslutning på faktisk grunnlag."], ["Hva sier borettslagsloven om utvendig vedlikehold?", "Ansvaret for utvendig vedlikehold av fasade, tak og fellesarealer ligger på borettslaget/sameiet som helhet, ikke på den enkelte andels- eller seksjonseier. Styret har dermed en plikt til å holde bygget i forsvarlig stand. Dokumentert fasadevask og en tilstandsrapport er et konkret tiltak som viser at vedlikeholdsplikten ivaretas – og som er nyttig ved et eventuelt styreskifte eller salg."], ["Hvordan dokumenteres jobben for protokoll og forsikring?", "Hver leveranse følges av en strukturert rapport i PDF: bilder før og etter, beskrivelse av utført arbeid, middel som er brukt, observerte avvik og anbefalte tiltak. Rapporten kan legges som vedlegg til styreprotokoll, brukes ved forsikringsoppgjør og inngå i byggets vedlikeholdshistorikk."], ["Merker beboerne noe til arbeidet?", "Svært lite. Det settes ikke opp stillas langs fasaden i ukevis, og parkering og fortau holdes i hovedsak åpne. Arbeidet gjøres utenfra, og vi koordinerer med styret og bistår med beboervarsling i forkant. For de fleste beboere er den største merkbare forskjellen at bygget plutselig er rent."], ["Får vi en fast kontaktperson?", "Ja. Med en løpende avtale får dere en kontaktperson som kjenner bygget – fasadetype, historikk og tidligere oppdrag. Det gir kontinuitet på tvers av oppdrag og raskere oppfølging ved spørsmål eller akutte behov."]]], ["Regelverk, sikkerhet og personvern", [["Hva bør jeg kreve av en droneoperatør for å vite at det er trygt og lovlig?", "Be om tre ting før avtale: operatørnummer (registrering hos Luftfartstilsynet), pilotenes sertifikater (A1/A3 og A2 i åpen kategori, og STS for mer krevende operasjoner nær folk og bygg), og gyldig forsikringsbevis. En seriøs leverandør deler dette uten motforestillinger. Hos Altivon er teknisk ansvarlig sertifisert med A1, A2, A3 og STS, og hvert oppdrag risikovurderes før dronen letter."], ["Er det lov å fly drone tett på bygg i tettbygd strøk?", "Ja, men det er regulert, og krever riktig kompetansenivå og planlegging. Flyging nær mennesker, bygg og trafikk hører gjerne inn under strengere kategorier (som standardscenarioene/STS i spesifikk kategori). En profesjonell operatør planlegger operasjonen slik at avstandskrav overholdes og omgivelsene ikke utsettes for risiko."], ["Hvordan ivaretar dere personvern når dere filmer bygg?", "Kameraet brukes til oppdraget – å dokumentere bygget – ikke til å filme naboer eller inn i vinduer. Vi planlegger flyging og bildetaking slik at personvernet ivaretas, og materialet håndteres og deles kun med kunden. Ved oppdrag på borettslag varsles beboere når det er relevant."], ["Er dronevask og -inspeksjon HMS-messig tryggere enn tradisjonelle metoder?", "Ja. God HMS-praksis sier at risiko helst skal fjernes, ikke bare sikres. Når vask og inspeksjon kan gjøres uten at noen forlater bakken, fjernes fallrisikoen ved kilden, og man unngår stillas som selv utgjør en risiko (klatring, fallende gjenstander, innbruddsvei). For byggeier betyr det lavere risiko og enklere ansvarsforhold."]]], ["Sesong, vær og praktisk", [["Når på året bør jeg vaske?", "Våren er høysesong: da fjernes vinterens veistøv, salt og pollen, og bygget står rent gjennom sommeren. Takrens og mosebehandling passer godt om sommeren og tidlig høst, slik at middelet får virke før frosten. Vinteren egner seg best til inspeksjon og termografi. Bestill vårvask tidlig – kapasiteten fylles raskt."], ["Kan dere jobbe om vinteren?", "Vask med vann krever temperaturer over frysepunktet, så streng kulde begrenser vaskeoppdrag. Inspeksjon og særlig termografi er derimot ideelt om vinteren, fordi temperaturforskjellen mellom inne og ute er størst da og varmetap vises tydeligst."], ["Hva med vær og vind på selve dagen?", "Droneflyging er væravhengig. Sterk vind, kraftig nedbør eller dårlig sikt kan gjøre at et oppdrag flyttes til en bedre dag av sikkerhets- og kvalitetshensyn. Vi følger værmeldingen tett og avtaler nytt tidspunkt ved behov – trygg og god gjennomføring går alltid foran å presse gjennom en flyging."], ["Må jeg være til stede når dere kommer?", "Vanligvis ikke, så lenge vi har tilgang til bygget, en fri flyplass og et vannuttak. Vi avtaler det praktiske på forhånd. For borettslag og sameier koordinerer vi med styret eller forvalter."], ["Hvor ofte bør bygget vaskes og inspiseres?", "En vanlig rytme er vindusvask årlig (gjerne vår), fasadevask og takrens hvert 1.–3. år etter behov, og en droneinspeksjon årlig som viser når vask faktisk trengs og fanger opp skader tidlig. Beliggenhet betyr mye: nordvendte, skyggefulle eller kystnære bygg trenger hyppigere oppfølging. Med en vedlikeholdsavtale følger vi opp intervallene for deg."]]]]''')
def _qa(q,a): return f'<details class="qa"><summary>{q}</summary><div class="qa-a"><p>{a}</p></div></details>'
_secs=''
for _s,_items in _FAQ:
    _secs+=f'<h2 class="faq-h rev">{_s}</h2><div class="rev">'+''.join(_qa(q,a) for q,a in _items)+'</div>'
faqpage=f'''<section class="page-hero"><div class="wrap"><span class="eyebrow c">FAQ</span><h1>Ofte stilte <span class="g">spørsmål</span></h1><p>Alt du lurer på om dronevask, inspeksjon, termografi, pris, sikkerhet og gjennomføring – ærlig besvart.</p><div class="crumb"><a href="index.html">Hjem</a> → FAQ</div></div></section>
<section class="sec" style="padding-top:52px"><div class="wrap" style="max-width:860px">{_secs}
<div style="margin-top:44px;background:var(--green-soft);border-radius:18px;padding:28px;text-align:center">
<h2 style="margin:0 0 8px;font-size:1.3rem">Fant du ikke svaret?</h2>
<p style="margin-bottom:18px">Still spørsmålet ditt direkte – vi svarer raskt og ærlig.</p>
<a href="kontakt.html" class="btn btn-primary">Kontakt oss {AR}</a></div>
</div></section>'''
page('faq.html','faq.html','FAQ – ofte stilte spørsmål | Altivon','Svar på de vanligste spørsmålene om fasadevask med drone, inspeksjon, termografi, pris, sikkerhet, borettslag og gjennomføring.',faqpage)


# ============ GALLERI ============
_ZOOM='<span class="zoom"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M14 10l7-7M9 21H3v-6M10 14l-7 7"/></svg></span>'
_vids=[('video/klipp-1.mp4','media/gallery-1.jpg','Fasadevask med drone'),('video/klipp-2.mp4','media/gallery-2.jpg','Vindusvask i høyden'),('video/klipp-3.mp4','media/gallery-3.jpg','Inspeksjon av tak'),('video/klipp-4.mp4','media/gallery-4.jpg','Skylling av fasade'),('video/klipp-5.mp4','media/gallery-5.jpg','Dronen i arbeid'),('hero.mp4','media/gallery-7.jpg','Altivon i Oslo')]
_vgrid=''.join(f'<div class="vtile rev"><video controls preload="metadata" playsinline poster="{p}"><source src="media/{v}" type="video/mp4"></video><span class="cap">{t}</span></div>' for v,p,t in _vids)
_fotos=[('gallery-1.jpg','Fasadevask, boligblokk'),('gallery-2.jpg','Vindusvask med rent vann'),('gallery-3.jpg','Dronen rigges'),('gallery-4.jpg','Fasade under vask'),('gallery-5.jpg','Inspeksjon av takflate'),('gallery-6.jpg','Takrens'),('gallery-7.jpg','Oversiktsbilde'),('gallery-8.jpg','Detalj i høyden'),('about.jpg','Altivon i Oslo'),('before.jpg','Før vask'),('after.jpg','Etter vask'),('hero-poster.jpg','Fra lufta')]
_fgrid=''.join(f'<div class="galtile rev" style="transition-delay:{(i%4)*60}ms"><img src="media/{f}" alt="{c}" loading="lazy">{_ZOOM}<span class="cap">{c}</span></div>' for i,(f,c) in enumerate(_fotos))
galpage=f'''<section class="page-hero"><div class="wrap"><span class="eyebrow c">Galleri</span><h1>Foto og <span class="g">video</span> fra oppdrag</h1><p>Et innblikk i hvordan vi jobber – fasadevask, vindusvask, takrens og inspeksjon, fra lufta og bakken.</p><div class="crumb"><a href="index.html">Hjem</a> → Galleri</div></div></section>
<section class="sec" style="padding-top:52px"><div class="wrap">
  <div class="sec-head c rev"><span class="eyebrow c">Foto</span><h2>Et utvalg av arbeidet vårt</h2><p>Bilder fra fasadevask, vindusvask, takrens og droneoppdrag. Klikk for å se større.</p></div>
  <div class="galgrid">{_fgrid}</div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="sec-head c rev"><span class="eyebrow c">Video</span><h2>Se hvordan vi jobber</h2><p>Korte klipp fra ekte oppdrag.</p></div>
  <div class="vgrid">{_vgrid}</div>
</div></section>'''
page('galleri.html','galleri.html','Galleri – foto og video | Altivon','Foto og video fra Altivons oppdrag: fasadevask, vindusvask, takrens og droneinspeksjon i Oslo-området.',galpage)

print("BUILD OK:", sorted(f for f in os.listdir(OUT) if f.endswith('.html')))

#!/usr/bin/env python3
"""Generate topic-matched SVG header illustrations for Altivon articles (brand green)."""
import os
OUT='/home/claude/design2/media/art'
os.makedirs(OUT,exist_ok=True)

W,H=1200,675
G='#12b06a';GD='#0d9c5e';GDD='#0a3527';SOFT='#e7f6ee';INK='#0c1f17';MUT='#8aa89a'

def wrap(inner,sky1='#f3fbf6',sky2='#e3f4ea'):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky1}"/><stop offset="1" stop-color="{sky2}"/></linearGradient>
<linearGradient id="gg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{G}"/><stop offset="1" stop-color="{GD}"/></linearGradient>
<linearGradient id="thermal" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#2036a8"/><stop offset=".45" stop-color="#8a2fb8"/><stop offset=".75" stop-color="#f2542d"/><stop offset="1" stop-color="#ffd23f"/></linearGradient>
<filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="{GDD}" flood-opacity="0.18"/></filter>
</defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
<circle cx="1030" cy="120" r="210" fill="{SOFT}" opacity=".7"/>
<circle cx="140" cy="560" r="160" fill="{SOFT}" opacity=".5"/>
{inner}
</svg>'''

def drone(x,y,s=1.0,tilt=0):
    return f'''<g transform="translate({x},{y}) scale({s}) rotate({tilt})" filter="url(#soft)">
<rect x="-38" y="-8" width="76" height="20" rx="10" fill="{GDD}"/>
<rect x="-14" y="6" width="28" height="14" rx="5" fill="{INK}"/>
<circle cx="0" cy="16" r="5" fill="{G}"/>
<line x1="-38" y1="0" x2="-74" y2="-16" stroke="{GDD}" stroke-width="7" stroke-linecap="round"/>
<line x1="38" y1="0" x2="74" y2="-16" stroke="{GDD}" stroke-width="7" stroke-linecap="round"/>
<ellipse cx="-74" cy="-20" rx="30" ry="6" fill="{G}" opacity=".85"/>
<ellipse cx="74" cy="-20" rx="30" ry="6" fill="{G}" opacity=".85"/>
<ellipse cx="-74" cy="-20" rx="30" ry="6" fill="none" stroke="{GDD}" stroke-width="2"/>
<ellipse cx="74" cy="-20" rx="30" ry="6" fill="none" stroke="{GDD}" stroke-width="2"/>
</g>'''

def building(x,y,w,h,cols=4,rows=6,fill='#ffffff',winfill=SOFT,rx=14):
    winw=(w-40)/cols-14; winh=(h-40)/rows-16
    wins=''
    for r in range(rows):
        for c in range(cols):
            wx=x+26+c*((w-40)/cols); wy=y+26+r*((h-40)/rows)
            wins+=f'<rect x="{wx:.0f}" y="{wy:.0f}" width="{winw:.0f}" height="{winh:.0f}" rx="4" fill="{winfill}" stroke="#d6e5dc"/>'
    return f'<g filter="url(#soft)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="#e6efe9"/>{wins}</g>'

def spray(x,y,angle=-35):
    drops=''.join(f'<circle cx="{x-i*26}" cy="{y+i*16}" r="{4+i%3}" fill="{G}" opacity="{0.85-i*0.07}"/>' for i in range(1,9))
    return f'<path d="M{x} {y} q -90 40 -190 130" stroke="{G}" stroke-width="10" fill="none" stroke-linecap="round" opacity=".55"/>'+drops

def ground():
    return f'<rect x="0" y="{H-60}" width="{W}" height="60" fill="{SOFT}"/><line x1="0" y1="{H-60}" x2="{W}" y2="{H-60}" stroke="#d6e5dc" stroke-width="3"/>'

ART={}

# 1 facade wash
ART['facade-wash']=wrap(ground()+building(180,150,360,465)+drone(760,240,1.25)+spray(700,270)+
  f'<path d="M300 220 q 14 26 0 44 q -14 -18 0 -44z" fill="{G}" opacity=".5"/><path d="M420 330 q 12 22 0 38 q -12 -16 0 -38z" fill="{G}" opacity=".4"/>')
# 2 window
ART['window']=wrap(ground()+f'''<g filter="url(#soft)"><rect x="330" y="120" width="540" height="430" rx="18" fill="#fff" stroke="#e6efe9"/>
<rect x="360" y="150" width="228" height="180" fill="#dff3ff"/><rect x="612" y="150" width="228" height="180" fill="#dff3ff"/>
<rect x="360" y="354" width="228" height="166" fill="#dff3ff"/><rect x="612" y="354" width="228" height="166" fill="#eaf8ff"/>
<path d="M612 354 h228 v70 q -120 40 -228 0 z" fill="{G}" opacity=".25"/>
<path d="M640 300 l150 -120" stroke="#fff" stroke-width="16" opacity=".8" stroke-linecap="round"/>
<path d="M400 480 l120 -90" stroke="#fff" stroke-width="12" opacity=".8" stroke-linecap="round"/></g>'''+drone(960,200,1.1)+
  f'<path d="M905 235 q -40 40 -60 90" stroke="{G}" stroke-width="9" fill="none" stroke-linecap="round" opacity=".6"/>')
# 3 roof moss
ART['roof']=wrap(ground()+f'''<g filter="url(#soft)"><path d="M240 360 L600 160 L960 360 Z" fill="#fff" stroke="#e6efe9"/>
<path d="M240 360 L600 160 L960 360" fill="none" stroke="{GD}" stroke-width="10" stroke-linejoin="round"/>
<rect x="320" y="360" width="560" height="200" fill="#fff" stroke="#e6efe9"/>
<rect x="380" y="410" width="90" height="110" rx="6" fill="{SOFT}"/><rect x="560" y="410" width="90" height="110" rx="6" fill="{SOFT}"/><rect x="730" y="410" width="90" height="110" rx="6" fill="{SOFT}"/>
<circle cx="430" cy="300" r="16" fill="{G}" opacity=".55"/><circle cx="500" cy="262" r="12" fill="{G}" opacity=".5"/><circle cx="562" cy="238" r="15" fill="{G}" opacity=".6"/><circle cx="668" cy="250" r="11" fill="{G}" opacity=".45"/><circle cx="740" cy="292" r="17" fill="{G}" opacity=".55"/>
</g>'''+drone(880,150,1.15))
# 4 solar
ART['solar']=wrap(ground()+f'''<circle cx="220" cy="150" r="70" fill="#ffd23f" opacity=".9"/>
<g filter="url(#soft)" transform="translate(330,250)">
<g transform="skewX(-18)"><rect x="0" y="0" width="560" height="280" rx="10" fill="{GDD}"/>
{''.join(f'<rect x="{16+c*136}" y="{16+r*90}" width="120" height="76" rx="6" fill="#12406b"/>' for r in range(3) for c in range(4))}
<rect x="16" y="16" width="120" height="76" rx="6" fill="#f2542d"/></g></g>'''+drone(860,160,1.1)+
  f'<path d="M815 195 q -30 40 -45 80" stroke="{G}" stroke-width="9" fill="none" stroke-linecap="round" opacity=".6"/>')
# 5 softwash
ART['softwash']=wrap(ground()+building(200,150,340,465,3,6)+f'''
<g opacity=".9">{''.join(f'<circle cx="{620+ (i*53)%330}" cy="{200+(i*97)%330}" r="{10+(i%4)*6}" fill="{G}" opacity="{0.16+(i%5)*0.1}"/>' for i in range(14))}</g>
<circle cx="800" cy="330" r="86" fill="none" stroke="{GD}" stroke-width="10" opacity=".6"/>
<circle cx="800" cy="330" r="54" fill="none" stroke="{G}" stroke-width="8" opacity=".7"/>''')
# 6 season
ART['season']=wrap(ground()+f'''<g filter="url(#soft)"><rect x="330" y="150" width="540" height="420" rx="20" fill="#fff" stroke="#e6efe9"/>
<rect x="330" y="150" width="540" height="92" rx="20" fill="url(#gg)"/><rect x="330" y="212" width="540" height="30" fill="{GD}"/>
{''.join(f'<rect x="{368+c*100}" y="{278+r*86}" width="72" height="58" rx="10" fill="{SOFT}"/>' for r in range(3) for c in range(5))}
<rect x="568" y="364" width="72" height="58" rx="10" fill="{G}"/>
</g><circle cx="220" cy="170" r="54" fill="#ffd23f" opacity=".9"/>
<path d="M980 460 l0 60 M955 480 l50 20 M1005 480 l-50 20" stroke="#9fd6ff" stroke-width="9" stroke-linecap="round"/>''')
# 7 rgb zoom
ART['rgb']=wrap(ground()+building(180,140,420,475,4,7)+f'''
<g filter="url(#soft)"><circle cx="760" cy="320" r="150" fill="#fff" stroke="{G}" stroke-width="12"/>
<line x1="866" y1="426" x2="980" y2="540" stroke="{G}" stroke-width="26" stroke-linecap="round"/>
<path d="M690 300 l40 40 l30 -55 l45 60" stroke="#f2542d" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="672" y="250" width="176" height="140" fill="none" stroke="{SOFT}" stroke-width="3" stroke-dasharray="8 8"/></g>'''+drone(1010,160,1.0))
# 8 thermal
ART['thermal']=wrap(ground()+f'''<g filter="url(#soft)"><rect x="330" y="140" width="420" height="475" rx="14" fill="url(#thermal)"/>
{''.join(f'<rect x="{362+c*100}" y="{176+r*76}" width="66" height="52" rx="5" fill="#0c1f17" opacity=".25"/>' for r in range(6) for c in range(4))}
<rect x="430" y="404" width="66" height="52" rx="5" fill="#ffd23f"/>
<rect x="630" y="252" width="66" height="52" rx="5" fill="#ff7847"/></g>
<g transform="translate(920,300)" filter="url(#soft)"><rect x="-64" y="-46" width="128" height="92" rx="14" fill="{GDD}"/><circle cx="0" cy="0" r="30" fill="#111c16" stroke="{G}" stroke-width="6"/><circle cx="0" cy="0" r="10" fill="url(#thermal)"/></g>'''+drone(920,170,1.0),sky1='#eef7ff',sky2='#e3f0ea')
# 9 annual checklist
ART['annual']=wrap(ground()+building(160,180,330,435,3,5)+f'''
<g filter="url(#soft)"><rect x="620" y="150" width="380" height="440" rx="20" fill="#fff" stroke="#e6efe9"/>
<rect x="620" y="150" width="380" height="80" rx="20" fill="url(#gg)"/>
{''.join(f'<g transform="translate(660,{270+i*80})"><circle cx="0" cy="0" r="20" fill="{SOFT}"/><path d="M-8 0 l6 7 l12 -14" stroke="{G}" stroke-width="6" fill="none" stroke-linecap="round"/><rect x="40" y="-9" width="220" height="18" rx="9" fill="{SOFT}"/></g>' for i in range(4))}
</g>'''+drone(400,120,1.0))
# 10 storm
ART['storm']=wrap(ground()+f'''<g filter="url(#soft)"><path d="M240 380 L600 190 L960 380 Z" fill="#fff" stroke="#e6efe9"/><rect x="320" y="380" width="560" height="180" fill="#fff" stroke="#e6efe9"/></g>
<g filter="url(#soft)"><ellipse cx="430" cy="120" rx="130" ry="58" fill="#c8d8d0"/><ellipse cx="560" cy="100" rx="110" ry="50" fill="#b6cabf"/></g>
<path d="M520 160 l-40 80 h44 l-36 84" stroke="#ffd23f" stroke-width="14" fill="none" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M700 250 l70 -36 l16 30 l-70 36 z" fill="{G}" opacity=".8" transform="rotate(14 735 250)"/>
<g stroke="#9fb8ac" stroke-width="7" stroke-linecap="round" opacity=".8"><line x1="880" y1="140" x2="960" y2="120"/><line x1="900" y1="190" x2="990" y2="170"/><line x1="870" y1="240" x2="950" y2="222"/></g>'''
  +drone(1030,300,1.05,8),sky1='#eef3f1',sky2='#dde9e2')
# 11 report
ART['report']=wrap(ground()+f'''<g filter="url(#soft)"><rect x="360" y="130" width="480" height="470" rx="20" fill="#fff" stroke="#e6efe9"/>
<rect x="400" y="180" width="200" height="22" rx="11" fill="{GDD}"/><rect x="400" y="220" width="320" height="14" rx="7" fill="{SOFT}"/>
<rect x="400" y="290" width="90" height="140" fill="{SOFT}"/><rect x="510" y="250" width="90" height="180" fill="{G}"/><rect x="620" y="330" width="90" height="100" fill="{GD}"/>
<line x1="400" y1="430" x2="800" y2="430" stroke="#e6efe9" stroke-width="3"/>
<circle cx="420" cy="480" r="12" fill="{G}"/><rect x="450" y="470" width="260" height="16" rx="8" fill="{SOFT}"/>
<circle cx="420" cy="530" r="12" fill="#ffd23f"/><rect x="450" y="520" width="220" height="16" rx="8" fill="{SOFT}"/>
</g>''')
# 12 ortho (top-down map)
ART['ortho']=wrap(f'''<g filter="url(#soft)"><rect x="240" y="110" width="720" height="470" rx="20" fill="#fff" stroke="#e6efe9"/>
{''.join(f'<line x1="{300+i*90}" y1="110" x2="{300+i*90}" y2="580" stroke="{SOFT}" stroke-width="2"/>' for i in range(8))}
{''.join(f'<line x1="240" y1="{170+i*80}" x2="960" y2="{170+i*80}" stroke="{SOFT}" stroke-width="2"/>' for i in range(6))}
<rect x="330" y="180" width="150" height="110" rx="8" fill="{GD}" opacity=".85"/><rect x="540" y="160" width="110" height="160" rx="8" fill="{G}" opacity=".8"/><rect x="700" y="220" width="180" height="100" rx="8" fill="{GDD}" opacity=".85"/>
<path d="M280 470 q 200 -70 620 -10" stroke="#c9dfd3" stroke-width="26" fill="none" stroke-linecap="round"/>
<circle cx="470" cy="430" r="34" fill="{SOFT}"/><circle cx="820" cy="420" r="26" fill="{SOFT}"/>
</g>'''+drone(600,80,1.0)+f'<path d="M600 108 L600 180 M560 150 L600 180 L640 150" stroke="{G}" stroke-width="6" fill="none" stroke-linecap="round" opacity=".6"/>')
# 13 3d wireframe iso
ART['3d']=wrap(ground()+f'''<g filter="url(#soft)" stroke="{GD}" stroke-width="5" fill="#ffffff">
<path d="M420 480 L420 260 L600 170 L780 260 L780 480 L600 570 Z"/>
<path d="M420 260 L600 350 L780 260 M600 350 L600 570" fill="none"/>
<path d="M420 480 L600 570 L780 480" fill="none"/>
</g>
<g stroke="{G}" stroke-width="2.5" opacity=".75" fill="none">
{''.join(f'<path d="M{420} {300+i*44} L600 {390+i*44} L780 {300+i*44}"/>' for i in range(4))}
{''.join(f'<line x1="{468+i*44}" y1="{284-i*22+0}" x2="{468+i*44}" y2="{504-i*22}"/>' for i in range(0))}
</g>
<circle cx="420" cy="260" r="9" fill="{G}"/><circle cx="600" cy="170" r="9" fill="{G}"/><circle cx="780" cy="260" r="9" fill="{G}"/><circle cx="600" cy="350" r="9" fill="{G}"/><circle cx="420" cy="480" r="9" fill="{G}"/><circle cx="780" cy="480" r="9" fill="{G}"/><circle cx="600" cy="570" r="9" fill="{G}"/>'''
  +drone(920,180,1.05))
# 14 pointcloud
import math,random
random.seed(7)
pts=''
for i in range(420):
    t=random.random()
    if t<0.55:
        x=430+random.random()*340; y=250+random.random()*300
        if 470<x<800 and 250<y<560: pts+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{2.6+random.random()*2.4:.1f}" fill="{G if random.random()>0.35 else GD}" opacity="{0.5+random.random()*0.5:.2f}"/>'
    else:
        x=460+random.random()*280; y=170+ (abs(x-600)/280)*90 + random.random()*26
        pts+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{2.4+random.random()*2:.1f}" fill="{GDD}" opacity="{0.4+random.random()*0.5:.2f}"/>'
ART['pointcloud']=wrap(ground()+pts+drone(900,160,1.05)+
  f'<path d="M860 200 L760 300 M900 210 L820 340 M940 200 L880 320" stroke="{G}" stroke-width="3" opacity=".45"/>')
# 15 volume
ART['volume']=wrap(ground()+f'''<g filter="url(#soft)"><path d="M240 560 q 180 -300 400 -150 q 200 130 320 150 Z" fill="{GD}" opacity=".9"/>
<path d="M240 560 q 180 -300 400 -150" fill="none" stroke="{GDD}" stroke-width="8"/></g>
<g stroke="{G}" stroke-width="5" fill="none" stroke-dasharray="10 8" opacity=".8">
<path d="M300 470 h560"/><path d="M360 380 h420"/><path d="M470 300 h220"/></g>
<g transform="translate(1000,300)"><line x1="0" y1="-120" x2="0" y2="120" stroke="{GDD}" stroke-width="6"/><path d="M-14 -100 L0 -124 L14 -100 M-14 100 L0 124 L14 100" stroke="{GDD}" stroke-width="6" fill="none"/><text x="24" y="8" font-family="Arial" font-size="42" font-weight="bold" fill="{GDD}">m³</text></g>'''
  +drone(560,150,1.05))
# 16 rules shield
ART['rules']=wrap(ground()+f'''<g filter="url(#soft)"><path d="M600 130 L800 200 v130 c0 130 -90 210 -200 250 c-110 -40 -200 -120 -200 -250 v-130 Z" fill="#fff" stroke="#e6efe9"/>
<path d="M600 170 L760 226 v104 c0 104 -72 168 -160 200 c-88 -32 -160 -96 -160 -200 v-104 Z" fill="{SOFT}"/>
<path d="M540 380 l45 45 l90 -100" stroke="{G}" stroke-width="18" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>'''
  +drone(300,180,0.95)+drone(930,220,0.8,-6))
# 17 hms
ART['hms']=wrap(ground()+building(700,160,300,455,3,6)+f'''
<g filter="url(#soft)" transform="translate(320,430)">
<circle cx="0" cy="-88" r="34" fill="#f0c9a8"/><path d="M-40 -96 a40 40 0 0 1 80 0 z" fill="{G}"/><rect x="-44" y="-100" width="88" height="12" rx="6" fill="{GD}"/>
<rect x="-34" y="-56" width="68" height="96" rx="18" fill="{GDD}"/><rect x="-30" y="40" width="24" height="80" rx="10" fill="{INK}"/><rect x="6" y="40" width="24" height="80" rx="10" fill="{INK}"/>
<rect x="-60" y="-30" width="30" height="64" rx="12" fill="{GDD}" transform="rotate(18)"/>
</g>
<rect x="230" y="{H-84}" width="220" height="24" rx="12" fill="{G}" opacity=".35"/>'''
  +drone(520,170,1.1)+f'<path d="M395 330 q 60 -80 100 -120" stroke="{MUT}" stroke-width="4" stroke-dasharray="8 8" fill="none"/>')
# 18 price
ART['price']=wrap(ground()+building(170,190,300,425,3,5)+f'''
<g filter="url(#soft)"><circle cx="760" cy="330" r="140" fill="#ffd23f"/><circle cx="760" cy="330" r="140" fill="none" stroke="#e2b41f" stroke-width="10"/>
<text x="760" y="368" text-anchor="middle" font-family="Arial" font-size="120" font-weight="bold" fill="{GDD}">kr</text></g>
<g stroke="{G}" stroke-width="10" stroke-linecap="round"><line x1="940" y1="440" x2="1030" y2="350"/><path d="M1030 350 l-26 4 M1030 350 l-6 26" fill="none"/></g>''')
# 19 methods split
ART['methods']=wrap(ground()+f'''<g filter="url(#soft)"><rect x="180" y="180" width="260" height="435" fill="#fff" stroke="#e6efe9"/>
<g stroke="{MUT}" stroke-width="8"><line x1="200" y1="200" x2="420" y2="200"/><line x1="200" y1="300" x2="420" y2="300"/><line x1="200" y1="400" x2="420" y2="400"/><line x1="200" y1="500" x2="420" y2="500"/>
<line x1="210" y1="180" x2="210" y2="615"/><line x1="410" y1="180" x2="410" y2="615"/><line x1="210" y1="200" x2="410" y2="300"/><line x1="210" y1="300" x2="410" y2="400"/></g></g>
<line x1="600" y1="130" x2="600" y2="600" stroke="#d6e5dc" stroke-width="4" stroke-dasharray="12 10"/>'''
  +building(700,180,300,435,3,5)+drone(850,120,1.1)+
  f'<path d="M800 152 q -30 40 -45 80" stroke="{G}" stroke-width="8" fill="none" stroke-linecap="round" opacity=".6"/>')
# 20 plan calendar+building
ART['plan']=wrap(ground()+building(680,200,300,415,3,5)+f'''
<g filter="url(#soft)"><rect x="180" y="160" width="420" height="380" rx="20" fill="#fff" stroke="#e6efe9"/>
<rect x="180" y="160" width="420" height="76" rx="20" fill="url(#gg)"/><rect x="180" y="212" width="420" height="24" fill="{GD}"/>
{''.join(f'<rect x="{212+c*76}" y="{262+r*80}" width="56" height="52" rx="10" fill="{SOFT}"/>' for r in range(3) for c in range(5))}
<path d="M296 300 l14 14 l24 -28" stroke="{G}" stroke-width="7" fill="none" stroke-linecap="round"/>
<path d="M448 380 l14 14 l24 -28" stroke="{G}" stroke-width="7" fill="none" stroke-linecap="round"/>
</g>''')
# 21 gutter
ART['gutter']=wrap(ground()+f'''<g filter="url(#soft)"><path d="M200 330 L640 170 L860 330" fill="#fff" stroke="#e6efe9" stroke-width="3"/>
<path d="M200 330 L640 170" stroke="{GD}" stroke-width="10"/>
<rect x="170" y="322" width="480" height="34" rx="17" fill="{GDD}"/>
<rect x="170" y="356" width="26" height="230" fill="{GDD}"/>
<circle cx="300" cy="330" r="12" fill="{G}"/><circle cx="370" cy="326" r="9" fill="{GD}"/><circle cx="430" cy="332" r="11" fill="{G}"/>
<path d="M520 322 q 8 -26 26 -30 q -2 22 -26 30z" fill="{G}"/>
</g>
<g fill="#7fb2e0" opacity=".8">{''.join(f'<path d="M{196+i%3*10} {400+i*36} q 8 12 0 22 q -8 -10 0 -22z"/>' for i in range(4))}</g>'''
  +drone(950,200,1.0))

for name,svg in ART.items():
    open(f'{OUT}/{name}.svg','w',encoding='utf-8').write(svg)
print("generated",len(ART),"illustrations:",', '.join(sorted(ART)))

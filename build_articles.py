#!/usr/bin/env python3
# Appends an "Artikler" section (index + 10 articles) to Design 2.
# Run AFTER build_d2.py. Uses the site's own media for headers (copyright-safe).
import os, re
OUT='/home/claude/design2'
ART=OUT+'/artikler'
os.makedirs(ART,exist_ok=True)

AR='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17 17 7M9 7h8v8"/></svg>'

# ---------- article data: (slug, category, title, lead, header_img, minutes, body_html) ----------
A=[]
# (slug, category, title, lead, header_img, minutes, tags, body) — KUN innhold fra FAQ-dokumentet

A.append(('fasadevask-steg-for-steg','Metode','Slik foregår en fasadevask med drone – steg for steg',
'Fra befaring til dokumentert resultat: hele prosessen forklart, slik den faktisk gjennomføres.',
'gallery-1.jpg',5,['metode','fasadevask','gjennomføring'],"""
<p>Et oppdrag starter med en befaring – fysisk eller ut fra bilder og kartmål – der vi vurderer materiale, tilstand og tilkomst og velger metode.</p>
<h2>På vaskedagen</h2>
<ul>
<li><b>Rigg:</b> Pumpe og vanntilførsel settes opp på bakken, og området sikres.</li>
<li><b>Vask:</b> En sertifisert operatør styrer dronen systematisk over fasaden – som regel fra topp til bunn – og påfører vann og et skånsomt, biologisk nedbrytbart middel gjennom en spesialdyse.</li>
<li><b>Ømfintlige flater:</b> Der det trengs brukes softwash med lavt trykk, som løser opp begroingen i stedet for å blåse den bort.</li>
<li><b>Dokumentasjon:</b> Resultatet dokumenteres med foto før og etter.</li>
</ul>
<p>Hele tiden står personellet trygt på bakken – ingen jobber i høyden, og det settes ikke opp stillas.</p>
<h2>Hvor lang tid tar det?</h2>
<p>De fleste bygg vaskes på én til to dager, mot flere uker med stillas – fordi det ikke er noen rigg som skal opp og ned. Et mindre bygg kan være ferdig på noen timer. Du får alltid et konkret tidsestimat i tilbudet.</p>
<h2>Blir det faktisk rent?</h2>
<p>Ja. På vinduer gir rent (avionisert) vann et stripefritt resultat uten såperester. På fasade fjerner softwash både det synlige belegget og selve begroingen, slik at flaten holder seg ren lenger – og på kraftig begrodde flater fortsetter effekten å utvikle seg i ukene etter vask, når nedbøren skyller bort døde sporer.</p>"""))

A.append(('hvorfor-drone-ikke-stillas','Metode','Hvorfor drone i stedet for stillas, lift eller tauarbeid?',
'Raskere, rimeligere og tryggere for vask og inspeksjon – og ærlig om når tradisjonelle metoder fortsatt trengs.',
'gallery-7.jpg',5,['stillas','metodevalg','totalkostnad'],"""
<p>For vask og inspeksjon er drone som regel raskere, rimeligere og tryggere: ingen rigg skal opp og ned, ingen sperring av fortau, og ingen jobber i høyden. En jobb som ville tatt uker med stillas, gjøres ofte på én til to dager.</p>
<h2>Er det billigere enn stillas?</h2>
<p>På høye bygg som regel ja – når du regner totalkostnad. Med stillas betaler du montering, leie i hele perioden og demontering, ofte over uker, pluss eventuell leie for å sperre fortau. Disse kostnadene kan overstige selve vasken. Med drone er riggen nede på timer. Sammenlign derfor totalkostnaden for hele jobben, ikke bare «vaskeprisen».</p>
<h2>Når trengs fortsatt tradisjonelle metoder?</h2>
<p>Ved oppgaver som krever fysisk berøring – reparasjon, fuging, maling – trengs fortsatt stillas, lift eller tauarbeid. Ofte lønner det seg å kombinere: en droneinspeksjon først viser nøyaktig hvor fysisk utbedring trengs, slik at riggen står kortest mulig.</p>
<p>Vi er ikke låst til én metode: Drone brukes der det gir best resultat, og lift, stang eller manuelt arbeid der det passer bygget bedre.</p>"""))

A.append(('fungerer-pa-alle-materialer','Metode','Fungerer dronevask på alle fasadematerialer?',
'Betong, tegl, tre, metall og glass – metoden tilpasses flaten. Det er det som skiller fagmessig vask fra skade.',
'gallery-4.jpg',4,['materialer','softwash','skånsom vask'],"""
<p>Ja – metoden brukes på betong, tegl, mur, naturstein, trepanel, fasadeplater, metallkledning og glass. Det som endrer seg, er trykket og middelet.</p>
<h2>Tilpasningen er faget</h2>
<p>Ømfintlige flater som puss, malt tre og eldre tegl vaskes skånsomt med softwash og lavt trykk, mens mer robuste flater tåler mer. Riktig tilpasning til materialet er nettopp det som skiller en fagmessig vask fra en som kan gjøre skade.</p>
<h2>Skader det fasaden?</h2>
<p>Nei – riktig utført er dronevask skånsommere enn ukyndig høytrykksspyling. Trykk, avstand og middel tilpasses materialet. Det er feil bruk av høytrykk – uansett tilkomstmetode – som skader fasader, ikke dronen.</p>
<p>Er du usikker på hva flaten din tåler? På befaringen tester vi gjerne en liten flate først, så ser du resultatet før hele bygget vaskes.</p>"""))

A.append(('solceller-og-tak','Metode','Solcellevask og takrens med drone',
'Skitne paneler taper produksjon, og mose bryter ned taket. Begge deler løses skånsomt – uten at noen går på taket.',
'gallery-6.jpg',4,['solceller','takrens','tak'],"""
<p>Ja, vi vasker både solcellepaneler og tak – og begge deler kan kombineres med droneinspeksjon i samme oppdrag.</p>
<h2>Solcellepaneler</h2>
<p>Paneler vaskes skånsomt med rent vann og lavt trykk for å hente tilbake produksjon – uten å skade antirefleksbelegg eller pakninger, og uten at noen går på taket.</p>
<h2>Tak</h2>
<p>Tak renses for mose og begroing med skånsom metode og mosemiddel, slik at fukt og frost ikke får bryte ned takflaten over tid.</p>
<h2>Hvorfor det haster mer enn det ser ut</h2>
<p>Mose holder på fukt, og i frostperioder utvider fukten seg og skader taksteinen gradvis. Skitne paneler taper produksjon jevnt og stille. I begge tilfeller er jevnlig, skånsom rens langt billigere enn konsekvensene av å vente.</p>"""))

A.append(('trygghet-for-beboere','Trygghet & miljø','Er dronevask trygt for beboere, bygg og omgivelser?',
'Beboerne kan være hjemme, området sikres, og operasjonen risikovurderes. Slik ivaretas tryggheten i praksis.',
'gallery-3.jpg',4,['beboere','sikkerhet','risikovurdering'],"""
<p>Ja. Beboerne kan være hjemme og ferdes normalt mens vi jobber – vi anbefaler bare at vinduer holdes lukket og at biler flyttes bort fra flaten som vaskes.</p>
<h2>Slik sikres oppdraget</h2>
<ul>
<li>Arbeidsområdet sikres og merkes.</li>
<li>Operasjonen risikovurderes før dronen letter.</li>
<li>Beboere varsles når det er relevant.</li>
</ul>
<p>Fordi ingen jobber i høyden og det ikke settes opp stillas, fjernes flere av de vanligste risikoene helt: fall fra høyde, fallende gjenstander, klatring – og stillaset som innbruddsvei.</p>
<h2>Hva om dere oppdager en skade?</h2>
<p>Da dokumenterer vi den med daterte, stedfestede bilder og tar den med i rapporten, gradert etter alvorlighet (akutt, bør utbedres, observeres) og med en anbefaling om tiltak. Små ting – løse beslag, begynnende riss, en tett takrenne – oppdages ofte i tide, mens de fortsatt er billige å utbedre.</p>
<h2>Er dere forsikret?</h2>
<p>Ja. Ansvarsforsikring for droneoperasjoner er lovpålagt, og vi opererer med gyldig forsikring, registrering hos Luftfartstilsynet og gyldige sertifikater. Det bør du kreve dokumentert av enhver droneleverandør.</p>"""))

A.append(('miljo-og-vaskemidler','Trygghet & miljø','Hvilke vaskemidler bruker vi – og er de miljøvennlige?',
'Biologisk nedbrytbare midler, ofte bare rent vann – og bevisst håndtering av avrenning.',
'gallery-2.jpg',3,['miljø','vaskemidler','rent vann'],"""
<p>Vi bruker biologisk nedbrytbare midler uten skadelige kjemikalier – og på vinduer ofte bare rent, avionisert vann helt uten middel.</p>
<h2>Hvorfor rent vann virker</h2>
<p>Avionisert vann er fritt for mineraler. Det er mineraler og såperester som lager striper – derfor tørker rent vann stripefritt, uten kjemi.</p>
<h2>Avrenning og omgivelser</h2>
<p>Avrenning håndteres bevisst, med hensyn til beplantning, husdyr og avløp. Middel doseres etter behov – kraftig begrodde flater trenger mer, lett tilsmussede mindre.</p>
<p>Målet er enkelt: et effektivt resultat med minst mulig miljøavtrykk.</p>"""))

A.append(('hva-koster-det','Pris','Hva koster fasadevask med drone – og hvorfor ingen fast m²-pris?',
'Areal, tilstand, materiale og tilkomst styrer prisen. Slik får du et presist tilbud – raskt.',
'about.jpg',5,['pris','tilbud','befaring'],"""
<p>Det ærlige svaret: det kommer an på bygget. Prisen avhenger av areal, tilstand, materiale, tilkomst og høyde. Areal er den viktigste driveren, og tilstand nummer to – en fasade som vaskes jevnlig krever mindre tid og middel enn en som ikke er vedlikeholdt på mange år.</p>
<h2>Hvorfor ikke fast kvadratmeterpris?</h2>
<p>Fordi to bygg med samme areal kan kreve svært ulik innsats. Grad av begroing, fasademateriale, antall detaljer, tilgang til vann og fri flyplass påvirker alle tidsbruken. En fast «per m²»-pris uten å ha sett bygget ville enten vært for høy (for å ta høyde for det verste) eller for lav. Derfor gir seriøse aktører ikke fast pris uten befaring.</p>
<h2>Slik får du et raskt tilbud</h2>
<ul>
<li><b>Adresse</b> – så vi kan se bygget på kart.</li>
<li><b>Noen bilder</b> av fasaden eller taket.</li>
<li><b>Kort beskrivelse</b> av hva du ønsker gjort.</li>
</ul>
<p>Da gir vi et estimat raskt, og bekrefter med en kostnadsfri, uforpliktende befaring før avtale. Vi holder til i Oslo og betjener Oslo-området – ta kontakt med adressen din, så bekrefter vi at vi kan ta oppdraget.</p>"""))

A.append(('vedlikeholdsavtale','Pris','Vedlikeholdsavtale: faste intervaller, fast kontaktperson',
'Vi følger opp vask, takrens og inspeksjon automatisk – du får jevn standard og forutsigbar økonomi.',
'gallery-5.jpg',4,['årsavtale','intervaller','forutsigbarhet'],"""
<p>Mange kunder foretrekker en årsavtale der vi følger opp intervallene for vask, takrens og inspeksjon automatisk – da slipper du å huske på det selv, og bygget holder jevn standard.</p>
<h2>Hvor ofte bør bygget vaskes og inspiseres?</h2>
<ul>
<li><b>Vindusvask:</b> årlig, gjerne vår.</li>
<li><b>Fasadevask og takrens:</b> hvert 1.–3. år etter behov.</li>
<li><b>Droneinspeksjon:</b> årlig – den viser når vask faktisk trengs og fanger opp skader tidlig.</li>
</ul>
<p>Beliggenhet betyr mye: nordvendte, skyggefulle eller kystnære bygg trenger hyppigere oppfølging enn solrike og tørre.</p>
<h2>Hva avtalen gir deg</h2>
<p>Omfang og hyppighet tilpasses bygget og behovet. Du får forutsigbar økonomi – og en fast kontaktperson som kjenner bygget: fasadetype, historikk og tidligere oppdrag. Det gir kontinuitet og raskere oppfølging ved spørsmål eller akutte behov.</p>"""))

A.append(('rapport-og-dokumentasjon','Inspeksjon & termografi','Dokumentasjonen du får: fra foto til rapport styret kan bruke',
'Foto før/etter som minimum – og strukturerte tilstandsrapporter med stedfestede, graderte funn.',
'after.jpg',4,['rapport','dokumentasjon','protokoll'],"""
<p>Som minimum får du foto før og etter hvert oppdrag. Ved inspeksjon får du en strukturert tilstandsrapport.</p>
<h2>Slik er rapporten bygget opp</h2>
<ul>
<li><b>Stedfestede funn:</b> Hvert funn knyttes til fasade/takflate og posisjon på bygget.</li>
<li><b>Gradering:</b> Akutt, bør utbedres, eller observeres.</li>
<li><b>Anbefalte tiltak</b> og oversiktsbilder som viser omfang.</li>
</ul>
<h2>Laget for å brukes</h2>
<p>Rapporten leveres som PDF og er laget for å kunne legges rett inn i styrepapirer, vedlikeholdsplan eller en forsikringssak: bilder før/etter, beskrivelse av utført arbeid, middel som er brukt, observerte avvik og anbefalte tiltak. Den kan legges som vedlegg til styreprotokollen og inngår i byggets vedlikeholdshistorikk.</p>"""))

A.append(('rgb-vs-termografi','Inspeksjon & termografi','RGB-inspeksjon og termografi: hva er forskjellen?',
'Fargekameraet viser det synlige – termisk kamera viser det skjulte. Sammen gir de hele bildet.',
'gallery-8.jpg',5,['termografi','RGB','varmetap'],"""
<p>En visuell RGB-inspeksjon bruker et høyoppløselig fargekamera og viser synlige forhold: riss, avskalling, skadde fuger, knekt takstein, korrosjon. Termografi bruker et termisk kamera og viser skjulte forhold ved å måle temperaturforskjeller på overflatene. De utfyller hverandre, og kombineres ofte i samme oppdrag.</p>
<h2>Hva termografi kan avdekke</h2>
<ul>
<li><b>Dårlig eller manglende isolasjon og kuldebroer</b> – varme felt som lekker ut på en kald dag.</li>
<li><b>Skjult fukt og lekkasjer</b> – fuktige materialer holder en annen temperatur enn tørre.</li>
<li><b>Luftlekkasjer</b> ved vinduer og dører.</li>
<li><b>Defekte solceller</b> – som går varmere enn friske.</li>
</ul>
<h2>Når bør termografi gjøres?</h2>
<p>Bygningstermografi krever temperaturforskjell mellom inne og ute – kalde, gjerne overskyede dager i fyringssesongen gir de tydeligste resultatene. Solcelleinspeksjon er motsatt: der trengs sol på panelene for at defekte celler skal skille seg ut. Vi planlegger tidspunktet etter hva som skal måles.</p>
<p>Resultatet er et konkret grunnlag for å prioritere etterisolering, tetting eller utbedring der det faktisk monner.</p>"""))

A.append(('3d-noyaktighet-og-bruk','Inspeksjon & termografi','3D-modeller og målinger: hvor nøyaktig – og hva kan de brukes til?',
'Centimeternøyaktighet med riktig oppsett, levert i standardformater – og ærlig om hva droneinspeksjon ikke erstatter.',
'hero-poster.jpg',5,['3D','nøyaktighet','takst'],"""
<p>Med riktig flyplan, kalibrering og bakkekontrollpunkter oppnås centimeternøyaktighet – og vi dokumenterer oppnådd nøyaktighet i leveransen, slik at du vet hva grunnlaget holder til.</p>
<h2>Formater du kan bruke direkte</h2>
<p>Modeller og punktskyer leveres i standardformater for CAD, GIS og BIM (som GeoTIFF, LAS/LAZ og E57) – eller som nettbasert visning du kan måle i via en lenke, uten spesialprogramvare.</p>
<h2>Erstatter det en takst?</h2>
<p>Droneinspeksjon gir svært god dekning av synlig tilstand på tak, fasade og detaljer i høyden – ofte bedre enn en manuell befaring, og helt uten arbeid i høyden. Enkelte forhold krever likevel fysisk kontroll eller en autorisert takstmann. Vi er tydelige på hva metoden dekker: inspeksjonen er et sterkt supplement til – og ofte et godt førstesteg før – en full tilstandsvurdering.</p>"""))

A.append(('borettslag-og-sameier','Borettslag','Borettslag og sameier: bestilling, loven og dokumentasjonen',
'Hvem kan bestille, hva sier borettslagsloven, og hvordan dokumenteres jobben for protokoll og forsikring?',
'before.jpg',6,['borettslag','styre','borettslagsloven'],"""
<p>Styreleder eller forretningsfører bestiller normalt på vegne av fellesskapet. Enkeltoppdrag innenfor ordinær vedlikeholdsramme kan styret bestille direkte, uten vedtak i generalforsamling eller sameiermøte. Flerårige avtaler som binder laget over tid, eller som påvirker felleskostnadene, bør derimot forankres i budsjettet som vedtas av eierne.</p>
<h2>Hva sier loven?</h2>
<p>Ansvaret for utvendig vedlikehold av fasade, tak og fellesarealer ligger på borettslaget eller sameiet som helhet – ikke på den enkelte andels- eller seksjonseier. Styret har dermed en plikt til å holde bygget i forsvarlig stand. Dokumentert fasadevask og en tilstandsrapport viser at vedlikeholdsplikten ivaretas – nyttig ved styreskifte og salg.</p>
<h2>Ferdig saksunderlag til styremøtet</h2>
<p>Vi kan levere et kort underlag tilpasset styremøtet: metodebeskrivelse, sammenligning mot stillas og lift, prisestimat for byggets areal, en enkel HMS-vurdering og forslag til vedtak.</p>
<h2>Hva merker beboerne?</h2>
<p>Svært lite. Ingen stillas langs fasaden i ukevis, parkering og fortau holdes i hovedsak åpne, og vi koordinerer med styret og bistår med beboervarsling. For de fleste er den største merkbare forskjellen at bygget plutselig er rent.</p>
<p>Med en løpende avtale får dere også en fast kontaktperson som kjenner bygget – det gir kontinuitet på tvers av styreperioder.</p>"""))

A.append(('regelverk-sertifikater-personvern','Regelverk','Lovlig droneflyging: sertifikater, tettbygd strøk og personvern',
'Dette skal være på plass hos en seriøs operatør – og slik ivaretas naboer og personvern i praksis.',
'gallery-3.jpg',5,['regelverk','sertifikater','personvern'],"""
<p>Be om tre ting før du signerer med en droneoperatør: operatørnummer (registrering hos Luftfartstilsynet), pilotenes sertifikater, og gyldig forsikringsbevis. En seriøs leverandør deler dette uten motforestillinger.</p>
<h2>Kompetansen bak</h2>
<p>Flyging nær mennesker, bygg og trafikk hører inn under strengere kategorier i regelverket – med krav til kompetanse, planlegging og avstander. Standardscenarioene (STS) i spesifikk kategori er laget for profesjonell flyging i slike omgivelser. Hos Altivon er teknisk ansvarlig sertifisert med A1, A2, A3 og STS, og hvert oppdrag risikovurderes før dronen letter.</p>
<h2>Er det lov å fly tett på bygg i by?</h2>
<p>Ja – men det er regulert, og krever riktig kompetansenivå og planlegging. En profesjonell operatør planlegger operasjonen slik at avstandskrav overholdes og omgivelsene ikke utsettes for risiko.</p>
<h2>Personvern</h2>
<p>Kameraet brukes til oppdraget – å dokumentere bygget – ikke til å filme naboer eller inn i vinduer. Flyging og bildetaking planlegges slik at personvernet ivaretas, materialet håndteres ryddig og deles kun med kunden, og beboere varsles når det er relevant.</p>
<h2>HMS: bakken er tryggest</h2>
<p>God HMS-praksis sier at risiko helst skal fjernes, ikke bare sikres. Når vask og inspeksjon gjøres uten at noen forlater bakken, fjernes fallrisikoen ved kilden – og du unngår stillas, som selv utgjør en risiko. For byggeier betyr det lavere risiko og enklere ansvarsforhold.</p>"""))

A.append(('sesong-vaer-praktisk','Sesong & praktisk','Sesong, vær og det praktiske rundt oppdraget',
'Når på året bør du vaske, hva skjer ved dårlig vær – og må du egentlig være hjemme?',
'gallery-7.jpg',5,['sesong','vær','praktisk'],"""
<p>Våren er høysesong for vask: da fjernes vinterens veistøv, salt og pollen, og bygget står rent gjennom sommeren. Takrens og mosebehandling passer godt om sommeren og tidlig høst, slik at middelet får virke før frosten. Bestill vårvask tidlig – kapasiteten fylles raskt.</p>
<h2>Kan dere jobbe om vinteren?</h2>
<p>Vask med vann krever plussgrader, så streng kulde begrenser vaskeoppdrag. Inspeksjon og særlig termografi er derimot ideelt om vinteren – da er temperaturforskjellen mellom inne og ute størst, og varmetap vises tydeligst.</p>
<h2>Hva med vær og vind på selve dagen?</h2>
<p>Droneflyging er væravhengig. Sterk vind, kraftig nedbør eller dårlig sikt kan gjøre at et oppdrag flyttes til en bedre dag – av sikkerhets- og kvalitetshensyn. Vi følger værmeldingen tett og avtaler nytt tidspunkt ved behov. Trygg gjennomføring går alltid foran å presse gjennom en flyging.</p>
<h2>Må du være til stede?</h2>
<p>Vanligvis ikke – så lenge vi har tilgang til bygget, en fri flyplass og et vannuttak. Det praktiske avtales på forhånd, og for borettslag koordinerer vi med styret eller forvalter.</p>"""))

# ---------- photo override: media/foto/<slug>.jpg replaces illustration when present ----------
import os as _os
A=[(s,c,t,l,('foto/'+s+'.jpg' if _os.path.exists(OUT+'/media/foto/'+s+'.jpg') else img),m,tg,bd) for (s,c,t,l,img,m,tg,bd) in A]

# ---------- CSS for articles ----------
css_add='''

/* ---- articles ---- */
.artgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:44px}
@media(max-width:900px){.artgrid{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.artgrid{grid-template-columns:1fr}}
.acard{background:#fff;border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;display:flex;flex-direction:column;transition:.35s var(--ease)}
.acard:hover{transform:translateY(-6px);box-shadow:0 30px 60px -40px rgba(10,53,39,.35);border-color:var(--green)}
.acard .ai{aspect-ratio:16/9;overflow:hidden;background:var(--green-soft)}
.acard .ai img{width:100%;height:100%;object-fit:cover;transition:transform .5s var(--ease)}
.acard:hover .ai img{transform:scale(1.06)}
.acard .ab{padding:22px;display:flex;flex-direction:column;gap:10px;flex:1}
.acard .chip{align-self:flex-start;background:var(--green-soft);color:var(--green-dd);border-radius:100px;padding:.28rem .75rem;font-size:.72rem;font-weight:700;font-family:var(--disp);letter-spacing:.06em;text-transform:uppercase}
.acard h3{font-size:1.14rem;line-height:1.3}
.acard p{color:var(--muted);font-size:.92rem;flex:1}
.acard .am{color:var(--faint);font-size:.8rem}
.afilter{display:flex;flex-wrap:wrap;gap:9px;justify-content:center;margin-top:30px}
.afilter button{border:1px solid var(--line2);background:#fff;color:var(--muted);font-family:var(--disp);font-weight:600;font-size:.84rem;border-radius:100px;padding:.5rem 1.05rem;cursor:pointer;transition:.25s}
.afilter button.on,.afilter button:hover{background:var(--green);border-color:var(--green);color:#fff}
.article{max-width:760px;margin:0 auto}
.article .ahead img{width:100%;border-radius:var(--r-lg);aspect-ratio:16/8;object-fit:cover;margin:30px 0 8px;border:1px solid var(--line)}
.article .meta{display:flex;gap:14px;color:var(--faint);font-size:.85rem;margin:10px 0 26px;flex-wrap:wrap}
.article h2{font-size:1.5rem;margin:36px 0 12px}
.article p{color:#2c443a;margin-bottom:16px;font-size:1.02rem}
.article ul{margin:0 0 18px 20px;color:#2c443a}
.article li{margin-bottom:9px}
.article b{color:var(--ink)}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin:-10px 0 22px}
.tags .tag{background:var(--bg-alt);border:1px solid var(--line);color:var(--muted);border-radius:100px;padding:.24rem .7rem;font-size:.75rem;font-family:var(--disp);font-weight:600}
.aback{display:inline-flex;align-items:center;gap:8px;color:var(--green);font-family:var(--disp);font-weight:600;font-size:.9rem;margin-bottom:6px}
'''
open(OUT+'/assets/style.css','a',encoding='utf-8').write(css_add)

# ---------- read shared chrome from an existing page ----------
tpl=open(OUT+'/om-oss.html',encoding='utf-8').read()
head_end=tpl.find('</head>')
foot_start=tpl.find('<footer class="foot">')
tail_start=tpl.find('<form name="tilbud"')
NAVHTML=tpl[tpl.find('<header class="nav"'):tpl.find('<section')]
FOOT_TAIL=tpl[foot_start:]
def head(title,desc):
    h=tpl[:head_end]
    h=re.sub(r'<title>.*?</title>',f'<title>{title}</title>',h)
    h=re.sub(r'<meta name="description" content=".*?">',f'<meta name="description" content="{desc}">',h)
    return h+'</head><body>'

def relativize(h):
    # protect the Artikler link so page-link pass can't corrupt it
    h=h.replace('href="artikler/index.html','href="__ARTIDX__')
    h=h.replace('href="assets/','href="../assets/').replace('src="assets/','src="../assets/')
    h=h.replace('src="media/','src="../media/')
    h=h.replace('href="media/','href="../media/')   # favicon etc.
    for p in ['index.html','losninger.html','prosjekter.html','om-oss.html','galleri.html','faq.html','kontakt.html','takk.html']:
        h=h.replace(f'href="{p}',f'href="../{p}')
    h=h.replace('href="__ARTIDX__','href="index.html')
    return h

def write_page(path,title,desc,body,rel=False):
    html=head(title,desc)+NAVHTML+body+FOOT_TAIL
    if rel: html=relativize(html)
    open(path,'w',encoding='utf-8').write(html)

# ---------- nav: add Artikler link to all top pages + article chrome ----------
import glob
for f in glob.glob(OUT+'/*.html'):
    h=open(f,encoding='utf-8').read()
    if 'href="artikler/index.html"' not in h:
        h=h.replace('<a href="om-oss.html">Om oss</a>','<a href="om-oss.html">Om oss</a><a href="artikler/index.html">Artikler</a>')
        h=h.replace('<a href="om-oss.html" class="on">Om oss</a>','<a href="om-oss.html" class="on">Om oss</a><a href="artikler/index.html">Artikler</a>')
        # mobile menu + footer
        h=h.replace('<a href="om-oss.html">Om oss</a><a href="artikler/index.html">Artikler</a><a href="kontakt.html">Kontakt</a></nav>',
                    '<a href="om-oss.html">Om oss</a><a href="artikler/index.html">Artikler</a><a href="kontakt.html">Kontakt</a></nav>')
        h=h.replace('<li><a href="om-oss.html#team">Team</a></li>','<li><a href="om-oss.html#team">Team</a></li><li><a href="artikler/index.html">Artikler</a></li>')
    open(f,'w',encoding='utf-8').write(h)

# refresh template pieces (with Artikler link) for article pages
tpl=open(OUT+'/om-oss.html',encoding='utf-8').read()
head_end=tpl.find('</head>')
NAVHTML=tpl[tpl.find('<header class="nav"'):tpl.find('<section')]
NAVHTML=NAVHTML.replace('href="om-oss.html" class="on"','href="om-oss.html"')
NAVHTML=NAVHTML.replace('href="artikler/index.html"','href="artikler/index.html" class="on"')
FOOT_TAIL=tpl[tpl.find('<footer class="foot">'):]

# ---------- article index ----------
cats=sorted(set(a[1] for a in A))
chips='<button class="on" data-c="alle">Alle</button>'+''.join(f'<button data-c="{c}">{c}</button>' for c in cats)
cards=''.join(f'''<a class="acard" href="{s}.html" data-c="{c}"><div class="ai"><img src="../media/{img}" alt="{t}" loading="lazy"></div><div class="ab"><span class="chip">{c}</span><h3>{t}</h3><p>{lead}</p><span class="am">{mins} min lesetid · {' · '.join(tags[:2])}</span></div></a>''' for s,c,t,lead,img,mins,tags,_ in A)
idx=f'''<section class="page-hero"><div class="ph-bg"><img src="../media/gallery-5.jpg" alt=""></div><div class="wrap"><span class="eyebrow c">Artikler</span><h1>Kunnskap om <span class="g">drone og vedlikehold</span></h1><p>Guider og innsikt om fasadevask, takrens, inspeksjon, termografi og datadrevet vedlikehold – skrevet for byggeiere, styrer og forvaltere.</p><div class="crumb"><a href="../index.html">Hjem</a> → Artikler</div></div></section>
<section class="sec"><div class="wrap">
  <div class="afilter rev" id="afilter">{chips}</div>
  <div class="artgrid rev" id="artgrid">{cards}</div>
</div></section>
<script>
(function(){{const f=document.getElementById('afilter'),g=document.getElementById('artgrid');if(!f)return;
f.querySelectorAll('button').forEach(b=>b.onclick=()=>{{f.querySelectorAll('button').forEach(x=>x.classList.toggle('on',x===b));
const c=b.dataset.c;g.querySelectorAll('.acard').forEach(a=>a.style.display=(c==='alle'||a.dataset.c===c)?'':'none');}});}})();
</script>'''
html=head('Artikler om dronevask, inspeksjon og vedlikehold | Altivon','Guider om fasadevask med drone, takrens, vindusvask, termografi, droneinspeksjon, solcellevask og vedlikeholdsplaner.')+NAVHTML+idx+FOOT_TAIL
html=relativize(html)
open(ART+'/index.html','w',encoding='utf-8').write(html)

# ---------- article pages ----------
AR2='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="15" height="15"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>'
for s,c,t,lead,img,mins,tags,body in A:
    art=f'''<section class="page-hero"><div class="wrap"><span class="eyebrow c">{c}</span><h1 style="font-size:clamp(1.9rem,4.4vw,3rem)">{t}</h1><p>{lead}</p><div class="crumb"><a href="../index.html">Hjem</a> → <a href="index.html">Artikler</a> → {c}</div></div></section>
<section class="sec" style="padding-top:54px"><div class="wrap"><div class="article rev">
<a class="aback" href="index.html">{AR2} Alle artikler</a>
<div class="ahead"><img src="../media/{img}" alt="{t}"></div>
<div class="meta"><span>{c}</span><span>·</span><span>{mins} min lesetid</span><span>·</span><span>Altivon</span></div>\n<div class="tags">{''.join(f'<span class="tag">#{x}</span>' for x in tags)}</div>
{body}
<div style="margin-top:40px;background:var(--green-soft);border-radius:18px;padding:26px;text-align:center">
<h2 style="margin:0 0 8px;font-size:1.3rem">Lurer du på hva dette betyr for ditt bygg?</h2>
<p style="margin-bottom:18px">Send oss noen bilder og en kort beskrivelse, så gir vi deg en ærlig vurdering – uforpliktende.</p>
<a href="../kontakt.html" class="btn btn-primary">Be om tilbud {AR}</a></div>
</div></div></section>'''
    html=head(f'{t} | Altivon',lead)+NAVHTML+art+FOOT_TAIL
    html=relativize(html)
    open(ART+f'/{s}.html','w',encoding='utf-8').write(html)

print("articles built:",len(A))

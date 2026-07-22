# Altivon – publisering på Netlify (gratis) + e-postvarsler fra skjemaet

Denne løsningen bruker **ingen Google-script og ingen formtjeneste-kode**.
All kode ligger i GitHub-repoet deres. Netlify henter repoet, publiserer siden,
og håndterer skjemaene innebygd. E-postvarsler kan gå til hvilken som helst
adresse – Gmail nå, Outlook (mathias@altivon.no) senere. Bytte = ett felt i
Netlify-panelet, ingen kodeendring.

## Steg 1 – Legg koden på GitHub (som før)
Last opp hele mappen (alle .html, assets/, media/) til GitHub-repoet.
(Om dere allerede bruker GitHub Pages: behold repoet – Netlify leser samme repo.)

## Steg 2 – Koble repoet til Netlify (5 min, gratis)
1. Gå til https://app.netlify.com → «Sign up» → velg **GitHub** (logg inn med GitHub-kontoen).
2. Klikk **Add new site → Import an existing project → GitHub**.
3. Velg Altivon-repoet.
4. Build settings: la alt stå tomt (statisk side) → **Deploy site**.
5. Etter ~1 minutt er siden live på en adresse som `altivon.netlify.app`.

## Steg 3 – Slå på e-postvarsler for skjemaet
1. I Netlify: velg siten → **Forms** i menyen.
   Der skal skjemaet **«tilbud»** ligge (oppdages automatisk fra koden).
2. Gå til **Site configuration → Notifications → Form submission notifications**
   → **Add notification → Email notification**.
3. Skriv inn mottakeradressen: `2.haacked@gmail.com` (test) – senere bytter dere
   bare dette feltet til `mathias@altivon.no` (Outlook fungerer helt likt).
4. Ferdig. Hver innsending sendes som e-post; vedlagte bilder kommer som
   nedlastingslenker i e-posten, og alle innsendinger (med bildene) ligger
   også trygt lagret under **Forms** i panelet.

## Steg 4 – Eget domene (når dere vil)
Site configuration → Domain management → Add domain → www.altivon.no
(Netlify gir gratis HTTPS automatisk.)

## Test
1. Åpne den publiserte siden (netlify.app-adressen).
2. Send inn skjemaet med 1–2 bilder.
3. Sjekk innboksen (og spam første gang) + Forms-fanen i Netlify.

## Begrensninger (gratisnivå)
- 100 innsendinger per måned og 10 MB filopplasting per måned.
  Mer enn nok for tilbudsforespørsler; kan oppgraderes ved behov.

## Viktig
- Skjemaet virker IKKE på GitHub Pages-adressen (github.io) – kun på
  Netlify-adressen/domenet, siden det er Netlify som mottar innsendingene.
- Filen `takk.html` kan beholdes; skjemaet viser uansett bekreftelse direkte.

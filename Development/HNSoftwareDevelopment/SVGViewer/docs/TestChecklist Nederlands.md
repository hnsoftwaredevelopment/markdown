# SVG Viewer — Handmatige testchecklist (US-7.3)

Loop deze lijst af in de echte app. Vink af wat werkt, noteer afwijkingen.
Herhaal de kernpaden in **alle drie de talen** (NL/EN/DE).

- App-versie getest: `2026.7.30.0`
- Datum / tester: `30-07-2026 / HN`
- Windows-thema tijdens test (licht/donker): `licht en donker`

> Tip: leg tijdens het testen meteen de screenshots vast voor US-7.4
> (PNG's in `docs\images\`): hoofdvenster (Volledig én Alleen SVG), preview met
> thumbnails, zoomviewer, Instellingen met vlaggen, en de Over-dialoog.

## 1. Opstarten
- [x] Splashscreen verschijnt bij het starten en vervaagt zodra het venster laadt. ✅ 2026-07-30
- [ ] De app opent in de **laatst gekozen taal**.
- [x] De laatst gekozen schijf is voorgeselecteerd (indien eerder gekozen). ✅ 2026-07-30
- [x] Logbestand bestaat: `%AppData%\SVGViewer\logs\app.log` bevat een regel ✅ 2026-07-30
      `... [INFO] SVG Viewer starting (v...)`. *(Bewijs dat logging werkt, zonder fout.)*

## 2. Venster- en taakbalk-icoon
- [x] Titelbalk-icoon staat op een wit vlakje en is goed zichtbaar — test ook met ✅ 2026-07-30
      een **donker** Windows-thema.
- [x] Taakbalk-icoon toont het nieuwe logo (transparant), duidelijk herkenbaar. ✅ 2026-07-30

## 3. Scannen & mappenmarkering (kernfunctionaliteit)
- [x] Schijf kiezen → scan start, de boom is **meteen** bruikbaar (lazy), ✅ 2026-07-30
      statusbalk toont voortgang (aantal mappen / met SVG).
- [x] Mappen mét SVG's: **blauw + vet + aantal**. Bovenliggende mappen op de route: ✅ 2026-07-30
      **blauw, normaal, zonder aantal**.
- [x] **Tijdens** een lopende scan wisselen naar "Alleen SVG" en terug naar ✅ 2026-07-30
      "Volledig" → de scan begint **niet** opnieuw; voortgang loopt door.
- [x] **Annuleren** (✕) tijdens een scan → scan stopt, tot dan gevonden resultaat ✅ 2026-07-30
      blijft staan; van view wisselen scant daarna **niet** opnieuw.
- [x] **Vernieuwen** (↻) → start wél een nieuwe scan (en toont bewerkte bestanden vers). ✅ 2026-07-30
- [x] **Schijf wisselen** → start een nieuwe scan (oude wordt netjes afgebroken). ✅ 2026-07-30
- [x] "Alleen SVG" toont alleen relevante takken; op een schijf/tak zonder SVG's ✅ 2026-07-30
      volgt een lege staat met de melding "geen SVG's gevonden".

## 4. Weergavegrootte (segmented control)
- [x] Grote / Middelgrote / Kleine iconen → thumbnails schalen mee. ✅ 2026-07-30
- [x] Details → lijstweergave (geen thumbnails). ✅ 2026-07-30
- [x] De actieve knop licht op; tooltips kloppen in elke taal. ✅ 2026-07-30

## 5. Preview & zoom
- [x] Map met SVG's selecteren → thumbnails renderen correct. ✅ 2026-07-30
- [x] **Dubbelklik** op een SVG → zoomviewer opent (niet de editor). ✅ 2026-07-30
- [x] In-/uitzoomen in de viewer werkt; sluiten werkt. ✅ 2026-07-30
- [x] Lege map geselecteerd → nette "geen SVG's"-melding, geen thumbnails. ✅ 2026-07-30

## 6. Contextmenu (rechtermuisknop op een SVG)
- [x] "Openen in editor" opent het bestand in de gekoppelde app (bijv. Inkscape). ✅ 2026-07-30
- [ ] "Openen met…" toont de Windows-dialoog.
- [x] "Tonen in Verkenner" opent Verkenner met het bestand geselecteerd. ✅ 2026-07-30
- [x] Foutpad: verwijder/hernoem een bestand en probeer het te openen → nette ✅ 2026-07-30
      melding (geen crash).

## 7. Instellingen (⚙)
- [ ] Taal wisselen NL → EN → DE: de **hele** UI vertaalt live (toolbar-tooltips,
      statusbalk, contextmenu, dialogen, bestandsgroottes/datums).
- [x] Bij de taalkeuze staan de **vlaggen** naast de namen; de geselecteerde vlag klopt. ✅ 2026-07-30
- [x] "Bevestiging vragen voordat een bestand wordt verwijderd" onthoudt de stand. ✅ 2026-07-30
- [x] Gekozen taal blijft behouden **na herstart** van de app. ✅ 2026-07-30

## 8. Help (❓) & Over (ℹ)
- [x] Help opent de handleiding in de standaardbrowser, in de **juiste taal** ✅ 2026-07-30
      (terugval op NL als een taalversie ontbreekt).
- [ ] Over toont het app-logo, het **versienummer**, de beschrijving en het
      HN-Software-logo op de donkere strook; "Sluiten" werkt.

## 9. Talen — kernpaden herhalen
- [x] Herhaal §3–§8 kort in **English** en **Deutsch**; let op dat álle teksten, ✅ 2026-07-30
      meldingen, groottes en datums in de gekozen taal staan (geen NL-restanten).

## 10. Logging verifiëren (zonder een echte crash)
- [x] `app.log` groeit met een nieuwe `starting`-regel bij elke start. ✅ 2026-07-30
- [x] *(Optioneel, ongevaarlijk foutpad)* Hernoem tijdelijk een handleiding-bestand ✅ 2026-07-30
      in de `Help`-map naast de `.exe` en klik op **Help** → je krijgt een nette
      melding én er verschijnt een `[WARN] Could not open the user guide` in `app.log`.
      Zet de naam daarna terug.
- [ ] *(Optioneel)* Controleer dat rotatie werkt: als `app.log` groot wordt,
      ontstaat `app.prev.log` (of vertrouw op de automatische test hiervoor).

## 11. Afsluiten
- [x] De app sluit netjes; er blijft geen `SVGViewer`-proces hangen. ✅ 2026-07-30

---
**Bevindingen / afwijkingen:**

| #   | Onderdeel        | Verwacht                                                                                 | Waargenomen                                                                                                                                                                                                   | Taal | Status                                         |
| --- | ---------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ---------------------------------------------- |
| 1   | 7 - Instellingen | Bij wisselen van taal worden alle teksten in de geselecteerde taal weergegeven           | De geselecteerde taal blijft op Nederlands staan, teksten worden dus alleen in het Nederlands weergegeven                                                                                                     | Alle | Bug                                            |
| 2   | 6 - Contextmenu  | Openen met... toont een dialoog met welke applicatie je de svg wilt openen               | Openen met geeft een foutmelding, openen opent wel de afbeelding in de gekoppelde applicatie openen met geeft een foutmelding "Het bestand kon niet worden geopend"<br><br>Deze foutmelding wordt niet gelogd |      | Bug<br>Indien lastig, "openen met" verwijderen |
| 3   | 10 - Logging     | Alle foutmeldingen, voor de gebruiker zichtbaar of onzichtbaar, worden gelogd in app.log | Zoals bij #2 gezegd niet alle foutmeldingen worden gelogd                                                                                                                                                     |      | Bug                                            |
| 4   | 5 - Preview      | De achtergrond van de preview et een solid color                                         | Was ik eerdr vergeten te melden de preview heeft een doorzichtige achtergrond, mooier is deze wit te maken, want het is storend dat je het achterliggende window  er door heen ziet.                          |      | Verbetering                                    |

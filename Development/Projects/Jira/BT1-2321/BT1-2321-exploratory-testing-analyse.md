# Exploratory testing analyse — BT1-2321

**Titel:** Determine clamp/support usability from laser-head collisions and beam clearances (.NET)
**Epic:** BT2-3028 — V912 - Position material for cutting
**Status:** Analysis Review
**Link:** https://voortman.atlassian.net/browse/BT1-2321

## 1. Waar gaat dit over

Voordat de positioning post processor (BT1-2326) kiest welk machineonderdeel het materiaal vasthoudt of ondersteunt bij een snede, moet er een geometrische check zijn: kan de bewegende laserkop fysiek tegen een onderdeel botsen, en komt de laserstraal te dicht bij een onderdeel?

Drie onderdelen zijn in scope:

- **Gripper** — klemt het materiaal aan de outfeed-kant (S1).
- **Measure roll unit (MRU)** — meet en verplaatst het materiaal aan de infeed-kant (S2).
- **Movable conveyor** — draagt het materiaal alleen van onderaf, klemt nooit (S3).

Voor een kandidaat-materiaalpositie en de kopstanden die een snede gebruikt, moet per onderdeel worden bepaald:

- **Collision** — raakt de laserkop (nozzle + behuizing) het onderdeel fysiek?
- **Clearance** — komt de laserstraal (gemodelleerd als rechte lijn) te dicht bij het onderdeel? Voor de movable conveyor geldt een harde marge van **20 mm** (INV3).

Het resultaat is puur rekenwerk vooraf (geen live/runtime state): per operatie een verzameling posities waarbij elk onderdeel mag klemmen, en welke conveyor-support-posities bruikbaar zijn. Dit voedt zowel de post processor (BT1-2326) als de validator BT1-2327 (die operaties afwijst die de manipulator niet kan positioneren).

**Buiten scope van deze ticket** (belangrijk om in het achterhoofd te houden tijdens exploratory testing, want dit is expres nog niet gedekt):
- De bredere "laser-head body clearance"-regel — nog onbeslist. Dat wil zeggen: alleen de nozzle/behuizing en de straal-als-lijn worden gecheckt, niet het volledige volume van de kop/arm (bijv. kabels, slangen, bevestigingsarm).
- Niet-snij-bewegingen (non-cutting work).
- Het opsplitsen van een staaf in stukken en het resulterende afvalstuk.

## 2. Waarom dit lastig is (risico-inschatting: Medium)

De clearance-geometrie — de straal-als-lijn versus de vorm van de onderdelen, met de kop onder verschillende hoeken — is volgens de auteur zelf het lastigste deel van positioneren. Fout = óf een botsing, óf materiaal dat slecht ondersteund wordt terwijl het systeem dacht dat het goed zat. Dat laatste is extra verraderlijk: een fout die niet meteen een crash geeft, maar een positie die "geldig" lijkt terwijl de werkelijke marge te klein is.

Uit de achtergrondspecificatie ("Positioning material" / V912 Processing zone design) komen een paar concrete risicogebieden naar voren die relevant zijn voor deze check, ook al staan ze niet letterlijk in de ticket:

- In de **blauwe cutting area** (infeed-kant) is er een bekend spanningsveld bij bevelen: bevelen richting outfeed geeft kans op een volumeconflict tussen laserkop/manipulatorarm en de MRU; bevelen richting infeed geeft kans dat de **uittredende** laserstraal de MRU raakt. Dit is exact het soort scenario waar deze ticket een antwoord op moet geven — een goede plek om gericht op te testen.
- De **rode cutting area** (outfeed-kant) is in de designdocumentatie nog letterlijk "to be defined". Als deze ticket ook posities in dat gebied moet beoordelen, is onduidelijk gedrag daar een reëel risico.
- Maximale mechanische bevelhoek is **46°** — een logische grenswaarde om expliciet te beproeven.

## 3. Belangrijkste aandachtspunten voor exploratory testing

### 3.1 De 20 mm clearance-grens (movable conveyor, INV3)
De unit tests dekken dit al "inclusief de exacte grens", maar exploratory testing kan hier net naast de gebaande paden zoeken:
- Precies op 20,0 mm — geaccepteerd of afgewezen? (En is dat consistent met hoe andere 20mm-grenzen in het systeem worden behandeld — inclusief of exclusief?)
- 19,9 / 20,1 mm — juiste kant van de beslissing?
- Combinaties waarbij de 20 mm marge net wordt gehaald door de hoek van de kop te variëren in plaats van de positie — dus dezelfde materiaalpositie, meerdere kophoeken, en kijken of de grens per hoek correct meebeweegt.
- De check is geïmplementeerd als "vergroot de bounding box van de conveyor met 20 mm en test lijn-tegen-box". Een bounding box is een benadering van de werkelijke (mogelijk niet-rechthoekige) vorm van de conveyor. Zoek naar situaties waar de bounding box ruimer of krapper is dan de echte vorm — dat kan een sneetje toestaan dat er in werkelijkheid niet had gemogen, of onterecht afwijzen.

### 3.2 Collision-detectie tegen gripper en MRU
- Kophoeken die precies de rand van het bereik raken (zie 46° max bevel) — juist bij extreme hoeken is de kans op een geometrische randfout het grootst.
- Situaties met een hand-over naar de gripper (CF1/CF2 in de spec) — de ticket vermeldt expliciet "including cuts that need a hand-over to the gripper". Test of de collision-check consistent blijft tijdens/rond het moment van overdracht, en niet alleen in de eindsituatie.
- Materiaal rond de grenswaarden uit de spec: gripper minimum materiaallengte 2002,5 mm, MRU-band tussen -1330 en -730 mm, conveyor reach tussen -177 en 520 mm. Combineer deze grenzen met verschillende kophoeken.

### 3.3 Interactie tussen de drie onderdelen tegelijk
De ticket vraagt om een resultaat per onderdeel, maar in de praktijk moet minstens één onderdeel houvast geven (INV1: materiaal wordt altijd door minstens één mover vastgehouden). Test scenario's waarbij:
- Geen enkel onderdeel een geldige positie oplevert (het "∅"-geval uit de spec) — wordt dit correct en begrijpelijk doorgegeven aan de afnemers (post processor / validator), of leidt dit tot een stille/foutieve fallback?
- Meerdere onderdelen tegelijk een geldige positie hebben — komt de juiste combinatie/voorkeur naar boven, of alleen "iets" geldigs?
- Grensgevallen waarbij het antwoord omslaat tussen "gripper mag klemmen" en "alleen MRU mag klemmen" bij een kleine verandering in materiaalpositie of hoek.

### 3.4 Representatieve snedevormen en kophoeken
De ticket zelf noemt dit als onderdeel van de unit tests ("a few representative cut shapes and head angles"), maar exploratory testing kan hier verder gaan dan "een paar":
- Rechte sneden (straight, loodrecht) versus volle bevel — dit valt samen met de blauw/groen-onderverdeling in de cutting area (blauw = alleen recht + beperkte bevel, groen = volledige bevel).
- Sneden precies op de overgang tussen cutting-area-zones (bijv. rond X=-150, de rand van de groene zone).
- Combinaties van een korte snede met een extreme kophoek, en een lange snede met een kleine hoek — niet alleen de "logische" combinaties.

### 3.5 Wat welbewust NIET gedekt is
Omdat de "wider laser-head body clearance"-regel nog onbeslist is, checkt deze functionaliteit alleen de nozzle/behuizing en de straal-als-lijn. Het is zinvol om, los van of dit een "bug" is, te verifiëren en te documenteren:
- Zijn er reeële combinaties waarbij een ander deel van de kop/arm (niet de nozzle) in de praktijk tegen een onderdeel zou botsen, terwijl deze check "geen collision" zegt? Dit is geen bug in deze ticket (expliciet out of scope), maar wel relevant om te melden aan het team/product, zodat het bewust risico blijft en niet per ongeluk als "afgedekt" wordt beschouwd.
- Idem voor de rode cutting area (nog niet gedefinieerd) — als het systeem daar toch een uitspraak doet, is dat uitspraak betrouwbaar of toevallig?

### 3.6 Afhankelijkheid van de machinedefinitie (BT1-2325)
Deze ticket hangt af van BT1-2325 (vormen en offsets van de onderdelen), die op moment van schrijven nog "In Progress" staat. Aandachtspunt: als de shapes/offsets daar nog wijzigen, kunnen eerder geteste grensgevallen in deze ticket stilzwijgend verschuiven. Bij het testen is het verstandig te noteren met welke versie/waarden van de machinedefinitie is getest, zodat een latere wijziging in BT1-2325 opnieuw gerichte regressie oplevert op juist deze grensgevallen.

## 4. Voorstel voor exploratory sessies (charters)

1. **Charter: 20 mm-grens rond de conveyor.** Tijdbox ~45 min. Doel: de rand van de clearance-beslissing vinden en vastleggen, met de combinatie van positie × hoek, niet alleen positie.
2. **Charter: hand-over-scenario's gripper ↔ MRU.** Tijdbox ~45 min. Doel: blijft de collision/clearance-uitspraak kloppen rond en tijdens een CF1/CF2-overdracht?
3. **Charter: "niemand kan vasthouden" en "iedereen kan vasthouden".** Tijdbox ~30 min. Doel: gedrag bij het ∅-geval en bij overlappende geldige opties in kaart brengen.
4. **Charter: extreme kophoeken (rond 46°) op de blauw/groen-grens.** Tijdbox ~30 min. Doel: geometrische randfouten bij bevelen vinden, met name de twee bekende risico's uit de designdocs (volumeconflict met MRU bij bevelen naar outfeed, straal-raakt-MRU bij bevelen naar infeed).
5. **Charter: buiten-scope-signalering.** Tijdbox ~20 min. Doel: geen bugs zoeken, maar bewust een lijstje maken van reële situaties die door de bekende scope-uitsluitingen (body clearance, rode zone) niet gedekt worden, om terug te koppelen aan het team.

## 5. Vragen om af te stemmen met het team (geen testbevindingen, maar aannames die het testen beïnvloeden)

- Is er al een concrete waarde voor `C2` (MRU laser-beam clearance)? De spec noemt die als "not yet binding" — zonder waarde is een deel van de MRU-clearance-check mogelijk nog niet zinvol te testen.
- Wanneer is BT1-2325 (machinedefinitie) stabiel genoeg om hierop te testen zonder dat de shapes nog wijzigen?
- Is er al zicht op wanneer dit "wired into positioning" is, zoals de ticket als voorwaarde noemt voor de exploratory testing?

---
*Analyse opgesteld ter voorbereiding van exploratory testing op BT1-2321, gebaseerd op de ticket zelf en de achtergrondspecificatie "Positioning material" en "V912 Processing zone – Design" (Confluence, ruimte Engineering).*

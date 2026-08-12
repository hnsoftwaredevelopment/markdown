# Testanalyse — gerelateerde tickets bij BT1-2321 (Epic BT2-3028: V912 - Position material for cutting)

Dit document behandelt de zes tickets die je hebt opgegeven, als vervolg op de eerdere analyse van BT1-2321. Voor elk ticket staan de aandachtspunten en concrete testpunten. Daarna volgt een samenvatting van alle tickets samen, een lijst met openstaande vragen, en een sectie met tests die pas mogelijk zijn zodra alles klaar is.

## 0. De keten in één plaatje

Alle tickets horen bij epic **BT2-3028 — V912 - Position material for cutting**. De afhankelijkheden lopen zo:

```
BT1-2324 (spike, Done)
   └─▶ BT1-2325 (machine-definitie, In Progress)
          └─▶ BT1-2321 (collision/clearance-check, Analysis Review — al geanalyseerd)
                 ├─▶ BT1-2322 (conveyor support, Analysis Review)
                 │      └─▶ BT1-2326 (positioning post-processor, Analysis Review)
                 │             └─▶ BT1-2323 (plan-checker/oracle, Analysis Review)
                 └─▶ BT1-2327 (validator, Analysis Review)
```

Praktisch: **BT1-2325 is nu de bottleneck** — zolang die niet klaar is (en de meetwaarden nog hardcoded/onbevestigd in code zitten), kunnen 2321, 2322, 2326 en 2327 wel losstaand met synthetische/mock-data getest worden, maar niet echt end-to-end.

## 1. BT1-2322 — Movable conveyor support positioning for cutting

**Status:** Analysis Review. **Risico:** Low–medium (leunt op BT1-2321).

### Waar het over gaat
Tijdens het positioneren moet de movable conveyor het materiaal zoveel mogelijk van onderaf ondersteunen, zodat het niet doorzakt. Voor elke snede wordt bepaald: steunt de conveyor, en waar zit de rol? Het is **best-effort**: steun geven waar een veilige positie bestaat, alleen overslaan als er geen ruimte is. Een veilige positie = de rol zit onder het materiaal, binnen het bereik van de conveyor (**-177 mm tot +520 mm**), én de laserstraal blijft 20 mm van de conveyor af (dat laatste komt uit BT1-2321). De rol kan op een paar plekken staan: helemaal ingetrokken (rust), onder de klauw van de gripper, of onder het materiaal voorbij de gripper. Als nergens een veilige positie is (bijv. materiaal helemaal naar de infeed-kant geduwd), valt het systeem terug op **edge positioning**: het materiaal net binnen het snijgebied leggen zodat de vaste bedrollen het grootste deel dragen.

### Aandachtspunten
- **Geen voorkeur tussen gelijkwaardige posities** — de ticket zegt expliciet dat elke veilige positie goed genoeg is. Dat is functioneel prima, maar is het gedrag ook **deterministisch**? Als twee keer dezelfde input een andere conveyor-positie oplevert, wordt regressietesten en foutopsporing lastiger. Dit is iets om gericht op te testen, ook al is het geen functionele bug per definitie.
- **Overlap van twee begrenzingen tegelijk** — het bereik van de conveyor (-177/+520 mm) én de 20 mm-clearance uit BT1-2321 moeten allebei gelden. Interessante combinaties zitten precies op de rand van één van beide terwijl de andere ruim voldoet, en omgekeerd.
- **Drie roller-modi (rust / onder de klauw / onder het materiaal voorbij de gripper) plus het "vrij hangend" geval** — check dat het systeem niet per ongeluk de verkeerde modus kiest wanneer twee modi qua positie dicht bij elkaar liggen.
- **Randgeval "off-cut > 800 mm"** wordt in de ticket genoemd als bestaand in het support-table van de machine, maar kan nu nog niet voorkomen (elke staaf ≥ 2002,5 mm, nog geen sneden die de staaf opdelen). Dit is een bewuste, tijdelijke aanname — zodra bar-splitting wordt gebouwd (buiten deze epic-scope voor nu) is dit een goede regressie-kandidaat.
- **Edge-positioning-fallback** — test het omslagpunt precies: op welk moment schakelt het systeem van "conveyor ondersteunt" naar "edge positioning"? Dat omslagpunt ligt aan de rand van het conveyor-bereik en is dus gevoelig voor dezelfde randfouten als bij BT1-2321.
- De ticket zelf noemt alleen **unit tests**, geen exploratory testing — in tegenstelling tot BT1-2321 en BT1-2327 waar dat wel expliciet staat. Dat is geen probleem, maar betekent dat als jij hier toch exploratory tijd aan besteedt, dat een bewuste keuze is (zeker gezien de afhankelijkheid van BT1-2321's clearance-berekening) en niet iets wat de ticket van je vraagt.

### Concrete testpunten
- Materiaal-/snijposities net binnen en net buiten het conveyorbereik (-177 / +520 mm), gecombineerd met verschillende materiaallengtes.
- Dezelfde input twee keer aanbieden en verifiëren of de gekozen conveyorpositie stabiel is.
- Een snede waarbij de enige veilige positie toevallig "onder de klauw van de gripper" is — check of dat gedetecteerd en correct als zodanig gerapporteerd wordt (in plaats van als "geen positie").
- Het exacte omslagpunt naar edge-positioning: net wel en net niet een veilige conveyorpositie beschikbaar.
- Een reeks van meerdere sneden op één staaf waarbij de conveyor tussen sneden van positie moet wisselen — check of dat elke keer opnieuw correct (en binnen bereik) gebeurt.

## 2. BT1-2323 — Plan-invariant validation harness for V912 positioning

**Status:** Analysis Review. **Risico:** Low (read-only check, past niets aan).

### Waar het over gaat
Omdat het hele positioneringsplan vooraf wordt uitgerekend (geen live state machine), kan het achteraf gecontroleerd worden door een simpele functie: plan erin, overtreden regels eruit. Dit is de "test oracle" voor BT1-2326. De regels:
- Materiaal wordt altijd door minstens één onderdeel gehouden (gripper of MRU).
- Elke overdracht tussen gripper en MRU gaat via een moment waarop beide vasthouden.
- De laserstraal komt nooit binnen 20 mm van de movable conveyor.
- De laserstraal blijft vrij van de measure roll unit — maar deze check **slaagt momenteel altijd**, omdat het snijgebied door constructie al ver genoeg van de MRU af ligt. Het wordt pas een echte beperking als snijden ooit dichter bij de MRU komt te liggen.

Dit is dus **anders** dan de validator (BT1-2327): die weigert onmogelijke operaties vooraf; deze checker bevestigt dat een al gegenereerd plan intern consistent is.

### Aandachtspunten
- De vierde regel (MRU-clearance) is op dit moment **een placeholder die altijd "ok" teruggeeft**. Dat is geen bug, maar wel iets om bewust te testen: bevestig dat hij inderdaad altijd doorlaat, zodat er geen verrassing is als iemand later denkt dat deze check al echt iets controleert.
- Deze ticket hangt af van BT1-2326 om **echte** plannen te genereren; met alleen deze ticket klaar kun je hem uitsluitend testen met handgemaakte (synthetische) plannen. Dat is prima voor de unit tests uit de ticket zelf, maar als exploratory tester wil je juist wachten tot BT1-2326 er is om **echte, door het systeem gegenereerde plannen** erdoorheen te halen — dat is waar onverwachte bugs (in 2326, niet in 2323) naar boven kunnen komen.
- Omdat het een read-only check is: verifieer dat het uitvoeren van de checker het gecontroleerde plan niet per ongeluk wijzigt.

### Concrete testpunten
- Voor elke regel afzonderlijk een plan bouwen dat **precies die ene regel** breekt, en controleren dat alleen die regel wordt gerapporteerd (geen valse positieven op de andere regels).
- Een grensgeval van de overdrachtsregel: een plan waarin het "beide vasthouden"-moment er net wel/net niet is (bijvoorbeeld één stap te vroeg vrijgegeven).
- Een volledig correct plan door de checker halen en bevestigen dat het schoon (zonder violations) doorkomt.
- Zodra BT1-2326 beschikbaar is: een paar van je eigen exploratory-scenario's uit BT1-2326 nogmaals door deze checker halen als extra vangnet.

## 3. BT1-2324 — Spike: confirm V912 positioning geometry and working direction

**Status:** Done (afgerond, geen productiecode). Dit is een onderzoeksticket — geen automatische tests, en dus ook niets om zelf te (exploratory) testen. Wel relevant om te kennen, omdat de uitkomst de **bronwaarheid** is voor de getallen die BT1-2325 en BT1-2321 gebruiken.

### Bevestigde waarden (uit de ticket-comments)
- MRU-materiaalband: **-730 → -1330 mm**, afgeleid uit bedrollen op -780/-1280 mm met minimaal 50 mm overhang.
- Bedrollen vast op **-780 mm** (dichtbij) en **-1280 mm** (ver); moeten altijd contact maken met het materiaal.
- Werkrichting: het Execution Framework is richtingsonafhankelijk; **X+ loopt richting de outfeed** — bevestigt het bestaande machine-frame.
- Conveyorbereik: **-177 → +520 mm** — correct.
- Snijgebied: **±150 mm**, volledige box 300 × 1160 × 460 mm — correct.

### Wat nog open bleef (relevant om in het achterhoofd te houden bij het testen van de andere tickets)
- De positie van de aandrijfrol (930 mm) is expliciet als **"fictional"** (verzonnen/placeholder) gemarkeerd, en de meetwiel-positie (1180 mm) is niet in het model gebakken — geen van beide is nu nodig voor positionering of clearance, maar de meetwiel-positie is relevant voor het nog open toekomstige punt "cut-away material at the measure-wheel position" uit de specificatie.
- Het model behandelt de MRU als één klem, terwijl de tekening een gescheiden horizontale + verticale klem beschrijft (met een hoogtelimiet voor de verticale klem) — erkend, maar niet volledig opgelost of dat onderscheid het model ooit moet bereiken.

**Aandachtspunt voor jou als tester:** als je bij BT1-2325/2321/2322/2326 een geometrische waarde tegenkomt die niet overeenkomt met de tabel hierboven, is dat een concrete afwijking om te melden — dit zijn de enige "officieel bevestigde" getallen.

## 4. BT1-2325 — V912 material-mover machine definition

**Status:** In Progress (blokkeert BT1-2321). **Risico:** Low (fundamenteel, ingekaderd tot V912; bestaande constructor blijft behouden zodat VACAM niet breekt).

### Waar het over gaat
Dit ticket beschrijft de V912-machine in code: de measure roll unit en de gripper als afzonderlijke "movers", plus `V912MaterialMover` die beide samen laat bewegen ("tandem"). Ook worden de vaste bedrollen (-780/-1280 mm, altijd in contact) gemodelleerd, en komen alle bevestigde metingen uit BT1-2324 als named settings binnen (hardcoded mag, met een follow-up als er nog geen database-configuratie is). Conveyor-tracking wordt bewust nog niet gebouwd.

### Aandachtspunten
- **Backwards compatibility is een harde eis**: de bestaande constructor `V912Machine(cuttingRecords, profileCutter)` moet blijven werken, omdat VACAM deze als vastgepinde NuGet-package aanroept. Dit is precies het soort regressie die makkelijk over het hoofd wordt gezien bij "gewoon een nieuwe constructor toevoegen".
- **Consistentie met BT1-2324**: de named settings moeten letterlijk overeenkomen met de bevestigde tabel (zie hierboven). Een kleine sign-fout of afgeronde waarde hier plant zich door naar alle latere tickets.
- **Hardcoded-tot-follow-up**: als de database-configuratie nog niet beschikbaar is, is hardcoderen toegestaan — mits er een follow-up ticket voor is. Waard om te checken of die follow-up er daadwerkelijk is/komt, zodat dit niet stilletjes "voor altijd hardcoded" blijft.
- Dit ticket is grotendeels **fundamenteel/technisch** (geen gebruikersgedrag) — het meeste hier is beter te verifiëren via de unit tests die de ticket zelf noemt (machine boot, MRU/gripper/mover blootgesteld, step-definities produceerbaar) dan via exploratory testing. Voor jou als tester is dit vooral relevant als **context**: als iets in 2321/2322/2326 vreemd gedrag toont, is de eerste vraag "komt dit van een verkeerde waarde/aanname hier in 2325?".

### Concrete testpunten (voor zover relevant voor een tester, niet alleen developer)
- Cross-check: haal de daadwerkelijk gebruikte constanten op (via config/settings, niet alleen documentatie) en vergelijk ze regel voor regel met de BT1-2324-tabel.
- Verifieer dat de bestaande VACAM-integratie (het pinned package-pad) nog steeds bouwt/werkt na deze wijziging — een regressietest, geen nieuwe functionaliteit.
- Als je toegang hebt tot een staging/testomgeving met een V912-machine-configuratie: controleer of de measure roll unit en de gripper allebei zichtbaar/aanstuurbaar zijn als los onderdeel, en of "beide tandem" ook echt als apart pad beschikbaar is.

## 5. BT1-2326 — Positioning post-processor for cutting — SCENARIO_CUT

**Status:** Analysis Review. **Risico:** Medium — dit is de kern-orkestratie, en leunt op BT1-2321 én BT1-2322.

### Waar het over gaat
Dit is het onderdeel dat voor elke geprogrammeerde snede daadwerkelijk kiest welk onderdeel (of onderdelen) het materiaal vasthoudt, en de bijbehorende machinestappen uitzendt. Drie manieren om vast te houden: **MRU** (sneden vanaf 1180 mm langs de staaf tot de voorkant — kan de achterste 1180 mm van de staaf niet zelf in het snijgebied krijgen), **Gripper** (vanaf de achterkant tot 785 mm voor de voorkant, en alléén als de staaf ≥ 2002,5 mm is), en **beide samen** (overlap van de twee bereiken, voor extra stevigheid). Het systeem houdt bij wie er op elk moment vasthoudt en wisselt van houder wanneer nodig. Klemstrips: de eerste versie klemt altijd met **3 strips** (staven boven 2000 mm).

### Aandachtspunten
- **Discrepantie tussen twee drempelwaarden**: de gripper mag pas gebruikt worden bij staven ≥ **2002,5 mm**, maar de klemstrip-regel spreekt over staven **"over 2000 mm"**. Wat gebeurt er precies met een staaf tussen 2000 en 2002,5 mm? Dit is een concrete, klein-maar-scherp testpunt dat rechtstreeks uit de ticicket-tekst naar boven komt.
- **Overgangen tussen houders** (MRU → beide → gripper, en terug) zijn de meest waardevolle testgevallen: precies op de randen van de bereiken (1180 mm vanaf achterkant voor MRU-start, 785 mm voor de voorkant voor gripper-eind) is de kans op een off-by-one of een verkeerd gekozen houder het grootst.
- **"Als niemand kan vasthouden is dat een bug — of de validator had het al moeten afwijzen."** Dat is een expliciete aanname die je kunt beproeven: bied bewust een operatie aan die op de rand van afwijzing door BT1-2327 zit, en kijk wat BT1-2326 doet als die validatie (nog) niet correct gekoppeld is — faalt het netjes, of genereert het stilletjes een fysiek onmogelijk plan?
- **Volgordelijkheid van stappen** wanneer een houderwissel én een conveyor-verplaatsing (BT1-2322) voor dezelfde snede allebei nodig zijn — is de volgorde van de uitgezonden stappen fysiek zinvol (bijv. conveyor eerst uit de weg voordat de gripper overneemt), of kan dat in theorie tegelijk/verkeerd-om gebeuren?
- **Meerdere sneden achter elkaar op één staaf**: test niet alleen of elke snede afzonderlijk een geldige houder/positie krijgt, maar of de **overgang** tussen twee opeenvolgende sneden consistent is — bijvoorbeeld geen onnodige extra wissel heen-en-terug tussen gripper en MRU wanneer dat niet nodig was.
- De ticket vraagt zelf om elk gegenereerd plan door de checker (BT1-2323) te laten lopen — een goede exploratory-gewoonte: na elk handmatig scenario ook even de checker erover heen halen als extra vangnet.

### Concrete testpunten
- Staven van exact 2000, 2002,4 en 2002,5 mm, met een snede die de klemstrip-keuze raakt.
- Een snede precies op 1180 mm vanaf de achterkant (MRU-drempel) en precies 785 mm voor de voorkant (gripper-drempel).
- Een reeks van 4–5 sneden die bewust heen en weer springen tussen "alleen MRU haalbaar" en "alleen gripper haalbaar", om overmatige of foutieve wissels te ontdekken.
- Een operatie die je verwacht dat de validator (BT1-2327) zou afwijzen, rechtstreeks aan de post-processor aanbieden (los van de validator) om het foutgedrag te zien.
- Elk van bovenstaande scenario's ook door de BT1-2323-checker halen.

## 6. BT1-2327 — Validation: reject operations the manipulator cannot position for

**Status:** Analysis Review. **Risico:** Low (faalt veilig — wijst af in plaats van verkeerd te positioneren).

### Waar het over gaat
Deze validator filtert onmogelijke operaties er vooraf uit. Voor de eerste versie: alleen operaties die **volledig binnen de groene snijzone** passen worden toegelaten; de rest wordt afgewezen. Ook afgewezen: operaties die alleen door de MRU gepositioneerd zouden kunnen worden, maar buiten de groene zone vallen omdat ze aan het **allerachterste eind van de staaf** liggen (de MRU kan de achterste 1180 mm niet in het snijgebied krijgen). Een operatie wordt afgewezen als **geen enkele** manier van vasthouden (gripper, MRU, of beide) hem in de groene zone kan plaatsen met een onderdeel dat daar mag klemmen (gebaseerd op BT1-2321). Het is afgestemd met Mohammad Pourmehdi dat "alleen de groene zone" acceptabel is voor deze eerste versie.

### Aandachtspunten
- Dit ticket noemt, net als BT1-2321, **expliciet exploratory/manual testing** in de testplan-sectie — dit is dus een van de tickets waar jouw exploratory werk het meest verwacht/gewaardeerd wordt.
- **Bewuste v1-beperking**: blauwe en rode zones worden domweg afgewezen, ook al zou een deel daarvan mechanisch misschien haalbaar zijn (zie de achtergrond-spec: blauw staat "te definiëren", rood staat letterlijk "to be defined"). Dat is geen bug, maar wel iets om te bevestigen en te documenteren — zodat als een gebruiker een blauwe-zone-snede aanbiedt en hij wordt afgewezen, dat gezien wordt als verwacht v1-gedrag en niet als incident.
- **Operaties die een hand-over naar de gripper nodig hebben** zitten expliciet IN scope — dus een belangrijke valse-negatieve-check is: worden dat soort operaties, die zonder hand-over zouden worden afgewezen maar mét hand-over wél passen, ook echt geaccepteerd? Dat is net zo belangrijk als het testen van de afwijzingen zelf.
- **Afhankelijkheid van BT1-2321's precisie**: de accept/reject-beslissing hier steunt volledig op het collision/clearance-resultaat uit BT1-2321. Elke onnauwkeurigheid daar (bijv. de bounding-box-benadering van de conveyor, of de 20 mm-grens) werkt hier direct door in een fout-geaccepteerde of fout-afgewezen operatie.

### Concrete testpunten
- Operaties precies op de rand van de groene zone (±150 mm) — net binnen en net buiten.
- Een snede precies op de 1180 mm-drempel vanaf de achterkant, gecombineerd met "MRU is de enige optie".
- Een operatie die zonder hand-over onmogelijk is maar mét hand-over (gripper) wél in de groene zone past — bevestig dat die geaccepteerd wordt.
- Een aantal bewuste blauwe- en rode-zone-operaties aanbieden en bevestigen dat ze consistent worden afgewezen (en dit als verwacht v1-gedrag documenteren, niet als bug).
- Grensgevallen waarbij BT1-2321 een marginale clearance teruggeeft (net wel/niet 20 mm) — controleer of de validator daar consistent mee omgaat.

## 7. Samenvatting van alle tickets

| Ticket | Titel | Status | Rol in de keten |
| --- | --- | --- | --- |
| BT1-2321 | Determine clamp/support usability from laser-head collisions and beam clearances | Analysis Review | Geometrische kern: botsing/clearance-check per onderdeel (gripper, MRU, conveyor) |
| BT1-2322 | Movable conveyor support positioning for cutting | Analysis Review | Bepaalt of en waar de conveyor het materiaal ondersteunt |
| BT1-2323 | Plan-invariant validation harness for V912 positioning | Analysis Review | Achteraf-checker/oracle: controleert of een gegenereerd plan alle regels naleeft |
| BT1-2324 | Spike: confirm V912 positioning geometry and working direction | **Done** | Bevestigt de meetwaarden die alle andere tickets gebruiken |
| BT1-2325 | V912 material-mover machine definition | In Progress | Modelleert de machine (MRU, gripper, tandem-mover) in code |
| BT1-2326 | Positioning post-processor for cutting — SCENARIO_CUT | Analysis Review | De kern-orkestratie: kiest houder + positie per snede, zendt stappen uit |
| BT1-2327 | Validation: reject operations the manipulator cannot position for | Analysis Review | Wijst vooraf operaties af die de machine niet aankan |

Samengevat bouwt dit geheel een **plan-vooraf-generator** voor het positioneren van een stalen profiel in de V912-lasermachine: eerst worden onmogelijke sneden eruit gefilterd (2327), dan wordt voor de rest een plan gemaakt (2326, leunend op de geometrie uit 2321 en de conveyor-logica uit 2322), en dat plan kan achteraf gecontroleerd worden op interne consistentie (2323). Alles steunt op de machinebeschrijving (2325) en de bevestigde metingen (2324, al afgerond).

## 8. Openstaande vragen (verzameld uit alle tickets)

- **C2 (MRU-laserstraalclearance)** stond in de achtergrondspecificatie als "nog niet bindend" — wordt dit voor nu afgedekt door de placeholder-check in BT1-2323 (die altijd slaagt), of moet hier nog een echte waarde/berekening komen?
- De aandrijfrol-positie (930 mm, gemarkeerd als **fictief**) en de meetwiel-positie (1180 mm) uit BT1-2324 zijn nog niet in het model verwerkt — relevant voor het nog open punt "cut-away material at the measure-wheel position" uit de specificatie. Wanneer wordt dit oppakt, en welke waarde is dan de echte?
- Moet het onderscheid tussen de horizontale en verticale klem van de MRU (met een hoogtelimiet voor de verticale klem, zoals de tekening beschrijft) ooit het model bereiken, of blijft de MRU voor altijd als één klem gemodelleerd?
- In BT1-2326: wat is het bedoelde gedrag voor een staaf tussen **2000 mm en 2002,5 mm** — de klemstrip-regel ("boven 2000 mm") en de gripper-ondergrens (2002,5 mm) spreken elkaar hier niet tegen, maar overlappen ook niet helemaal duidelijk.
- De bredere "laser-head body clearance"-regel (BT1-2321) is nog onbeslist — wanneer en door wie wordt die alsnog vastgesteld?
- De rode en blauwe snijzones staan in de "V912 Processing zone – Design"-tekening nog als "te definiëren" — is er een plan om dat ooit op te pakken, of blijft "alleen groene zone" de blijvende scope voor V912?
- Is BT1-2325 al zo ver dat de named settings echt uit database-configuratie komen, of draait dit nog op hardcoded waarden met een (nog te maken?) follow-up ticket?

## 9. Tests die alleen mogelijk zijn zodra álles klaar is

Deze zijn pas echt uitvoerbaar zodra BT1-2325, BT1-2321, BT1-2322, BT1-2326 én BT1-2327 allemaal klaar zijn (BT1-2323 is techisch al eerder met synthetische plannen te testen, maar krijgt hier zijn volle waarde):

1. **Volledige end-to-end job**: een realistische reeks sneden op één staaf door de hele pijplijn heen — validator wijst onmogelijke sneden af (2327), de post-processor bouwt het volledige plan met houder- en conveyorkeuzes voor de rest (2326 + 2321 + 2322), en de checker bevestigt dat het hele plan intern consistent is (2323). Dit is de enige plek waar je ontdekt of de losse onderdelen echt goed op elkaar aansluiten.
2. **Meerdere handovers + conveyor-verplaatsingen in dezelfde job**: de volgorde en onderlinge afhankelijkheid van stappen over de hele plan-lengte heen is alleen zichtbaar met de volledige pijplijn, niet per ticket afzonderlijk.
3. **Regressie op de grensgevallen die je per ticket hierboven al hebt gevonden** — bijvoorbeeld het 2000–2002,5 mm-gat in BT1-2326 gecombineerd met de exacte 20 mm-grens uit BT1-2321: deze zitten op de naad tussen twee tickets en zijn dus het makkelijkst te missen als je per ticket apart test.
4. **Determinisme/consistentie over de hele keten**: dezelfde input twee keer door de volledige pijplijn heen, en controleren of je exact hetzelfde plan terugkrijgt (relevant omdat BT1-2322 bewust "geen voorkeur" heeft tussen gelijkwaardige conveyorposities).
5. **Prestatie/doorloop bij een lange staaf met veel sneden**: pas met de hele keten samen zie je of plan-generatie + validatie + checker samen niet onaanvaardbaar traag worden.
6. **Wat nadrukkelijk nog niet getest kan worden, ook niet dan**: de daadwerkelijke aansturing van de VACAM-machine. BT1-2325 noemt expliciet dat de VACAM-package-bump en command-generators voor de nieuwe stap-types een **apart, nog niet aangemaakt vervolgticket** zijn. Zonder dat werk kun je deze pijplijn dus wel valideren als plan, maar niet als daadwerkelijke machinebesturing.

---
*Analyse opgesteld als vervolg op de eerdere BT1-2321-analyse, gebaseerd op de tickets BT1-2322 t/m BT1-2327 en de achtergrondspecificatie "Positioning material" (Confluence, ruimte Engineering).*

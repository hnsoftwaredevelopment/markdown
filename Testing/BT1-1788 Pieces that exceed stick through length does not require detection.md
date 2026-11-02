---
ticket: BT1-1788
jira: https://voortman.atlassian.net/browse/BT1-1788
status: In Test
fix: ExecutionPlanner PR #589 (gemerged 2026-10-27)
package: Voortman.Execution.Beams.Configuration >= 2.151.0
backup: 20240041_V630_250425_171852.zip
tags: [testplan, vacam, execution-planner, measure-rollers]
---

# BT1-1788 Pieces that exceed stick through length does not require detection

## Probleem

Op een V630M met LES (backup `20240041_V630`) gelden deze instellingen:

| Instelling | Waarde |
|---|---|
| Maximum stick through length | 6800 mm |
| Outfeed.OutfeedPosition | 2500 mm |
| Maximale materiaallengte op de outfeed | 6000 mm |

In batch 18 (batch ID 19) zitten 2 producten van 2750 mm. VACAM doet een *detect front* op het reststuk, terwijl dat reststuk toch handmatig van de infeed af moet. Dat kost een infeed en een detect, en daarna gaat het materiaal weer terug naar de infeed.

Oorzaak: `PieceExceedsStickThroughLength` in `DeterminePiecesThatRequireDetection` keek alleen naar de lengte van het stuk. De outfeed-positie werd niet meegenomen.

## Fix

ExecutionPlanner [PR #589](https://github.com/voortman-steel-machinery/ExecutionPlanner/pull/589) (VincentVel). Een reststuk telt nu als te lang als een van deze twee voorwaarden waar is:

1. `lengte > maximum stick through length` (de oude controle, die bleef bestaan)
2. `outfeedPosition + lengte > maximum stick through length` (nieuw)

De eerste controle staat los van de tweede. Zo kan een negatieve outfeed-positie een stuk dat op zichzelf al te lang is niet alsnog laten passeren.

Een te lang reststuk krijgt geen detectie en blijft op de infeed liggen voor handmatige verwijdering. De rest van de logica is ongewijzigd:

- Een handmatige deling (manual division): geen detectie.
- Een product (geen reststuk): detectie als het verder bewerkt kan worden.
- Een reststuk dat niet te lang is: detectie alleen als `RestMaterialToOutfeed` aan staat.

De outfeed-positie wordt nu doorgegeven in alle measure-rollers-factories:

| Machine | Varianten |
|---|---|
| V630Mk2 | Back-to-back saw, Back-to-back saw met fixed rotatable table, Standalone |
| V631 | Back-to-back saw, Back-to-back saw met fixed rotatable table, Standalone |
| V633 | Back-to-back saw, Standalone |

Hij wordt ook doorgegeven in de mappers `DetectMaterialMapper`, `ClampMaterialDuringExecutionMapper`, `MoveMaterialBackwardsMapper` en `MaterialClampedByMeasureRollUnitMapper`.

> [!warning] Blocker: VACAM develop bevat de fix nog niet
> De fix zit in `Voortman.Execution.Beams.Configuration` 2.151.0 en hoger. VACAM develop gebruikt op 2026-11-02 nog **2.150.0**, en er staat geen open PR voor de update (de laatste Renovate-update was 2.145.0, PR #22274).
>
> Opties:
> - Wachten tot Renovate de package op develop bijwerkt.
> - Een VACAM-worktree van develop met de package lokaal op 2.151.0 of hoger zetten en die bouwen (Visual Studio mode). Dit gebeurt alleen lokaal en wordt niet gepusht.

## Grenswaarden voor de backup

Met stick through 6800 mm en outfeed-positie 2500 mm ligt de nieuwe grens op **6800 - 2500 = 4300 mm** voor de lengte van het reststuk.

| Lengte reststuk | Oud (2.150) | Nieuw (>= 2.151) |
|---|---|---|
| <= 4300 mm | detectie | detectie (onveranderd) |
| 4300 < lengte <= 6800 mm | detectie | **geen detectie** |
| > 6800 mm | geen detectie | geen detectie (onveranderd) |

Detectie van een reststuk gebeurt in alle gevallen alleen als `RestMaterialToOutfeed` aan staat. Dat moet ik nog nakijken in de backup.

De lengte van het reststuk is de materiaallengte min de producten, de zaagsneden en de clear cuts. Om een gewenste lengte te krijgen pas je de materiaallengte in de batch aan. De echte lengte van het reststuk staat in de operation list.

## Voorbereiding

- [ ] VACAM met Execution package >= 2.151.0 (zie blocker)
- [ ] Backup `20240041_V630_250425_171852.zip` uit Jira lokaal terugzetten (vacam-simulation skill)
- [ ] In de backup nakijken: `MaximumStickThroughLength`, `Outfeed.OutfeedPosition`, `RestMaterialToOutfeed` en de materiaallengte van batch 18
- [ ] Referentie: dezelfde batch één keer draaien op develop met 2.150.0 en de operation list bewaren, zodat je oud en nieuw kunt vergelijken

## Hoe je het resultaat controleert

In de operation list (`Logs\AutomaticProductionList\Operation List <tijd>.csv`) kijk je bij het reststuk naar deze regels:

- *Infeed current material* / *Detect front material* / *Detect end material* voor het reststuk
- het terugvoeren van het materiaal naar de infeed

Zonder detectie hoort het reststuk na de laatste zaagsnede op de infeed te blijven, met een melding aan de operator om het handmatig te verwijderen.

## Testcases

### TC1 Reproductie uit het ticket (batch 18)

- **Stappen:** start de backup, start batch 18 (2 x 2750 mm) en draai de productie tot de laatste zaagsnede.
- **Verwacht:** geen *detect front* op het reststuk en geen terugvoer naar de infeed. Het reststuk blijft op de infeed liggen voor handmatige verwijdering.
- **Vergelijk:** de operation list van 2.150.0 bevat die stappen nog wel. De nieuwe lijst is korter.

### TC2 Reststuk net onder de grens

- **Stappen:** stel de materiaallengte zo in dat het reststuk ongeveer 4200 mm wordt.
- **Verwacht:** het reststuk wordt gedetecteerd en gaat naar de outfeed (als `RestMaterialToOutfeed` aan staat). Dit is gelijk aan het oude gedrag.

### TC3 Reststuk net boven de grens

- **Stappen:** stel het reststuk in op ongeveer 4400 mm.
- **Verwacht:** geen detectie, en het reststuk blijft op de infeed. Dit is het nieuwe gedrag.

### TC4 Reststuk langer dan de stick through length

- **Stappen:** stel het reststuk in op ongeveer 7000 mm.
- **Verwacht:** geen detectie. Dit was ook vóór de fix al zo.

### TC5 RestMaterialToOutfeed uit

- **Stappen:** zet `RestMaterialToOutfeed` uit en herhaal TC2.
- **Verwacht:** geen detectie van het reststuk. Dit is ongewijzigd.

### TC6 Producten worden nog steeds gedetecteerd

- **Stappen:** gebruik een batch met meerdere producten waarbij een tussenstuk verder bewerkt moet worden.
- **Verwacht:** de detectie van producten (geen reststukken) is ongewijzigd, ook als een product langer is dan 4300 mm.

### TC7 Regressie op een andere machine

- **Stappen:** neem een V631- of V633-backup met measure rollers uit `\\vasoftware\Testdata\RegressionTests`, bereken de grens met de instellingen van die machine en herhaal TC2 en TC3.
- **Verwacht:** hetzelfde gedrag als op de V630. Zo zie je dat de outfeed-positie in alle factories goed wordt doorgegeven.

### TC8 Handmatige deling (optioneel)

- **Stappen:** zet een handmatige deling op het reststuk.
- **Verwacht:** geen detectie. Dit is ongewijzigd.

## Risico's en aandachtspunten

- **Negatieve of afwijkende outfeed-positie.** De unit tests dekken dit af (een negatieve positie maakt een te lang stuk niet geldig). Test het in VACAM alleen als een configuratie dat echt gebruikt.
- **Planning.** Omdat het reststuk niet meer gedetecteerd wordt, kan de volgorde in de operation list veranderen (minder stappen). Let op dat de laatste zaagsnede en de afvoer van het laatste product niet veranderen.
- **Simulatie.** In VASIM moet het materiaal op de juiste plek liggen. Voor een V630/V631 is X het achtereind van de balk (front = X + lengte). Het produce-script stopt bij een dialoog die het niet kent, zoals de melding om materiaal handmatig te verwijderen. Die beantwoord je dan zelf.
- **Unit tests.** Die bestaan al voor de grens (`outfeedPosition` 2000 tegenover 2001) en voor een negatieve outfeed-positie. Ze opnieuw draaien voegt weinig toe. De VACAM-test laat zien dat de juiste configuratiewaarden echt doorkomen.

## Resultaat

| TC | Resultaat | Opmerking |
|---|---|---|
| TC1 | | |
| TC2 | | |
| TC3 | | |
| TC4 | | |
| TC5 | | |
| TC6 | | |
| TC7 | | |
| TC8 | | |

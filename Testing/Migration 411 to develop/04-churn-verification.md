# 04 — Churn + verificatie (kwantitatieve rangorde compleet)
Baselines: OUD=`4.11.33.14`, NIEUW=`develop`. Vervolg op `03-heatmap.md`.

## Verificatie ❓-objecten (nieuw vs. hernoemd)
Getoetst door de token in de 4.11-boom te zoeken:
- **Écht nieuw** (0 hits op 4.11 → nieuw gedrag/nieuwe inbedrijfstelling): `SawIntegratedShortPieceRemover`, `ChainLifter`, `Manipulator`, `MaterialPusher`, `CncInterpolationManager`.
- **Nieuwe abstractie over bestaand gedrag**: `MaterialClampingSystem` (klemmen bestond via `Chuck`/`ClampCylinder`).
- **Refactor/uitsplitsing** (laag risico): `SawBandControl` — `SawBand` bestond al binnen `Saw` (6 POU's op 4.11).

## Churn-methode
Eén `git diff -M10% -l0 --numstat` over `twincat/` mét rename-detectie, gebucket per nieuw object.
- **churn** = som van gewijzigde regels op POU's die git als hernoemd/verplaatst-én-bewerkt herkende (= veranderd bestaand gedrag).
- **newlines** = toevoegingen op POU's zonder 4.11-tegenhanger (= nieuwe functionaliteit).
- Kanttekeningen: TcPOU zijn XML, dus churn bevat wat metadata-ruis (relatieve rangorde blijft geldig). Rename-render-artefacten (`Carousel}`, `DrillV2`, spelling `TranverseTransport`) zijn genegeerd.

## Resultaat per in-scope object

### Gedeeld (beide machines)
| Object | churn | newlines | totaal |
|---|---:|---:|---:|
| **MeasureUnit** | 80.547 | 18.045 | **98.592** |
| **Drill_V2** | 52.960 | 61.010 | **113.970** |
| **Drill** | 64.020 | 3.076 | **67.096** |
| **Saw** | 27.611 | 17.326 | **44.937** |
| Transport | 24.638 | 2.679 | 27.317 |
| Conveyor | 21.292 | 3.049 | 24.341 |
| TransportGroup | 12.871 | 614 | 13.485 |
| DrillChanger | 6.786 | 2.796 | 9.582 |
| InterpolationManager | 4.513 | 4.613 | 9.126 |
| ImprintUnit | 7.296 | 934 | 8.230 |
| InkJetMarker | 6.113 | 156 | 6.269 |
| CncInterpolationManager (nieuw) | 422 | 2.573 | 2.995 |
| *NcAxis (infra)* | 40.370 | 4.799 | 45.169 |
| *Axis (infra)* | 27.782 | 2.150 | 29.932 |

### V630 / V630 Mk2 (Measure Rollers) — extra
| Object | churn | newlines | totaal |
|---|---:|---:|---:|
| **MeasureRollUnit** | 25.127 | 5.372 | **30.499** |
| SawFixedRotatableTable (nieuw; alleen bij die zaagvariant) | 0 | 1.337 | 1.337 |

### V631 (Single Gripper + ShortPieceRemover) — extra
| Object | churn | newlines | totaal | Aard |
|---|---:|---:|---:|---|
| **ShortPieceRemover** | 7.584 | 4.418 | **12.002** | churn + nieuw |
| **SawIntegratedShortPieceRemover** | 209 | 7.561 | **7.770** | ≈volledig nieuw |
| Carriage | 5.300 | 1.747 | 7.047 | churn |
| Manipulator | 169 | 4.664 | 4.833 | ≈volledig nieuw |
| Chuck | 3.454 | 673 | 4.127 | churn |
| ClampCylinder | 3.356 | 69 | 3.425 | churn |
| MaterialClampingSystem | 295 | 3.204 | 3.499 | ≈nieuwe abstractie |
| ChainLifter | 44 | 1.886 | 1.930 | ≈volledig nieuw |
| MaterialPusher | 0 | 1.394 | 1.394 | volledig nieuw |

## Interpretatie & rangorde
1. **De grootste kostenpost is gedeeld, niet machine-specifiek.** `MeasureUnit`, `Drill_V2`, `Drill` en `Saw` domineren met tienduizenden regels churn *en* nieuw. Dit is de basis-effort voor **élke** 4.11→4.32-upgrade, ongeacht machine, en het staat **niet** in de bekende upgrade-stappen → ongedocumenteerd → expliciet testen.
2. **V630-delta bovenop het gedeelde:** vooral `MeasureRollUnit` (30k, overwegend churn = bestaand gedrag flink herzien). Relatief overzichtelijk: geen net-nieuwe subsystemen (behalve evt. de rotatable-table zaagvariant).
3. **V631-delta bovenop het gedeelde:** een cluster van **deels tot volledig nieuwe subsystemen** — `SawIntegratedShortPieceRemover`, `Manipulator`, `MaterialPusher`, `ChainLifter` (≈100% nieuw) en de nieuwe `MaterialClampingSystem`-abstractie, naast churn op `ShortPieceRemover`/`Carriage`/`Chuck`/`ClampCylinder`.

➡️ **Bevestigd:** de V631 draagt substantieel meer *nieuw/onbekend* oppervlak dan de V630. Voor de V630 zit het risico vooral in *gewijzigd bestaand* gedrag (churn), voor de V631 in *nieuw* gedrag (inregelen/testen van subsystemen die op 4.11 niet bestonden).

## Nuance voor de effort-inschatting
- **Churn** (bestaand gedrag herzien) → validatie: werkt de machine nog hetzelfde? Risico dat gedrag subtiel wijzigt.
- **Newlines / nieuwe subsystemen** → inbedrijfstelling: nieuwe functionaliteit configureren, referenties/assen inregelen, testen. Doorgaans meer uren per eenheid dan churn-validatie.
- De gedeelde drivers (measure/drill/saw) zijn zó groot dat een **representatieve test op één machine per type** waarschijnlijk efficiënter is dan per klantmachine alles opnieuw beoordelen.

## Volgende (later, per afspraak): deep-dive
Aanbevolen volgorde op basis van deze cijfers:
1. Gedeeld: `MeasureUnit` → `Drill_V2` → `Drill` → `Saw` (grootste impact, beide machines).
2. V630: `MeasureRollUnit`.
3. V631: `ShortPieceRemover` + de nieuwe subsystemen (`SawIntegratedShortPieceRemover`, `Manipulator`, `MaterialPusher`, `ChainLifter`, `MaterialClampingSystem`).
Per object: inspecteer de churn-diffs op gedragswijzigingen (motion/timing/sequencing/interfaces) en de nieuwe POU's op toegevoegde functionaliteit; scoor risico × effort met de rubriek uit het playbook.

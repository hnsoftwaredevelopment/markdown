# 06 — Deep-dive: Drill_V2 (gedeeld)
Baselines: OUD=`4.11.33.14`, NIEUW=`develop`. Raakt **beide** machines (drilzone / drilunits). Bestond al op 4.11.
Magnitude (uit `04`): churn **52.960** / nieuw **61.010** — grootste *nieuw* oppervlak van alle objecten. 340 commits.

## Aard van de wijziging
**1. Zelfde architectureel refactor als MeasureUnit** (gedeelde MCPL-golf): `I_MachineStatus`/`I_MaterialContext`-injectie via `FB_init`, `MA_`→interface, messaging-rename, layer-/ObjectType-violation-fixes (MCPL-2936/2998/3076), platform-library-updates, verplaatste/hernoemde CMD-functies.
> ⚠️ **Belangrijk voor de effort-optelsom:** deze refactorgolf is grotendeels *dezelfde* wijziging die ook MeasureUnit (en tientallen andere modules) raakt. Valideer die **één keer** (leverancier-CI / één representatieve machine), niet opnieuw per object.

**2. Drill-specifieke nieuwe functionaliteit (91 nieuwe POU's)**
- **Operatie-commando-datalaag** `DR2_GetData_Command*` per bewerking: `Drill`, `Tap`, `Sink`, `Mill`, `ProfileMeasure`, `LayoutMark`, `LineMarkX`, `LineMarkY`, `MultiLineMarkX`, `MarkSlave`, `InterpolationYZ`, `Center`. → herstructurering van hoe boor-/mark-/freesbewerkingen worden aangestuurd.
- **As-limieten**: `DR2_CalculateTargetYLimits`, `DR2_GetCalculatedMax/MinimumYAxis`, `DR2_GetAbsMinMaxZAxis`, `DR2_CalculatePositionZEnd` → gewijzigde bewegingsenvelope-berekening.
- **Collision**: `DR2_GetCollisionObjectIdCollection`, `DR2_GetChangerCollisionObjectIdCollection`.
- **Tool-change**: `DR2_ChangerPrepareToolPosition(s)`, `DR2_ConstructTool`.
- **Marking/slave** (koppelt aan LayoutMarkingUnit — beide machines optioneel).
- **Web support**: `DR2_GetDrillWebSupportID` → koppelt aan gedocumenteerde 4.31 web-support-wijziging (V631).
- Interface-detail: SWMS-11107 hernoemt input `InUserID`→`inCallerID` (i.l.m. `I_AxisMoving`); SWMS-11229 `cCmdWait`/timer.

## Risicoanalyse (wat kan anders werken?)
- **Drilunit = hart van beide machines** (boren, tappen, verzinken, frezen, markeren, profielmeten). Hoge gedragsimpact per definitie.
- **Operatie-dispatch geherstructureerd**: als behoud-van-gedrag lukt → laag; maar de omvang vraagt functioneel testen van **elke bewerking die de machine uitvoert**.
- **As-limieten opnieuw berekend** → bewegingsenvelope. Kan reachability/collision subtiel wijzigen; let op machines die dicht bij hun grenzen werken.
- **Interface/contract**: `FB_init`-injectie, `MA_`→interface, `inCallerID`-rename → interne contractwijzigingen.
- **Kruisverwijzing `02`**: web-support (4.31) en interpolatie/IM (4.12) zijn deels gedocumenteerd; de brede operatie-refactor + as-limieten **niet**.

## Score (rubriek)
| As | Score | Onderbouwing |
|---|:--:|---|
| Gedragsimpact | 3 | Boor-/frees-/markeer-motion-kern; operatie-dispatch + as-limieten herzien |
| Machinerelevantie | 3 | Drilunit = kernfunctie beide machines |
| Interface-breuk | 3 | `FB_init`, `MA_`→interface, `inCallerID`, command-datalaag, layer-fixes |
| Config-migratie | 2 | Collision-objecten/tool-posities/as-limieten wrsch. nieuwe config; geen bevestigde verplichte ConfigCheck gezien |
| **Totaal** | **11 → H (hoog)** | |

## Effort (tijd)
Grootste van de gedeelde objecten qua validatie-oppervlak.
- Functioneel hertesten van **alle bewerkingstypen** die de machine doet: boren, tappen, verzinken, (indien aanwezig) frezen, layout/lijn-markeren, profielmeten.
- As-limieten / bewegingsenvelope en collision verifiëren; tool-change-prep.
- **Inschatting:** grootteorde **≈ 1–2 dagen** drilunit-validatie per drilconfiguratie (meer bij frees-/uitgebreide markeeropties). Vraagt méér per-machine-aandacht dan MeasureUnit, omdat de markeer-/bewerkingsopties per machine verschillen. Kalibreer met jullie commissioning-ervaring.
- **Aftrek:** de gedeelde refactorgolf niet dubbeltellen met `05`.

## Gedocumenteerd?
**Deels.** Web-support (4.31) en IM (4.12) staan in `02`; de operatie-command-refactor en as-limieten **niet** → die expliciet testen.

## Te verifiëren (onsite / vervolg)
1. Werken alle bewerkingstypen (boor/tap/sink/mark/profielmeet, evt. frees) na upgrade functioneel identiek?
2. Zijn de as-limieten (Y/Z) na de nieuwe berekening gelijk aan 4.11 voor deze machine-geometrie?
3. Nieuwe collision-object-config vereist? Tool-change-posities nog correct?
4. `DR2_GetDrillWebSupportID` i.c.m. de 4.31 web-support-stap (V631) — samen valideren.

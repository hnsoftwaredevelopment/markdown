# 05 — Deep-dive: MeasureUnit (gedeeld)
Baselines: OUD=`4.11.33.14`, NIEUW=`develop`. Raakt **beide** machines (meeteenheid-abstractie; concreet = `MeasureRollUnit` bij V630, `SingleGripperFeederTruck` bij V631).
Magnitude (uit `04`): churn **80.547** / nieuw **18.045** — grootste enkele object. 480 commits in het bereik.

## Aard van de wijziging
Twee sporen, samen goed voor de enorme churn:

**1. Architectureel refactor (behoud-van-gedrag als bedoeling)**
- Modules losgekoppeld van globale variabelenlijsten (GVL's); toestand via interfaces geïnjecteerd (`I_MachineStatus`, `I_MaterialContext`) met `FB_init` (dependency injection).
- `MA_*`-machineglobale accessors vervangen door interface-properties (o.a. `MA_GetCentralSafety`, `MA_AutomaticListActive/Available`).
- Motion losgekoppeld via access-adapters (`FB_MotionMeasureUnitAccessAdapter`; zie ook HEAD-commit "Decouple FB_NcAxis … via Motion access adapters").
- Alle messaging-functies hernoemd; CMD-functies verplaatst naar hun modules; null-object-pattern (`FB_NullMeasureUnit`).
- Tickets: MCPL-2998, -3009, -3010, -3076, e.a.

**2. Nieuwe functionaliteit (73 nieuwe POU's)**
- **CNC-as-variant**: `FB_CncHandler_MeasureUnit` + `FB_MU_{GoToParkingPosition,GoToRest,Jog,ReferenceRun,Rest}_CncAxis`. Nieuw motion-pad naast de bestaande NcAxis-aansturing.
- **`FB_MU_ConfigCheck`** — valideert configuratie bij opstart.
- **Telemetrie** (`FB_MeasureUnitTelemetry`), **collision-model** (`FB_MeasureUnitCollisionModel`), **klemdruk-regeling** (`FB_MU_ControlClampPressure`), **belt-tensioner-monitoring** (`FB_MonitorBeltTensioner`), **chain-lifter-deelname** (`MU_GetChainLifter*`), blow-off-chips, extra clamp-positie-getters/preconditie-checks.
- SWMS-11185 (extra diagnose meetwiel-correctie), SWMS-10893 (bepaal werkelijke klempositie SHC bij opstart).

## Risicoanalyse (wat kan anders werken?)
- **Kerngedrag meten/klemmen breed geraakt.** Ook al is het refactor "behoud-van-gedrag", de omvang (34+ module-GVL's, alle messaging) betekent reëel regressierisico dat niet met lezen te borgen is — alleen met functioneel testen.
- **Interface/contract-breuk (intern):** `FB_init`-injectie en `MA_`→interface zijn contractwijzigingen. Voor een klant met standaard leverancierscode is dit intern; het risico zit in de aggregaat-correctheid, niet in klant-eigen code.
- **Config-migratie — concreet upgrade-risico:** `FB_MU_ConfigCheck` kan op een geüpgradede 4.11-machine configuratiefouten melden die er op 4.11 niet waren (past bij het procedure-uitgangspunt "waarschuw bij configuratiefout"). Kan opstart blokkeren tot config compleet is.
- **NcAxis vs CncAxis:** nieuw CNC-as-pad. ❓ Te verifiëren: draaien de meeteenheden van deze V630/V631 op NcAxis of CncAxis, en is het juiste pad geconfigureerd?

## Score (rubriek uit playbook)
| As | Score | Onderbouwing |
|---|:--:|---|
| Gedragsimpact | 3 | Meten/klemmen = motion-kern; breed herzien + nieuwe motion-varianten |
| Machinerelevantie | 3 | Meeteenheid is kernfunctie van beide machines |
| Interface-breuk | 3 | `FB_init`-injectie, `MA_`→interface, messaging-rename (veel interne contracten) |
| Config-migratie | 3 | Nieuwe `ConfigCheck` + mogelijk nieuwe/CNC-config vereist |
| **Totaal** | **12 → H (hoog)** | |

**Nuance:** een groot deel is *structureel* refactor (lager echt gedragsrisico míts de leverancier-CI/tests solide zijn); het *verhoogde* risico zit in de nieuwe subsystemen (CNC-as, klemdruk, collision) en de `ConfigCheck`.

## Effort (tijd)
Niet config-only. Verwacht **"merge + hertest" oplopend naar deelrecommissioning** van de meeteenheid:
- Config-check-fouten na upgrade oplossen (config aanvullen) — commissioning onsite.
- NcAxis/CncAxis-modus verifiëren en juiste pad configureren.
- Functioneel hertesten: referencerun, meten, klemmen/klemdruk, rustposities, (indien aanwezig) chain-lifter-samenspel.
- **Inschatting:** grootteorde **≈ 0,5–1 dag** meeteenheid-validatie per machinetype (exacte uren afstemmen met jullie commissioning-ervaring). Omdat dit gedeeld is: **één representatieve test per meeteenheid-type** (MeasureRollUnit voor V630, gripper-feedertruck voor V631) i.p.v. per klantmachine.

## Gedocumenteerd?
**Nee** — geen MeasureUnit-stap in `02` binnen ons bereik → ongedocumenteerde wijziging → expliciet testen; niet leunen op de upgradeprocedure.

## Te verifiëren (onsite / vervolg)
1. Meldt `FB_MU_ConfigCheck` fouten op een geüpgradede machine? Zo ja, welke config ontbreekt?
2. NcAxis of CncAxis voor deze meeteenheden?
3. Zijn klemdruk-regeling / collision-model / telemetrie standaard actief of optioneel, en vergen ze nieuwe I/O-referenties?

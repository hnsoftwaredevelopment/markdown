# CNCI-23 Auto config G-code interface

Epic: [CNCI-23](https://voortman.atlassian.net/browse/CNCI-23) · status New · design: [Design Auto config G-code interface (CNCI-23)](https://voortman.atlassian.net/wiki/spaces/RD/pages/2236612633/Design+Auto+config+G-code+interface+CNCI-23)

Testplan voor wat met VASIM te testen is. Gemaakt op 2026-11-18 op basis van de designpagina en de tickets. Alle stories staan nog op Ready for refinement; alleen de POC's bestaan (M-codes: [PR #23077](https://github.com/voortman-steel-machinery/vacam-twincat/pull/23077), V.E.-variabelen: draft [PR #23133](https://github.com/voortman-steel-machinery/vacam-twincat/pull/23133)).

## Wat de epic verandert

Tot nu toe staan de M-codes (`m_synch`) en de V.E.-variabelen in het TwinCAT-project. Een nieuwe M-code of variabele betekent een projectwijziging en een activatie per machine. Met deze epic configureert de PLC ze zelf bij elke CNC-start:

- **M-codes (BT1-2482):** de PLC heeft één M-codetabel (47 regels) en een lijst M-nummers per machinetype (V912 en LARS, gelijk). Na `bHLIInit` + 5 s schrijft de PLC `C:\TwinCAT\Mc\Cnc\MFunctions<machine>_Ch1.lis` en laadt die over ADS in het CNC-kanaal. Daarna leest de PLC van elke M-code `V.G.M_FCT[nr].SYNCH` terug. Een afwijking is een configuratiefout.
- **V.E.-variabelen (BT1-2476):** de PLC maakt het kanaaldeel van de V.E.-lijst uit de eigen `ST_Ve…`-structs (18 structs, 4 kanaalvariabelen), schrijft `VeChannelVariables_Generated.lis` en `.vedat`, laadt de lijst in de CNC, haalt de kanaalpointer op en controleert de grootte. Het globale deel (V912: 58 × REAL64 en `LaserPulseControlData`) blijft in het TwinCAT-project en moet blijven werken.
- **Startpoort (BT1-2479):** de referentierun en automatische programma's wachten tot beide lijsten *configured* zijn. Gaat er een mis, dan wordt de referentierun geweigerd.
- **Feature flag (BT1-2481):** machine-eigenschap "Use CNC improvements" (`bCncImprovementsEnabled`), standaard uit. Uit betekent: de machine werkt zoals nu.
- **Contractversie (BT1-2484):** de PLC geeft `LaserProcessContractVersion` (start 1.0.0) aan VACAM; de G-codegenerator weigert een machine met een hogere major dan hij kent.
- **Integratietest (BT1-2486)** en **documentatie (BT1-2487)**. BT1-2489 is een onderzoek zonder productiecode.

Machines: V912, en LARS als die met VACAM draait. V353 valt erbuiten.

## Opzet

- VACAM develop via de VACAM Launcher RC, TwinCAT in kernel mode, VASIM rc.
- Machine: V912. Kandidaat-backup: `20250113_V912_260715_073921` (de backup uit appendix D van de designpagina) of de V912-backups in `C:\Temp\Customers\2025` (20250112, 20250113).
- Controle zonder HMI waar mogelijk, met eigen ADS-scripts vanaf de testlaptop:
  - de bestanden in `C:\TwinCAT\Mc\Cnc` (inhoud, regeleinden, `#` en `Ende` aan het eind);
  - `V.G.M_FCT[nr].SYNCH` per M-code lezen op naam (index group `16#122301`, offset `16#48`);
  - de status van de PLC-blokken (configured, error) en de machinetoestand (`MachineState_ReferenceRun`);
  - `LaserProcessContractVersion` in `MachineObjectsArray.Machine`;
  - `bCncImprovementsEnabled` in de PLC en in de MC-database.
- Per test eerst een nulmeting met de flag uit, dan met de flag aan.

## Bekende beperkingen van de V912 in simulatie

Deze kunnen de test blokkeren. Ze staan ook bij de vragen.

- BT1-2325: de user mode runtime laadt geen CNC-drivers (TcCnc). Via de Launcher (kernel mode) mislukte de referentierun op 2026-11-09, omdat de Launcher Z rond 2886 mm start terwijl de CNC-limiet van de backup 2691,2 mm is (BT1-2303). Sinds kort draait TwinCAT op mijn laptop in kernel mode; dat is voor de V912 nog niet opnieuw geprobeerd.
- In simulatie stopt een productielijst bij `ScanProfile.nc` met -5663 ("Error at GCodeHandler object"). De V912 kan in deze ontwikkelfase nog niet snijden.
- De laser-spiescheck moet eerst gevalideerd worden (Machine › V912 - System error control › Laser safety handler › Manual control › "Validate laser spies").

## Testgevallen

### Feature flag (BT1-2481)

| #   | Geval                                                                                             | Verwacht                                                                                                       |
| --- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| F1  | V912 zonder ingestelde eigenschap starten (AC1)                                                   | geen `.lis`-bestanden geschreven, `bCncImprovementsEnabled` FALSE in de PLC, referentierun en lijsten zoals nu |
| F2  | Eigenschap op Yes, VACAM en CNC herstarten (AC2)                                                  | beide lijsten geladen en gecontroleerd voordat de referentierun verdergaat                                     |
| F3  | Machine-eigenschappen openen bij V912, en bij een machine buiten scope (bijv. V353 of V631) (AC3) | "Use CNC improvements" met helptekst alleen bij V912 (en LARS); de helptekst noemt dat een herstart nodig is   |
| F4  | Eigenschap wijzigen zonder herstart                                                               | geen effect tot VACAM en CNC herstart zijn                                                                     |

### M-codes (BT1-2482)

| # | Geval | Verwacht |
|---|---|---|
| M1 | V912 starten met de flag aan (AC1, AC6) | `MFunctionsV912_Ch1.lis` in `C:\TwinCAT\Mc\Cnc`, met één `m_synch`-regel per M-code van de V912-lijst (41 nummers), `#` en `Ende`, CRLF; geladen binnen `bHLIInit` + 5 s plus herhalingen, vóór het einde van de referentierun; log "definitions loaded and verified" |
| M2 | Map `C:\TwinCAT\Mc\Cnc` vooraf verwijderen | de PLC maakt `C:\TwinCAT\Mc` en `C:\TwinCAT\Mc\Cnc` zelf aan |
| M3 | Terugleeswaarden: `V.G.M_FCT[nr].SYNCH` van alle 41 M-codes over ADS lezen | elke waarde gelijk aan de tabel: MVS_SVS = 2, MOS = 1, MOS_TS = 262144 (16#40000) |
| M4 | M-code die het project niet kent, bijv. M406 (MOS_TS) (AC2) | leest terug als MOS_TS; komt in een VACAM-programma met dat type bij de PLC aan |
| M5 | M-code die het project met een ander type definieert (AC3) | leest terug met het type uit de lijst |
| M6 | Andere kanaalparameters na het laden (AC4) | ongewijzigd; een programma loopt zoals met de flag uit |
| M7 | CNC-herstart (AC7) | bestand opnieuw geschreven en geladen vóór de referentierun verdergaat |
| M8 | Flag uit (AC8) | geen bestand geschreven of geladen; M-codes uit het project zoals nu |
| M9 | Map niet schrijfbaar maken (rechten weigeren op `C:\TwinCAT\Mc\Cnc`) (AC5) | na 5 herhalingen met 2 s ertussen `cConfigurationError` met een dialoog die de stap noemt; referentierun geweigerd (samen met S3) |
| M10 | M-code in een programma die niet in de machinelijst staat (regel 14) | systeemfout, programma stopt |

AC9 (tabelcontroles, M999, dubbele nummers) en de afwijkende terugleeswaarde vallen onder TcUnit. Op VASIM alleen als er een testbuild komt (zie vragen).

### V.E.-variabelen (BT1-2476)

| # | Geval | Verwacht |
|---|---|---|
| V1 | V912 starten met de flag aan (AC1) | `VeChannelVariables_Generated.lis` en `.vedat` geschreven; 18 structs (kinderen vóór ouders), 4 `CHANNEL`-variabelen (`LaserSource`, `LaserHead`, `GasControl`, `V412Specific`), namen exact als op Confluence (`Treshold`, `Dutycycle`, `MaxStraylightProces`), `array_size 0`, geen globale variabelen, eindigt met `Ende`; geen fout in de log |
| V2 | Lijst vergelijken met de Confluence-pagina [V.E. Variable structure definition](https://voortman.atlassian.net/wiki/spaces/RD/pages/1414299724/V.E.+Variable+structure+definition) | types, leden en volgorde gelijk aan appendix A.5 van de designpagina |
| V3 | TC1 uit het ticket: een globale variabele (bijv. `V.E.PierceTime`) lezen vóór en na het laden, dan een globale en een kanaalvariabele (bijv. `V.E.LaserSource.Set.Power`) lezen en schrijven | beide werken; de globale variabele houdt zijn waarde; een waarde die de PLC via de kanaalpointer schrijft, is in de CNC te zien |
| V4 | Laat pointer (TC2, AC5): PLC start vóór VACAM de CncCommunication heeft ingeschakeld | de PLC blijft om de 2 s vragen tot de pointer geldig is; geen fout tijdens het wachten |
| V5 | Globale variabelen na het laden (AC8, risico "verkeerde pointer") | `Jerk` en `PierceTime` en de andere globale variabelen veranderen niet door het laden of door schrijven via de kanaalpointer |
| V6 | Flag uit (AC6) | geen lijst geschreven of geladen, geen pointer beschikbaar; V.E.-lijst uit het project |
| V7 | Bestaand productieprogramma (AC8) | de globale V.E.-variabelen werken zoals nu; in simulatie alleen tot `ScanProfile.nc` |

AC2 (array, STRING, onbekend type), AC3 (CNC weigert de lijst), AC4 (grootteverschil) en AC7 (referentiecontrole in CI) zijn TcUnit en pipeline. Op VASIM alleen met een testbuild.

### Startpoort (BT1-2479)

| # | Geval | Verwacht |
|---|---|---|
| S1 | Referentierun direct na het opstarten starten, flag aan (AC1) | machine wacht in `MachineState_ReferenceRun` tot beide lijsten *configured* zijn en de V.E.-pointer geldig is, en loopt dan door; een M-code tijdens de referentierun heeft het type uit de lijst |
| S2 | Flag uit (AC3) | referentierun start zoals nu |
| S3 | M-codelijst kan niet geladen worden (via M9) (AC2) | referentierun geweigerd; de dialoog van `cConfigurationError` noemt de oorzaak |
| S4 | Handbediening en MDI (probing, async bewegingen) vóór *configured* | starten niet |
| S5 | Programma starten vóór *configured* (`ContinueCurrentPage`) | wacht |

### Contractversie (BT1-2484)

| # | Geval | Verwacht |
|---|---|---|
| C1 | `LaserProcessContractVersion` over ADS lezen, flag aan | 1.0.0 |
| C2 | G-code genereren met de flag uit (AC5) | geen versiecontrole, uitvoer gelijk aan nu (vergelijken met dezelfde batch op develop zonder de wijziging) |
| C3 | Machine met een hogere major dan de generator kent (AC2) | genereren geweigerd met een melding die beide versies noemt; alleen op VASIM met een testbuild |

AC1, AC3 en AC4 zijn C#-unittests en de CI-referentiecontrole.

### Integratietest (BT1-2486)

Dit ticket is zelf de test. Uitvoeren met de testbuild waarin een test-V.E.-variabele alleen in een PLC-struct en een test-M-code alleen in de tabel en de machinelijst staat; het TwinCAT-project blijft ongewijzigd.

| # | Geval | Verwacht |
|---|---|---|
| I1 | Update installeren zonder TwinCAT-activatie, programma met de test-variabele en test-M-code draaien (AC1) | variabele gelezen en geschreven, M-code uitgevoerd met het type uit de lijst |
| I2 | Test-M-code in de machinelijst maar niet in de tabel (AC2) | dialoog noemt het nummer, geen lijst geladen, referentierun geweigerd |
| I3 | CNC-herstart, referentierun starten (AC3) | wacht tot beide lijsten *configured* zijn, loopt dan |
| I4 | Flag uit (AC4) | geen lijsten, referentierun zoals nu |
| I5 | Per kernelversie: groottecontrole en een paar variabelen op naam lezen | V.E.-indeling gelijk aan de PLC; globale variabelen werken nog |

De stappen leg ik vast zodat ze per kernelversie herhaald kunnen worden.

### Regressie

| # | Geval | Verwacht |
|---|---|---|
| R1 | V912 op develop met de flag uit: referentierun, handfuncties, een lijst tot `ScanProfile.nc` | gelijk aan develop zonder de wijziging |
| R2 | Andere CNC-machine zonder machinelijst (V353) op dezelfde build | niets geschreven of geladen in `C:\TwinCAT\Mc\Cnc`, geen startpoort, werkt zoals nu |

### Documentatie (BT1-2487)

Review door iemand die niet aan de epic werkte: kan een servicemonteur met `docs/design/cnc.md` vinden waarom een referentierun wacht of geweigerd wordt (logregels, terugleeswaarden) en hoe de flag uit moet (AC2)?

## Vragen

1. **V912 in simulatie.** De referentierun mislukte op 2026-11-09 door de Z-startpositie (BT1-2303, BT1-2325). Is er inmiddels een V912-backup of Launcher-instelling waarmee de referentierun in VASIM werkt? Zonder referentierun zijn S1 tot en met S5, M7 en I3 niet te testen.
2. **LARS.** Is er een LARS-backup voor VACAM-modus en draait LARS in VASIM? Zo niet, is testen op alleen de V912 genoeg, omdat LARS dezelfde M-codelijst gebruikt?
3. **Testbuilds.** Voor M10, C3, I1 en I2 en de foutgevallen (onbekende M-code, afwijkende terugleeswaarde, CNC weigert de V.E.-lijst, grootteverschil) is een build nodig die afwijkt van develop. Komen er setups van een testbranch, en hoe installeer ik die via de Launcher?
4. **Logregels.** Waar lees ik de `ADSLOGSTR`-regels van de opstartstap in simulatie (TwinCAT-logger, XAE-output of Windows-eventlog)? Komen ze ook in de VACAM-log?
5. **V.E. lezen zonder HMI.** Kan ik V.E.-variabelen (globaal en kanaal) over ADS op naam lezen en schrijven, zoals `V.G.M_FCT[nr].SYNCH`? Of moet het via de CNC-HMI of `#MSG` in een MDI-regel? Is de CNC-HMI in simulatie beschikbaar?
6. **Symboolnamen.** Welke PLC-symbolen geven de status van de M-codestap en de V.E.-stap (configured, error, aantal herhalingen) en van de startpoort? Dan kan ik die over ADS volgen.
7. **M-codes uitvoeren.** De V912 kan in simulatie geen productielijst afmaken (stopt bij `ScanProfile.nc`). Is er een testprogramma (`.nc` of MDI) dat M406 (MOS_TS) en een paar andere M-codes uitvoert, zodat M4 en I1 te controleren zijn?
8. **CNC-herstart in simulatie.** Wat bedoelen M7 en I3 met CNC-herstart: TwinCAT herstarten, alleen de PLC resetten, of VACAM en TwinCAT samen? TwinCAT mag niet naar Config terwijl VASIM draait, dus in simulatie wordt het een herstart van de hele omgeving.
9. **Map niet schrijfbaar.** Mag ik voor M9 de rechten op `C:\TwinCAT\Mc\Cnc` op mijn laptop aanpassen (daarvoor zijn misschien adminrechten nodig), of is er een betere manier om de foutstap op te wekken?
10. **POC's nu al testen.** PR #23077 is volgens de designpagina de definitieve M-codeoplossing. Heeft het zin om die branch nu al in VASIM te testen (M1 tot en met M6), voordat BT1-2482 klaar is?
11. **Feature flag in de database.** Bij `bUseMotionLibraryVeloGenerator` (BT1-2317) stond de rij pas in de MC-database na een wijziging, en gaf alleen VACAM herstarten "PLC is into Error state". Geldt dat ook voor `bCncImprovementsEnabled`, en is een herstart van PLC, VASIM en VACAM samen de bedoelde werkwijze?
12. **BT1-2489.** Het onderzoek kan de aanpak veranderen (bijvoorbeeld het globale V.E.-deel of de huidige `m_synch` ook laden). Wacht ik met V3, V5 en M5 tot dat onderzoek klaar is?

## Resultaat

| # | Resultaat | Opmerking |
|---|---|---|
| F1–F4 | open | wacht op BT1-2481 |
| M1–M10 | open | wacht op BT1-2482 (of de POC, vraag 10) |
| V1–V7 | open | wacht op BT1-2476 |
| S1–S5 | open | wacht op BT1-2479 en vraag 1 |
| C1–C3 | open | wacht op BT1-2484 |
| I1–I5 | open | wacht op BT1-2486 en een testbuild (vraag 3) |
| R1–R2 | open | |

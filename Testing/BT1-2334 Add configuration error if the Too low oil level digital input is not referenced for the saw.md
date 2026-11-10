# BT1-2334 Add configuration error if the "Too low oil level" digital input is not referenced for the saw

Ticket: [BT1-2334](https://voortman.atlassian.net/browse/BT1-2334) · status In Test · ontwikkelaar André Holtschlag

## Doel

Na een update naar VACAM 4.11.36.0 of hoger geeft een zaag met zaagtype VBS1x50b (`Saw.Type` = 17) een configuratiefout als de referentie "Too low oil level" van de hydraulic generator niet gekoppeld is:

> Reference 'Too low oil level' of the hydraulic generator is not configured

VACAM moet ondanks de fout gewoon starten, zodat de service-engineer de referentie kan koppelen. Na het koppelen, opslaan en herstarten van VACAM en TwinCAT is de fout weg (mail van André aan service, bijlage bij het ticket).

## Opzet

- VACAM `4.11.36-alpha.14371` (nieuwste in `\\vasoftware\setups\VACAM\Vacam-4.11`), gestart met de vacam-simulation-plugin.
- Backup uit het ticket: `20250008_V100_260604_160529.zip` (William Hare, VB1250 20250008 met V631 20250009), VACAM 4.11.32.18 in de backup.
- Uitgangssituatie in `MC_20250008_VB1250_260604`: `Saw[0].Type` = 17, `HydraulicGeneratorSaw[0].TooLowOilLevel` leeg, digitale ingang `LowOilLevel` (DI 6) bestaat maar is niet gekoppeld.

## Testgevallen

| # | Geval | Verwacht |
|---|---|---|
| T1 | VBS1x50b, referentie leeg | configuratiefout, VACAM start wel |
| T2 | T1, daarna "Low oil level" koppelen, opslaan, VACAM en TwinCAT herstarten | fout weg |
| T3 | VBS1x50b, referentie op een verkeerde ingang | configuratiefout of altijd de Low Oil-melding; op de juiste ingang zetten lost het op |
| T4 | VBS1x50b met de koppeling al goed (andere VB1250-backup) | geen fout |
| T5 | ander zaagtype, referentie leeg | geen fout |

## Resultaat

| # | Resultaat | Opmerking |
|---|---|---|
| T1 | **OK:** met de VACAM Launcher RC en TwinCAT in Run geeft VACAM de configuratiefout. Referentie `TooLowOilLevel` van `HydraulicGeneratorSaw[0]` is 0 (leeg) | Eerdere pogingen met de plugin (08:00 zonder TwinCAT, 08:20 met TwinCAT) gaven geen fout. TwinCAT bleef toen in Config door de trial license, en zonder PLC is de knop Machines er niet. Launcher-databases: `MC_20250008_VB1250`, `VACAM_20250008` |
| T2 | **OK:** Too low oil level op DI 6 gezet (10:35). De melding bleef staan tot VACAM en TwinCAT herstart waren, daarna weg. Eindstand: Too low oil level DI 6, High oil temperature DI 5, Low oil level leeg | onderweg was High oil temperature per ongeluk losgekoppeld, daarna teruggezet op DI 5 |
| T3 | niet apart uitgevoerd | |
| T4 | **OK:** dezelfde test op 3 andere V100-configuraties, overal werkt het zoals beschreven | Herbert |
| T5 | niet apart uitgevoerd | |

## Conclusie

De configuratiefout "Reference 'Too low oil level' of the hydraulic generator is not configured" verschijnt bij een VBS1x50b-zaag zonder koppeling. VACAM start gewoon op, en na het koppelen en herstarten van VACAM en TwinCAT is de fout weg. Dit klopt met de instructie in de mail van André aan service. Let op: de fout verdwijnt pas na een herstart, niet direct na het opslaan.

## Bevinding: het nummer van de ingang verschilt per machine

Bij de AMADA V631 (`20250067_V631_260404`, met een VBS1x50b-zaag, `Saw.Type` = 17) was "Too low oil level" na het koppelen aan DI 6 nog steeds fout. Daarna bleef de melding "Oil level too low" staan. DI 6 is bij deze machine `Power24VBussystemOK` (onder `SystemError`). De juiste ingang is hier DI 113 `LowOilLevel`. Na het koppelen aan DI 113 en een herstart was de melding weg (bevestigd door Herbert, 2026-11-06).

| Machine | Ingang voor "Too low oil level" | High oil temperature |
|---|---|---|
| VB1250 William Hare (20250008) | DI 6 `LowOilLevel` | DI 5 |
| V631 AMADA (20250067) | DI 113 `LowOilLevel` | DI 112 |

Een V631 met zaag heeft twee hydraulic generators: die van de boorstraat (`HydraulicGenerator[0]`, eigen ingang DI 62 `TooLowOilLevel`, al goed gekoppeld) en die van de zaag (`HydraulicGeneratorSaw`). De configuratiefout gaat alleen over die van de zaag.

### Zo vind je de juiste ingang

1. Open in de machineconfiguratie de hydraulic generator van de **zaag**: `SawZone → Saw → SawFrame → HydraulicGeneratorSaw`. Neem niet die van de boorstraat.
2. Onder dit object hangen de digitale ingangen die bij de generator horen. Zoek de ingang met de naam **"Low oil level"** (of "Too low oil level"). Het nummer achter "Digital input" is het part number dat je nodig hebt.
3. Ter controle: "High oil temperature" van dezelfde generator staat meestal al op de ingang ernaast (bij AMADA 112 en 113, bij William Hare 5 en 6).
4. Kies bij de referentie "Too low oil level" als part type DigitalInput en als part number het nummer uit stap 2. Sla op en herstart VACAM en TwinCAT.

Niet doen: een nummer van een andere machine overnemen. Een verkeerde ingang geeft geen configuratiefout meer, maar wel de melding "Oil level too low" tijdens het gebruik.

Voor testers met toegang tot de database geeft deze query de ingangen onder de zaaggenerator:

```sql
SELECT o.Tag, o.ObjectNumber
FROM Object o JOIN Object p ON p.ID = o.Parent
WHERE p.Tag = 'HydraulicGeneratorSaw' AND o.ClassID = 2;
```

**Voorstel voor André:** neem stap 1 en 2 op in de mail aan service, zodat de engineer de ingang onder de zaaggenerator kiest en geen vast nummer.

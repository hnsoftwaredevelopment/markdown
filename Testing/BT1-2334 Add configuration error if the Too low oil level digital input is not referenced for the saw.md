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
| T1 | **Fout:** geen configuratiefout, niet zonder TwinCAT (08:00) en niet met TwinCAT en VASIM rc (08:20). Ook niets in het VACAM-log. Referentie `TooLowOilLevel` van `HydraulicGeneratorSaw[0]` is 0 (leeg) | gezien door Herbert |
| T2 | | |
| T3 | | |
| T4 | | |
| T5 | | |

# 00 — Repo-inventarisatie & haalbaarheid
**Repo (lokaal):** `C:\DevOps\vacam-twincat` (geldige git-checkout, branch `develop`)
**Upgrade:** 4.11.x → develop (4.32)

---

## 1. Baselines (gepind)

| Rol | Ref | Toelichting |
|---|---|---|
| **OUD** | `4.11.33.14` | Nieuwste 4.11-patch (hoogste `4.11.*`-tag via `--sort=-v:refname`). Draaiende klanten "op 4.11.x" zitten hier vermoedelijk op — pas aan als een specifieke klant op een lagere 4.11.x zit. |
| **NIEUW** | `develop` | In-ontwikkeling 4.32. Er bestaat nog **geen** `4.32.*`-tag; hoogste release-tag is `4.30.36`. |

Head van develop: `12522216e17` (merge PR #19990, MCPL-3017 — Decouple FB_NcAxis MachineControl couplings).

---

## 2. Structuur op topniveau

- **`twincat/`** — de PLC-/TwinCAT-kant. Broncode in `twincat/src/Main Objects/...` als `.TcPOU`-bestanden (function blocks, methods, properties). Verder `UnitTests/`, `test/`, `3d-models/`, `TranslationResources/`.
- **`vacam/`** — de .NET-applicatiekant. Kernlogica in `vacam/Library/Execution/...`. Verder `Domain/`, `ProductionLine/`, `Tests/`, `Voortman.Machine.Simulation/`.

## 3. Hoe machines & opties in de code zitten

- **Machines = expliciete klassen** in `vacam/Library/Execution/MachineDefinition/Machines/`, die **componenten** samenstellen uit `vacam/Library/Execution/MachineDefinition/MachineComponents/`. Dit maakt per-machine + per-component scopen mogelijk.
- **`VB1250` / `VB1x50` bestaan NIET als code-term** (0 hits) — dat zijn verkoop-/configaanduidingen.
- **B2B heet in code `BackToBack`.**
- Versie-/machinespecifieke PLC-code staat als suffix in bestandsnamen: `_V630`, `_V631`.

## 4. Doelmachines → entry-klassen + kandidaat-componenten

### A. V630 / V630 Mk2 — B2B met Measure Rollers V2
Entry-klasse(n):
- `.../Machines/V630Mk2MeasureRollersBackToBack.cs`
- `.../Machines/V630Mk2MeasureRollersBackToBackSawFixedRotatableTable.cs` (variant)

> ⚠️ **Let op:** er is **geen** losse `V630MeasureRollersBackToBack.cs` (niet-Mk2) in de Machines-map — alleen `V630Mk2...`. Te verifiëren in Fase 1: gebruikt de "gewone" V630 dezelfde definitie/basisklasse, of staat die elders?

Kandidaat-componenten (te bevestigen door de entry-klasse te lezen):
`MeasureRollers.cs`, `MeasureRollUnit.cs`, `MeasureUnitAdapter.cs`, `Saw.cs`, `SawClamping.cs`, `SawFixedRotatableTable.cs`, `Infeed.cs`, `AutomaticOutfeed.cs`/`ManualOutfeed.cs`, `DrillUnit*.cs`.

### B. V631 — B2B met Single Gripper en ShortPieceRemover
Entry-klasse:
- `.../Machines/V631SingleGripperFeederTruckBackToBack.cs`

Kandidaat-componenten:
`SingleGripperFeederTruck.cs`, `Gripper.cs`, `ShortPieceRemover.cs`, `Saw.cs`, `SawClamping.cs`, plus PLC: `twincat/src/Main Objects/SawIntegratedShortPieceRemover/...`.

---

## 5. Omvang van de kloof (headline)

| Scope | Bestanden | +regels | −regels |
|---|---|---|---|
| Totaal | 34.084 | ~7.041.000 | ~6.979.000 |
| `twincat/` | 12.185 | ~1.501.000 | ~1.168.000 |
| `vacam/` | 21.861 | ~5.536.000 | ~5.809.000 |
| **Commits ertussen** | **97.517** | | |

**Conclusie:** een brede diff is onbruikbaar én onbetaalbaar in tokens. Bovendien zijn de regelaantallen sterk vertekend door tests, 3D-modellen, vertalingen en gegenereerde bestanden → **regelaantal is hier een slechte risico-maat**. We scopen strak op broncode.

### Filterregels (échte broncode)
Bij elke diff/`--stat` uitsluiten:
```
":(exclude)*/3d-models/*" ":(exclude)*.obj"
":(exclude)*/Tests/*" ":(exclude)*/UnitTests/*" ":(exclude)*/UnitTest_*/*" ":(exclude)*/test/*"
":(exclude)*/TranslationResources/*" ":(exclude)*.phrase.yml"
```
Focus-paden voor gedrag:
- .NET: `vacam/Library/Execution/**` (m.n. `MachineComponents/` en `Machines/`)
- PLC: `twincat/src/Main Objects/**` (`.TcPOU`)

---

## 6. Haalbaarheidsconclusie

**Ja, uitvoerbaar** — mits strak gescoped per component. De aanpak:

1. **Fase 1 (volgende blok, goedkoop):** lees de twee entry-klassen om de exacte componentsamenstelling per doelmachine te bevestigen, en verifieer het V630-vs-V630Mk2-punt. Machine-klassen zijn kleine bestanden.
2. **Fase 2 (heatmap, goedkoop):** per component één `git diff --shortstat OUD NIEUW -- <component>` (met filters) → kwantitatieve magnitude per component.
3. **Fase 3 (verdieping, per component):** alleen componenten met noemenswaardige magnitude → `git log --oneline` (intentie) + gerichte `git diff` per bestand. Risico + effort via de rubriek uit het playbook.
4. **Fase 4 (roll-up):** per machine samenvoegen tot een risicoregister.

Elk deelgebied → een eigen `NN-<deelgebied>.md`.

---

## 7. Volgende blok (Fase 1) — exact wat te draaien

```powershell
cd C:\DevOps\vacam-twincat
# Samenstelling V630Mk2 B2B Measure Rollers
git show develop:vacam/Library/Execution/MachineDefinition/Machines/V630Mk2MeasureRollersBackToBack.cs
# Samenstelling V631 B2B Single Gripper + SPR
git show develop:vacam/Library/Execution/MachineDefinition/Machines/V631SingleGripperFeederTruckBackToBack.cs
```
Doel: uit deze twee klassen de definitieve lijst componenten halen die elke machine gebruikt → dát wordt de scope voor de heatmap.

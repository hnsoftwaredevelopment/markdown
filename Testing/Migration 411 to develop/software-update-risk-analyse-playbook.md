# Software Update Risicoanalyse — Playbook
**Repo:** `voortman-steel-machinery/vacam-twincat`
**Upgrade:** 4.11.x → `develop` (4.32)
**Machines in scope:**
- V630 en V630 Mk2 — VB1250 B2B met Measure rollers V2
- V631 — VB1x50 B2B met Single Gripper en ShortPieceRemover

---

## Uitgangspunten

- **Token-zuinig:** nooit hele bronbestanden lezen. Werk in deze volgorde van goedkoop → duur:
  1. `git log --oneline` (intentie van wijzigingen)
  2. `git diff --stat` (magnitude = ruwe risico-proxy)
  3. `git diff <bestand>` (alleen waar nodig, per bestand)
- **Eén module = één prompt = één `.md`.** Elke stap is klein en herstartbaar.
- **Baselines pinnen:** leg één keer de exacte "oud"- (4.11.x tag/commit) en "nieuw"-baseline (develop-head, 4.32) vast en verwijs daar in alle latere stappen naar.
- **Drempel voor diepe analyse:** is een module-diff `--stat` klein (bv. < ~100 regels)? Dan volstaat een korte samenvatting. Is een enkel bestand > ~400 regels diff? Samenvatten i.p.v. volledig citeren.

---

## Fase 0 — Oriëntatie & haalbaarheid
**Doel:** de "kaart" bouwen. Geen diepe analyse. → `00-repo-inventory.md`

> Je hebt toegang tot de repo `vacam-twincat` (branch `develop`). Doe **geen** diepgaande code-analyse; lever alleen een inventarisatie:
> 1. Welke git-tags/branches bestaan er rond versie **4.11.x** en **4.32**? Geef de exacte tag/commit die we als *oud* (4.11.x) en *nieuw* (develop/4.32) baseline gebruiken. Noteer beide als `OUD=` en `NIEUW=`.
> 2. Geef de mappenstructuur op topniveau (max. 2 niveaus diep).
> 3. Hoe worden machinetypes (V630, V630 Mk2, V631) en opties (**Measure Rollers V2**, **Single Gripper**, **ShortPieceRemover**, **VB1250 / VB1x50 B2B**) in de code weergegeven? Aparte libraries/mappen, compile-conditionals, of configbestanden/parameters?
> 4. Conclusie: is een per-module diff-analyse haalbaar, en **welke paden horen bij welke module**?
>
> Output naar `00-repo-inventory.md`.

---

## Fase 1 — Versie-delta heatmap
**Doel:** kwantitatief overzicht: waar is het meest veranderd. → `01-version-delta-overview.md`

> Gebruik de baselines `OUD`/`NIEUW` uit `00-repo-inventory.md`. Lees **geen** volledige bestanden.
> - Draai `git diff --stat OUD..NIEUW` en groepeer de uitkomst per topniveau-map/module.
> - Draai `git log --oneline OUD..NIEUW` en tel commits per module.
>
> Lever één tabel: per module → **#commits · #bestanden gewijzigd · +regels · −regels · magnitude (L/M/H)**. Magnitude is puur op basis van omvang, nog geen inhoudelijk oordeel.
>
> Output naar `01-version-delta-overview.md`.

---

## Fase 2 — Per-module verdieping (herhaal per module)
**Doel:** inhoudelijk risico + effort per functionele module.
Eén prompt per module, elk naar een eigen bestand:
- `02-measure-rollers-v2.md`
- `03-single-gripper.md`
- `04-shortpieceremover.md`
- `05-b2b-handling.md` (VB1250 / VB1x50)
- (eventueel extra gedeelde modules die uit Fase 1 als H/M naar voren komen)

> Analyseer **uitsluitend** module `<MODULE>` (paden uit `00-repo-inventory.md`: `<PADEN>`). Werk in deze volgorde en stop zodra je genoeg signaal hebt:
> 1. `git log --oneline OUD..NIEUW -- <PADEN>` → wat was de **intentie** van de wijzigingen?
> 2. `git diff --stat OUD..NIEUW -- <PADEN>` → magnitude.
> 3. Alleen indien nodig, per bestand: `git diff OUD..NIEUW -- <bestand>`. Diff > ~400 regels? Samenvatten.
>
> Classificeer elke relevante wijziging als:
> - **Gedrag/functioneel** (motion, timing, sequencing, I/O-gedrag, safety)
> - **Interface/contract** (gewijzigde FB-signaturen, globale variabelen, parameter-defaults) ← *de stille brekers*
> - **Structureel/refactor**
> - **Cosmetisch**
>
> Vul per wijziging de **risicotabel** in (rubriek onderaan dit playbook). Sluit af met: modulescore, geschatte validatie-/aanpassingstijd, en aandachtspunten voor inbedrijfstelling.
>
> Output naar `<bestandsnaam van de module>.md`.

---

## Fase 3 — Roll-up per machine
**Doel:** modulescores samenvoegen tot een risicoregister per machine.
→ `10-v630-risk-register.md`, `11-v631-risk-register.md`

> Combineer de per-module `.md`-bestanden tot een risicoregister voor `<MACHINE + CONFIG>`. Neem **alleen** modules mee die deze machine/config daadwerkelijk gebruikt (zie `00-repo-inventory.md`).
> Geef per machine: totaal risicoprofiel, geschatte inbedrijfstellingstijd, en een geprioriteerde actielijst (risico × effort).
>
> Output naar `10-v630-risk-register.md` (resp. `11-...`).

---

## Gedeelde risicorubriek

Scoor elke wijziging op vier assen (1 = laag, 3 = hoog):

| As | 1 | 2 | 3 |
|---|---|---|---|
| **Gedragsimpact** | cosmetisch/refactor | logica gewijzigd, zelfde interface | motion/timing/safety geraakt |
| **Machinerelevantie** | module niet gebruikt door deze machine | zijdelings | kernfunctie van deze config |
| **Interface-breuk** | geen | interne wijziging | FB-signatuur / globale var / param-default gewijzigd |
| **Config-migratie** | geen nieuwe params | nieuwe optionele params | nieuwe verplichte params die 4.11 niet zet |

**Risicoscore** = som van de vier assen (4–12) → **L (4–6) · M (7–9) · H (10–12)**.

**Effort (inbedrijfstelling):**
- **Config-only** — parameters overzetten (uren)
- **Merge + hertest** — code samenvoegen, functioneel hertesten (dagdeel–dag)
- **Volledige recommissioning** — motion/safety opnieuw afregelen en valideren (meerdere dagen)

**Prioriteit** = risico afgezet tegen effort:

| | Effort laag | Effort midden | Effort hoog |
|---|---|---|---|
| **Risico H** | Nu doen | Plannen + capaciteit | Plannen + capaciteit |
| **Risico M** | Nu doen | Inplannen | Bewust beslissen |
| **Risico L** | Meepakken | Meepakken | Accepteren/uitstellen |

---

## Bestandsoverzicht (verwachte output)

```
00-repo-inventory.md            # kaart + baselines OUD/NIEUW
01-version-delta-overview.md    # kwantitatieve heatmap
02-measure-rollers-v2.md        # per-module verdieping
03-single-gripper.md
04-shortpieceremover.md
05-b2b-handling.md
10-v630-risk-register.md        # roll-up per machine
11-v631-risk-register.md
```

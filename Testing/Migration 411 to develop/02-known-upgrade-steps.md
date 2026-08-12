# 02 — Bekende upgrade-stappen (uit VACAM upgrade procedure)
Bron: `VACAM_upgrade_procedure.md` (intern). Baselines: OUD=`4.11.33.14`, NIEUW=`develop` (4.32).

## Waarom dit meetelt
Dit document is de **"known knowns"-laag** van de analyse:
- Wat hierin staat = gedocumenteerde breaking change **mét** remediation → **lagere onzekerheid, beter in te schatten effort.**
- Wat de code-diff straks vindt maar wat hier **niet** in staat = ongedocumenteerde wijziging → **verhoogd risico.**
- Het document bevestigt bovendien het uitgangspunt: upgrades bevatten "known (major) refactoring causing breaking changes". Terminologie: *update* = binnen een branch (4.8.100→4.8.150), *upgrade* = tussen branches (4.8→4.11). Wij doen dus een reeks upgrades.

> ⚠️ Detailprocedures staan op gelinkte wiki-/JIRA-/PR-pagina's die ik van hieruit niet kan openen. Voor de items hieronder is dat vooral relevant voor het web support-punt (PR #18929).

## Relevante stappen in ons bereik (alleen ≥ 4.12; alles ≤ 4.11.27 is al toegepast)

### [General] — geldt voor beide machines
| Vanaf | Actie / breaking change | Type effort |
|---|---|---|
| 4.12 | TMC-bestand herladen | Config, standaard |
| 4.12 | IM load buffer verhogen naar 512 kByte (`IM_Extra`) — *van toepassing als de machine een interpolation manager gebruikt; drilmachines doen dat doorgaans* | Config, per machine te checken |
| 4.13.2 | TMC-bestand herladen | Config, standaard |
| 4.16 | VACAMOfficeStarter minimaal versie 1.1.3 | Randvoorwaarde tooling |
| 4.19 | **Overstap naar .NET 8 framework** — runtimes installeren (`\\vasoftware\Setups\DotNet Installers`); installer controleert dit. Plus nieuwe `CameraRtspPlayer`-installer *als de machine zo'n camera heeft* (na VACAM-installatie uitvoeren). | Randvoorwaarde runtime + evt. camera |
| 4.21 | .NET 8 **x86** runtime nodig voor de installer | Randvoorwaarde runtime |

### V631 — B2B · Single Gripper + ShortPieceRemover
| Vanaf | Actie / breaking change | Relevantie |
|---|---|---|
| 4.31 | **[rechts-naar-links machines met web support]** Valideer dat cylinder 1 de linker cilinder (uitvoerzijde) aanstuurt. Zie PR #18929. | **Direct relevant** — de V631-config heeft (optioneel) WebSupport. Van toepassing *als deze machine rechts-naar-links is en web support heeft.* Per klantmachine verifiëren. |

### V630 / V630 Mk2 — B2B · Measure Rollers V2
Geen machine-specifieke stappen ≥ 4.12 in dit document. Alleen de [General]-items hierboven.

## Historisch gevoelige gebieden (≤ baseline — al toegepast, maar diff-aandacht waard)
Deze stonden onder onze baseline en zijn dus al uitgevoerd, maar ze verraden wél waar aan V630/V631 in het verleden gesleuteld is. Bij de diff (Fase 3) hier extra opletten of er sindsdien opnieuw is bijgewerkt:
- **Infeed/outfeed roller offsets** — `fOffsetFirstRoller` / `fOffsetLastRoller` (4.8.125, [V630/V631]).
- **Rolling taps** default-parameters voor drilmachines (4.10, [V630/V631]).
- **Toolchanger** — referentie *Sensor System Pressure Present* (air pressure DI) (4.11, [V630]).
- **DrillV2** — *Spindle position during tool change* parameter (4.11.8).
- **BufferLinkPreferences** — waarden 5/26/27 verwijderd, nieuw 42 `ContainsPreferableOutfeedSection` (4.11.13).
- **[V631M]** niet-herstelde link `...SMM_Profile` (4.10) — sinds 4.8 ongebruikt; check of dit terugkomt.
- **[VB1x50b]** material detection input op type 'Reset' (4.8.403) — VB1x50 = V631-aanduiding.

## Gebruik in de risicoregisters (Fase 4)
Per risico-item straks een kolom **"gedocumenteerd?"**:
- **Ja** → verwijs naar de stap hierboven; effort = grotendeels bekend (vaak config/randvoorwaarde).
- **Nee** (alleen door diff gevonden) → hogere onzekerheid; kandidaat voor extra test-/inbedrijfstellingstijd.

---
**Nummering:** de heatmap schuift hiermee door naar `03-heatmap.md`.

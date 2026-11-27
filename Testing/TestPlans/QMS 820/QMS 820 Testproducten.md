---
type: testdata
jira: BT1-2432
title: "QMS 820 Testproducten"
created: 2026-11-25
tags: [qms820, testdata]
---

# QMS 820 Testproducten

Producten om de sortering, de take overs en de validatie gericht te raken. Maten in mm. Waar "band" staat: de band van de measure wheel aan de datum line-kant (zie [[QMS 820 Analyse]] §4).

> [!warning] Correctie 26-11: richting van x
> In de eerste versie stond "x gemeten vanaf de voorkant van het product (outfeed-kant)". Dat klopt **niet** voor de NC1-bestanden. De x-waarden in de tabellen hieronder zijn bedoeld als **machinepositie** (machine-x, vanaf de outfeed-kant). Hoe een DSTV-x daar terechtkomt, hangt af van de rotatie die VACAM kiest:
> - Regel: **machine-x = lengte − x in het opgeloste product** (na de rotatie die VACAM kiest; te zien als `SolvedRotation` en in het venster "Add batch", kolom Rotation).
> - HEA300 (P10, P10b): rotatie None. DSTV x 150 kwam op machine-x ≈ 5850 (infeed-kant).
> - L150x14 (P10L, P10Lz): VACAM staat alleen rotatie **Z** toe ("Permitted rotation: Front:Z"; de knop Z is grijs). Dat draait het stuk 180°: DSTV x 150 kwam op machine-x 150 (voorkant), DSTV x 5850 op machine-x 5850 (infeed-kant).
> - Controleer daarom na het maken van de batch altijd waar de bewerkingen in de productielijst staan.

> [!warning] Correctie 26-11: groep B werkt niet met een I-profiel
> Een I-profiel ligt met het lijf horizontaal; de measure wheel loopt op de achterste flens **op halve hoogte**, precies waar het lijf aan de flens vastzit (HEA300: band 145–155). Een gat of uitsparing in die band is op een I-profiel niet te maken. Getest op de V631 van Overhalla (26-11):
> - uitsparing 10 mm lang (y 0–145): "Milling not possible" (te smal voor een vingerfrees Ø16);
> - uitsparing 40 mm lang tot y 145: maakbaar, maar raakt de band alleen op de rand en blokkeert niet. Default, DwF en Min plannen alle drie zonder fallback of undoable;
> - uitsparing 40 mm lang tot y 160 (door de band): "Milling not possible" (frees kan niet door de aansluiting van het lijf).
>
> Daarom zijn P10 en P11 omgezet naar een **L-profiel**, zoals in de echte klantgevallen (SWMS-11375 L200x100x15, SWMS-10421 L-profiel). Bij een L ligt de band laag op het liggende been (0 tot 2 × dikte + 5); een gat laag in het staande been valt daarin en is gewoon te boren. P12 t/m P16 volgen dezelfde aanpak zodra ze aan de beurt zijn.
>
> **Uitkomst L150x14 (26-11, V631 Overhalla, met de PR):** NC1 in `C:\Temp\QMS820\NC1-BLz\` (gemaakt met `qms-nc1-blz.ps1`): Ø22 op y 42 in beide benen (rand op 31, band 0–33), aan de infeed-kant op machine-x 5500 en 5850, plus Ø22 op y 105 om de 1000. Default, DwF en Min plannen alle drie **zonder** fallback en zonder undoable. Default: take over naar MRU 2 bij 730, die houdt het materiaal tot het eind vast; de gaten in de band zijn de laatste bewerkingen. Min: eerst zagen (2800), één keer terug, take over naar MRU 2 bij 5316. Conclusie: een gat in de band aan de infeed-kant blokkeert alleen als daarna nog over dat stuk gemeten moet worden; bij één stuk zonder bewerkingen erachter is dat niet zo. Voor het blokkerende geval (take over onmogelijk) zijn de klantjobs SWMS-10421, -10635, -11058 en -11375 het bewijs: die worden zonder de PR geannuleerd en met DwF gered (zie testplan R-01).

De maten gaan uit van een machine met wielen op ±440/±210 en een clamping margin van 60 mm (meetgebied ≈ 1000 mm). Vóór gebruik controleer ik de echte offsets in de backup (drive wheel x offset, measure wheel x offset, clamping margin) en schuif ik de posities in het meetgebied mee.

Ik maak de producten als DSTV-bestanden (NC1). Die kan ik zelf schrijven, zodat ze herhaalbaar zijn en ook op een echte machine gebruikt kunnen worden. Elk product krijgt de naam `QMS820-Pxx`.

## Groep A: sortering en bewegingsrichting

| # | Product | Profiel, lengte | Bewerkingen | Doel |
|---|---|---|---|---|
| P01 | Twee gereedschappen afwisselend | HEA200, 6000, standalone stuk | Ø18 en Ø22 afwisselend om de 500 mm in het lijf (x 250..5750); Ø18 in beide flenzen op x 1000, 3000, 5000 | Default groepeert per gereedschap (heen en weer); Minimize: één richting, meer automatische wissels. Telt reversals en wissels. |
| P02 | Nesting met 6 stukken | IPE300, 12000 staaf, 6 stukken van 1800 | per stuk: 2x Ø22 in het lijf, 2x Ø18 in elke flens, verdeeld over het stuk | B2B met zaag: detected pieces, outfeed MRU pass dalend, infeed MRU pass stijgend, afzagen bij de zaag (BT1-2437 happy flow). |
| P03 | Flange removal op twee flenzen | HE160A, 6000 | flange removal over 4000 mm op beide flenzen (DU2 en DU3), plus Ø18 in het lijf om de 1000 | Herhaling van SWMS-10576/-11017: Default nu zonder uitstel van flange removals; Minimize: beide flenzen in één doorgang. |
| P04 | Handmatige wissel | HEA200, 6000 | gaten die een gereedschap vragen dat niet in het magazijn staat (handmatige wissel), verspreid over de lengte, plus normale gaten | Handmatige wissels blijven gegroepeerd (BT1-2437) of worden waar nodig toegevoegd (EP#654, job 5089). |
| P05 (nog niet gemaakt) | Gat zonder positie / markering | HEA200, 4000 | layout marking + gaten | Stappen zonder positie, markeringen tussen gaten. |

### Zo zien P01 tot en met P03 eruit

Weergave uit het VACAM-venster "Add batch", van boven naar beneden: bovenflens, lijf, onderflens. De NC1-bestanden staan in `C:\Temp\QMS820\NC1\` en worden gemaakt met `qms-nc1.ps1`. VACAM matcht de profielen als HE200A, IPE300 en HE160A. Bij P03 meldt de import "Outer contours not counter clockwise specified"; "Fix product" lost dat op en de block-outs blijven goed.

**P01**: HE200A 6000, Ø18 en Ø22 om en om in het lijf, Ø18 in beide flenzen op 1000, 3000 en 5000.
![[QMS820-P01.png]]

**P02**: IPE300, 6 stuks van 1800 op een staaf van 12000.
![[QMS820-P02.png]]

**P03**: HE160A 6000, flange removal van 40 mm diep van 1000 tot 5000 op beide flenzen, Ø18 in het lijf om de 1000.
![[QMS820-P03.png]]

## Groep B: measure wheel, meetgebied en validatie

| # | Product | Profiel, lengte | Bewerkingen | Verwacht met Minimize |
|---|---|---|---|---|
| P10 | Gat in de band, meetgebied, take over onmogelijk | HEA300, 6000 | Ø22 in de achterste flens (datum line-kant) op halve hoogte op x 5850 en x 5500; Ø22 in het lijf om de 1000 | De gaten die de laatste take over blokkeren worden undoable en gemeld; de rest wordt gemaakt; geen exception (BT1-2440). |
| P11 | Gat in de band, meetgebied, take over mogelijk | HEA300, 6000 | één Ø22 in de achterste flens op halve hoogte op x 5850 | Gemaakt, met take over naar de outfeed MRU op het laatste moment. |
| P10N | Gaten in de band op elk stuk, meerdere stukken op één staaf (zoals SWMS-11375) | L150x14, 1000, aantal 6 op een staaf van 12000 | Ø22 in de band (y 42, beide benen) op x 100 en 900; Ø22 op y 105 op x 500 | Default faalt (take over niet mogelijk); DwF en Min plannen alles zonder iets weg te halen (27-11). Een single-product versie (P10L, 6000) blokkeert niet. |
| P10M | Dichtere variant van P10N | L150x14, 500, aantal 12 op een staaf van 12000 | Ø22 in de band (y 42, beide benen) op x 40, 250 en 460; Ø22 op y 105 op x 150 | Default faalt; DwF en Min plannen alles zonder iets weg te halen (27-11). |
| P12 | Gat in de band buiten het meetgebied | HEA300, 6000 | Ø22 in de achterste flens op halve hoogte op x 3000 | Gemaakt. Measure wheel loopt er niet overheen terwijl hij meet. |
| P13 | Gat buiten de band | HEA300, 6000 | Ø22 in de achterste flens 40 mm onder de bovenkant, op x 5850 | Blokkeert niet, wordt vroeg gemaakt. |
| P14 | Gat in de voorste flens | HEA300, 6000 | Ø22 in de voorste flens op halve hoogte op x 5850 | Blokkeert niet (verkeerde kant). |
| P15 | Kopplaat-gatenpatroon + blokkerend gat | HEA300, 6000 | 4x Ø22 in het lijf binnen 200 mm van het infeed-einde + één Ø22 in de band op x 5600 | Het patroon wordt eerst gemaakt, alleen het blokkerende gat wordt mogelijk undoable (EP#654). |
| P16 | Mix flange removal en gaten in het meetgebied | HEA300, 6000 | flange removal 100 lang in de band op x 5700, Ø22 in de band op x 5850 | Dezelfde regels voor beide (BT1-2440). |
| P17 | BT1-2469 reproductie | HE300A, 9000, kop- en eindsnede | Ø20 in het lijf op x 1000 en 8800; flange removals van 10 lang (x ± 5) in de band op x 7000, 7600, 8200, 8995 | Bekende bug: "There should at least be one take over path", ook met fallback. Vastleggen. |
| P18 | Lange sleuf | HEA200, 6000 | gefreesde sleuf van 1200 lang in de band, midden in het stuk | Herhaling van SWMS-11118: sleuf langer dan de afstand tussen de wielen. |

## Groep C: profieltypes en band

Elk profiel met één "fout" gat in de band in het meetgebied (zoals P10) en één gat net buiten de band (zoals P13). Zo is per profiel te zien of de band goed berekend wordt.

| # | Profiel | Bijzonderheid |
|---|---|---|
| P20 | RHS 200x100x6 (M) | 3x herhalen met measure wheel position Standard, Bottom en Top |
| P21 | L 100x100x10 | twee plaatsingen (lijf onder, flens onder): band 0 tot 2x dikte + 5 |
| P22 | UPE200 | band op de binnenkant van het lijf; ook 180° gedraaid |
| P23 | T-profiel | band midden in de flensdikte |
| P24 | Strip 200x20 | band midden in de dikte |
| P25 | Ronde buis 168x8 | band halverwege de hoogte |
| P26 | Special profile of bundel | geen band: niets blokkeert de measure wheel, alleen regel 1 telt |

## Groep D: korte stukken, schuine einden, V633

| # | Product | Doel |
|---|---|---|
| P30 | Kort stuk van 600 en van 400 op een staaf met lange stukken | regel 1 (350 mm vasthouden), short parts forwarding |
| P31 | Stuk met schuine snede (45°) aan beide kanten | bruikbare lengte korter, windows kleiner |
| P32 | V633: gat op een backwards piece en een gat op het forwards piece vlak bij de zaagsnede | aparte x'-as-groepen met Minimize, één groep met Default (BT1-2438) |
| P33 | V633: SHS60/3 met een block-out vlak voor de snede die het forwards piece losmaakt | herhaling van VACAM job 22343 (EP#654) |
| P34 | V633: groep vlak bij het begin of einde van het materiaal en bij een division | één of twee clamps, force calculation |

## Groep E: klantbatches (regressie en echte gevallen)

Backups uit de QMS-tickets. Elk eerst in 4.11 zonder de wijziging plannen (verwacht resultaat uit het ticket) en dan met de PR.

| Backup | Machine | Ticket | Wat was er mis |
|---|---|---|---|
| `20250006_V633_260121_181915.zip` (+ Batch.zip) | V633 standalone | SWMS-10421 | cycle list aborted |
| `20230179_V633_260128_130642.zip` | V633 standalone | SWMS-10455 | batch cancelled |
| `20240105_V631_260217_164726.zip` | V631 standalone | SWMS-10576 | flange removal heen en weer |
| `20250006_V633_260227_114256.zip` | V633 standalone | SWMS-10635 | hoekprofiel, cancelled |
| `20250031_V631_260304_134633.zip`, `..._260313_034542.zip` (+ `711713_NOVII.nc`, `C-706.7z`) | V631 B2B | SWMS-10725 | "There should be a take over path" |
| `20230083_V633_260318_142836.zip` | V633 standalone | SWMS-10758 | vreemde volgorde flange removal, 6 mm afwijking |
| `20190178_V631_260428_114500.zip` | V631 B2B | SWMS-11000 | te veel heen en weer |
| `20220106_V631_260422_115720.zip` | V631 standalone | SWMS-11017 | frezen DU2/DU3 na elkaar |
| `20240062_V633_260513_135406.zip`, `..._260519_141310.zip` (+ NC1-bestanden) | V633 B2B | SWMS-11058 | take over onmogelijk door gefreesde flens |
| `20250009_V631_260527_152844.zip` | V631 standalone | SWMS-11118 | sleuf langer dan de wielafstand |
| `20250057_V631_260709_161951.zip` | V631 | SWMS-11375 | L-profiel stopt direct |

Lokaal staan al: `20250031_V631_260526_104013` (Maksim, zelfde klant als SWMS-10725), `20230006_V631_260128_141549`, `20250067_V631_260404_112234`, `20240041_V630_250425_171852`, `20200047_V633_250319_141727`. Ik moet nog nagaan welke daarvan measure rollers hebben.

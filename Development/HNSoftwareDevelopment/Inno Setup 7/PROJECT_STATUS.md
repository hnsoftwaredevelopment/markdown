# Inno Setup 7 Knowledgebase — herstelstatus

Laatst bijgewerkt: 6 augustus 2026

## Doel

KS-001 wordt één Nederlandstalig naslagboek over Inno Setup 7 voor professionele Windows-installers. De uitgave combineert vier bestaande delen, gebruikt de HN Software Development Knowledge Series-vormgeving en heeft één echte Word-inhoudsopgave waarin de vier delen als hoofdniveau verschijnen.

## Herstelde bronbestanden

De volledige inhoud is teruggevonden in `C:\Users\hnijk\OneDrive\Word\Knowledgebases\Innosetup`:

| Bron | Onderwerp |
| --- | --- |
| `InnoSetup7-Knowledgebase_Deel01.docx` | Fundamenten en declaratieve scriptsecties |
| `InnoSetup7-Knowledgebase_Deel02.docx` | Pascal Script en de `[Code]`-sectie |
| `InnoSetup7-Knowledgebase_Deel03.docx` | .NET-deployment, signing, buildautomatisering en frameworkarchitectuur |
| `InnoSetup7-Knowledgebase_Deel04.docx` | Cookbook met 31 praktijkrecepten |
| `InnoSetup7-Knowledgebase.png` | Goedgekeurde digitale cover met het eigen HN Software-logo |
| `HN_Software_Development_Knowledge_Series_Template.docx` | Basis voor stijlen, codeblokken, tip-/waarschuwingsblokken en inhoudsopgave |

De bestanden `InnoSetup7-Knowledgebase_Masterdocument.docx` en `InnoSetup7-Knowledgebase.docx` bevatten alleen een skelet en zijn niet de volledige samengestelde uitgave.

## Besloten publicatiestructuur

1. Cover
2. Titel- en publicatiepagina
3. Voorwoord
4. Eén automatische Word-inhoudsopgave
5. Deel I — Fundamenten en declaratieve scriptsecties
6. Deel II — Pascal Script en de `[Code]`-sectie
7. Deel III — Deployment, signing en release engineering
8. Deel IV — Inno Setup Cookbook
9. Versiehistorie en HN Software Development-pagina

Voor de inhoudsopgave geldt deze hiërarchie:

| Niveau | Word-stijl |
| --- | --- |
| Deel | Kop 1 |
| Hoofdstuk | Kop 2 |
| Subhoofdstuk | Kop 3 |
| Technisch detail | Kop 4 |

## Besluiten uit de eerdere chat

- Publicatie: **KS-001, Volume 1, versie 1.1**.
- De cover gebruikt een brede onderwerpafbeelding, zonder tekst over de afbeelding; de definitieve PNG bevat het eigen logo.
- De Knowledge Series-template en de cover worden beide gebruikt.
- De documentatie behandelt de inhoud volledig; het toekomstige HN Software Installer Framework wordt daarnaast als herbruikbare projectstructuur uitgewerkt.

## Vervolgwerk

- De gecombineerde Word-uitgave is structureel in Word en visueel via LibreOffice/PDF gecontroleerd. Cover, hiërarchie, tabellen, code- en kaderblokken renderen correct.
- LibreOffice werkt Word-TOC-velden niet bij. Open daarom de uitgave in Word en gebruik `Ctrl+A`, `F9` en **Gehele tabel bijwerken** voordat je een definitieve PDF maakt.
- Het Installer Framework-starterproject staat klaar met modules, buildpipeline, hash en release-manifest. De eerste concrete applicatie is nog nodig als pilot voor een volledige build-, installatie-, upgrade- en uninstall-test.
- Houd de voortgang en ontwerpbesluiten in deze map bij; de Markdown-documentatie wordt ook naar Obsidian gespiegeld.

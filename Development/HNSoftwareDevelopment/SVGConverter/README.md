# SVG Resource Converter

Een WPF-applicatie (.NET 8) om SVG-bestanden om te zetten naar XAML-resources voor een
.NET ResourceDictionary: als kleuren-behoudende `DrawingImage` of als kleurloze
`Geometry`/`GeometryGroup`. Je kunt een enkel SVG-bestand converteren, of een hele map in
één keer (batch) naar één gecombineerd `.xaml`-bestand.

De resource-key die je in je applicatie gebruikt is altijd exact de bestandsnaam van de
SVG (zonder `.svg`-extensie).

**Deze conversielogica (`Services/SvgConverterLogic.cs` en de bijbehorende modellen) is
ook overgenomen in `SVGViewer`** (`C:\DevOps\hnsoftwaredevelopment\SVGViewer\`), waar je
er direct vanuit de bestaande bestandenbrowser bij kunt via rechtermuisknop op een
SVG-bestand, een selectie van meerdere bestanden, of een map ("Exporteren als
XAML-resource..."). Beide apps gebruiken dezelfde engine en leveren dus identieke output;
een fix in de één (zoals de FillRule/rect-ellips-lijn-fix hieronder) moet ook in de ander
worden doorgevoerd als je ze los van elkaar blijft onderhouden.

## Belangrijk: nog niet gebouwd/getest

Deze code is geschreven in een cloud-omgeving zonder toegang tot nuget.org, dus ik heb
het project hier **niet kunnen restoren, bouwen of draaien**. De conversielogica is
overgenomen van de bestaande `SvgToXaml`-tool (die je al gebruikt en waarvan je zegt dat
die vrijwel alles correct omzet) - zie `THIRD-PARTY-NOTICES.md` - dus de kans op
functionele verrassingen is klein, maar er kunnen kleine compileerfouten in zitten
(bijvoorbeeld een net iets andere methode-signatuur in de huidige SharpVectors-versie
t.o.v. de oude 1.2.0 die de bestaande tool gebruikt). Open het project in Visual Studio,
laat NuGet restoren en bouw het; als er compileerfouten zijn, stuur me de foutmelding dan
even door, dan los ik het gericht op.

## Openen en bouwen

1. Open `SvgResourceConverter.sln` in Visual Studio 2022 (17.8 of nieuwer, met de
   ".NET Desktop Development"-workload).
2. Visual Studio herstelt automatisch het NuGet-pakket `SharpVectors` (versie 1.8.5).
3. Build de oplossing (Ctrl+Shift+B) en start `SvgResourceConverter` (F5).

## Gebruik

1. Kies **Enkel SVG-bestand** of **Map met SVG-bestanden (batch)**.
2. Blader naar de bron (bestand of map).
3. Kies het uitvoerformaat:
   - **DrawingImage (met kleur)** - genereert `Geometry` + `DrawingGroup` +
     `DrawingImage`. Gebruik als `Source` van een `<Image>`.
   - **Geometry (monochroom)** - genereert een `Geometry` (of `GeometryGroup` als het
     icoon uit meerdere paden bestaat), zonder kleurinformatie. Gebruik als `Data` van
     een `<Path>` met een zelf te kiezen `Foreground`.
4. Vul de **bestandsnaam** voor het uitvoerbestand in (bijv. `Icons.xaml`). In welke map
   dat bestand terechtkomt, stel je één keer in via **Instellingen** linksboven: standaard
   "zelfde map als de SVG-bestanden", of een vast eigen pad (handig als je de SVG's ergens
   anders bewaart dan je WPF-project). De uiteindelijke map zie je als grijze tekst onder
   het bestandsnaamveld.
5. Klik op **Converteren**, en voeg het gegenereerde bestand toe aan je project en merge
   het in je `ResourceDictionary` (bijvoorbeeld via `App.xaml`):

   ```xml
   <ResourceDictionary.MergedDictionaries>
       <ResourceDictionary Source="Resources/Icons.xaml" />
   </ResourceDictionary.MergedDictionaries>
   ```

6. Gebruik het icoon in je eigen XAML, bijvoorbeeld:

   ```xml
   <!-- DrawingImage-modus -->
   <Image Source="{StaticResource Mailings}" Width="24" Height="24" />

   <!-- Geometry-modus -->
   <Path Data="{StaticResource Mailings}" Fill="{DynamicResource MyAccentBrush}" />
   ```

Bij batchconversie van een map met dubbele (na opschoning identieke) bestandsnamen wordt
het tweede bestand overgeslagen en zie je dat terug in de statuskolom van de
voorbeeldlijst.

## Groter voorbeeld per icoon

Dubbelklik op een rij in de voorbeeldlijst voor een apart venster met een grotere weergave
van dat icoon. Vier knoppen laten je schakelen tussen:

- **Kleurvoorbeeld** - het icoon zoals het eruitziet als `DrawingImage` (met de originele
  SVG-kleuren).
- **Monochroom voorbeeld** - hoe hetzelfde icoon eruitziet als kleurloze `Geometry`,
  hier zwart getekend zodat je het silhouet kan beoordelen.
- **XAML (kleur)** en **XAML (monochroom)** - de exacte gegenereerde XAML-tekst voor
  beide varianten, ongeacht welk uitvoerformaat je op het hoofdscherm hebt gekozen.

## Beperkingen van de conversie

De conversie-engine (SharpVectors) dekt het overgrote deel van praktische, statische
SVG-iconen goed af: paden, basisvormen (rect/cirkel/ellips/lijn/polygon), groepen en
transforms, meerdere kleuren, kleurverlopen (gradients) en clip-paths, en tekst (die de
app altijd omzet naar contourgeometrie, zodat het resultaat geen lettertype nodig heeft
tijdens gebruik in je WPF-app). Bekende aandachtspunten:

- **Filters** (bijv. `feGaussianBlur`, drop-shadow, kleurmatrices) worden door
  SharpVectors niet of nauwelijks ondersteund.
- **Patterns en masks** zijn historisch minder volledig ondersteund dan paden/vormen/
  gradients.
- **Animaties (SMIL, `<animate>`)** worden genegeerd - logisch, want de uitvoer is een
  statische XAML-resource.
- **Tekst-elementen** worden omgezet naar contouren met het lettertype dat op *deze*
  machine (waar je converteert) geïnstalleerd staat; ontbreekt dat lettertype, dan wijkt
  de vorm van de tekst iets af van het origineel.
- In **Geometry-modus** gaan kleuren/kleurverlopen per ontwerp verloren (dat is het hele
  punt van die modus) - gebruik **DrawingImage** als je de originele kleuren wil behouden.

Kortom: voor "normale" iconen (zoals in je voorbeelden) zou vrijwel alles moeten werken;
bij zwaar gestileerde SVG's met filters/patterns/masks kan het resultaat afwijken.

### Geometry (monochroom) specifiek: waarom dit soms leeg of onvolledig oogt

Een SVG met kleur kan niet altijd 1-op-1 worden "platgeslagen" tot één silhouet - dat is
geen bug per se, maar een eigenschap van hoe zo'n icoon is opgebouwd. Twee concrete
oorzaken zijn gevonden en opgelost naar aanleiding van jouw test:

- **Losse rect/cirkel/ellips/lijn-vormen werden overgeslagen.** SharpVectors zet een
  eenvoudige `<rect>`/`<circle>`/`<ellipse>`/`<line>` niet altijd om naar een pad, maar
  laat het soms als eigen (Rectangle/Ellipse/Line)Geometry staan. Geometry-modus keek
  daar niet naar en liet die vorm(en) gewoon weg - bij een icoon dat volledig uit zulke
  basisvormen bestaat, zag je dus niets; bij een mix van paden en basisvormen zag je enkel
  de paden. Dit is nu gerepareerd: deze vormen worden alsnog meegenomen.
- **Overlappende deelvormen konden een "gat" veroorzaken.** Een `GeometryGroup` zonder
  expliciete `FillRule` valt in WPF terug op `EvenOdd`; als twee losse (oorspronkelijk
  los gekleurde) vormen elkaar overlappen, sneed dat een stuk weg in plaats van het als
  gevuld te behandelen. De app zet nu expliciet `FillRule="Nonzero"` op de gegenereerde
  `GeometryGroup`, wat dat probleem voorkomt.

Eén categorie blijft inherent beperkt: een `<line>` (of een pad dat alleen bedoeld is om
te *stroken*, zonder vulling) heeft van zichzelf geen oppervlak. Geometry-modus kent geen
lijndikte/pen, dus zo'n vorm blijft, ook na de fix hierboven, onzichtbaar zodra je hem als
gevulde `Geometry` gebruikt - dat is geen bug maar wiskundig verwacht (een lijn "vullen"
geeft niets om te vullen).

**Is Geometry-modus dan nog zinvol, of kun je beter alleen de kleurenvariant houden?**
Voor "gesloten"/silhouet-achtige iconen (vlakke vormen, geen dunne lijntjes) blijft
Geometry-modus, na deze fix, een prima en bruikbare optie - dat is precies het scenario
waar hij voor bedoeld is (één kleur, zelf een `Foreground` kiezen in je eigen XAML). Voor
"outline"/lijn-stijl iconensets (waar het icoon vrijwel alleen uit dunne, gestrokete
lijnen bestaat, zonder vlakken) is Geometry-modus minder geschikt en is DrawingImage de
veiligere keuze. Het advies is dus niet "de optie weghalen", maar: gebruik het
dubbelklik-voorbeeldvenster (Monochroom voorbeeld) om per icoon(set) te controleren of het
silhouet er goed uitziet vóórdat je het in Geometry-modus opneemt in je resource-bestand.

## Vertalingen (NL/EN/DE) beheren met ResXManager

Alle teksten in de UI zitten in
`src/SvgResourceConverter/Localization/Resources/Strings.resx` (Nederlands, de
neutrale/standaard taal), `Strings.en.resx` en `Strings.de.resx`. Open ze met de
ResXManager-extensie in Visual Studio om nieuwe teksten toe te voegen of te wijzigen -
ResXManager houdt de drie bestanden en de gegenereerde `Strings.Designer.cs`
automatisch synchroon.

De taal is in de applicatie zelf ook live om te schakelen (rechtsboven), zonder herstart.

## Projectstructuur

```
src/SvgResourceConverter/
  App.xaml(.cs)                   Opstart, default taal (Nederlands)
  MainWindow.xaml(.cs)            Hoofdscherm
  SettingsWindow.xaml(.cs)        Instellingen (standaard uitvoermap)
  IconDetailWindow.xaml(.cs)      Groter voorbeeld per icoon (dubbelklik in de lijst)
  ViewModels/                     MainViewModel, SettingsViewModel, IconDetailViewModel (MVVM, geen externe library)
  Services/SvgConverterLogic.cs   De eigenlijke SVG -> XAML-conversie (SharpVectors)
  Services/SettingsService.cs     Laadt/bewaart instellingen als JSON in %AppData%
  Models/                         SvgIconItem, AppSettings, OutputPathMode
  Localization/                   Strings.resx (NL) + Strings.en.resx + Strings.de.resx
```

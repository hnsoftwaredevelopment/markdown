## Resultaat

Series beheren is beschikbaar in de hoofdwerkbalk. De gebruiker kan series zoeken, boekaantallen bekijken, boeken op exact numerieke volgorde doorlopen en een hele serie expliciet hernoemen. Een bestaande doelserie wordt geweigerd; nummers en overige boekgegevens blijven behouden.

## Opslag en gedrag

- Bestaand Series/SeriesNumber-model, zonder migratie of mapverplaatsingen. Dezelfde trim-/hoofdletterongevoelige groepering als het seriefilter; accentverschillen blijven apart.
- Dunne naamindex en sorteersleutels van alleen de geselecteerde serie; decimalen vóór paginering sorteren, auteurs alleen per geladen pagina. Geen omslagen in beheerlijsten.
- Eén database-transactie met hercontrole van bron, doel, alle bevestigde boek-ID's en oorspronkelijke serienamen. Alleen Series/UpdatedUtc wijzigt.
- Na commit bestaande BookService-bestandssynchronisatie met actuele metadata. Bestandsproblemen zijn aparte waarschuwingen per boek; geen onterechte rollbackmelding of automatische herhaling.
- Nieuwe naam blijft geselecteerd in dezelfde zoekcontext. Hoofdscherm, details en seriefilter worden bij sluiten via de bestaande reconciliatie bijgewerkt met behoud van geladen omslagen.
- Zichtbare splitter, begrensde/gevirtualiseerde lijsten, toetsenbordbediening en zes talen.

## Verificatie

- `dotnet test EbookManager.sln -c Debug --no-restore`: **980 geslaagd**, 0 mislukt/overgeslagen.
- `dotnet build src/EbookManager.App/EbookManager.App.csproj -c Debug --no-restore`: **0 waarschuwingen, 0 fouten**.
- Enige testbuild: `Builds\Debug\Saga.exe`, bestandsversie **2026.10.24.52**, laatst geschreven **24 oktober 2026 15:01:45 Europe/Amsterdam**. Precies één Saga.exe onder Builds.
- Tijdelijke SQLite-tests: numerieke paginering met 210 boeken, hernoemen van 510 boeken, Unicodevarianten, doelconflict, verouderde bron/boekset, volledige rollback en behoud van scalairen en relaties. Echte metadata.json, bestandsfout en annulering vóór/na commit getest.
- Eigen review op correctheid, eenvoud, architectuur, veiligheid en prestaties. Resultaatmelding na commit en splittercontrast aangescherpt. WPF-render met fictieve data op 1040×650 en 800×480 gecontroleerd; echte bibliotheek niet gebruikt voor fouttests.
- README verwijst naar de actuele [Milestone 50-checklist](docs/manual-tests/milestone-50-checklist.md). Alle acht nieuwe/gewijzigde Markdown-bestanden exact naar Obsidian gespiegeld en SHA256 gecontroleerd.

## Nog open

Handmatige gebruikersacceptatie van de nieuwe build volgens de checklist; deze is bewust niet afgevinkt. Serienummers bewerken, series samenvoegen/splitsen, online gegevens en volledigheidsdetectie vallen buiten deze slice. Geen nieuwe dependency, schema of writer; daarvoor zijn migratie-/installatiecontroles niet van toepassing. Alleen de gebruiker mergt.

# M04-S07 — Regels koppelen

Status: geïmplementeerd op m04-installatiekeuzes; wacht op gebruikersacceptatie. S06 is gepusht als bbef6d9.

Open een bestandsregel, mapregel of snelkoppeling en kies **Koppelen aan keuzes**. Binnen de kolom Componenten of Taken is één overeenkomende keuze genoeg. Zijn beide kolommen ingevuld, dan moet in beide een keuze overeenkomen. Leeg betekent geen beperking. Inno Setup voert dit uit met de native [Components- en Tasks-parameters](https://jrsoftware.org/ishelp/topic_componentstasksparams.htm), zonder gegenereerde installatiecode. Een type bepaalt via zijn componentselectie welke regels van toepassing zijn.

Projectformaat 16 bewaart deze koppelingen. Oudere projecten openen zonder nieuwe beperkingen. Verwijderen of hernoemen van een gebruikte component of taak is geblokkeerd; het venster toont de betrokken regels. Ongeldige verwijzingen blokkeren bewaren en exporteren. Voor elke snelkoppeling moet minstens één bestandsregel het doelbestand bij alle keuzes van die snelkoppeling leveren. Als verschillende bestandsregels het bestand elk slechts voor een deel van de keuzes leveren, ondersteunt Studio die gecombineerde dekking nog niet. Een ongekoppelde bestandsregel of een minder beperkende koppeling volstaat.

Studio biedt hier geen vrije booleaanse expressies, taskhiërarchie of dynamische zichtbaarheid van taken per component. De proef blijft een simulatie van keuzes, zonder bestanden te installeren. Een direct gekoppelde bovenliggende component kan ook zonder geselecteerde subcomponenten worden gekozen, conform Inno Setup. Bij een startmenusnelkoppeling met een taakkoppeling bepaalt die taak de keuze; de native optie om geen startmenumap te maken onderdrukt die snelkoppeling niet.

## Twee schone installaties vergelijken

1. Maak een testproject met een altijd te installeren bestand en een tweede bestand, bijvoorbeeld handleiding.txt. Maak component Handleiding, alleen geselecteerd bij Volledig. Koppel de bestandsregel van handleiding.txt aan Handleiding.
2. Maak de taak Bureaubladsnelkoppeling, standaard niet aangevinkt. Maak een bureaubladsnelkoppeling naar handleiding.txt en koppel haar aan Handleiding én Bureaubladsnelkoppeling. Koppel eventueel een lege testmap aan dezelfde keuzes.
3. Bouw de installer. Installeer met **Volledig** en vink de taak aan. Controleer het vaste bestand, de handleiding, de snelkoppeling en eventueel de map.
4. Verwijder deze testinstallatie en controleer dat de testlocatie schoon is. Installeer opnieuw met **Compact** en laat de taak uit. Alleen het vaste bestand moet worden geïnstalleerd. Test desgewenst ook Volledig zonder de taak: de handleiding is er wel, de snelkoppeling en optionele map niet.
5. Bewaar en heropen het project. Controleer de vinkjes in de regelvensters. Probeer een gebruikte component of taak te verwijderen. Maak daarna de snelkoppeling minder beperkt dan haar doelbestand en controleer dat export de fout meldt.

Release-build zonder fouten of waarschuwingen; 294 tests geslaagd. De nieuwe tests controleren native compilatie, behoud bij Opslaan als en migratie, ongeldige verwijzingen en beschikbaarheid van snelkoppelingsdoelen. Daadwerkelijke installaties zijn aan de gebruiker gelaten.

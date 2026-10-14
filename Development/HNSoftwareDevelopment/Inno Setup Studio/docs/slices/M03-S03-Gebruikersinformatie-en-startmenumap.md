# M03-S03 — Gebruikersinformatie en startmenumap

Status: geïmplementeerd; wacht op gebruikerscontrole en acceptatie op m03-wizardpaginas.

Resultaat: vanuit het paginaoverzicht Gebruikersinformatie en Startmenumap instellen. Gebruikersinformatie: pagina aan/uit, standaardnaam en organisatie en vorige gegevens gebruiken. Startmenumap: automatisch/tonen/verbergen, standaardnaam, keuze om geen map te maken en vorige keuze gebruiken. Alleen native richtlijnen; serienummer vereist CheckSerial en hoort bij latere scripting.

Criteria: instellingen worden opgeslagen en geëxporteerd met gecontroleerde migratie; preview-invoer in het instelvenster is tijdelijk; de paginastatus volgt de beschikbare inhoud. Zolang er geen Icons-regels zijn, verschijnt Startmenumap niet in de installer, ook niet bij Tonen. Snelkoppelingen volgen in M04; geen kunstmatige Icons-regel in het gebruikersproject. Voorwaarden en grenzen zijn zichtbaar in de UI.

Afbakening: nog geen volledige Uitproberen-route voor deze pagina’s. Het invoervoorbeeld toont de relevante velden en bewaart geen proefinvoer; native constanten blijven zichtbaar als expressies. Native gebruikersgegevens en updategedrag worden door Inno Setup bepaald. Algemene instellingen, geen eigen titelvertalingen in deze slice.

Bronnen: [UserInfoPage](https://jrsoftware.org/ishelp/topic_setup_userinfopage.htm), [DisableProgramGroupPage](https://jrsoftware.org/ishelp/topic_setup_disableprogramgrouppage.htm), [AllowNoIcons](https://jrsoftware.org/ishelp/topic_setup_allownoicons.htm).

Handmatig: stel naam/organisatie in, sluit/open en controleer opslag. Wijzig alleen proefinvoer en controleer dat de projectstatus niet verandert. Bouw en draai de installer: gebruikersinformatie verschijnt en de echte invoer is bewerkbaar. Schakel uit: de pagina verdwijnt en instellingen blijven bewaard. Stel startmenumapbeleid in, sla op/open en controleer export; de pagina blijft zonder snelkoppelingen afwezig. Controleer Nederlands/Engels/Duits en een kleiner venster.

Genoteerd voor latere wizardbediening: Licentie en andere configuratiepagina’s moeten ook duidelijk via het gewone hoofdscherm bereikbaar worden. Nu is toegang via het paginaoverzicht. Dit verandert de scope van S03 niet; meenemen bij de verdere navigatie-/wizardproef.

Verificatie: Release-build zonder fouten of waarschuwingen. De volledige regressierun slaagt met 202 tests. Daarna zijn opslag/migratie, ongeldige invoer, drie Studio-talen en drie native compilerproeven toegevoegd; de laatste gerichte run slaagt met 25 tests. ISCC 7.1.0 accepteert gebruikersinformatie en automatisch/tonen/verbergen voor de startmenumap. Een snelkoppeling wordt uitsluitend in de compilerproef toegevoegd om de native mapkeuze toepasbaar te maken; het gebruikersproject krijgt geen snelkoppelingen. Geen GUI of installer is automatisch gestart.

Formaat 8 bewaart PageSettings. Formaten 1–7 krijgen veilige native beginwaarden; bestaande documenten, talen, teksten en identiteit blijven behouden. Gebruikersinformatie blijft standaard uit. Startmenubeleid begint Automatisch, zonder expliciete mapnaam; de native standaard blijft gelden. Beginvelden mogen native constanten bevatten. Studio-verwijzingen {AppName}/{AppVersion} worden voor export vervangen door letterlijke applicatiegegevens, zonder opnieuw als verwijzing te worden geïnterpreteerd.

Bediening: selecteer Gebruikersinformatie of Startmenumap in Paginaoverzicht en kies Pagina instellen, ook als de status rood is. Proefvelden onder Invoervoorbeeld zijn alleen tijdelijk. De proefvelden gebruiken de Studio-taal; zij zijn geen exacte afbeelding van de native wizard. De volledige wizardnavigatie volgt in de verdere M03-slices. Bij een kleinere venstergrootte kan het instelvenster scrollen.

Commit/push pas na expliciete gebruikersacceptatie. Documentatie is gespiegeld naar Obsidian en gecontroleerd.

# Inschrijfmail

Bij de eerste festivalinschrijving bewaart Mijn de te verzenden berichten in dezelfde databasetransactie als de inschrijving en de logging. De actieve eerste en tweede contactpersonen en het kooradres krijgen ieder een bevestiging, met ontdubbeling per e-mailadres. De organisatie krijgt een apart bericht voor de drie adressen uit de bestaande PHP-route. Een wachtlijstinschrijving krijgt een expliciete wachtlijsttekst. De kosten in de koormail komen uit dezelfde berekening als op het inschrijfscherm.

Wijzigen of definitief bevestigen van een bestaande inschrijving maakt geen nieuwe aanmeldmail aan. De eerste aanmeldmail gebruikt voorlopig vaste Nederlandse tekst. De beheerbare factuurtekst en definitieve PDF horen bij de verdere facturatie.

De verzender biedt mislukte berichten opnieuw aan met oplopende wachttijd. Het logboek van de applicatie vermeldt het berichtnummer en fouttype, zonder e-mailadres of inhoud. Herhaalde aanvragen maken geen dubbele wachtrijregels. Gewone SMTP garandeert geen eenmalige aflevering als de verbinding wegvalt direct nadat de mailserver het bericht heeft geaccepteerd.

Op dev schrijft de verzender de berichten uitsluitend naar de afgeschermde mailopvang `/var/lib/amusing-mijn-dev/mailopvang`. Bij productie-omschakeling zijn migratie 008, lees-/schrijfrechten op de wachtrij en SMTP-configuratie nodig. De productie-SMTP-route is nog niet getest of geactiveerd.

## Acceptatie op dev.mijn

Log in met testaccount 1 en schrijf Testkoor Mailopvang in met 21 deelnemers en podiumtype B. In Mijn staat daarna € 100,00 inclusief btw. De wachtrij verwerkt het koorbericht en de aparte berichten voor de organisatie. Op dev blijven ze in de mailopvang.

De integratietest controleert dubbele aanmelding, een mislukte verzendpoging en het opnieuw aanbieden aan de mailopvang. De ingelogde HTTPS-controles op dev.mijn zijn geslaagd.

## Mailinglayouts

Afgesproken voor de verdere uitwerking in Beheer. Mijn kiest bij de eerste aanmelding op basis van de opgeslagen wachtlijststatus een van twee koorsjablonen met een eigen onderwerp en tekst.

- **Aanmelding ontvangen** bevat de inschrijfgegevens en het deelnamebedrag.
- **Aanmelding op de wachtlijst** vermeldt dat deelname nog niet is toegezegd en dat het koor bericht krijgt zodra er een plek beschikbaar is. Deze mail bevat geen betaalverzoek.

Herbert heeft de test op dev.mijn geaccepteerd. De tabel op het inschrijfscherm heet Deelnamekosten en heeft een lijn onder de kolomkoppen en onder de btw-regel.

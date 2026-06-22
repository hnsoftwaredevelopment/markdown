swart_en_co

# De opslagruimte voor macro's kan niet worden geopend

![1547114361025](images/1547114361025.png)

![](images/swartenco.png)

![img](images/clip_image002.jpg)

|                       |                        |
| --------------------- | ---------------------- |
| Datum contact         | 10-01-2019 11:00       |
| Kantoor               | Swart & Co 020-5456121 |
| Contactpersoon        | Soesie Wongso          |
| Analyse uitgevoerd    |                        |
| Oplossing gevonden    | ja                     |
| Vervolg actie vereist | nee                    |



Bekend probleem van Office 97 - 2013, onbekend vanaf 2016

## Macro is niet gecompileerd op de huidige machine of met het huidige gebruikers profiel

1. Maak de ontwikkelaarsmode zichtbaar in het lint:

   > Bestand – Opties – Lint aanpassen – Ontwikkelaars tabblad aanvinken>

2. Open het sjabloon

3. ALT+F11 (nu verschijnt de foutmelding)

4. Ga naar menu: Foutopsporing – Project compileren (Meestal zie je niets, wordt alleen deze optie uit gegrijst ten teken dat dit gebeurt is)

5. Druk CTRL-S (opslaan)

6. Sluit het document



Hierna zou het document probleemloos moeten openen

 

Schakel wel het menu met de ontwikkelaarsmodus weer uit indien dat ongewenst is voor de gebruiker

> Bestand – Opties – Lint aanpassen – Ontwikkelaars tabblad uitvinken

## Andere mogelijke oorzaken

- Naamgeving document: Bijzondere tekens (` & ^ € ¤ " enz)
- Beschadigde normal.dot, kopieer de normal.dot van een machine of gebruiker zonder het probleem
- Template is niet gemigreerd naar de gebruikte office versie. Open het sjabloon en sla het op als nieuw sjabloon





Opgepakt samen met Joeri Baijens, voor 2 testgebruikers uitgevoerd en leek te werken)


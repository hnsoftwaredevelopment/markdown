# Wat is Inno Setup

Inno Setup is een programma waarmee je installatieprogramma's bouwt voor Windows-applicaties. Je stopt je eigen software erin en Inno Setup zet er een enkel .exe-bestand van, dat gebruikers vervolgens draaien om jouw programma te installeren. Jordan Russell bouwde het in 1997, Martijn Laan is sindsdien mede-ontwikkelaar. Het is open source en de broncode staat op GitHub.

## Wat het voor je doet

Je schrijft een scriptbestand (.iss) waarin je vastlegt welke bestanden mee moeten, waar ze moeten komen te staan en welke snelkoppelingen je wilt aanmaken. Inno Setup compileert dat script tot een werkend installatieprogramma. De resulterende installer kan zo klein zijn als 2 MB, afhankelijk van wat je meelevert en welke compressie je kiest.

Een paar dingen die het programma standaard aankan:

- Installaties met en zonder beheerdersrechten
- Compressie via deflate, bzip2 of 7-Zip LZMA
- Silent install en silent uninstall, handig als je de installatie wilt scripten of automatiseren
- Meertalige installers, inclusief talen die van rechts naar links lopen
- Versleuteling, wachtwoordbeveiliging en digitale ondertekening van de installer
- Een ingebouwde Pascal-scriptingengine, waarmee je eigen logica aan de installatie toevoegt
- Een vergroot- en verkleinbare wizard, met ondersteuning voor donkere modus

## Voor welke systemen

Inno Setup richt zich op Windows-versies vanaf 2009: Windows 11, Windows 10, de Server-varianten en ARM-gebaseerde architecturen naast de gebruikelijke x64. Grote namen die het gebruiken voor hun eigen installers zijn Visual Studio Code, Git for Windows en Embarcadero Delphi.

## Licentie

Inno Setup zelf is auteursrechtelijk beschermde software. Gebruik je het commercieel, dan heb je een commerciële licentie nodig. Kijk op de site van Jordan Russell voor de actuele voorwaarden voordat je het in een commercieel traject inzet.

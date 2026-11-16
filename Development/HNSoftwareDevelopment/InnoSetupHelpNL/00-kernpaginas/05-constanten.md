# Constanten

Constanten zijn vaste tekstwaarden tussen accolades, zoals `{app}`, die Inno Setup tijdens de installatie vervangt door een echt pad of een echte waarde. Je gebruikt ze overal waar je een pad, gebruikersnaam of ander gegeven nodig hebt dat pas op het moment van installeren bekend is.

## Basisregels

Wil je een letterlijke `{` in je tekst, typ hem dan twee keer (`{{`). Een `}` hoef je nooit te verdubbelen. Staat een constante al met een backslash aan het eind van zijn waarde, dan haalt Inno Setup een backslash die je er zelf achter zet automatisch weg. Wil je dat voorkomen, zet dan `{\}` neer.

## Mappen

| Constante | Waar hij naar verwijst |
|---|---|
| `{app}` | De map die de gebruiker kiest om je programma te installeren |
| `{win}` | De Windows-systeemmap |
| `{sys}` | System32; op 64-bit Windows standaard de 32-bit bestanden |
| `{sysnative}` | Op 64-bit Windows de 64-bit systeembestanden, op 32-bit Windows hetzelfde als {sys} |
| `{syswow64}` | SysWOW64, voor 32-bit bestanden op 64-bit Windows |
| `{src}` | De map met je Setup-bestanden |
| `{sd}` | De systeemschijf, meestal C: |
| `{commonpf}`, `{commonpf32}`, `{commonpf64}` | De Program Files-mappen |
| `{commoncf}`, `{commoncf32}`, `{commoncf64}` | De Common Files-mappen |
| `{tmp}` | Een tijdelijke map die Setup zelf aanmaakt en na afloop weer verwijdert |
| `{commonfonts}` | De lettertypemap |
| `{dao}` | De DAO-map |
| `{dotnet11}`, `{dotnet20}`, `{dotnet2032}`, `{dotnet2064}`, `{dotnet40}`, `{dotnet4032}`, `{dotnet4064}` | Installatiemappen van de bijbehorende .NET Framework-versie |

## Gebruikersmappen (shell folders)

| Constante | Waar hij naar verwijst |
|---|---|
| `{group}` | De Startmenu-map die de gebruiker in de wizard kiest |
| `{localappdata}` | De lokale Application Data van de huidige gebruiker |
| `{userappdata}`, `{commonappdata}` | Application Data-mappen |
| `{usercf}` | Common Files van de huidige gebruiker (Windows 7 en hoger) |
| `{userdesktop}`, `{commondesktop}` | Bureaublad-mappen |
| `{userdocs}`, `{commondocs}` | Mijn Documenten-mappen |
| `{userfavorites}` | Favorieten van de huidige gebruiker |
| `{userfonts}` | Lettertypen van de huidige gebruiker (Windows 10 versie 1803 en hoger) |
| `{userpf}` | Program Files van de huidige gebruiker (Windows 7 en hoger) |
| `{userprograms}`, `{commonprograms}` | Programma's-mappen in het Startmenu |
| `{usersavedgames}` | Saved Games van de huidige gebruiker |
| `{usersendto}` | De Verzenden naar-map van de huidige gebruiker |
| `{userstartmenu}`, `{commonstartmenu}` | De hoofdmap van het Startmenu |
| `{userstartup}`, `{commonstartup}` | Opstart-mappen |
| `{usertemplates}`, `{commontemplates}` | Sjablonen-mappen |

## Auto-constanten

De auto-varianten kiezen zelf de juiste map: bij een installatie met beheerdersrechten pakken ze de common-variant, zonder beheerdersrechten de user-variant. Gebruik ze als je script op beide manieren moet werken: `autoappdata`, `autocf`, `autocf32`, `autocf64`, `autodesktop`, `autodocs`, `autofonts`, `autopf`, `autopf32`, `autopf64`, `autoprograms`, `autostartmenu`, `autostartup`, `autotemplates`.

## Overige constanten

| Constante | Waar hij naar verwijst |
|---|---|
| `{\}` | Een letterlijke backslash |
| `{%NAAM\|Standaardwaarde}` | De waarde van een omgevingsvariabele, met terugval op de standaardwaarde |
| `{cmd}` | Het volledige pad naar cmd.exe |
| `{computername}` | De computernaam |
| `{drive:Pad}` | Alleen de schijfletter uit een pad |
| `{groupname}` | Alleen de naam van de Startmenu-map, zonder pad |
| `{wizardhwnd}` | Het vensterhandle van de Setup-wizard |
| `{ini:Bestandsnaam,Sectie,Sleutel\|Standaardwaarde}` | Een waarde uit een .ini-bestand |
| `{language}` | De interne naam van de gekozen taal |
| `{cm:BerichtNaam}`, `{cm:BerichtNaam,Argumenten}` | De waarde van een custom message |
| `{reg:HKxx\Subsleutelnaam,Waardenaam\|Standaardwaarde}` | Een waarde uit het register |
| `{param:ParamNaam\|Standaardwaarde}` | De waarde van een command-line parameter |
| `{srcexe}` | Het volledige pad naar het Setup-uitvoerbestand |
| `{uninstallexe}` | Het volledige pad naar het deïnstallatieprogramma |
| `{sysuserinfoname}`, `{sysuserinfoorg}` | Registratiegegevens uit Windows zelf |
| `{userinfoname}`, `{userinfoorg}`, `{userinfoserial}` | Gegevens die de gebruiker zelf invulde in de wizard |
| `{username}` | De gebruiker die Setup of het deïnstallatieprogramma uitvoert |
| `{log}` | De naam van het logbestand, als logging aanstaat |

## Speciale tekens in constanten

Gebruik je een constante met meerdere parameters, zoals `{%}`, `{ini:}`, `{reg:}`, `{param:}` of `{cm:}`, dan moet je speciale tekens percent-encoden: een komma wordt `%2c`, een pipe wordt `%7c`, een sluitende accolade wordt `%7d` en een procentteken wordt `%25`.

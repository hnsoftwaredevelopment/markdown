# Algemene parameters

Drie parameters kun je in meerdere secties tegenkomen. Ze bepalen niet wat een item doet, maar of Inno Setup het item überhaupt verwerkt.

## Languages

Met Languages bepaal je bij welke geïnstalleerde talen een item wordt meegenomen. Je geeft een of meer taalnamen op, gescheiden door spaties, of je bouwt een booleaanse expressie. Zet je geen Languages-parameter neer, dan verwerkt Inno Setup het item sowieso, tenzij een andere parameter dat blokkeert.

## MinVersion

MinVersion legt de minimale Windows-versie vast waarop een item wordt verwerkt. Je kunt hier ook een buildnummer of servicepack-niveau in meenemen. Deze parameter overschrijft de algemene instelling die je in de [Setup]-sectie hebt staan. Laat je hem weg, dan speelt de Windows-versie geen rol en wordt het item op elke ondersteunde versie verwerkt.

## OnlyBelowVersion

OnlyBelowVersion doet het omgekeerde van MinVersion: het item wordt niet verwerkt vanaf de opgegeven versie. Zet je hem op 0, dan is er geen bovengrens. Wil je dat deze parameter daadwerkelijk iets blokkeert, moet de waarde hoger liggen dan 6.1. Ook deze parameter overschrijft, indien aanwezig, de algemene instelling.

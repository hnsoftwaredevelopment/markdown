Geen rechten om Powershell uit te voeren

Geen rechten om Powershell uit te voeren

http://techgenix.com/powershell-errors-term-not-recognized/

Run Powershell als administrator

Scripts uitvoeren door:
powershell -ExecutionPolicy ByPass -File "C:\Scripts\powershellscript.ps1"

OF

Powershell -executionpolicy unrestricted -command "C:\Scripts\MSGraph_FileUpload_v1.0.ps1"

Maar je kunt ook eeerst de poliy aanpassen en dan normaal de  scripts draaien

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

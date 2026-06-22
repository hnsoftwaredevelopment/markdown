Connect to Master on Azure

# Connect to Master on Azure

## Set the correct registry settings to connect to Azure
```Registry
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Innolan\Azure]
"customerprefix"="Master2101_"
"server"="dev-sql-01-alure.database.windows.net"

[HKEY_LOCAL_MACHINE\SOFTWARE\Innolan\Azure\Alure]
"database"="Alure"

[HKEY_LOCAL_MACHINE\SOFTWARE\Innolan\Azure\Autor]
"database"="Autor"

[HKEY_LOCAL_MACHINE\SOFTWARE\Innolan\Azure\DocDb]
"database"="AlureDoc"

[HKEY_LOCAL_MACHINE\SOFTWARE\Innolan\Azure\InstallDir]
"Alure"="c:\\Program Files\\Innolan\\Alure.NET"
"AlureUpdater"="c:\\Program Files\\Innolan\\AlureUpdater"
"Autor"="c:\\Program Files\\Innolan\\Autor.NET"
"AlureScanConnector"="c:\\Program Files\\Innolan\\Alure Scan Connector\\"
"AlureOutlookConnector"="C:\\Program Files\\Innolan\\Alure Outlook ConnectorX64\\"
```

## Set che correct AlureCostomSettings.Config
```XML
<?xml version="1.0"?>
<configuration>
  <appSettings>
    <add key="DatabaseConfiguratie" value="Azure" />
    <add key="Server" value="Azure" />
    <add key="Logging" value="false" />
  </appSettings>
  <connectionString>
	<add key="Server" value="dev-sql-01-alure.database.windows.net,1450" />
    <add key="DatabaseName" value="Alure" />
  </connectionString>
  <CtiConfiguration>
    <add key="OpenIfNumberNotFound" value="True" />
  </CtiConfiguration>
</configuration>
```

## To connect from **S**ql **S**erver **M**anagement **S**tudio
|||
|---|---|
|Server|dev-sql-01-alure.database.windows.net|
|Login|resadmin|
|Password|Kk7zu!iCTza3eX8G|


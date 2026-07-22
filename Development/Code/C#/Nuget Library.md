Nuget Library

Nuget Library

Nuget packages are stored in the project *packages* folder for example:
`c:\Data\DevOps\CSharpProject\packages`
and registered in the 'packages.config'
for example:

```xml
<?xml version="1.0" encoding="utf-8"?>
<packages>
  <package id="FontAwesome.Sharp" version="5.14.1" targetFramework="net472" />
  <package id="IronXL.Excel" version="2020.9.1" targetFramework="net472" />
</packages>
```
* * *
Tools > Nuget Package Manager > Packet Manager Console
* * *
`Install-Package System.Linq -Version 4.3.0`

`Install-Package IronXL.Excel -Version 2020.9.1`

`Install-Package FontAwesome.Sharp -Version 5.14.1`
Icons to use with this package can be found at: [fontawesome.com](https://fontawesome.com/icons?d=gallery&m=free)

`Install-Package Microsoft.Office.Interop.Word -Version 15.0.4797.1003`

to read JSO files
`Install-Package Microsoft.Extensions.Configuration -Version 5.0.0-rc.1.20451.14`
`Install-Package Microsoft.Extensions.Configuration.Json -Version 5.0.0-rc.1.20451.14`

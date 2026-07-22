Add Microsoft Nugetpackeges to the project

Add Microsoft Nugetpackeges to the project
Open the csproj file and add whatever is neccesary

```xml
  <ItemGroup>
    <PackageReference Include="Microsoft.Office.Interop.Excel" Version="15.0.4795.1000" />
    <PackageReference Include="Microsoft.Office.Interop.Outlook" Version="15.0.4797.1003" />
    <PackageReference Include="Microsoft.Office.Interop.PowerPoint" Version="15.0.4420.1017" />
    <PackageReference Include="Microsoft.Office.Interop.Word" Version="15.0.4797.1003" />
  </ItemGroup>
```

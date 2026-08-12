Install nuget: cefsharp WinForms

Install nuget: cefsharp WinForms

Change the *.csproj file

Search the first ``<PropertyGroup>`` tag and add:
```xml
<CefSharpAnyCpuSupport>true</CefSharpAnyCpuSupport>
```

After that edit the App.config file
Edit the ``<configuration>`` tag
```xml
  <runtime>
    <assemblyBinding xmlns="urn:schemas-microsoft.com:asm.v1">
      <probing privatePath="x86"/>
    </assemblyBinding>
  </runtime>
```

In your code add:
```C#
using CefSharp;
using CefSharp.WinForms;
```

Mevor the main() function add:
```C#
public ChromiumWebBrowser chromeBrowser;
```

After the main function  Initialize Chromium, add InitializeChromium(); inside the Main function also
Total code will look like this

```C#
using CefSharp;
using CefSharp.WinForms;

namespace Example
{
    public partial class Main : Form
    {
        public ChromiumWebBrowser chromeBrowser;

        public Main()
        {
            InitializeComponent();
						 InitializeChromium();
        }

        public void InitializeChromium()
        {
            CefSettings settings = new CefSettings();
            // Initialize cef with the provided settings
            Cef.Initialize(settings);
            // Create a browser component
            chromeBrowser = new ChromiumWebBrowser("http://ourcodeworld.com");
            // Add it to the form and fill it to the form window.
            this.Controls.Add(chromeBrowser);
            chromeBrowser.Dock = DockStyle.Fill;
        }
    }
}

```

XML Parsing

# XML Parsing
[TOC]
* * *

## Sample XML File
```XML
<Menus>
	<RootMenu id="STE" name="Stock Enquiry">
		<SubMenu id="ITM" name="Item Enquiry" form="ItemEnquiryForm" />
		<SubMenu id="LOC" name="Location Enquiry" form="LocationEnquiryForm" />
		<SubMenu id="LOT" name="Lot Enquiry" form="LotEnquiryForm" />
		<SubMenu id="PKG" name="Package Enquiry" form="PackageEnquiryForm" />
	</RootMenu>
	<RootMenu id="DIS" name="Dispatch">
		<SubMenu id="PPK" name="Piak and Pack" form="PickAndPackForm" />
			<SubMenu id="PUT" name="2 Steps Putaway" form="PutAwayForm" />
	</RootMenu>
</Menus>
```
## Use an XmlReader to find a specific element and get an attribute value.
```C#
string myXml = "<test><a i=\"1\"/><a i=\"2\"/></a></a></test>";
System.IO.MemoryStream ms = new System.IO.MemoryStream(System.Text.Encoding.UTF8.GetBytes(myXml));
System.Xml.XmlReader xr = System.Xml.XmlReader.Create(ms);

int firstIValue = 0;

while (xr.Read())
{
  if(xr.NodeType == System.Xml.XmlNodeType.Element)
    if (xr.Name == "a")
    {
      firstIValue = Convert.ToInt32(xr["i"]);
      break;
    }
}
```

## Use LINQ
```C#
XElement xelement = XElement.Load(@"C:\Menu.xml");
IEnumerable<XElement> menus = xelement.Elements();
List<string> subMenuList = new List<string>();
foreach (var menu in menus)
{
	if (menu.Attribute("id").Value == "STE")
	{
		foreach (var submenu in menu.Elements())
		{
			subMenuList.Add(submenu.Attribute("name").Value);
		}
	}
}
```

## Use XPath within the Xml DOM
```C#
string name;
XmlDocument xml = new XmlDocument();
xml.Load("theFile.xml"); 
// Or any other method to load your xml data in the XmlDocument.
// For example if your xml data are in a string, use the LoadXml method.
XmlElement elt = xml.SelectSingleNode("//SubMenu[@id='STE']") as XmlElement;
if(elt!=null)
{
  name=elt.GetAttribute("name");  
}
```

### If you need to retrieve a list of elements, you can use the SelectNodes method (it returns an XmlNodeList object). 

```C#
XmlNodeList submenus = xml.SelectNodes("//RootMenu[@id='STE']/SubMenu");
List<string> names = new List<string>();
foreach(XmlNode n in submenus)
{
  if(n is XmlElement)
    names.Add((n as XmlElement).GetAttribute("name"));
}
```

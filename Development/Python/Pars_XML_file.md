Pars_XML_file

## How to parse content of a variable in a xml tag

### Example XML File (items.xml)

```xml
<data>
    <items>
        <item name="item1"></item>
        <item name="item2"></item>
        <item name="item3"></item>
        <item name="item4"></item>
    </items>
</data>
```

### Python code to parse item names

```python
from xml.dom import minidom

xmldoc = minidom.parse('items.xml')

itemlist = xmldoc.getElementsByTagName('item')

print('Number of items : ', len(itemlist))

print('First item value: ', itemlist[0].attributes['name'].value)

for s in itemlist:
    print(s.attributes['name'].value)
```

### Output

> ```
> Number of items : 4
> First item value: item1
> item1
> item2
> item3
> item4
> ```


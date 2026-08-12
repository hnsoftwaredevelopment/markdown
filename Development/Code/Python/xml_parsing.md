xml_parsing

# Python XML with ElementTree: Beginner's Guide

Learn how you can parse, explore, modify and populate XML files with the Python ElementTree package, for loops and XPath expressions.

As a data scientist, you'll find that understanding XML is powerful for both web-scraping and general practice in parsing a structured document.



In this tutorial, you'll cover the following topics:



- You'll learn more about [XML](https://www.datacamp.com/community/tutorials/python-xml-elementtree#intro) and you'll get introduced to the [Python `ElementTree` package](https://www.datacamp.com/community/tutorials/python-xml-elementtree#elementtree).

- Then, you'll discover how you can [explore XML trees](https://www.datacamp.com/community/tutorials/python-xml-elementtree#explore) to understand the data that you're working with better with the help of `ElementTree` functions, for loops and XPath expressions.

- Next, you'll learn how you can [modify an XML file](https://www.datacamp.com/community/tutorials/python-xml-elementtree#modify); And

- You'll utilize

   

  xpath expresssions

   to populate XML files

  

## What is XML?

XML stands for "Extensible Markup Language". It is mainly used in webpages, where the data has a specific structure and is understood dynamically by the XML framework.

XML creates a tree-like structure that is easy to interpret and supports a hierarchy. Whenever a page follows XML, it can be called an XML document.

- XML documents have sections, called *elements*, defined by a beginning and an ending *tag*. A tag is a markup construct that begins with `<` and ends with `>`. The characters between the start-tag and end-tag, if there are any, are the element's content. Elements can contain markup, including other elements, which are called "child elements".
- The largest, top-level element is called the *root*, which contains all other elements.
- Attributes are name–value pair that exist within a start-tag or empty-element tag. An XML attribute can only have a single value and each attribute can appear at most once on each element.

To understand this a little bit better, take a look at the following (shortened) XML file:

```python
<?xml version="1.0"?>
<collection>
    <genre category="Action">
        <decade years="1980s">
            <movie favorite="True" title="Indiana Jones: The raiders of the lost Ark">
                <format multiple="No">DVD</format>
                <year>1981</year>
                <rating>PG</rating>
                <description>
                'Archaeologist and adventurer Indiana Jones 
                is hired by the U.S. government to find the Ark of the 
                Covenant before the Nazis.'
                </description>
            </movie>
               <movie favorite="True" title="THE KARATE KID">
               <format multiple="Yes">DVD,Online</format>
               <year>1984</year>
               <rating>PG</rating>
               <description>None provided.</description>
            </movie>
            <movie favorite="False" title="Back 2 the Future">
               <format multiple="False">Blu-ray</format>
               <year>1985</year>
               <rating>PG</rating>
               <description>Marty McFly</description>
            </movie>
        </decade>
        <decade years="1990s">
            <movie favorite="False" title="X-Men">
               <format multiple="Yes">dvd, digital</format>
               <year>2000</year>
               <rating>PG-13</rating>
               <description>Two mutants come to a private academy for their kind whose resident superhero team must 
               oppose a terrorist organization with similar powers.</description>
            </movie>
            <movie favorite="True" title="Batman Returns">
               <format multiple="No">VHS</format>
               <year>1992</year>
               <rating>PG13</rating>
               <description>NA.</description>
            </movie>
               <movie favorite="False" title="Reservoir Dogs">
               <format multiple="No">Online</format>
               <year>1992</year>
               <rating>R</rating>
               <description>WhAtEvER I Want!!!?!</description>
            </movie>
        </decade>    
    </genre>

    <genre category="Thriller">
        <decade years="1970s">
            <movie favorite="False" title="ALIEN">
                <format multiple="Yes">DVD</format>
                <year>1979</year>
                <rating>R</rating>
                <description>"""""""""</description>
            </movie>
        </decade>
        <decade years="1980s">
            <movie favorite="True" title="Ferris Bueller's Day Off">
                <format multiple="No">DVD</format>
                <year>1986</year>
                <rating>PG13</rating>
                <description>Funny movie about a funny guy</description>
            </movie>
            <movie favorite="FALSE" title="American Psycho">
                <format multiple="No">blue-ray</format>
                <year>2000</year>
                <rating>Unrated</rating>
                <description>psychopathic Bateman</description>
            </movie>
        </decade>
    </genre>
```

From what you have read above, you see that

- `<collection>` is the single root element: it contains all the other elements, such as `<genre>`, or `<movie>`, which are the child elements or subelements. As you can see, these elements are nested.

**Note** that these child elements can also act as parents and contain their own child elements, which are then called "sub-child elements".

- You'll see that, for example, the `<movie>` element contains a couple of "attributes", such as `favorite` `title` that give even more information!

With this short intro to XML files in mind, you're ready to learn more about `ElementTree`!



## Introduction to ElementTree

The XML tree structure makes navigation, modification, and removal relatively simple programmatically. Python has a built in library, `ElementTree`, that has functions to read and manipulate XMLs (and other similarly structured files).

First, import `ElementTree`. It's a common practice to use the alias of `ET`:

```python
import xml.etree.ElementTree as ET
```



## Parsing XML Data

In the XML file provided, there is a basic collection of movies described. The only problem is the data is a mess! There have been a lot of different curators of this collection and everyone has their own way of entering data into the file. The main goal in this tutorial will be to read and understand the file with Python - then fix the problems.

First you need to read in the file with `ElementTree`.

```python
tree = ET.parse('movies.xml')
root = tree.getroot()
```

Now that you have initialized the tree, you should look at the XML and print out values in order to understand how the tree is structured.

Every part of a tree (root included) has a tag that describes the element. In addition, as you have seen in the introduction, elements might have attributes, which are additional descriptors, used especially for repeated tag usage. Attributes also help to validate values entered for that tag, once again contributing to the structured format of an XML.

You'll see later on in this tutorial that attributes can be pretty powerful when included in an XML!

```python
root.tag
'collection'
```

At the top level, you see that this XML is rooted in the `collection` tag.

```python
root.attrib
{}
```

So the root has no attributes.

### For Loops

You can easily iterate over subelements (commonly called "children") in the root by using a simple "for" loop.

```python
for child in root:
    print(child.tag, child.attrib)
genre {'category': 'Action'}
genre {'category': 'Thriller'}
genre {'category': 'Comedy'}
```

Now you know that the children of the root `collection` are all `genre`. To designate the genre, the XML uses the attribute `category`. There are Action, Thriller, and Comedy movies according the `genre` element.

Typically it is helpful to know all the elements in the entire tree. One useful function for doing that is `root.iter()`. You can put this function into a "for" loop and it will iterate over the entire tree.

```python
[elem.tag for elem in root.iter()]
['collection',
 'genre',
 'decade',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'decade',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'genre',
 'decade',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'decade',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'genre',
 'decade',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'decade',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'decade',
 'movie',
 'format',
 'year',
 'rating',
 'description',
 'decade',
 'movie',
 'format',
 'year',
 'rating',
 'description']
```

This gives a general notion for how many elements you have, but it does not show the attributes or levels in the tree.

There is a helpful way to see the whole document. Any element has a `.tostring()` method. If you pass the root into the `.tostring()` method, you can return the whole document. Within `ElementTree` (remember aliased as `ET`), `.tostring()` takes a slightly strange form.

Since `ElementTree` is a powerful library that can interpret more than just XML, you must specify both the encoding and decoding of the document you are displaying as the string. For XMLs, use `'utf8'` - this is the typical document format type for an XML.

```python
print(ET.tostring(root, encoding='utf8').decode('utf8'))
<?xml version='1.0' encoding='utf8'?>
<collection>
    <genre category="Action">
        <decade years="1980s">
            <movie favorite="True" title="Indiana Jones: The raiders of the lost Ark">
                <format multiple="No">DVD</format>
                <year>1981</year>
                <rating>PG</rating>
                <description>
                'Archaeologist and adventurer Indiana Jones 
                is hired by the U.S. government to find the Ark of the 
                Covenant before the Nazis.'
                </description>
            </movie>
               <movie favorite="True" title="THE KARATE KID">
               <format multiple="Yes">DVD,Online</format>
               <year>1984</year>
               <rating>PG</rating>
               <description>None provided.</description>
            </movie>
            <movie favorite="False" title="Back 2 the Future">
               <format multiple="False">Blu-ray</format>
               <year>1985</year>
               <rating>PG</rating>
               <description>Marty McFly</description>
            </movie>
        </decade>
        <decade years="1990s">
            <movie favorite="False" title="X-Men">
               <format multiple="Yes">dvd, digital</format>
               <year>2000</year>
               <rating>PG-13</rating>
               <description>Two mutants come to a private academy for their kind whose resident superhero team must 
               oppose a terrorist organization with similar powers.</description>
            </movie>
            <movie favorite="True" title="Batman Returns">
               <format multiple="No">VHS</format>
               <year>1992</year>
               <rating>PG13</rating>
               <description>NA.</description>
            </movie>
               <movie favorite="False" title="Reservoir Dogs">
               <format multiple="No">Online</format>
               <year>1992</year>
               <rating>R</rating>
               <description>WhAtEvER I Want!!!?!</description>
            </movie>
        </decade>    
    </genre>

    <genre category="Thriller">
        <decade years="1970s">
            <movie favorite="False" title="ALIEN">
                <format multiple="Yes">DVD</format>
                <year>1979</year>
                <rating>R</rating>
                <description>"""""""""</description>
            </movie>
        </decade>
        <decade years="1980s">
            <movie favorite="True" title="Ferris Bueller's Day Off">
                <format multiple="No">DVD</format>
                <year>1986</year>
                <rating>PG13</rating>
                <description>Funny movie about a funny guy</description>
            </movie>
            <movie favorite="FALSE" title="American Psycho">
                <format multiple="No">blue-ray</format>
                <year>2000</year>
                <rating>Unrated</rating>
                <description>psychopathic Bateman</description>
            </movie>
        </decade>
    </genre>

    <genre category="Comedy">
        <decade years="1960s">
            <movie favorite="False" title="Batman: The Movie">
                <format multiple="Yes">DVD,VHS</format>
                <year>1966</year>
                <rating>PG</rating>
                <description>What a joke!</description>
            </movie>
        </decade>
        <decade years="2010s">
            <movie favorite="True" title="Easy A">
                <format multiple="No">DVD</format>
                <year>2010</year>
                <rating>PG--13</rating>
                <description>Emma Stone = Hester Prynne</description>
            </movie>
            <movie favorite="True" title="Dinner for SCHMUCKS">
                <format multiple="Yes">DVD,digital,Netflix</format>
                <year>2011</year>
                <rating>Unrated</rating>
                <description>Tim (Rudd) is a rising executive
                 who “succeeds” in finding the perfect guest, 
                 IRS employee Barry (Carell), for his boss’ monthly event, 
                 a so-called “dinner for idiots,” which offers certain 
                 advantages to the exec who shows up with the biggest buffoon.
                 </description>
            </movie>
        </decade>
        <decade years="1980s">
            <movie favorite="False" title="Ghostbusters">
                <format multiple="No">Online,VHS</format>
                <year>1984</year>
                <rating>PG</rating>
                <description>Who ya gonna call?</description>
            </movie>
        </decade>
        <decade years="1990s">
            <movie favorite="True" title="Robin Hood: Prince of Thieves">
                <format multiple="No">Blu_Ray</format>
                <year>1991</year>
                <rating>Unknown</rating>
                <description>Robin Hood slaying</description>
            </movie>
        </decade>
    </genre>
</collection>
```

You can expand the use of the `iter()` function to help with finding particular elements of interest. `root.iter()` will list all subelements under the root that match the element specified. Here, you will list all attributes of the `movie` element in the tree:

```python
for movie in root.iter('movie'):
    print(movie.attrib)
{'favorite': 'True', 'title': 'Indiana Jones: The raiders of the lost Ark'}
{'favorite': 'True', 'title': 'THE KARATE KID'}
{'favorite': 'False', 'title': 'Back 2 the Future'}
{'favorite': 'False', 'title': 'X-Men'}
{'favorite': 'True', 'title': 'Batman Returns'}
{'favorite': 'False', 'title': 'Reservoir Dogs'}
{'favorite': 'False', 'title': 'ALIEN'}
{'favorite': 'True', 'title': "Ferris Bueller's Day Off"}
{'favorite': 'FALSE', 'title': 'American Psycho'}
{'favorite': 'False', 'title': 'Batman: The Movie'}
{'favorite': 'True', 'title': 'Easy A'}
{'favorite': 'True', 'title': 'Dinner for SCHMUCKS'}
{'favorite': 'False', 'title': 'Ghostbusters'}
{'favorite': 'True', 'title': 'Robin Hood: Prince of Thieves'}
```

You can already see how the `movies` have been entered in different ways. Don't worry about that for now, you'll get a chance to fix one of the errors later on in this tutorial.



### XPath Expressions

Many times elements will not have attributes, they will only have text content. Using the attribute `.text`, you can print out this content.

Now, print out all the descriptions of the movies.

```python
for description in root.iter('description'):
    print(description.text)
                'Archaeologist and adventurer Indiana Jones 
                is hired by the U.S. government to find the Ark of the 
                Covenant before the Nazis.'

None provided.
Marty McFly
Two mutants come to a private academy for their kind whose resident superhero team must 
               oppose a terrorist organization with similar powers.
NA.
WhAtEvER I Want!!!?!
"""""""""
Funny movie about a funny guy
psychopathic Bateman
What a joke!
Emma Stone = Hester Prynne
Tim (Rudd) is a rising executive
                 who “succeeds” in finding the perfect guest, 
                 IRS employee Barry (Carell), for his boss’ monthly event, 
                 a so-called “dinner for idiots,” which offers certain 
                 advantages to the exec who shows up with the biggest buffoon.

Who ya gonna call?
Robin Hood slaying
```

Printing out the XML is helpful, but XPath is a query language used to search through an XML quickly and easily. XPath stands for XML Path Language and uses, as the name suggests, a "path like" syntax to identify and navigate nodes in an XML document.

Understanding XPath is critically important to scanning and populating XMLs. `ElementTree` has a `.findall()` function that will traverse the immediate children of the referenced element. You can use XPath expressions to specify more useful searches.

Here, you will search the tree for movies that came out in 1992:

```python
for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)
{'favorite': 'True', 'title': 'Batman Returns'}
{'favorite': 'False', 'title': 'Reservoir Dogs'}
```

The function `.findall()` always begins at the element specified. This type of function is extremely powerful for a "find and replace". You can even search on attributes!

Now, print out only the movies that are available in multiple formats (an attribute).

```python
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(movie.attrib)
{'multiple': 'Yes'}
{'multiple': 'Yes'}
{'multiple': 'Yes'}
{'multiple': 'Yes'}
{'multiple': 'Yes'}
```

Brainstorm why, in this case, the print statement returns the "Yes" values of `multiple`. Think about how the "for" loop is defined. Could you rewrite this loop to print out the movie titles instead? Try it below:

**Tip**: use `'...'` inside of XPath to return the parent element of the current element.

```python
for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):
    print(movie.attrib)
{'favorite': 'True', 'title': 'THE KARATE KID'}
{'favorite': 'False', 'title': 'X-Men'}
{'favorite': 'False', 'title': 'ALIEN'}
{'favorite': 'False', 'title': 'Batman: The Movie'}
{'favorite': 'True', 'title': 'Dinner for SCHMUCKS'}
```



## Modifying an XML

Earlier, the movie titles were an absolute mess. Now, print them out again:

```python
for movie in root.iter('movie'):
    print(movie.attrib)
{'favorite': 'True', 'title': 'Indiana Jones: The raiders of the lost Ark'}
{'favorite': 'True', 'title': 'THE KARATE KID'}
{'favorite': 'False', 'title': 'Back 2 the Future'}
{'favorite': 'False', 'title': 'X-Men'}
{'favorite': 'True', 'title': 'Batman Returns'}
{'favorite': 'False', 'title': 'Reservoir Dogs'}
{'favorite': 'False', 'title': 'ALIEN'}
{'favorite': 'True', 'title': "Ferris Bueller's Day Off"}
{'favorite': 'FALSE', 'title': 'American Psycho'}
{'favorite': 'False', 'title': 'Batman: The Movie'}
{'favorite': 'True', 'title': 'Easy A'}
{'favorite': 'True', 'title': 'Dinner for SCHMUCKS'}
{'favorite': 'False', 'title': 'Ghostbusters'}
{'favorite': 'True', 'title': 'Robin Hood: Prince of Thieves'}
```

Fix the '2' in Back 2 the Future. That should be a find and replace problem. Write code to find the title 'Back 2 the Future' and save it as a variable:

```python
b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
print(b2tf)
<Element 'movie' at 0x10ce00ef8>
```

Notice that using the `.find()` method returns an element of the tree. Much of the time, it is more useful to edit the content within an element.

Modify the `title` attribute of the Back 2 the Future element variable to read "Back to the Future". Then, print out the attributes of your variable to see your change. You can easily do this by accessing the attribute of an element and then assigning a new value to it:

```python
b2tf.attrib["title"] = "Back to the Future"
print(b2tf.attrib)
{'favorite': 'False', 'title': 'Back to the Future'}
```

Write out your changes back to the XML so they are permanently fixed in the document. Print out your movie attributes again to make sure your changes worked. Use the `.write()` method to do this:

```python
tree.write("movies.xml")

tree = ET.parse('movies.xml')
root = tree.getroot()

for movie in root.iter('movie'):
    print(movie.attrib)
{'favorite': 'True', 'title': 'Indiana Jones: The raiders of the lost Ark'}
{'favorite': 'True', 'title': 'THE KARATE KID'}
{'favorite': 'False', 'title': 'Back to the Future'}
{'favorite': 'False', 'title': 'X-Men'}
{'favorite': 'True', 'title': 'Batman Returns'}
{'favorite': 'False', 'title': 'Reservoir Dogs'}
{'favorite': 'False', 'title': 'ALIEN'}
{'favorite': 'True', 'title': "Ferris Bueller's Day Off"}
{'favorite': 'FALSE', 'title': 'American Psycho'}
{'favorite': 'False', 'title': 'Batman: The Movie'}
{'favorite': 'True', 'title': 'Easy A'}
{'favorite': 'True', 'title': 'Dinner for SCHMUCKS'}
{'favorite': 'False', 'title': 'Ghostbusters'}
{'favorite': 'True', 'title': 'Robin Hood: Prince of Thieves'}
```

## Fixing Attributes

The `multiple` attribute is incorrect in some places. Use `ElementTree` to fix the designator based on how many formats the movie comes in. First, print the `format` attribute and text to see which parts need to be fixed.

```python
for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)
{'multiple': 'No'} DVD
{'multiple': 'Yes'} DVD,Online
{'multiple': 'False'} Blu-ray
{'multiple': 'Yes'} dvd, digital
{'multiple': 'No'} VHS
{'multiple': 'No'} Online
{'multiple': 'Yes'} DVD
{'multiple': 'No'} DVD
{'multiple': 'No'} blue-ray
{'multiple': 'Yes'} DVD,VHS
{'multiple': 'No'} DVD
{'multiple': 'Yes'} DVD,digital,Netflix
{'multiple': 'No'} Online,VHS
{'multiple': 'No'} Blu_Ray
```

There is some work that needs to be done on this tag.

You can use regex to find commas - that will tell whether the `multiple` attribute should be "Yes" or "No". Adding and modifying attributes can be done easily with the `.set()` method.

**Note**: `re` is the standard regex interpreter for Python. If you want to know more about regular expressions, consider [this tutorial](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial).

```python
import re

for form in root.findall("./genre/decade/movie/format"):
    # Search for the commas in the format text
    match = re.search(',',form.text)
    if match:
        form.set('multiple','Yes')
    else:
        form.set('multiple','No')

# Write out the tree to the file again
tree.write("movies.xml")

tree = ET.parse('movies.xml')
root = tree.getroot()

for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)
{'multiple': 'No'} DVD
{'multiple': 'Yes'} DVD,Online
{'multiple': 'No'} Blu-ray
{'multiple': 'Yes'} dvd, digital
{'multiple': 'No'} VHS
{'multiple': 'No'} Online
{'multiple': 'No'} DVD
{'multiple': 'No'} DVD
{'multiple': 'No'} blue-ray
{'multiple': 'Yes'} DVD,VHS
{'multiple': 'No'} DVD
{'multiple': 'Yes'} DVD,digital,Netflix
{'multiple': 'Yes'} Online,VHS
{'multiple': 'No'} Blu_Ray
```

## Moving Elements

Some of the data has been placed in the wrong decade. Use what you have learned about XML and `ElementTree` to find and fix the decade data errors.

It will be useful to print out both the `decade` tags and the `year` tags throughout the document.

```python
for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text, '\n')
{'years': '1980s'}
1981 

1984 

1985 

{'years': '1990s'}
2000 

1992 

1992 

{'years': '1970s'}
1979 

{'years': '1980s'}
1986 

2000 

{'years': '1960s'}
1966 

{'years': '2010s'}
2010 

2011 

{'years': '1980s'}
1984 

{'years': '1990s'}
1991 
```

The two years that are in the wrong decade are the movies from the 2000s. Figure out what those movies are, using an XPath expression.

```python
for movie in root.findall("./genre/decade/movie/[year='2000']"):
    print(movie.attrib)
{'favorite': 'False', 'title': 'X-Men'}
{'favorite': 'FALSE', 'title': 'American Psycho'}
```

You have to add a new decade tag, the 2000s, to the Action genre in order to move the X-Men data. The `.SubElement()` method can be used to add this tag to the end of the XML.

```python
action = root.find("./genre[@category='Action']")
new_dec = ET.SubElement(action, 'decade')
new_dec.attrib["years"] = '2000s'

print(ET.tostring(action, encoding='utf8').decode('utf8'))
<?xml version='1.0' encoding='utf8'?>
<genre category="Action">
        <decade years="1980s">
            <movie favorite="True" title="Indiana Jones: The raiders of the lost Ark">
                <format multiple="No">DVD</format>
                <year>1981</year>
                <rating>PG</rating>
                <description>
                'Archaeologist and adventurer Indiana Jones 
                is hired by the U.S. government to find the Ark of the 
                Covenant before the Nazis.'
                </description>
            </movie>
               <movie favorite="True" title="THE KARATE KID">
               <format multiple="Yes">DVD,Online</format>
               <year>1984</year>
               <rating>PG</rating>
               <description>None provided.</description>
            </movie>
            <movie favorite="False" title="Back to the Future">
               <format multiple="No">Blu-ray</format>
               <year>1985</year>
               <rating>PG</rating>
               <description>Marty McFly</description>
            </movie>
        </decade>
        <decade years="1990s">
            <movie favorite="False" title="X-Men">
               <format multiple="Yes">dvd, digital</format>
               <year>2000</year>
               <rating>PG-13</rating>
               <description>Two mutants come to a private academy for their kind whose resident superhero team must 
               oppose a terrorist organization with similar powers.</description>
            </movie>
            <movie favorite="True" title="Batman Returns">
               <format multiple="No">VHS</format>
               <year>1992</year>
               <rating>PG13</rating>
               <description>NA.</description>
            </movie>
               <movie favorite="False" title="Reservoir Dogs">
               <format multiple="No">Online</format>
               <year>1992</year>
               <rating>R</rating>
               <description>WhAtEvER I Want!!!?!</description>
            </movie>
        </decade>    
    <decade years="2000s" /></genre>
```

Now append the X-Men movie to the 2000s and remove it from the 1990s, using `.append()` and `.remove()`, respectively.

```python
xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(xmen)

print(ET.tostring(action, encoding='utf8').decode('utf8'))
<?xml version='1.0' encoding='utf8'?>
<genre category="Action">
        <decade years="1980s">
            <movie favorite="True" title="Indiana Jones: The raiders of the lost Ark">
                <format multiple="No">DVD</format>
                <year>1981</year>
                <rating>PG</rating>
                <description>
                'Archaeologist and adventurer Indiana Jones 
                is hired by the U.S. government to find the Ark of the 
                Covenant before the Nazis.'
                </description>
            </movie>
               <movie favorite="True" title="THE KARATE KID">
               <format multiple="Yes">DVD,Online</format>
               <year>1984</year>
               <rating>PG</rating>
               <description>None provided.</description>
            </movie>
            <movie favorite="False" title="Back to the Future">
               <format multiple="No">Blu-ray</format>
               <year>1985</year>
               <rating>PG</rating>
               <description>Marty McFly</description>
            </movie>
        </decade>
        <decade years="1990s">
            <movie favorite="True" title="Batman Returns">
               <format multiple="No">VHS</format>
               <year>1992</year>
               <rating>PG13</rating>
               <description>NA.</description>
            </movie>
               <movie favorite="False" title="Reservoir Dogs">
               <format multiple="No">Online</format>
               <year>1992</year>
               <rating>R</rating>
               <description>WhAtEvER I Want!!!?!</description>
            </movie>
        </decade>    
    <decade years="2000s"><movie favorite="False" title="X-Men">
               <format multiple="Yes">dvd, digital</format>
               <year>2000</year>
               <rating>PG-13</rating>
               <description>Two mutants come to a private academy for their kind whose resident superhero team must 
               oppose a terrorist organization with similar powers.</description>
            </movie>
            </decade></genre>
```

## Build XML Documents

Nice, so you were able to essentially move an entire movie to a new decade. Save your changes back to the XML.

```python
tree.write("movies.xml")

tree = ET.parse('movies.xml')
root = tree.getroot()

print(ET.tostring(root, encoding='utf8').decode('utf8'))
<?xml version='1.0' encoding='utf8'?>
<collection>
    <genre category="Action">
        <decade years="1980s">
            <movie favorite="True" title="Indiana Jones: The raiders of the lost Ark">
                <format multiple="No">DVD</format>
                <year>1981</year>
                <rating>PG</rating>
                <description>
                'Archaeologist and adventurer Indiana Jones 
                is hired by the U.S. government to find the Ark of the 
                Covenant before the Nazis.'
                </description>
            </movie>
               <movie favorite="True" title="THE KARATE KID">
               <format multiple="Yes">DVD,Online</format>
               <year>1984</year>
               <rating>PG</rating>
               <description>None provided.</description>
            </movie>
            <movie favorite="False" title="Back to the Future">
               <format multiple="No">Blu-ray</format>
               <year>1985</year>
               <rating>PG</rating>
               <description>Marty McFly</description>
            </movie>
        </decade>
        <decade years="1990s">
            <movie favorite="True" title="Batman Returns">
               <format multiple="No">VHS</format>
               <year>1992</year>
               <rating>PG13</rating>
               <description>NA.</description>
            </movie>
               <movie favorite="False" title="Reservoir Dogs">
               <format multiple="No">Online</format>
               <year>1992</year>
               <rating>R</rating>
               <description>WhAtEvER I Want!!!?!</description>
            </movie>
        </decade>    
    <decade years="2000s"><movie favorite="False" title="X-Men">
               <format multiple="Yes">dvd, digital</format>
               <year>2000</year>
               <rating>PG-13</rating>
               <description>Two mutants come to a private academy for their kind whose resident superhero team must 
               oppose a terrorist organization with similar powers.</description>
            </movie>
            </decade></genre>

    <genre category="Thriller">
        <decade years="1970s">
            <movie favorite="False" title="ALIEN">
                <format multiple="No">DVD</format>
                <year>1979</year>
                <rating>R</rating>
                <description>"""""""""</description>
            </movie>
        </decade>
        <decade years="1980s">
            <movie favorite="True" title="Ferris Bueller's Day Off">
                <format multiple="No">DVD</format>
                <year>1986</year>
                <rating>PG13</rating>
                <description>Funny movie about a funny guy</description>
            </movie>
            <movie favorite="FALSE" title="American Psycho">
                <format multiple="No">blue-ray</format>
                <year>2000</year>
                <rating>Unrated</rating>
                <description>psychopathic Bateman</description>
            </movie>
        </decade>
    </genre>

    <genre category="Comedy">
        <decade years="1960s">
            <movie favorite="False" title="Batman: The Movie">
                <format multiple="Yes">DVD,VHS</format>
                <year>1966</year>
                <rating>PG</rating>
                <description>What a joke!</description>
            </movie>
        </decade>
        <decade years="2010s">
            <movie favorite="True" title="Easy A">
                <format multiple="No">DVD</format>
                <year>2010</year>
                <rating>PG--13</rating>
                <description>Emma Stone = Hester Prynne</description>
            </movie>
            <movie favorite="True" title="Dinner for SCHMUCKS">
                <format multiple="Yes">DVD,digital,Netflix</format>
                <year>2011</year>
                <rating>Unrated</rating>
                <description>Tim (Rudd) is a rising executive
                 who “succeeds” in finding the perfect guest, 
                 IRS employee Barry (Carell), for his boss’ monthly event, 
                 a so-called “dinner for idiots,” which offers certain 
                 advantages to the exec who shows up with the biggest buffoon.
                 </description>
            </movie>
        </decade>
        <decade years="1980s">
            <movie favorite="False" title="Ghostbusters">
                <format multiple="Yes">Online,VHS</format>
                <year>1984</year>
                <rating>PG</rating>
                <description>Who ya gonna call?</description>
            </movie>
        </decade>
        <decade years="1990s">
            <movie favorite="True" title="Robin Hood: Prince of Thieves">
                <format multiple="No">Blu_Ray</format>
                <year>1991</year>
                <rating>Unknown</rating>
                <description>Robin Hood slaying</description>
            </movie>
        </decade>
    </genre>
</collection>
```

## Conclusion

There are some key things to remember about XMLs and using `ElementTree`.

Tags build the tree structure and designate what values should be delineated there. Using smart structuring can make it easy to read and write to an XML. Tags always need opening and closing brackets to show the parent and children relationships.

Attributes further describe how to validate a tag or allow for boolean designations. Attributes typically take very specific values so that the XML parser (and the user) can use the attributes to check the tag values.

`ElementTree` is an important Python library that allows you to parse and navigate an XML document. Using `ElementTree` breaks down the XML document in a tree structure that is easy to work with. When in doubt, print it out (`print(ET.tostring(root, encoding='utf8').decode('utf8'))`) - use this helpful print statement to view the entire XML document at once. It helps to check when editing, adding, or removing from an XML.

Now you are equipped to understand XML and begin parsing!

*References:*

- <https://docs.python.org/3.5/library/xml.etree.elementtree.html>
- <https://en.wikipedia.org/wiki/XML>
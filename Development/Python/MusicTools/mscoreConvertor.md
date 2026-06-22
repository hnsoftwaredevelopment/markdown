mscoreConvertor

```python
import os


def list_files(startpath, extention):
    for root, dirs, files in os.walk(startpath):
        #print(os.path.basename(root))
        for f in files:
            if f[-4:] == extention:
                print(f)


def list_tree(startpath):
    for root, dirs, files in os.walk(startpath):
        print(os.path.abspath(root))


pathApp2 = "C:\\Program Files (x86)\\MuseScore 2\\bin\\musescore.exe"
pathApp3 = "C:\\Program Files\\MuseScore 3\\bin\\musescore3.exe"
pathScore2 = "C:\\Data\\Stack\\Partituren"
pathScore3 = "C:\\Data\\Stack\\3.0\\Partituren"
pathExport2 = "C:\\Data\\Stack\\Partituren\\Export"
pathExport3 = "C:\\Data\\Stack\\Partituren\\Export"
PathExpType1 = "\\PDF"
PathExpType2 = "\\MP3"
PathExpType3 = "\\MXL"
PathExpType4 = "\\MusicXML"

print(pathScore2 + "\\*.mscz")

list_files(pathScore2, "mscz")
#list_tree(pathScore2)
```

Structuren



A score has a name, containing a score number, title and additional type info this number is the key value

| Key  | MuseScore File | PDF File    | Audio File  | MusicXML      |
| ---- | -------------- | ----------- | ----------- | ------------- |
|      | Type\|Title    | Type\|Title | Type\|Title | MXL\|MusicXML |


```base
filters:
  and:
    - file.path.startsWith("Development/C#/WPF")
    - file.name != "WPF"
properties:
  file.name:
    displayName: Document
  note.tags:
    displayName: Tags
views:
  - type: table
    name: Table
    order:
      - file.name
      - tags
      - file.ctime
    sort:
      - property: file.name
        direction: DESC
    columnSize:
      file.name: 317

```

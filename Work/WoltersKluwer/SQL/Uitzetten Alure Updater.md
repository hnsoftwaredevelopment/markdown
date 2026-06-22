Uitzetten Alure Updater

# Switch on/of Alure updater

## Show all Alure Updater related settings
```SQL
Select * from INSTELLING Where rubriek ='AutoUpdate' AND sleutel = 'updatesAutomatischUitvoeren'
```

## Switch off the auto updater

```SQL
UPDATE INSTELLING SET waarde = 'False' Where rubriek ='AutoUpdate' AND sleutel = 'updatesAutomatischUitvoeren' 
```

## To switch it back on:
```SQL
UPDATE INSTELLING SET waarde = 'True' Where rubriek ='AutoUpdate' AND sleutel = 'updatesAutomatischUitvoeren' 
```

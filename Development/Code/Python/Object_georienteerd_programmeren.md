Object_georienteerd_programmeren

# Programmeren in Python/Object-georiënteerd programmeren

[TOC]

## Object Georiënteerd Programmeren

OGP (Engels: Object Oriented Programming of OOP) is een programmeerstijl (of paradigma, een wijze van werken) waarbij logische objecten gemaakt worden welke methodes (functies, acties of gebeurtenissen) en eigenschappen (waarden) bevatten. De bedoeling is dat dit leidt tot meer leesbare en herbruikbare code. Conceptueel bestaat een programma uit objecten die aangemaakt worden en met elkaar interacteren.
Indien we een programma schrijven waarin we een aantal wagens moeten kunnen beheren, dan kunnen we een auto als een object binnen deze software beschouwen. Elke auto heeft een aantal eigenschappen zoals een kleur, aantal kilometers en een topsnelheid. Maar een auto heeft ook een aantal opties zoals remmen, versnellen en draaien. In plaats van elke auto van een aparte code te voorzien zullen we een klasse Car gebruiken welke deze standaard mogelijkheden zal vastleggen.

## Aanmaken van een klasse

Een voorbeeld van een eenvoudige implementatie van de klasse Car kan er als volgt uitzien:

```python
class car:
    def brake(self):
        print("Remmen")
	def accelerate(self):
        print("Gas geven")
```



Het keyword class gaat de definitie van een klasse vooraf, dit is gevolgd door de naam van de klasse, 'car' in dit geval. Vervolgens bevat deze klasse twee lidfuncties namelijk brake en accelerate. Bemerk dat de eerste parameter van een lidfunctie steeds self is, dit is een verwijzing naar het object zelf. Vervolgens kan de klasse op de volgende manier gebruikt worden:

```python
car1 = car()
car2 = car()
car1.brake()
car2.accelerate()
```



Hier worden twee verschillende instanties (objecten) van de car klasse aangemaakt, vervolgens wordt op het eerste object de methode brake() opgeroepen en op de tweede de methode accelerate().

## Attributen

Op dit punt is er op data niveau geen onderscheid mogelijk tussen de twee objecten, dit is omdat er geen private data gekoppeld is aan de objecten. Wanneer er echter attributen (properties) toegevoegd worden kunnen deze gebruikt worden om onderscheid te maken tussen objecten. Men kan een eigenschap (dit valt te beschouwen als een variabele gekoppeld aan het object) als volgt zetten en opvragen:

```python
car1 = car()
car2 = car()
car1.color="Red"
car2.color="Blue"
print(car1.color)
print(car2.color)
```



Wanneer het attribuut echter niet gezet is resulteert dit in een fout:

```python
car3 = car()
print(car3.color)
>>> Traceback (most recent call last):
>>> File "<stdin>", line 1, in <module>
>>> AttributeError: car instance has no attribute 'color'
```



Juist omwille van deze reden is het een goede vuistregel om toegang tot attributen te doen via lidfuncties. Dit zijn de bekende get en set functies om attributen op te vragen en te wijzigen. Wanneer de car uitgebreid wordt met de naam van de eigenaar zit dit er als volgt uit:


​    

```python
class car:
    ... previous methods ...

	def set_owner(self,Owners_Name):
    	""" This will set the owner property """
    	self._owner = Owners_Name
	def get_owner(self): 
        """ This will retrieve the owner property """
        return self._owner 
```


Merk op dat de naam van het attribuut start met een underscore (_), op deze manier wordt de naam van het attribuut verborgen voor gebruikers.

## Een klasse uitbreiden

Wanneer extra functionaliteit aan een klasse toegevoegd dient te worden, of wanneer men een iets meer specifieke implementatie van een bestaande klasse wenst te gebruiken, dan gaat men vaak gebruik maken van overerving. Dit heeft als extra voordeel dat de bestaande klasse niet gewijzigd zal worden. Wanneer een klasse afgeleid wordt van een bestaande klasse, dan zal deze alle bestaande lidfuncties overerven. In het voorbeeld van de car klasse kunnen we deze uitbreiden tot een truck klasse welke mogelijkheden biedt om te laden en te lossen. In code ziet dit er als volgt uit:

```
class truck(car):
	def load(self):
		print("Laden van de truck")
	def unload(self):
		print("Lossen van de truck")
```

Indien nu een truck object aangemaakt wordt zal deze kunnen remmen, versnellen, geladen worden en gelost worden, het is zelfs mogelijk om een dezelfde lidfunctie te overschrijven (overriden), op deze manier kan een lidfunctie een andere functionaliteit implementeren. In dit geval kan mijn bijvoorbeeld een klasse dier implementeren met een lidfunctie spreek welke het geluid print welke het dier maakt, indien men dan aparte dieren gaat afleiden (bijvoorbeeld een hond, een kat) kan met de spreek lidfunctie per diersoort gaan aanpassen.

## Speciale lidfuncties

Een constructor is een lidfunctie die opgeroepen wordt wanneer een object aangemaakt wordt, deze wordt typisch gebruikt om de attributen te initialiseren op de juiste standaardwaarden. In Python noemt de constructor __init__, de constructor kan eveneens argumenten krijgen. Het volgende voorbeeld toont de constructor van een car object waar bepaalde eigenschappen als parameter gezet worden:

```python
class new_car(car):
	def __init__(self,brand, model, year):
        # Sets all the properties
        self.brand = brand
        self.model = model
        self.year = year
	def start_car(self):
		''' Start the cars engine '''
		print("vroem vroem")
	if __name__ == "__main__":
		# Creates two instances of new_car, each with unique properties
        car1 = new_car("Ford","F-150",2001)
        car2 = new_car("Toyota","Corolla",2007)
        car1.start_car()
        car2.start_car()
```

Van <https://nl.wikibooks.org/wiki/Programmeren_in_Python/Object-geori%C3%ABnteerd_programmeren> 
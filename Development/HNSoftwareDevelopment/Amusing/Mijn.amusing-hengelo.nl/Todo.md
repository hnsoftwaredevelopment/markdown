Samen met Pauline hebben we gekeken naar dev.mijn-amusing-hengelo.nl een aantal opmerkingen gemaakt die nog verwerkt moeten worden .
* **Mijn - Inschrijfbevestiging**
	  * Deze bevat de {Notamelding} . Deze ziet er in het mail voorbeeld als volgt uit:
		 "De nota voor deze inschrijving is separaat verstuurd naar de penningmeester."
		 Hier zou tussen haakjes het e-mail adres van de penningmeester worden toegevoegd: "De nota voor deze inschrijving is separaat verstuurd naar de penningmeester (penningmeester@koor.nl)."
	* Daarnaast is geeft Notamelding} een lange oncontroleerbare tekst voor de  eindgebruiker. ik zou liever zelf controle hebben over de tekst en alleen rol en e-mail als variabelen opnemen, dat zou er als volgt uitzien:
	  "De nota voor deze inschrijving is separaat verstuurd naar {RolNotaOntvanger} ({MailNotaOntvanger})."
*  **Mijn - Inschrijfbevestiging organisatie**
	*  Deze mail sjabloon ontbreekt nog in dev.beheer en moet nog worden gemaakt zodat ook deze tekst aan te passen is
	*  De tekst ziet er nu als volgt uit:
	  "Hallo Amusing-Hengelo organisatie,  
	  
	  Zojuist heeft {Groepsnaam} zich ingeschreven voor het komende festival.  
	  
	  Met {Aantal zangers} deelnemers en ze willen gebruik maken van podiumtype {Podiumtype}. 
	  
	  Bevestigingsmail is verstuurd naar: {MailBevestigingOntvanger}  (RolBevestigingNotvanger)  
	  
	  Nota is verstuurd naar: {MailNotaOntvanger}  ({RolNotaNotvanger}) .
	  
	  Groeten,  
	  Korenfestival Amusing Hengelo"
	  
	  Deze regel: "Met 15 deelnemers en ze willen gebruik maken van podiumtype C. " moet worden opgesplitst in 2 regels:
	  "Aantal deelnemers: {Aantal zangers}
	  Podiumtype {Podiumtype}"
* Mijn - Mail met deelnamenota
	*  Deze mail sjabloon ontbreekt nog in dev.beheer en moet nog worden gemaakt zodat ook deze tekst aan te passen is
	* De tekst ziet er nu als volgt uit: 
	  "Hallo,  
	  
	  Hierbij ontvangt u de deelnamenota voor {Koornaam} voor het Korenfestival Amusing Hengelo {Editie}.  
	  De totale deelnamekosten bedragen € {TotaalbedragNota} . De specificatie en betaalgegevens staan in de PDF in de bijlage.
	  
	  Met vriendelijke groeten,  
	  Korenfestival Amusing Hengelo"
	  
	  De volledige naam van de penningmeester/contact 1 moet worden getoond als diegene waarnaar de nota naartoe is gestuurd. Dus:
	  "Hallo {VolledigenaamNotaOntvanger}"
	  
	  De eerste regel in het bericht moet worden: "Hierbij ontvangt u de factuur voor de deelnamekosten voor {Koornaam} voor het Korenfestival Amusing Hengelo {Editie}."
	  
	  Daarnaast moet voor de ondertekening een regel over de betalingstermijn worden toegevoegd:
	  "De termijn voor de betaling van de totale deelnamekosten is 6 weken na datum inschrijving ({Datum inschrijving}) en voor {EindeInschrijvingFestival}"  
* Mijn - Deelname nota
	*  Dit is welliswaar geen mail sjabloon maar een sjabloon voor de bijlage, toch zou het handig zijn dat ok deze te beheren is in beheer, maar ontbreekt nog in dev.beheer en moet nog worden gemaakt zodat ook deze tekst aan te passen is
	* De tekst van de nota is goed, maar ook daar moet nog wel de regel met de betaaltermijn worden genoemd
	  "De termijn voor de betaling van de totale deelnamekosten is 6 weken na datum inschrijving ({Datum inschrijving}) en voor {EindeInschrijvingFestival}"
	
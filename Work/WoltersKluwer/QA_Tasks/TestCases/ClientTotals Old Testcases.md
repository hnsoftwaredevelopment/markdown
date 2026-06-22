ClientTotals Old Testcases

ClientTotals Old Testcases
Subject: Test suite: Cliënttotalen (Suite ID: 16706)

Test suite 16706: Cliënttotalen
Properties 
________________________________________
State: 	In Progress
Type: 	Static Suite
Configurations: 	Windows 7 and IE 8
Test cases (6) 
________________________________________
Test case 12911: VPA - Berekeningen overzicht cliënttotalen - VPA en toch gedeclareerd
SUMMARY 
De data beschreven in de attachment is afkomstig van de user story mbt berekende velden op de cliëntkaart. Deze is hier hergebruikt.

STEPS
# 	Action 	Expected value 	Attachments 
1	Voeg de testdata uit de bijlage toe aan de masterdatabase	-	
2	Genereer 3 termijnfacturen voor Eislander (2014-1,2 en 3)	-	
3	Genereer 1 termijnfactuur voor Gaardenbeek (2014-1)	-	
4	Ga naar Factureren, Definitieve facturen en factureer de eerste 2 termijnfacturen van Eislander en die van Gaardenbeek	3 termijnfacturen gegenereerd	
5	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
6	Haal selectie op met Jaar = 2014, Periode = 1 en verder de default instellingen	Lijst wordt getoond	
7	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 800,00 Concept = 0,00 Gefactureerd = 800,00 OHW mutaties = 0,00	
8	Maak de weekstaten van Huysman definitief	-	
9	Fiatteer de weekstaten van Huysman	-	
10	Verwerk vervolgens de mutaties van periode 2014-1 t/m periode 2014-1 via 'Verwerking mutaties'	18 mutaties verwerkt	
11	Ga naar Declareren per client en selecteer Eislander	-	
12	Kies voor 'Samenstellen declaratie'	-	
13	Voeg via het tabblad OHW de boeking voor kostensoort 7 toe aan de declaratie	Kostensoort 7 is onderdeel van de VPA definitie dus daarom niet meegenomen in de declaratie	
14	Ga naar Factureren, Definitieve facturen en factureer de zojuist aangemaakt declaratie (in periode 2014-1!)	Factuur wordt gegenereerd	
15	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
16	Haal selectie op met Jaar = 2014, Periode = 1 en verder de default instellingen	Lijst wordt getoond	
17	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 2285,75 (Volgens de definitie valt kostensoort 7 onder VPA maar het bedrag is toch gedeclareerd, het wordt daarom meegenomen als meerwerk) Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 3085,75 Concept = 0,00 Gefactureerd = 3085,75 OHW mutaties = 0,00	
18	Controleer berekende velden voor Gaardenbeek	OHW begin = 0,00 Omzet = 1504.50 Bijgeboekt = 0,00 Afgeboekt = 0,00 OHW mutaties = 1204,50	
19	Haal selectie op met Jaar = 2014, Periode = 1 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
20	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3894,25 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 3085,75 Concept = 0,00 Gefactureerd = 3085,75 OHW mutaties = 808,50	
LINKS 
ID 	WorkItemType 	Link type 	Title 
12628
User Story	Tests	VPA – overzicht Cliënttotalen – aanpassen berekeningen
12700
Test Case	Related	Uren - Cliëntkaart - Berekende velden VPA
12838
Test Case	Related	VPA - Berekeningen overzicht cliënttotalen OHW begin / OHW mutaties / Omzet
13167
Test Case	Related	VPA - Calculations Liquidityreport
18904
Task	Tests	Regressietest Uren 2
20244
Task	Shared Steps	Cliënttotalen
12900
Test Case	Related	VPA - Berekeningen overzicht cliënttotalen Afgeboekt / Bijgeboekt / Overgeboekt
ATTACHMENTS 
Name 	Size 	Date Attached 	Comments 
BerekendeVeldenVPAClientkaart.docx
495kb	Thu Apr 10 2014	
LATEST TEST OUTCOME
Outcome	Tester	Configuration	Run by	Date completed	Duration in seconds	Build number
None
Herbert Nijkamp - Wolters Kluwer 	Windows 7 and IE 8	Herbert Nijkamp - Wolters Kluwer 	Thursday, March 22, 2018	0	
Test case 12900: VPA - Berekeningen overzicht cliënttotalen Afgeboekt / Bijgeboekt / Overgeboekt
SUMMARY 
De data beschreven in de attachment is afkomstig van de user story mbt berekende velden op de cliëntkaart. Deze is hier hergebruikt.
Testcase bij voorkeur uitvoeren aansluitend op of in combinatie met op 12838.

STEPS
# 	Action 	Expected value 	Attachments 
1	Uitgangsituatie	G:\03 Development\5. Projecten\Plan van Aanpak - Testing\20 Applicatiepaden\DB Applicatiepad 17. Testen vanaf stap 39.	
2	Voeg de testdata uit 1 bijlage toe aan de masterdatabase , document BerekendeVeldenVPAClientkaart	-	
3	Genereer 3 termijnfacturen voor Eislander (2014-1,2 en 3)	-	
4	Genereer 2 termijnfacturen voor Gaardenbeek (2014-1 en 2014-2)	-	
5	Ga naar Factureren, Definitieve facturen en factureer de eerste 2 termijnfacturen van Eislander en de eerste van Gaardenbeek	3 termijnfacturen gegenereerd	
6	Ga naar Declareren per cliënt en vraag de lijst op met de optie 'VPA-termijnfacturen tonen' aangevinkt	Lijst wordt getoond	
7	Selecteer de termijnfactuur van Eislander en kies voor 'Invoeren declaratiecorrecties'	Voer de declaratiecorrecties in zoals beschreven in attachment	
8	Selecteer de termijnfactuur van Gaardenbeek en kies voor 'Invoeren declaratiecorrecties'	Voer de declaratiecorrecties in zoals beschreven in attachment	
9	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
10	Haal selectie op met Jaar = 2014, Periode = 1 en verder de default instellingen	Lijst wordt getoond	
11	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 800,00 Bij-/afgeboekt = 17,50 Bijgeboekt = 217,50 Afgeboekt = 200,00 Def Fact = 800,00 Concept = 0,00 Gefactureerd = 800,00 OHW mutaties = 17,50	
12	Controleer berekende velden voor Gaardenbeek	OHW begin = 0,00 Omzet = 300,00 Bij-/afgeboekt = 0,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 300,00 Concept = 0,00 Gefactureerd = 300,00 OHW mutaties = 0,00	
13	Haal selectie op met Jaar = 2014, Periode = 3 en verder de default instellingen	Lijst wordt getoond	
14	Controleer berekende velden voor Eislander	OHW begin = 17,50 Omzet = 800,00 Bij-/afgeboekt = 0,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 17,50	
15	Controleer berekende velden voor Gaardenbeek	OHW begin = 0,00 Omzet = 300,00 Bij-/afgeboekt = -95,59 Bijgeboekt = 55,85 Afgeboekt = -151,44 Def Fact = 0,00 Concept = 300,00 Gefactureerd = 300,00 OHW mutaties = -95,59	
16	Haal selectie op met Jaar = 2014, Periode = 1 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
17	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3510,00 Bij-/afgeboekt = 17,50 Bijgeboekt = 217,50 Afgeboekt = -200,00 Def Fact = 800,00 Concept = 0,00 Gefactureerd = 800,00 OHW mutaties = 2727,50	
18	Log in als Mdw	Ingelogd als medewerker Zomer	
19	Maak de ingevoerde weekstaat voor 2014 - 1 - week 2 definitief	Weekstaat definitief	
20	Log in als Admin	Ingelogd als Huysman	
21	Zet via administratiebeheer het actuele jaar op 2014 en periode op 1	-	
22	Fiatteer de weekstaat van Zomer	-	
23	Verwerk vervolgens de mutaties van periode 2014-1 t/m periode 2014-1 via 'Verwerking mutaties'	5 mutaties verwerkt	
24	Ga naar Declareren per client en selecteer Eislander	-	
25	Kies voor 'Samenstellen declaratie'	-	
26	Ga naar Factureren, Definitieve facturen en factureer de zojuist aangemaakt declaratie	Factuur wordt gegenereerd	
27	Zet via administratiebeheer het actuele jaar op 2014 en periode op 3	-	
28	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
29	Haal selectie op met Jaar = 2014, Periode = 1 en verder de default instellingen	Lijst wordt getoond	
30	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 1608,50 Bij-/afgeboekt = 17,50 Bijgeboekt = 217,50 Afgeboekt = -200,00 Def Fact = 1626,00 Concept = 0,00 Gefactureerd = 1626,00 OHW mutaties = 0,00	
31	Haal selectie op met Jaar = 2014, Periode = 1 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
32	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3510,00 Bij-/afgeboekt = 17,50 Bijgeboekt = 217,50 Afgeboekt = -200,00 Def Fact = 1626,00 Concept = 0,00 Gefactureerd = 1626,00 OHW mutaties = 1901,50	
33	Maak de weekstaten van Huysman definitief	-	
34	Fiatteer de weekstaten van Huysman	-	
35	Verwerk vervolgens de mutaties van periode 2014-1 t/m periode 2014-1 via 'Verwerking mutaties'	18 mutaties verwerkt	
36	Ga naar Declareren per cliënt en vraag de lijst op met de optie 'VPA-termijnfacturen tonen' aangevinkt	Lijst wordt getoond	
37	Selecteer de termijnfactuur van Eislander en kies voor 'Invoeren declaratiecorrecties'	Voer de overboekingen in zoals beschreven in attachment	
38	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
39	Haal selectie op met Jaar = 2014, Periode = 3 en verder de default instellingen	Lijst wordt getoond	
40	Controleer berekende velden voor Eislander	OHW begin = 1901,50
Omzet = 800,00
Bij-/afgeboekt = 115,00
Bijgeboekt = 175,00
Afgeboekt = -60,00
Overgeboekt = -67,50
Def Fact = 0,00
Concept = 800,00
Gefactureerd = 800,00
OHW mutaties = 1949,00	
41	Klik door op de afzonderlijke velden	Controleer dat de mutaties die getoond worden de verwachte zijn	
42	Controleer berekende velden voor Gaardenbeek	OHW begin = 1204,50
Omzet = 0,00
Bij-/afgeboekt = -104,09
Bijgeboekt = 63,35
Afgeboekt = -167,44
Overgeboekt = 67,50
Def Fact = 0,00
Concept = 0,00
Gefactureerd = 0,00
OHW mutaties = 1167,91	
43	Klik door op de afzonderlijke velden	Controleer dat de mutaties die getoond worden de verwachte zijn	
LINKS 
ID 	WorkItemType 	Link type 	Title 
12628
User Story	Tests	VPA – overzicht Cliënttotalen – aanpassen berekeningen
12700
Test Case	Related	Uren - Cliëntkaart - Berekende velden VPA
12838
Test Case	Related	VPA - Berekeningen overzicht cliënttotalen OHW begin / OHW mutaties / Omzet
12880
User Story	Tests	VPA - Berekeningen aanpassen (opdrachtbeheer - DPC)
12911
Test Case	Related	VPA - Berekeningen overzicht cliënttotalen - VPA en toch gedeclareerd
13167
Test Case	Related	VPA - Calculations Liquidityreport
13338
Test Case	Related	VPA - Berekeningen overzicht cliënttotalen Afgeboekt / Bijgeboekt / Overgeboekt (afwijken op cliëntniveau)
17196
Task	Tests	Regressietest applicatiepad 17
17813
Task	Tests	Regressietest Uren + Planning & Control
17995
Task	Tests	Regressietest Uren + Planning & Control
18218
Task	Tests	Regressietest Uren + Planning & Control
18541
Task	Tests	Regressietest Uren 3
18904
Task	Tests	Regressietest Uren 2
19232
Task	Tests	Regressietest Uren 3
20244
Task	Shared Steps	Cliënttotalen
ATTACHMENTS 
Name 	Size 	Date Attached 	Comments 
InvoerenDeclaratiecorrecties.docx
119kb	Thu Apr 10 2014	
BerekendeVeldenVPAClientkaart.docx
495kb	Thu Apr 10 2014	
InvoerOverboekingen.docx
65kb	Thu May 08 2014	
LATEST TEST OUTCOME
Outcome	Tester	Configuration	Run by	Date completed	Duration in seconds	Build number
None
Herbert Nijkamp - Wolters Kluwer 	Windows 7 and IE 8	Herbert Nijkamp - Wolters Kluwer 	Thursday, March 22, 2018	0	
Test case 12838: VPA - Berekeningen overzicht cliënttotalen OHW begin / OHW mutaties / Omzet
SUMMARY 
De data beschreven in de attachment is afkomstig van de user story mbt berekende velden op de cliëntkaart. Deze is hier hergebruikt.

STEPS
# 	Action 	Expected value 	Attachments 
1	Voeg de testdata uit de bijlage toe aan de masterdatabase	-	
2	Genereer 3 termijnfacturen voor Eislander (2014-1,2 en 3)	-	
3	Genereer 1 termijnfactuur voor Gaardenbeek (2014-1)	-	
4	Ga naar Factureren, Definitieve facturen en factureer de eerste 2 termijnfacturen van Eislander en die van Gaardenbeek	3 termijnfacturen gegenereerd	
5	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
6	Haal selectie op met Jaar = 2014, Periode =1 en verder de default instellingen	Lijst wordt getoond	
7	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 800,00 Concept = 0,00 Gefactureerd = 800,00 OHW mutaties = 0,00 OHW actueel = 0,00	
8	Controleer berekende velden voor Gaardenbeek	OHW begin = 0,00 Omzet = 300,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 300,00 Concept = 0,00 Gefactureerd = 300,00 OHW mutaties = 0,00 OHW actueel = 0,00	
9	Haal selectie op met Jaar = 2014, Periode = 1 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
10	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3510,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 800,00 Concept = 0,00 Gefactureerd = 800,00 OHW mutaties = 2710,00 OHW actueel = 2710,00	
11	Controleer berekende velden voor Gaardenbeek	OHW begin = 0,00 Omzet = 1504,50 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 300,00 Concept = 0,00 Gefactureerd = 300,00 OHW mutaties = 1204,50 OHW actueel = 1204,50	
12	Haal selectie op met Jaar = 2014, Periode = 3 en verder de default instellingen	Lijst wordt getoond	
13	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 0,00 OHW actueel = 0,00	
14	Haal selectie op met Jaar = 2014, Periode = 3 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
15	Controleer berekende velden voor Eislander	OHW begin = 2710,00 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 2710,00 OHW actueel = 2710,00	
16	Log in als Mdw	Ingelogd als medewerker Zomer	
17	Maak de ingevoerde weekstaat voor 2014 - 1 - week 2 definitief	Weekstaat definitief	
18	Log in als Admin	Ingelogd als Huysman	
19	Zet via administratiebeheer het actuele periode jaar op 2014 en periode op 1	-	
20	Fiatteer de weekstaat van Zomer	-	
21	Verwerk vervolgens de mutaties van periode 2014-1 t/m periode 2014-1 via 'Verwerking mutaties'	5 mutaties verwerkt	
22	Ga naar Declareren per client en selecteer Eislander	-	
23	Kies voor 'Samenstellen declaratie'	-	
24	Ga naar Factureren, Definitieve facturen en factureer de zojuist aangemaakt declaratie	Factuur wordt gegenereerd	
25	Zet via administratiebeheer het actuele periode jaar op 2014 en periode op 3	-	
26	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
27	Haal selectie op met Jaar = 2014, Periode = 1 en verder de default instellingen	Lijst wordt getoond	
28	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 1608,50 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 1608,50 Concept = 0,00 Gefactureerd = 1608,50 OHW mutaties = 0,00 OHW actueel = 0,00	
29	Haal selectie op met Jaar = 2014, Periode = 1 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
30	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3510,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 1608,50 Concept = 0,00 Gefactureerd = 1608,50 OHW mutaties = 1901,50 OHW actueel = 1901,50	
31	Haal selectie op met Jaar = 2014, Periode = 3 en verder de default instellingen	Lijst wordt getoond	
32	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 0,00 OHW actueel = 0,00	
33	Haal selectie op met Jaar = 2014, Periode = 3 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
34	Controleer berekende velden voor Eislander	OHW begin = 1901,50 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 1901,50 OHW actueel = 1901,50	
35	Maak de weekstaten van Huysman definitief	-	
36	Fiatteer de weekstaten van Huysman	-	
37	Verwerk vervolgens de mutaties van periode 2014-1 t/m periode 2014-1 via 'Verwerking mutaties'	18 mutaties verwerkt	
38	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
39	Haal selectie op met Jaar = 2014, Periode = 1 en verder de default instellingen	Lijst wordt getoond	
40	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3510,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 1608,50 Concept = 0,00 Gefactureerd = 1608,50 OHW mutaties = 1901,50 OHW actueel = 1901,50	
41	Controleer berekende velden voor Gaardenbeek	OHW begin = 0,00 Omzet = 1504.50 Bijgeboekt = 0,00 Afgeboekt = 0,00 OHW mutaties = 1204.50 OHW actueel = 1204,50	
42	Haal selectie op met Jaar = 2014, Periode = 1 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
43	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3510,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 1608,50 Concept = 0,00 Gefactureerd = 1608,50 OHW mutaties = 1901,50 OHW actueel = 1901,50	
44	Haal selectie op met Jaar = 2014, Periode = 3 en verder de default instellingen	Lijst wordt getoond	
45	Controleer berekende velden voor Eislander	OHW begin = 1901,50 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 1901,50 OHW actueel = 1901,50	
46	Controleer berekende velden voor Gaardenbeek	OHW begin = 1204,50 Omzet = 0,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 0,00 Gefactureerd = 0,00 OHW mutaties = 1204,50 OHW actueel = 1204,50	
LINKS 
ID 	WorkItemType 	Link type 	Title 
12628
User Story	Tests	VPA – overzicht Cliënttotalen – aanpassen berekeningen
12700
Test Case	Related	Uren - Cliëntkaart - Berekende velden VPA
12880
User Story	Tests	VPA - Berekeningen aanpassen (opdrachtbeheer - DPC)
12900
Test Case	Related	VPA - Berekeningen overzicht cliënttotalen Afgeboekt / Bijgeboekt / Overgeboekt
12911
Test Case	Related	VPA - Berekeningen overzicht cliënttotalen - VPA en toch gedeclareerd
13167
Test Case	Related	VPA - Calculations Liquidityreport
13337
Test Case	Related	VPA - Berekeningen overzicht cliënttotalen OHW begin / OHW mutaties / Omzet (afwijken op cliëntniveau)
18904
Task	Tests	Regressietest Uren 2
20244
Task	Shared Steps	Cliënttotalen
ATTACHMENTS 
Name 	Size 	Date Attached 	Comments 
BerekendeVeldenVPAClientkaart.docx
495kb	Thu Apr 10 2014	
LATEST TEST OUTCOME
Outcome	Tester	Configuration	Run by	Date completed	Duration in seconds	Build number
None
Herbert Nijkamp - Wolters Kluwer 	Windows 7 and IE 8	Herbert Nijkamp - Wolters Kluwer 	Thursday, March 22, 2018	0	
Test case 13337: VPA - Berekeningen overzicht cliënttotalen OHW begin / OHW mutaties / Omzet (afwijken op cliëntniveau)
SUMMARY 
De data beschreven in de attachment is een uitbreiding op de testdata zoals gebruikt voor het testen van de functionaliteit zonder afwijkingen per cliënt.

STEPS
# 	Action 	Expected value 	Attachments 
1	Voeg de testdata uit de bijlage toe aan de masterdatabase (tot Invoer declaratiecorrecties)	-	
2	Genereer 3 termijnfacturen voor Eislander (2014-1,2 en 3)	-	
3	Genereer 1 termijnfactuur voor Gaardenbeek (2014-1)	-	
4	Ga naar Factureren, Definitieve facturen en factureer de eerste 2 termijnfacturen van Eislander en die van Gaardenbeek	3 termijnfacturen gegenereerd	
5	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
6	Haal selectie op met Jaar = 2014, Periode =1 en verder de default instellingen	Lijst wordt getoond	
7	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 800,00 Concept = 0,00 Gefactureerd = 800,00 OHW mutaties = 0,00 OHW actueel = 0,00	
8	Controleer berekende velden voor Gaardenbeek	OHW begin = 0,00 Omzet = 300,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 300,00 Concept = 0,00 Gefactureerd = 300,00 OHW mutaties = 0,00 OHW actueel = 0,00	
9	Haal selectie op met Jaar = 2014, Periode = 1 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
10	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3510,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 800,00 Concept = 0,00 Gefactureerd = 800,00 OHW mutaties = 2710,00 OHW actueel = 2710,00	
11	Controleer berekende velden voor Gaardenbeek	OHW begin = 0,00 Omzet = 1504,50 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 300,00 Concept = 0,00 Gefactureerd = 300,00 OHW mutaties = 1204,50 OHW actueel = 1204,50	
12	Haal selectie op met Jaar = 2014, Periode = 3 en verder de default instellingen	Lijst wordt getoond	
13	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 0,00 OHW actueel = 0,00	
14	Haal selectie op met Jaar = 2014, Periode = 3 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
15	Controleer berekende velden voor Eislander	OHW begin = 2710,00 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 2710,00 OHW actueel = 2710,00	
16	Log in als Mdw	Ingelogd als medewerker Zomer	
17	Maak de ingevoerde weekstaat voor 2014 - 1 - week 2 definitief	Weekstaat definitief	
18	Log in als Admin	Ingelogd als Huysman	
19	Zet via administratiebeheer het actuele periode jaar op 2014 en periode op 1	-	
20	Fiatteer de weekstaat van Zomer	-	
21	Verwerk vervolgens de mutaties van periode 2014-1 t/m periode 2014-1 via 'Verwerking mutaties'	5 mutaties verwerkt	
22	Ga naar Declareren per client en selecteer Eislander	-	
23	Kies voor 'Samenstellen declaratie'	-	
24	Ga naar Factureren, Definitieve facturen en factureer de zojuist aangemaakt declaratie	Factuur wordt gegenereerd	
25	Zet via administratiebeheer het actuele periode jaar op 2014 en periode op 3	-	
26	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
27	Haal selectie op met Jaar = 2014, Periode = 1 en verder de default instellingen	Lijst wordt getoond	
28	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 1608,50 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 1608,50 Concept = 0,00 Gefactureerd = 1608,50 OHW mutaties = 0,00 OHW actueel = 0,00	
29	Haal selectie op met Jaar = 2014, Periode = 1 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
30	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3510,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 1608,50 Concept = 0,00 Gefactureerd = 1608,50 OHW mutaties = 1901,50 OHW actueel = 1901,50	
31	Haal selectie op met Jaar = 2014, Periode = 3 en verder de default instellingen	Lijst wordt getoond	
32	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 0,00 OHW actueel = 0,00	
33	Haal selectie op met Jaar = 2014, Periode = 3 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
34	Controleer berekende velden voor Eislander	OHW begin = 1901,50 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 1901,50 OHW actueel = 1901,50	
35	Maak de weekstaten van Huysman definitief	-	
36	Fiatteer de weekstaten van Huysman	-	
37	Verwerk vervolgens de mutaties van periode 2014-1 t/m periode 2014-1 via 'Verwerking mutaties'	18 mutaties verwerkt	
38	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
39	Haal selectie op met Jaar = 2014, Periode = 1 en verder de default instellingen	Lijst wordt getoond	
40	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3510,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 1608,50 Concept = 0,00 Gefactureerd = 1608,50 OHW mutaties = 1901,50 OHW actueel = 1901,50	
41	Controleer berekende velden voor Gaardenbeek	OHW begin = 0,00 Omzet = 1504.50 Bijgeboekt = 0,00 Afgeboekt = 0,00 OHW mutaties = 1204.50 OHW actueel = 1204,50	
42	Haal selectie op met Jaar = 2014, Periode = 1 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
43	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3510,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 1608,50 Concept = 0,00 Gefactureerd = 1608,50 OHW mutaties = 1901,50 OHW actueel = 1901,50	
44	Haal selectie op met Jaar = 2014, Periode = 3 en verder de default instellingen	Lijst wordt getoond	
45	Controleer berekende velden voor Eislander	OHW begin = 1901,50 Omzet = 800,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 1901,50 OHW actueel = 1901,50	
46	Controleer berekende velden voor Gaardenbeek	OHW begin = 1204,50 Omzet = 0,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 0,00 Gefactureerd = 0,00 OHW mutaties = 1204,50 OHW actueel = 1204,50	
LINKS 
ID 	WorkItemType 	Link type 	Title 
12628
User Story	Tests	VPA – overzicht Cliënttotalen – aanpassen berekeningen
12838
Test Case	Related	VPA - Berekeningen overzicht cliënttotalen OHW begin / OHW mutaties / Omzet
12880
User Story	Tests	VPA - Berekeningen aanpassen (opdrachtbeheer - DPC)
13338
Test Case	Related	VPA - Berekeningen overzicht cliënttotalen Afgeboekt / Bijgeboekt / Overgeboekt (afwijken op cliëntniveau)
18904
Task	Tests	Regressietest Uren 2
20244
Task	Shared Steps	Cliënttotalen
11580
User Story	Tests	VPA - afwijking van template bij een client
13246
Test Case	Related	VPA - Berekeningen Opdrachtbeheer (afwijken op cliëntniveau)
13283
Test Case	Related	Uren - VPA - Afwijken op cliëntniveau - Autorisatie
13287
Test Case	Related	Uren - VPA - Afwijken op cliëntniveau - CRUD
13291
Test Case	Related	Uren - VPA - Afwijken op cliëntniveau - Dupliceren
13335
Test Case	Related	VPA - Berekeningen Liquiditeitsoverzicht OHW (afwijken op cliëntniveau)
13336
Test Case	Related	VPA - Berekende velden in declareren per cliënt (afwijken op cliëntniveau)
13507
Test Case	Related	Uren - VPA - Afwijken op cliëntniveau - Aan-/uitzetten instelling
ATTACHMENTS 
Name 	Size 	Date Attached 	Comments 
TestDataAfwijkingen per cliënt.docx
472kb	Tue May 20 2014	
LATEST TEST OUTCOME
Outcome	Tester	Configuration	Run by	Date completed	Duration in seconds	Build number
None
Herbert Nijkamp - Wolters Kluwer 	Windows 7 and IE 8	Herbert Nijkamp - Wolters Kluwer 	Thursday, March 22, 2018	0	
Test case 13338: VPA - Berekeningen overzicht cliënttotalen Afgeboekt / Bijgeboekt / Overgeboekt (afwijken op cliëntniveau)
SUMMARY 
De data beschreven in de attachment is een uitbreiding op de testdata zoals gebruikt voor het testen van de functionaliteit zonder afwijkingen per cliënt.
Testcase bij voorkeur uitvoeren aansluitend op of in combinatie met op 13337.

STEPS
# 	Action 	Expected value 	Attachments 
1	Voeg de testdata uit de bijlage toe aan de masterdatabase (tot Invoer declaratiecorrecties)	-	
2	Genereer 3 termijnfacturen voor Eislander (2014-1,2 en 3)	-	
3	Genereer 2 termijnfacturen voor Gaardenbeek (2014-1 en 2014-2)	-	
4	Ga naar Factureren, Definitieve facturen en factureer de eerste 2 termijnfacturen van Eislander en de eerste van Gaardenbeek	3 termijnfacturen gegenereerd	
5	Ga naar Declareren per cliënt en vraag de lijst op met de optie 'VPA-termijnfacturen tonen' aangevinkt	Lijst wordt getoond	
6	Selecteer de termijnfactuur van Eislander en kies voor 'Invoeren declaratiecorrecties'	Voer de declaratiecorrecties in zoals beschreven in attachment	
7	Selecteer de termijnfactuur van Gaardenbeek en kies voor 'Invoeren declaratiecorrecties'	Voer de declaratiecorrecties in zoals beschreven in attachment	
8	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
9	Haal selectie op met Jaar = 2014, Periode = 1 en verder de default instellingen	Lijst wordt getoond	
10	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 800,00 Bij-/afgeboekt = 17,50 Bijgeboekt = 217,50 Afgeboekt = 200,00 Def Fact = 800,00 Concept = 0,00 Gefactureerd = 800,00 OHW mutaties = 17,50	
11	Controleer berekende velden voor Gaardenbeek	OHW begin = 0,00 Omzet = 300,00 Bij-/afgeboekt = 0,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 300,00 Concept = 0,00 Gefactureerd = 300,00 OHW mutaties = 0,00	
12	Haal selectie op met Jaar = 2014, Periode = 3 en verder de default instellingen	Lijst wordt getoond	
13	Controleer berekende velden voor Eislander	OHW begin = 17,50 Omzet = 800,00 Bij-/afgeboekt = 0,00 Bijgeboekt = 0,00 Afgeboekt = 0,00 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 17,50	
14	Controleer berekende velden voor Gaardenbeek	OHW begin = 0,00 Omzet = 300,00 Bij-/afgeboekt = -95,59 Bijgeboekt = 55,85 Afgeboekt = -151,44 Def Fact = 0,00 Concept = 300,00 Gefactureerd = 300,00 OHW mutaties = -95,59	
15	Haal selectie op met Jaar = 2014, Periode = 1 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
16	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3510,00 Bij-/afgeboekt = 17,50 Bijgeboekt = 217,50 Afgeboekt = -200,00 Def Fact = 800,00 Concept = 0,00 Gefactureerd = 800,00 OHW mutaties = 2727,50	
17	Log in als Mdw	Ingelogd als medewerker Zomer	
18	Maak de ingevoerde weekstaat voor 2014 - 1 - week 2 definitief	Weekstaat definitief	
19	Log in als Admin	Ingelogd als Huysman	
20	Zet via administratiebeheer het actuele jaar op 2014 en periode op 1	-	
21	Fiatteer de weekstaat van Zomer	-	
22	Verwerk vervolgens de mutaties van periode 2014-1 t/m periode 2014-1 via 'Verwerking mutaties'	5 mutaties verwerkt	
23	Ga naar Declareren per client en selecteer Eislander	-	
24	Kies voor 'Samenstellen declaratie'	-	
25	Ga naar Factureren, Definitieve facturen en factureer de zojuist aangemaakt declaratie	Factuur wordt gegenereerd	
26	Zet via administratiebeheer het actuele jaar op 2014 en periode op 3	-	
27	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
28	Haal selectie op met Jaar = 2014, Periode = 1 en verder de default instellingen	Lijst wordt getoond	
29	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 1608,50 Bij-/afgeboekt = 17,50 Bijgeboekt = 217,50 Afgeboekt = -200,00 Def Fact = 1626,00 Concept = 0,00 Gefactureerd = 1626,00 OHW mutaties = 0,00	
30	Haal selectie op met Jaar = 2014, Periode = 1 en verder de instelling 'Weergeven onverwerkte mutaties' aangevinkt	Lijst wordt getoond	
31	Controleer berekende velden voor Eislander	OHW begin = 0,00 Omzet = 3510,00 Bij-/afgeboekt = 17,50 Bijgeboekt = 217,50 Afgeboekt = -200,00 Def Fact = 1626,00 Concept = 0,00 Gefactureerd = 1626,00 OHW mutaties = 1901,50	
32	Maak de weekstaten van Huysman definitief	-	
33	Fiatteer de weekstaten van Huysman	-	
34	Verwerk vervolgens de mutaties van periode 2014-1 t/m periode 2014-1 via 'Verwerking mutaties'	18 mutaties verwerkt	
35	Ga naar Declareren per cliënt en vraag de lijst op met de optie 'VPA-termijnfacturen tonen' aangevinkt	Lijst wordt getoond	
36	Selecteer de termijnfactuur van Eislander en kies voor 'Invoeren declaratiecorrecties'	Voer de overboekingen in zoals beschreven in attachment	
37	Ga naar Declareren, Cliënttotalen	Selectiescherm wordt geopend	
38	Haal selectie op met Jaar = 2014, Periode = 3 en verder de default instellingen	Lijst wordt getoond	
39	Controleer berekende velden voor Eislander	OHW begin = 1919,00 Omzet = 800,00 Bij-/afgeboekt = 115,00 Bijgeboekt = 175,00 Afgeboekt = -60,00 Overgeboekt = -67,50 Def Fact = 0,00 Concept = 800,00 Gefactureerd = 800,00 OHW mutaties = 1966,50	
40	Klik door op de afzonderlijke velden	Controleer dat de mutaties die getoond worden de verwachte zijn	
41	Controleer berekende velden voor Gaardenbeek	OHW begin = 1204,50 Omzet = 0,00 Bij-/afgeboekt = -104,09 Bijgeboekt = 63,35 Afgeboekt = -167,44 Overgeboekt = 67,50 Def Fact = 0,00 Concept = 0,00 Gefactureerd = 0,00 OHW mutaties = 1167,91	
42	Klik door op de afzonderlijke velden	Controleer dat de mutaties die getoond worden de verwachte zijn	
LINKS 
ID 	WorkItemType 	Link type 	Title 
12628
User Story	Tests	VPA – overzicht Cliënttotalen – aanpassen berekeningen
12880
User Story	Tests	VPA - Berekeningen aanpassen (opdrachtbeheer - DPC)
18904
Task	Tests	Regressietest Uren 2
20244
Task	Shared Steps	Cliënttotalen
12900
Test Case	Related	VPA - Berekeningen overzicht cliënttotalen Afgeboekt / Bijgeboekt / Overgeboekt
11580
User Story	Tests	VPA - afwijking van template bij een client
13246
Test Case	Related	VPA - Berekeningen Opdrachtbeheer (afwijken op cliëntniveau)
13283
Test Case	Related	Uren - VPA - Afwijken op cliëntniveau - Autorisatie
13287
Test Case	Related	Uren - VPA - Afwijken op cliëntniveau - CRUD
13291
Test Case	Related	Uren - VPA - Afwijken op cliëntniveau - Dupliceren
13335
Test Case	Related	VPA - Berekeningen Liquiditeitsoverzicht OHW (afwijken op cliëntniveau)
13336
Test Case	Related	VPA - Berekende velden in declareren per cliënt (afwijken op cliëntniveau)
13507
Test Case	Related	Uren - VPA - Afwijken op cliëntniveau - Aan-/uitzetten instelling
13337
Test Case	Related	VPA - Berekeningen overzicht cliënttotalen OHW begin / OHW mutaties / Omzet (afwijken op cliëntniveau)
ATTACHMENTS 
Name 	Size 	Date Attached 	Comments 
TestDataAfwijkingen per cliënt.docx
472kb	Tue May 20 2014	
LATEST TEST OUTCOME
Outcome	Tester	Configuration	Run by	Date completed	Duration in seconds	Build number
None
Herbert Nijkamp - Wolters Kluwer 	Windows 7 and IE 8	Herbert Nijkamp - Wolters Kluwer 	Thursday, March 22, 2018	0	
Test case 16279: Uren - Declareren -Cliënttotalen - Calculations provisions
SUMMARY 
Wanneer voorzieningen zijn ingesteld dan kan met script S03471.sql voor alle cliënten voorzieningen records aangemaakt worden in de actuele periode.
 
 
Zie attachment voor ingevoerde waarden voor voorzieningen.

STEPS
# 	Action 	Expected value 	Attachments 
1	Draai script S03488.sql	Provisions is build for customer and not default available.	
2	Zet de uitgangssituatie klaar uit attachment	There is no attachment - look in summary	
3	Ga naar Uren - Declareren - Cliënttotalen	-	
4	Stel periode in	@Periode	
5	Uitkomst 'Vrzng OHW actueel'	@VrzngOHWactueel	
6	Uitkomst 'Vrzng OHW beginstand'	@VrzngOHWbeginstand	
7	Uitkomst 'Vrzng Debiteur actueel'	@VrzngDebiteuractueel	
8	Uitkomst 'Vrzng Debiteur beginstand'	@VrzngDebiteurbeginstand	
9	---------	 	
10	Laat 'Overzicht cliënttotalen' open staan	-	
11	Ga in het Configuratiescherm naar Overig-Algemeen en maak instelling 'Kostensoort tbv 'Voorziening OHW' leeg.	-	
12	Haal 'Overzicht cliënttotalen' opnieuw op	Kolommen 'Vrnzg OHW actueel' en 'Vrnzg OHW beginstand' worden nog wel getoond maar niet meer berekend. Worden alleen berekend wanneer een kostensoort bij instelling 'Kostensoort tbv 'Voorziening OHW' is geselecteerd.	
13	Laat 'Overzicht cliënttotalen' open staan	-	
14	Ga in het Configuratiescherm naar Overig-Algemeen en maak instelling 'Kostensoort tbv 'Voorziening Debiteur' leeg.	-	
15	Haal 'Overzicht cliënttotalen' opnieuw op	Kolommen 'Vrnzg deb. actueel' en 'Vrnzg deb. beginstand' worden nog wel getoond maar niet meer berekend. Worden alleen berekend wanneer een kostensoort bij instelling 'Kostensoort tbv 'Voorziening Debiteur' is geselecteerd.	
16	Sluit 'Overzicht cliënttotalen'	 	
17	Haal 'Overzicht cliënttotalen' opnieuw op	De kolommen mbt voorzieningen worden nu niet meer getoond.	
18	---------	 	
19	Wanneer de kostensoorten t.b.v. voorzieningen niet geblokkeerd zijn dan kunnen meerdere boekingen in een periode aanwezig zijn.	Op het overzicht cliënttotalen worden de aanwezige voorzieningen bij elkaar opgeteld.	
PARAMETERS 

Periode	VrzngOHWactueel	VrzngOHWbeginstand	VrzngDebiteuractueel	VrzngDebiteurbeginstand
2013-12	Beldman 130 en Donkaard 1010	Beldman - en Donkaard -	Beldman 810 en Donkaard 962,41	Beldman - en Donkaard -
2014-12	Beldman 250 en Donkaard 2300	Beldman 130 en Donkaard 1010	Beldman 375 en Donkaard 1012,58	Beldman 810 en Donkaard 962,41
2015-3	Beldman 600 en Donkaard 2000	Beldman 250 en Donkaard 2300	Beldman 1250 en Donkaard 1980	Beldman 375 en Donkaard 1012,58
2015-4	Beldman 750 en Donkaard 1160	Beldman 250 en Donkaard 2300	Beldman 1275 en Donkaard 1999	Beldman 250 en Donkaard 2300
				
LINKS 
ID 	WorkItemType 	Link type 	Title 
18904
Task	Tests	Regressietest Uren 2
20244
Task	Shared Steps	Cliënttotalen
15940
User Story	Tests	Koenen - maatwerk Voorzieningen
16231
Test Case	Related	Uren - Declareren - Invoeren voorzieningen
16232
Test Case	Related	Uren - Weekstaat - Periodewissel
16233
Test Case	Related	Uren - Weekstaat - Periodewissel - Voorzieningen - Bepalen opdrachtnummer
16234
Test Case	Related	Uren - Declareren -Cliënttotalen - columns according to Provisions
16235
Test Case	Related	Uren - Edit declarations - Correctionreason with/without explanation
16236
Test Case	Related	Uren - Analyseren - Correcties naar reden (report)
16287
Test Case	Related	Uren - Weekstaat - Periodewissel - Voorzieningen komen meerdere keren voor
LATEST TEST OUTCOME
Outcome	Tester	Configuration	Run by	Date completed	Duration in seconds	Build number
None
Herbert Nijkamp - Wolters Kluwer 	Windows 7 and IE 8	Herbert Nijkamp - Wolters Kluwer 	Thursday, March 22, 2018	0	

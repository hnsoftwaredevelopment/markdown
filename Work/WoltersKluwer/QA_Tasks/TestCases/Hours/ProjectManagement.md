ProjectManagement

# **Opdrachtbeheer**

[TOC]

-----------------------------



## Current Test Cases:

- 13178
- 13246

### Comment from the tester

It was difficult to see the differences between both testcases. And again, same data and actions as in previous testcases. Only an other list.

### Over all conclusion on the current Test Cases of QA 

Only a very small part of Projectmanagement is acualy tested, mainly the content of the report, but the actual functionality of Projectmanagement is not tested at all. So main goal for QA is to create a new set of test cases that acualy test the important issues of Projectmanagement



## **Projectmanagement**

### Accesspoints

- Uren - Cliënten - Opdrachtbeheer					All
- Uren - Cliënten - Prijsafspraken - Opdrachtbeheer			Cust. + Project
- Uren - Cliënten - Budgetbewaking - Opdrachtbeheer			Cust. + Project
- Uren - Declareren - Declareren per cliënt -  Opdrachtbeheer		Customer
- CRM - Dashboard - Opdrachtbeheer					Customer

### POI

#### Selection made for every accesspoint

Access from different Accesspoints, the shown list should be a result of the selection that is made by the accesspoint.
The first (base) access point shows all projects for all customers, the second on from the VPA report only shows the selected Project for that price agreement (so selection on available customer and project number)

#### Selection screen

**Selectiontab (Selectie):**

- Declaration corrections are included in the realization
- Show projects from expired clients

**Perplexity (Knelpunten):**

- Include excluded projects
- Closing deadline
- Exceeding budget
- Substitution budget subproject
- Realization budget subproject
- Exceeding normhours
- Realization of normhours
- Not fully scheduled

Add new project



### Settings



## Worked out Testcase 13178

13178 VPA - Calculations in "Opdrachtbeheer"

1. Add testdata from attachment "RegressieTestInvoerData.docx".
   1. Don't look at the numbers of the year or project in this document. Just add a new year and use the new year and the year before.
2. Generate 3 terminvoices for Eislander (period 1, 2 and 3)
3. Generate 1 terminvoice for Gaardenbeek (period ?).
4. Go to Uren > Factureren > Definitieve facturen and print the first 2 terminvoices of Eislander and the terminvoice of Gaardenbeek
5. Go to Uren > Cliënten > Opdrachtbeheer
6. Get the data
   1. For EISLANDER and GAARDENBEEK you see 2 records
7. Make the columns 'OHW' en 'OHW Budget' visible.
8. Save these settings and refresh the list	 
   1. Columns now have values
9. Check the values for EISLANDER
10. Click on the hyperlinks	
    1. Check if you see the expected data
11. Go to tab 'Kengetallen'
12. Check the values
    1. OHW must be the same as in the list
13. Go to tab 'Deelopdrachten'
    1. Check total of column 'Omzet' and compare with list of projects
14. Make the timesheets of employee Huysman definitive
15. "Fiatteer" the timesheets of employee Huysman
16. "Verwerk" the mutations of period 1 via 'Verwerking mutaties'	
    1. 18 mutaties verwerkt
17. Go to Uren > Declareren > Declareren per client
18. Get data for Period = 3 with 'VPA-termijnfacturen tonen' checked
19. Select the terminvoice from Eislander and click on 'Invoeren declaratiecorrecties'
    1. Add the corrections as described in attachment "RegressieTestInvoerDeclaratiecorrecties.docx". Just use the same projectnumbers
20. Select the terminvoice from Gaardenbeek and click on 'Invoeren declaratiecorrecties'
    1. Add the corrections as described in attachment "RegressieTestInvoerDeclaratiecorrecties.docx"
21. Go to Uren > Cliënten > Opdrachtbeheer
22. Get the data.
23. Check the values for EISLANDER
24. Go to tab 'Kengetallen'
25. Check the values
    1. Compare with values in the list
26. Go to tab 'Deelopdrachten'
    1. Check the totals
27. Go to Uren > Declareren > Declareren per client
28. Get data for Period 3 with option 'VPA-termijnfacturen tonen' checked
29. Select the terminvoice from Eislander and click on 'Invoeren declaratiecorrecties'
    1. Add the records as described in attachment "RegressieTestInvoerOverboekingen.docx"
30. Go to Uren > Cliënten > Opdrachtbeheer
31. Get data
32. Check values for EISLANDER
33. Click on hyperlinks and check shown mutations
34. Go to tab 'Kengetallen'
35. Check the values
    1. OHW mutaties = 1421,00
36. Go to tab 'Deelopdrachten'. Compare the values
37. Add in the timesheet Incidental costs on Client EISLANDER (Period = 1 and Week = 4)
    1. Werksoort 101 ( = VPA ) van €112,-
    2. Werksoort 151 (= Meerwerk) van €76,-
38. Go to Uren > Cliënten > Opdrachtbeheer
39. Get the data
40. Warning!;
    1. There is a setting Uren > Instellingen > Configuratiescherm > Overig > Planning & Control with the name 'Incidentele kosten bij werksoort meetellen (indien gekoppeld)'. This setting affects the results
41. Check the values for EISLANDER	
42. Go to tab 'Kengetallen'
43. Check the values
44. Go to tab 'Deelopdrachten'
    1. Compare the totals with the list of projects
45. Open selection window and uncheck the option 'Correcties meetellen in omzet'. Get the data.
46. Check the values for EISLANDER
47. Go to tab 'Kengetallen'
48. Check the values
49. Go to tab 'Deelopdrachten'
    1. Compare the totals with the values in the list of projects
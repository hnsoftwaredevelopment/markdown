20181231_Comments_on_regressiontest

# 20181231 Comments on regressiontest

## Relationlist

### ALU-48

Add new relation on with same Fiscalnumber : entering the number from the test is not giving an warning but an error “ Fiscaalnummer niet geldig”



## Outlook connector

Selecteren van relatie in archiveer scherm werkt nu anders. Vervallen relaties zijn standaard niet zichtbaar.
Selecteren eigenaar die vervallen is werkt niet goed. Na selectie is deze toch niet zichtbaar. Antieke dropdown ...



## Gebruikersbeheer

### TC 13933 & TC 13934 

depend on non existing previous testcases.



## Clienten

### 11634

Raluca: Bad testcase, functionality has changed



### 11597

Raluca: Functionality has changed



### 11637

Raluca: ClientGroup tab is still displayed, even if the client does not belong to any group

Marco: Testcase is weird. Non existing Clientgroups are used.



### 11764

Raluca: OK

Marco: Base on VPA 1.0



### 11798

Raluca: step 17. Tabpage still visible, should not be visible

Marco: Authorization is not logical. For making the tab invisible task 40 with function 5406 needs to be used. Old en new VPA combined.



### ALU-119

Raluca: for group 4, which already exists from master database, not able to check “Opdrachten selecteren”. I have created a new group 5, but is visible in the ClientGroup Tab and it should not be visible there.

Marco: data in Master is different from testcase. Group 4 contains Clients and no Projects. Maybe change Master db?



### ALU-120 & ALU-121 & ALU-122 & ALU-123

Raluca: clientGroup not displayed in red

Marco: colors are not implemented in new style???



### ALU-124

Raluca: In Autorisatie,turn Task 39, Function 5405, not working, still being able to check/uncheck client groups.

Marco: this seems a bug










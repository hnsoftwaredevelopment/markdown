Create_working_Alure_environment

**Software:**

- Alure Reg Keys
- Alure(910)
- Autorisatie(910)
- Batch
- DATA
- MSSQL2014
- PowerISO
- dotnetfx35


 **Steps:**

Install PowerISO and reboot

Install dotnetfx35

Copy DATA to "C:\\Program Files (x86)\\Innonal\\" (without .config files)

Install latest MSSQL Using the installation manual

Make changens in the **SQL Server Configuration Manager** (as discribed in the same manual)


 **Alure10**

-   Install Alure 10
-   Install Author
-   Copy Config files from DATA naar C:\\Program Files (86)\Innolan\Alure.NET


 **Alure910**

-   Copy Alure910
-   Copy Autorisatie910
-   Load reg file Alure910.reg


 Attach databases in SQL Management Studio

Open New Query in Management Studio end enter:

`exec autor.bda.sp-sync_server` 

And wait for completion


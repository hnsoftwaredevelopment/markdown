# Create Modelbuilder database
Create Modelbuilder database

\[TOC\]

## Structure

```
[DB]: modelbbuilder
├─┬─[TBL]: category
│ └─┬─[REC]: category_Id			int 		NOT NULL	**PK**
│   ├─[REC]: category_Shortname			varchar(15)
│   ├─[REC]: category_Description		varchar(55)
│   ├─[REC]: category_Fullpath			varchar(120)
│   └─[REC]: category_IsRoot			TynyInt(1)
│
├─┬─[TBL]: countries
│ └─┬─[REC]: country_Id				int 		NOT NULL	**PK**
│   ├─[REC]: country_code			varchar(4)			**UK** 
│   ├─[REC]: currency_Symbol			varchar(2)
│   ├─[REC]: country_Description		varchar(45)
│   └─[REC]: currency_Id 			int
│
├─┬─[TBL]: currencies
│ └─┬─[REC]: currency_Id			int		NOT NULL	**PK**
│   ├─[REC]: currency_Code			varchar(4)	NOT NULL	**UK**
│   ├─[REC]: currency_Symbol 			varchar(2) 	NOT NULL	**UK**
│   ├─[REC]: currency_Description		varchar(45)	NOT NULL
│   └─[REC]: currency_ConversionRate		float
│
├─┬─[TBL]: language
│ └─┬─[REC]: language_Id			int		NOT NULL	**PK**
│   ├─[REC]: language_code 			varchar(4)	NOT NULL	**UK**
│   └─[REC]: language_Description		varchar(45)	NOT NULL
│
├─┬─[TBL]: products
│ └─┬─[REC]: product_Id				int		NOT NULL	**PK**
│   ├─[REC]: product_Code			varchar(20) 	NOT NULL	**UK**
│   ├─[REC]: product_Description		varchar(150) 	NOT NULL
│   ├─[REC]: category_Id			int
│   ├─[REC]: category_Description 		varchar(45)
│   ├─[REC]: supplier_Id 			int
│   ├─[REC]: supplier_Name 			varchar(45)
│   ├─[REC]: product_SupplierProductNumber	varchar(20)
│   ├─[REC]: storage_Id 			int
│   ├─[REC]: storage_Description 		varchar(50)
│   └─[REC]: product_Price 			float
│
├─┬─[TBL]: projects
│ └─┬─[REC]: projects_Id			int		NOT NULL	**PK**
│   ├─[REC]: projects_Description		varchar(50)	NOT NULL
│   ├─[REC]: projects_StartDate			date
│   ├─[REC]: projects_ExpectedEndDate		date
│   ├─[REC]: projects_EndDate			date
│   ├─[REC]: projects_TotalCost			decimal(5,2)
│   └─[REC]: projects_TotalMinutes		int
│
├─┬─[TBL]: storage
│ └─┬─[REC]: storage_Id				int		NOT NULL	**PK**
│   ├─[REC]: storage_Code			varchar(20)	NOT NULL	**UK**
│   └─[REC]: storage_Description		varchar(150)	
│
├─┬─[TBL]: supplier
│ └─┬─[REC]: supplier_Id			int		NOT NULL	**PK**
│   ├─[REC]: supplier_Code			varchar(20) 	NOT NULL	**UK**
│   ├─[REC]: supplier_Name			varchar(150) 	NOT NULL
│   ├─[REC]: supplier_Address1			varchar(150)
│   ├─[REC]: supplier_Address2			varchar(150)
│   ├─[REC]: supplier_Zip			varchar(15)
│   ├─[REC]: supplier_City			varchar(40)
│   ├─[REC]: country_Id				int
│   ├─[REC]: country_Code			varchar(4)
│   ├─[REC]: supplier_Url			varchar(255)
│   ├─[REC]: supplier_PhoneGeneral		varchar(40)
│   ├─[REC]: supplier_PhoneSales		varchar(40)
│   ├─[REC]: supplier_PhoneSupport		varchar(40)
│   ├─[REC]: supplier_MailGeneral		varchar(80)
│   ├─[REC]: supplier_MailSales			varchar(80)
│   ├─[REC]: supplier_MailSupport		varchar(80)
│   ├─[REC]: supplier_Memo			longtext
│   ├─[REC]: currency_Id			int
│   └─[REC]: currency_Code			varchar(4)
│
└─┬─[TBL]: worktypes
  └─┬─[REC]: worktypes_Id			int		NOT NULL	**PK**
    ├─[REC]: worktypes_Description		varchar(45)
    └─[REC]: worktypes_ParentId			int
```

## Create the database and use it

```mariadb
CREATE DATABASE IF NOT EXISTS `modelbuilder` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `modelbuilder`;
```

## Links to all tables

[Create and fill brand table](../../../../../Typora/ICT/C_/Modelbouwbeheer/Databases/Create%20and%20fill%20brand%20table.md)

[Create and fill category table](../../../../../Typora/ICT/C_/Modelbouwbeheer/Databases/Create%20and%20fill%20category%20table.md)

[Create and fill country table](../../../../../Typora/ICT/C_/Modelbouwbeheer/Databases/Create%20and%20fill%20country%20table.md)

[Create and fill product table](../../../../../Typora/ICT/C_/Modelbouwbeheer/Databases/Create%20and%20fill%20product%20table.md)

[Create and fill project table](../../../../../Typora/ICT/C_/Modelbouwbeheer/Databases/Create%20and%20fill%20project%20table.md)

[Create and fill storage table](../../../../../Typora/ICT/C_/Modelbouwbeheer/Databases/Create%20and%20fill%20storage%20table.md)

[Create and fill storagesupplier table](../../../../../Typora/ICT/C_/Modelbouwbeheer/Databases/Create%20and%20fill%20storagesupplier%20table.md)

[Create and fill supplier table](../../../../../Typora/ICT/C_/Modelbouwbeheer/Databases/Create%20and%20fill%20supplier%20table.md)

[Create and fill unit table](../../../../../Typora/ICT/C_/Modelbouwbeheer/Databases/Create%20and%20fill%20unit%20table.md)

[Create and fill worktype table](../../../../../Typora/ICT/C_/Modelbouwbeheer/Databases/Create%20and%20fill%20worktype%20table.md)
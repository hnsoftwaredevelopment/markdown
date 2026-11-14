# Create and fill unit table
Create and fill unit table

\[TOC\]

## Create table: unit

```mariadb
CREATE TABLE IF NOT EXISTS `unit` (
  `unit_Id` int NOT NULL AUTO_INCREMENT,
  `unit_Name` varchar(150) NOT NULL DEFAULT '0',
  PRIMARY KEY (`unit_Id`),
  UNIQUE KEY `unit_Name` (`unit_Name`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

## Fill table unit with base content

```mariadb
DELETE FROM `unit`;
/*!40000 ALTER TABLE `unit` DISABLE KEYS */;
INSERT INTO `unit` (`unit_Id`, `unit_Name`) VALUES
	(1, ''),
	(6, 'cm'),
	(11, 'dl'),
	(4, 'Fles'),
	(7, 'gr'),
	(9, 'kg'),
	(12, 'ltr'),
	(8, 'mgr'),
	(10, 'ml'),
	(5, 'mm'),
	(13, 'mtr'),
	(3, 'Set'),
	(2, 'Stuk');
```
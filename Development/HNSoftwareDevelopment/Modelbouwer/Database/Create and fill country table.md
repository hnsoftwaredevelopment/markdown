# Create and fill country table
Create and fill country table

\[TOC\]

## Create table: country

```mariadb
DROP TABLE IF EXISTS `country`;
CREATE TABLE IF NOT EXISTS `country` (
  `country_Id` int NOT NULL AUTO_INCREMENT,
  `country_Code` varchar(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `country_Defaultcurrency_Symbol` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '€',
  `country_Name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `country_Defaultcurrency_Id` int DEFAULT NULL,
  PRIMARY KEY (`country_Id`) USING BTREE,
  UNIQUE KEY `country_Code_UNIQUE` (`country_Code`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

## Fill table country with base content

```mariadb
DELETE FROM `country`;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` (`country_Id`, `country_Code`, `country_Defaultcurrency_Symbol`, `country_Name`, `country_Defaultcurrency_Id`) VALUES
	(1, 'NL', '€', 'Nederland', 1),
	(2, 'UK', '£', 'Engeland', 2),
	(3, 'US', '$', 'Verenigde staten', 3),
	(4, 'DE', '€', 'Duitsland', 1),
	(5, 'ESP', '€', 'Spanje', 1),
	(6, 'CH', 'Y', 'China', 4),
	(15, 'IT', '€', 'Italë', 1);
```
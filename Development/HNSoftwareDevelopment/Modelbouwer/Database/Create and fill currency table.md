# Create and fill currency table
Create and fill currency table

\[TOC\]

## Create table: currency

```mariadb
DROP TABLE IF EXISTS `currency`;
CREATE TABLE IF NOT EXISTS `currency` (
  `currency_Id` int NOT NULL AUTO_INCREMENT,
  `currency_Code` varchar(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `currency_Symbol` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `currency_Name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `currency_ConversionRate` float(6,4) DEFAULT NULL,
  PRIMARY KEY (`currency_Id`) USING BTREE,
  UNIQUE KEY `currency_Code` (`currency_Code`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

## Fill table currency with base content

```mariadb
DELETE FROM `currency`;
INSERT INTO `currency` (`currency_Id`, `currency_Code`, `currency_Symbol`, `currency_Name`, `currency_ConversionRate`) VALUES
	(1, 'EUR', '€', 'Euro', 1.0000),
	(2, 'GBP', '£', 'Britse pond', 1.1079),
	(3, 'USD', '$', 'Amerikaanse dollar', 0.8442),
	(4, 'YEN', 'Y', 'Yen', 3.3400),
	(5, 'TST', 'T', 'Testje', 1.2300);
```
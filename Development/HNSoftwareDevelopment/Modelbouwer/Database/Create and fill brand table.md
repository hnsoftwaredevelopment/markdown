# Create and fill brand table
Create and fill brand table

\[TOC\]

## Create table: brand

```mariadb
CREATE TABLE IF NOT EXISTS `brand` (
  `brand_Id` int NOT NULL AUTO_INCREMENT,
  `brand_Name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`brand_Id`),
  UNIQUE KEY `barnd_Name` (`brand_Name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='List of brands for tools, kits, suplies and all other stuf';
```

## fill table category with base content

```mariadb
DELETE FROM `brand`;
INSERT INTO `brand` (`brand_Id`, `brand_Name`) VALUES
	(17, 'Aeronaut'),
	(4, 'Amati'),
	(5, 'Artesania'),
	(12, 'Billing Boats'),
	(14, 'Caldercraft'),
	(15, 'Constructo'),
	(18, 'Corel'),
	(2, 'Dremel'),
	(3, 'Excel'),
	(10, 'Humbrol'),
	(16, 'Krick'),
	(6, 'Mantua'),
	(13, 'Model Shipways'),
	(7, 'Modelcraft'),
	(8, 'Occre'),
	(19, 'Panart'),
	(1, 'Proxxon'),
	(9, 'Revell'),
	(20, 'Sergal'),
	(11, 'Tamiya');
```
# Create and fill product table
Create and fill product table

\[TOC\]

## Create table: product

```mariadb
CREATE TABLE IF NOT EXISTS `product` (
  `product_Id` int NOT NULL AUTO_INCREMENT,
  `product_Code` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `product_Name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `product_CategoryId` int DEFAULT NULL,
  `product_CategoryName` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `product_SupplierId` int DEFAULT NULL,
  `product_SupplierName` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `product_SupplierProductNumber` varchar(20) DEFAULT NULL,
  `product_StorageId` int DEFAULT NULL,
  `product_StorageName` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `product_Price` int DEFAULT '0',
  `product_ProjectCosts` int NOT NULL DEFAULT '0',
  `product_MinimalStock` int DEFAULT NULL,
  `product_StandardOrderQuantity` int DEFAULT NULL,
  `product_BrandId` int DEFAULT NULL,
  `product_BrandName` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`product_Id`),
  UNIQUE KEY `product_Code` (`product_Code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

## Fill table product with base content

```mariadb
DELETE FROM `product`;
INSERT INTO `product` (`product_Id`, `product_Code`, `product_Name`, `product_CategoryId`, `product_CategoryName`, `product_SupplierId`, `product_SupplierName`, `product_SupplierProductNumber`, `product_StorageId`, `product_StorageName`, `product_Price`, `product_ProjectCosts`, `product_MinimalStock`, `product_StandardOrderQuantity`, `product_BrandId`, `product_BrandName`) VALUES
	(1, 'BANKSCHROEF', 'Proxxon Bankschroef', 510, 'Afwerkingerking', 1, 'Cornwall Model Boats Ltd', NULL, 1, 'Herberts Werf', 10500, 0, 0, 0, NULL, NULL);
```
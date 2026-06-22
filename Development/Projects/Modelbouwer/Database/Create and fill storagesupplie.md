# Create and fill storagesupplier table
Create and fill storagesupplier table

\[TOC\]

## Create table: storagesupplier

```mariadb
CREATE TABLE IF NOT EXISTS `storagesupplier` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `supplier_Id` int NOT NULL DEFAULT '0',
  `supplier_Name` varchar(150) DEFAULT NULL,
  `product_Id` int NOT NULL DEFAULT '0',
  `supplierProductNumber` varchar(150) DEFAULT NULL,
  `supplierProductName` varchar(150) DEFAULT NULL,
  `supplierProductPrice` float(10,2) DEFAULT '0.00',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='List for all products per supplier';
```

## Fill table storagesupplier with base content

```mariadb
DELETE FROM `storagesupplier`;
INSERT INTO `storagesupplier` (`Id`, `supplier_Id`, `supplier_Name`, `product_Id`, `supplierProductNumber`, `supplierProductName`, `supplierProductPrice`) VALUES
	(1, 1, 'Cornwall Model Boats Ltd', 1, '1234', 'Proxxon Vench', 29.95);
```
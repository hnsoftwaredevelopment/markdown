# Create and fill project table
Create and fill project table

\[TOC\]

## Create table: project

```mariadb
DROP TABLE IF EXISTS `project`;
CREATE TABLE IF NOT EXISTS `project` (
  `projects_Id` int NOT NULL AUTO_INCREMENT,
  `projects_Name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `projects_StartDate` date DEFAULT NULL,
  `projects_ExpectedEndDate` date DEFAULT NULL,
  `projects_EndDate` date DEFAULT NULL,
  `projects_TotalCost` decimal(5,2) DEFAULT NULL,
  `projects_TotalMinutes` int DEFAULT NULL,
  PRIMARY KEY (`projects_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

## Fill table project with base content

```mariadb
DELETE FROM `project`;
```
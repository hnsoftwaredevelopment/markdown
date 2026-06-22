# Category database
Category database

|Versie |Datum | |---|---|--- |4.1|09-02-2021|

```
-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server versie:                8.0.21 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Versie:              11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Structuur van  tabel modelbuilder.categories wordt geschreven
CREATE TABLE IF NOT EXISTS `categories` (
  `category_Id` int NOT NULL AUTO_INCREMENT,
  `category_ShortName` varchar(15) DEFAULT NULL,
  `category_Description` varchar(55) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `category_Fullpath` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `category_IsRoot` tinyint DEFAULT '1',
  `category_ParentId` int DEFAULT NULL,
  PRIMARY KEY (`category_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=614 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumpen data van tabel modelbuilder.categories: ~104 rows (ongeveer)
DELETE FROM `categories`;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` (`category_Id`, `category_ShortName`, `category_Description`, `category_Fullpath`, `category_IsRoot`, `category_ParentId`) VALUES
	(510, 'AFW', 'Afwerking', 'AFW', 1, NULL),
	(511, 'BRUI', 'Veroudering/Bruinering', 'AFW\\BRUI', 0, 510),
	(512, 'MASK', 'Maskering', 'AFW\\MASK', 0, 510),
	(513, 'PENS', 'Penselen', 'AFW\\PENS', 0, 510),
	(514, 'VERF', 'Verf', 'AFW\\VERF', 0, 510),
	(515, 'LAK', 'Lak', 'AFW\\LAK', 0, 510),
	(516, 'LIJM', 'Lijm', 'AFW\\LIJM', 0, 510),
	(517, 'HOUT', 'Houtlijm', 'AFW\\LIJM\\HOUT', 0, 516),
	(518, 'SEC', 'Secondenlijm', 'AFW\\LIJM\\SEC', 0, 516),
	(519, 'GER', 'Gereedschap', 'GER', 1, NULL),
	(520, 'ALG', 'Algemeen', 'GER\\ALG', 0, 519),
	(521, 'ACC', 'Accessoires', 'GER\\ALG\\ACC', 0, 520),
	(522, 'ELC', 'Elektrisch', 'GER\\ELC', 0, 519),
	(523, 'ACC', 'Accessoires', 'GER\\ELC\\ACC', 0, 522),
	(524, 'HAND', 'Hand', 'GER\\HAND', 0, 519),
	(525, 'ACC', 'Accessoires', 'GER\\HAND\\ACC', 0, 524),
	(526, 'MEET', 'Meetgereedschap', 'GER\\MEET', 0, 519),
	(527, 'ACC', 'Accessoires', 'GER\\MEET\\ACC', 0, 526),
	(528, 'HULP', 'Hulpmiddelen', 'HULP', 1, NULL),
	(529, 'OPB', 'Opbergmiddelen', 'HULP\\OPB', 0, 528),
	(530, 'SCHUUR', 'Schuurpapier', 'HULP\\SCHUUR', 0, 528),
	(531, 'MAT', 'Materiaal', 'MAT', 1, NULL),
	(532, 'BESL', 'Scheepsbeslag', 'MAT\\BESL', 0, 531),
	(533, 'ANKER', 'Ankers', 'MAT\\BESL\\ANKER', 0, 532),
	(534, 'BEELD', 'Boegbeelden', 'MAT\\BESL\\BEELD', 0, 532),
	(535, 'BEL', 'Scheepsbellen/hoorns', 'MAT\\BESL\\BEL', 0, 532),
	(536, 'BLOK', 'Blokken', 'MAT\\BESL\\BLOK', 0, 532),
	(537, 'BOLD', 'Kikkers/Bolders/Klampen', 'MAT\\BESL\\BOLD', 0, 532),
	(538, 'BOOT', 'Bijboten', 'MAT\\BESL\\BOOT', 0, 532),
	(539, 'DEK', 'Dekattributen', 'MAT\\BESL\\DEK', 0, 532),
	(540, 'KLOK', 'Scheepsklokken', 'MAT\\BESL\\KLOK', 0, 532),
	(541, 'LANT', 'Lantaarns', 'MAT\\BESL\\LANT', 0, 532),
	(542, 'MAST', 'Mastvoetten', 'MAT\\BESL\\MAST', 0, 532),
	(543, 'NAGEL', 'Korvijnagels(Belayingpins)', 'MAT\\BESL\\NAGEL', 0, 532),
	(544, 'OOG', 'Ogen', 'MAT\\BESL\\OOG', 0, 532),
	(545, 'PIN', 'Bevestigingspinnen', 'MAT\\BESL\\PIN', 0, 532),
	(546, 'POMP', 'Pompen', 'MAT\\BESL\\POMP', 0, 532),
	(547, 'POORT', 'Patrijspoorten', 'MAT\\BESL\\POORT', 0, 532),
	(548, 'RSTR', 'Roosters', 'MAT\\BESL\\RSTR', 0, 532),
	(549, 'SCHUT', 'Geschut', 'MAT\\BESL\\SCHUT', 0, 532),
	(550, 'STUUR', 'Stuurwielen', 'MAT\\BESL\\STUUR', 0, 532),
	(551, 'TRAP', 'Trappen', 'MAT\\BESL\\TRAP', 0, 532),
	(552, 'VLAG', 'Vlaggenmasten', 'MAT\\BESL\\VLAG', 0, 532),
	(553, 'WANT', 'Want/Mast/Geleiding', 'MAT\\BESL\\WANT', 0, 532),
	(554, 'BEUK', 'Beuken', 'MAT\\BEUK', 0, 531),
	(555, 'LAT', 'Lat', 'MAT\\BEUK\\LAT', 0, 554),
	(556, 'PLT', 'Plaat', 'MAT\\BEUK\\PLT', 0, 554),
	(557, 'PRF', 'Profiel', 'MAT\\BEUK\\PRF', 0, 554),
	(558, 'RND', 'Rond', 'MAT\\BEUK\\RND', 0, 554),
	(559, 'VIERK', 'Vierkant', 'MAT\\BEUK\\VIERK', 0, 554),
	(560, 'EIK', 'Eiken', 'MAT\\EIK', 0, 531),
	(561, 'LAT', 'Lat', 'MAT\\EIK\\LAT', 0, 560),
	(562, 'PLT', 'Plaat', 'MAT\\EIK\\PLT', 0, 560),
	(563, 'PRF', 'Profiel', 'MAT\\EIK\\PRF', 0, 560),
	(564, 'RND', 'Rond', 'MAT\\EIK\\RND', 0, 560),
	(565, 'VIERK', 'Vierkant', 'MAT\\EIK\\VIERK', 0, 560),
	(566, 'GAREN', 'Garen', 'MAT\\GAREN', 0, 531),
	(567, 'BEIGE', 'Beige', 'MAT\\GAREN\\BEIGE', 0, 566),
	(568, 'BRN', 'Bruin', 'MAT\\GAREN\\BRN', 0, 566),
	(569, 'WIT', 'Wit', 'MAT\\GAREN\\WIT', 0, 566),
	(570, 'ZWART', 'Zwart', 'MAT\\GAREN\\ZWRT', 0, 566),
	(571, 'KOP', 'Koper', 'MAT\\KOP', 0, 531),
	(572, 'DRD', 'Draad', 'MAT\\KOP\\DRD', 0, 571),
	(573, 'PLT', 'Plaat', 'MAT\\KOP\\PLT', 0, 571),
	(574, 'PRF', 'Profiel', 'MAT\\KOP\\PRF', 0, 571),
	(575, 'RND', 'Rond', 'MAT\\KOP\\RND', 0, 571),
	(576, 'STRP', 'Strip', 'MAT\\KOP\\STRP', 0, 571),
	(577, 'VIERK', 'Vierkant', 'MAT\\KOP\\VIERK', 0, 571),
	(578, 'KUNST', 'Kunststof', 'MAT\\KUNST', 0, 531),
	(579, 'PLT', 'Plaat', 'MAT\\KUNST\\PLT', 0, 578),
	(580, 'PRF', 'Profiel', 'MAT\\KUNST\\PRF', 0, 578),
	(581, 'RND', 'Rond', 'MAT\\KUNST\\RND', 0, 578),
	(582, 'STRP', 'Strip', 'MAT\\KUNST\\STRP', 0, 578),
	(583, 'VIERK', 'Vierkant', 'MAT\\KUNST\\VIERK', 0, 578),
	(584, 'MAH', 'Mahoni', 'MAT\\MAH', 0, 531),
	(585, 'LAT', 'Lat', 'MAT\\MAH\\LAT', 0, 584),
	(586, 'PLT', 'Plaat', 'MAT\\MAH\\PLT', 0, 584),
	(587, 'PRF', 'Profiel', 'MAT\\MAH\\PRF', 0, 584),
	(588, 'RND', 'Rond', 'MAT\\MAH\\RND', 0, 584),
	(589, 'VIERK', 'Vierkant', 'MAT\\MAH\\VIERK', 0, 584),
	(590, 'MESS', 'Messing', 'MAT\\MESS', 0, 531),
	(591, 'DRD', 'Draad', 'MAT\\MESS\\DRD', 0, 590),
	(592, 'PLT', 'Plaat', 'MAT\\MESS\\PLT', 0, 590),
	(593, 'PRF', 'Profiel', 'MAT\\MESS\\PRF', 0, 590),
	(594, 'RND', 'Rond', 'MAT\\MESS\\RND', 0, 590),
	(595, 'STRP', 'Strip', 'MAT\\MESS\\STRP', 0, 590),
	(596, 'VIERK', 'Vierkant', 'MAT\\MESS\\VIERK', 0, 590),
	(597, 'NOOT', 'Noten', 'MAT\\NOOT', 0, 531),
	(598, 'LAT', 'Lat', 'MAT\\NOOT\\LAT', 0, 597),
	(599, 'PLT', 'Plaat', 'MAT\\NOOT\\PLT', 0, 597),
	(600, 'PRF', 'Profiel', 'MAT\\NOOT\\PRF', 0, 597),
	(601, 'RND', 'Rond', 'MAT\\NOOT\\RND', 0, 597),
	(602, 'VIERK', 'Vierkant', 'MAT\\NOOT\\VIERK', 0, 597),
	(603, 'VUUR', 'Vuren', 'MAT\\VUUR', 0, 531),
	(604, 'LAT', 'Lat', 'MAT\\VUUR\\LAT', 0, 602),
	(605, 'PLT', 'Plaat', 'MAT\\VUUR\\PLT', 0, 602),
	(606, 'PRF', 'Profiel', 'MAT\\VUUR\\PRF', 0, 602),
	(607, 'RND', 'Rond', 'MAT\\VUUR\\RND', 0, 602),
	(608, 'VIERK', 'Vierkant', 'MAT\\VUUR\\VIERK', 0, 602),
	(609, 'ZEIL', 'Zeilen', 'MAT\\ZEIL', 0, 531),
	(610, 'BRN', 'Bruin', 'MAT\\ZEIL\\BRN', 0, 609),
	(611, 'CREME', 'Beige', 'MAT\\ZEIL\\CREME', 0, 609),
	(612, 'WIT', 'Wit', 'MAT\\ZEIL\\WIT', 0, 609),
	(613, 'ZWRT', 'Zwart', 'MAT\\ZEIL\\ZWRT', 0, 609);
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

```

CREATE DATABASE IF NOT EXISTS `ollivanders_flask`;
USE `ollivanders_flask`;

CREATE TABLE IF NOT EXISTS `items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `sellIn` int(11) NOT NULL,
  `quality` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DELETE FROM `items`;
INSERT INTO `items` (`name`, `sellIn`, `quality`) VALUES
	('+5 Dexterity Vest', 10, 20),
	('Aged Brie', 2, 0),
	('Elixir of the Mongoose', 5, 7),
	('Sulfuras, Hand of Ragnaros', 0, 80),
	('Sulfuras, Hand of Ragnaros', -1, 80),
	('Backstage passes to a TAFKAL80ETC concert', 15, 20),
	('Backstage passes to a TAFKAL80ETC concert', 10, 49),
	('Backstage passes to a TAFKAL80ETC concert', 5, 49),
	('Conjured Mana Cake', 3, 6);
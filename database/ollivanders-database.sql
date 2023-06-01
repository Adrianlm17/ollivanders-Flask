
CREATE DATABASE IF NOT EXISTS `ollivanders_flask`;
USE `ollivanders_flask`;

CREATE TABLE IF NOT EXISTS `items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `itemType` varchar(250) NOT NULL,
  `name` varchar(250) NOT NULL,
  `sellIn` int(11) NOT NULL,
  `quality` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DELETE FROM `items`;
INSERT INTO `items` (`itemType`,`name`, `sellIn`, `quality`) VALUES
	('NormalItem', '+5 Dexterity Vest', 10, 20),
	('AgedBrie', 'Aged Brie', 2, 0),
	('NormalItem', 'Elixir of the Mongoose', 5, 7),
	('Sulfuras', 'Sulfuras, Hand of Ragnaros', 0, 80),
	('Sulfuras', 'Sulfuras, Hand of Ragnaros', -1, 80),
	('Backstage', 'Backstage passes to a TAFKAL80ETC concert', 15, 20),
	('Backstage', 'Backstage passes to a TAFKAL80ETC concert', 10, 49),
	('Backstage', 'Backstage passes to a TAFKAL80ETC concert', 5, 49),
	('Conjured', 'Conjured Mana Cake', 3, 6);
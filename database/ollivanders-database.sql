
CREATE DATABASE IF NOT EXISTS `ollivanders_flask`;
USE `ollivanders_flask`;


CREATE TABLE IF NOT EXISTS `items` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(250) DEFAULT NULL,
  `sellIn` int(11) DEFAULT NULL,
  `quality` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


DELETE FROM `items`;
INSERT INTO `items` (`id`, `name`, `sellIn`, `quality`) VALUES
	(1, '+5 Dexterity Vest', 10, 20),
	(2, 'Aged Brie', 2, 0),
	(3, 'Elixir of the Mongoose', 5, 7),
	(4, 'Sulfuras, Hand of Ragnaros', 0, 80),
	(5, 'Sulfuras, Hand of Ragnaros', -1, 80),
	(6, 'Backstage passes to a TAFKAL80ETC concert', 15, 20),
	(7, 'Backstage passes to a TAFKAL80ETC concert', 10, 49),
	(8, 'Backstage passes to a TAFKAL80ETC concert', 5, 49),
	(9, 'Conjured Mana Cake', 3, 6);

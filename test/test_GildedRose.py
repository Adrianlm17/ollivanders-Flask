from domain.GildedRose import *
import pytest

@pytest.fixture
def gilded_rose():
    items = [
        Conjured("+5 Dexterity Vest", 10, 20),
        AgedBrie("Aged Brie", 2, 0),
        NormalItem("Elixir of the Mongoose", 5, 7),
        Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
        Sulfuras("Hand of Ragnaros", -1, 80),
        BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 15, 20),
        BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 10, 49),
        BackstagePasses("Backstage passes to a TAFKAL80ETC concert", 5, 49),
        Conjured("Conjured Mana Cake", 3, 6)
    ]
    return GildedRose(items)



# ----------------------- AGED BRIE ----------------------- 

@pytest.mark.test_Aged_Brie
def test_Aged_Brie(gilded_rose):
    assert str(gilded_rose.items[1]) == "Aged Brie, 2, 0"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[1]) == "Aged Brie, 1, 1"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[1]) == "Aged Brie, 0, 2"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[1]) == "Aged Brie, -1, 4"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[1]) == "Aged Brie, -2, 6"



# ----------------------- NORMAL ITEM ----------------------- 

@pytest.mark.test_Elixir
def test_Elixir(gilded_rose):
    assert str(gilded_rose.items[2]) == "Elixir of the Mongoose, 5, 7"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[2]) == "Elixir of the Mongoose, 4, 6"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[2]) == "Elixir of the Mongoose, 3, 5"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[2]) == "Elixir of the Mongoose, 2, 4"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[2]) == "Elixir of the Mongoose, 1, 3"



# ----------------------- SULFURAS ----------------------- 

@pytest.mark.test_Sulfuras
def test_Sulfuras(gilded_rose):
    assert str(gilded_rose.items[3]) == "Sulfuras, Hand of Ragnaros, 0, 80"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[3]) == "Sulfuras, Hand of Ragnaros, 0, 80"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[3]) == "Sulfuras, Hand of Ragnaros, 0, 80"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[3]) == "Sulfuras, Hand of Ragnaros, 0, 80"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[3]) == "Sulfuras, Hand of Ragnaros, 0, 80"

@pytest.mark.test_Sulfuras_dos
def test_Sulfuras_dos(gilded_rose):
    assert str(gilded_rose.items[4]) == "Hand of Ragnaros, -1, 80"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[4]) == "Hand of Ragnaros, -1, 80"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[4]) == "Hand of Ragnaros, -1, 80"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[4]) == "Hand of Ragnaros, -1, 80"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[4]) == "Hand of Ragnaros, -1, 80"



# ----------------------- BACKSTAGE PASSES ----------------------- 

@pytest.mark.test_BackstagePasses
def test_BackstagePasses(gilded_rose):
    assert str(gilded_rose.items[5]) == "Backstage passes to a TAFKAL80ETC concert, 15, 20"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[5]) == "Backstage passes to a TAFKAL80ETC concert, 14, 21"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[5]) == "Backstage passes to a TAFKAL80ETC concert, 13, 22"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[5]) == "Backstage passes to a TAFKAL80ETC concert, 12, 23"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[5]) == "Backstage passes to a TAFKAL80ETC concert, 11, 24"

@pytest.mark.test_BackstagePasses_dos
def test_BackstagePasses_dos(gilded_rose):
    assert str(gilded_rose.items[6]) == "Backstage passes to a TAFKAL80ETC concert, 10, 49"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[6]) == "Backstage passes to a TAFKAL80ETC concert, 9, 50"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[6]) == "Backstage passes to a TAFKAL80ETC concert, 8, 50"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[6]) == "Backstage passes to a TAFKAL80ETC concert, 7, 50"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[6]) == "Backstage passes to a TAFKAL80ETC concert, 6, 50"

@pytest.mark.test_BackstagePasses_tres
def test_BackstagePasses_tres(gilded_rose):
    assert str(gilded_rose.items[7]) == "Backstage passes to a TAFKAL80ETC concert, 5, 49"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[7]) == "Backstage passes to a TAFKAL80ETC concert, 4, 50"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[7]) == "Backstage passes to a TAFKAL80ETC concert, 3, 50"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[7]) == "Backstage passes to a TAFKAL80ETC concert, 2, 50"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[7]) == "Backstage passes to a TAFKAL80ETC concert, 1, 50"



# ----------------------- CONJURED ----------------------- 
 
@pytest.mark.test_Conjured
def test_Conjured(gilded_rose):
    assert str(gilded_rose.items[8]) == "Conjured Mana Cake, 3, 6"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[8]) == "Conjured Mana Cake, 2, 4"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[8]) == "Conjured Mana Cake, 1, 2"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[8]) == "Conjured Mana Cake, 0, 0"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[8]) == "Conjured Mana Cake, -1, 0"

@pytest.mark.test_Conjured_dos
def test_Conjured_dos(gilded_rose):
    assert str(gilded_rose.items[0]) == "+5 Dexterity Vest, 10, 20"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[0]) == "+5 Dexterity Vest, 9, 18"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[0]) == "+5 Dexterity Vest, 8, 16"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[0]) == "+5 Dexterity Vest, 7, 14"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[0]) == "+5 Dexterity Vest, 6, 12"
    gilded_rose.updateGildedRose()
    assert str(gilded_rose.items[0]) == "+5 Dexterity Vest, 5, 10"

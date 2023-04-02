class GildedRose:

    def __init__(self, items):
        
        self.items = items
        
    def updateGildedRose(self):

        for item in self.items:
            item.updateQuality()


class Item:

    def __init__(self, name, sellIn, quality):
        
        self.name = name
        self.sellIn = sellIn
        self.quality = quality


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sellIn, self.quality)
    


class NormalItem(Item):

    def __init__(self, name, sellIn, quality):

        Item.__init__(self, name, sellIn, quality)
    
    
    def setSellIn(self):

        self.sellIn = self.sellIn - 1
    

    def setQuality(self, price):

        if self.quality + price > 50:
            self.quality = 50

        elif 50 >= self.quality + price >= 0:
            self.quality += price

        else:
            self.quality = 0


    def updateQuality(self):

        if self.sellIn > 0:
            self.setQuality(-1)

        else:
            self.setQuality(-2)
            
        self.setSellIn()



class AgedBrie(NormalItem):
    
    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)


    def updateQuality(self):
        if self.sellIn > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)

        self.setSellIn()



class BackstagePasses(NormalItem):

    def __init__(self, name, sellIn, quality):   
        NormalItem.__init__(self, name, sellIn, quality)

    def updateQuality(self):

        if self.sellIn < 0:
            self.quality = 0

        elif self.sellIn <= 5:
            self.setQuality(3)

        elif self.sellIn <= 10:
            self.setQuality(2)
            
        else:
            self.setQuality(1)

        self.setSellIn()



class Conjured(NormalItem):

    def __init__(self, name, sellIn, quality):
        NormalItem.__init__(self, name, sellIn, quality)


    def updateQuality(self):
        
        if self.sellIn >= 0:
            self.setQuality(-2)

        self.setSellIn()



class Sulfuras(NormalItem):

    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)

    
    def updateQuality(self):    
        pass

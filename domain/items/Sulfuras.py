from domain.items.NormalItem import NormalItem, Item

class Sulfuras(NormalItem):

    def __init__(self, name, SellIn, quality):
        Item.__init__(self, name, SellIn, quality)

    
    def updateQuality(self):    
        pass
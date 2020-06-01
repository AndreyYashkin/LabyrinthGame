from enum import Enum


class Item(Enum): # TODO все-же нужно что-то другое, а не Enum. Добавление новых item'ов не очень гибкое
    KEY = 0
    BOAT = 1
    GUN = 2
    KNIFE = 3
    GRENADE = 4
    
    def code(self):
        return self.name().upper()
    
    
    def name(self):
        if self == Item.KEY:
            return 'Key'
        elif self == Item.BOAT:
            return 'Boat'
        elif self == Item.GUN:
            return 'Gun'
        elif self == Item.KNIFE:
            return 'Knife'
        elif self == Item.GRENADE:
            return 'Grenade'    
    
    
    @staticmethod
    def itemFromCode(itemCode):
        for item in Item:
            if itemCode == item.code():
                return item

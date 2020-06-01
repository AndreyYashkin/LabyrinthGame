from .abstractentity import AbstractEntity
from enum import Enum


# TODO как-то переделать текст сообщения о сборе предметов, чтобы не нужно было использовать his/her
class Sex(Enum):
    FEMALE = 0
    MALE = 1


class Player(AbstractEntity):
    def __init__(self, name, sex : Sex, logger, cell):
        self.sex = sex # FIXME если это поставить после __init__, то будет краш т.к. это в collectItems используется
        AbstractEntity.__init__(self, name, logger, True, True, cell)
        self.permanentProperties['canBeMovedByCell'] = True
        
    
    @staticmethod
    def entityType(self):
        return 'Player'
    
    
    def onCellEntrance(self):
        self.collectItems()
    
    
    def collectItems(self): # TODO обощить и перенести в AbstractEntity по обрзцу removeFromInventory
        toCollect = set()
        alreadyInInventory = set()
        for item in self.cell.itemsInCell:
            if item not in self.inventory:
                toCollect.add(item)
            else:
                alreadyInInventory.add(item)
        
        self.cell.itemsInCell.difference_update(toCollect)
        
        self.inventory.update(toCollect)
        toCollectNames = [item.name() for item in toCollect]
        message = '{0} collects {1}'.format(self.name, toCollectNames)
        if len(toCollect) > 0:
            alreadyInInventoryNames = [item.name() for item in alreadyInInventory]
            if self.sex == Sex.FEMALE:
                word = 'her'
            else:
                word = 'his'
            message += ', while {0} are already in {1} inventory'.format(alreadyInInventoryNames, word)
            self.logger.sendMessage(self, message)
    
    
    def kill(self):
        self.throwAwayInventory
        self.cell.entitiesInside.remove(self)
        self.permanentProperties.clear()
        self.permanentProperties['dead'] = True
        self.cell = None

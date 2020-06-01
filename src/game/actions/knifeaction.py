from .abstractaction import AbstractAction
from ..mapobjects.direction import Direction
from ..mapobjects.entities.knife import Knife
from ..mapobjects.item import Item


class KnifeAction(AbstractAction):
    def __init__(self):
        AbstractAction.__init__(self)


    @staticmethod
    def actionCode():
        return 'KNIFE'
    
    
    @staticmethod
    def actionName():
        return 'Knife attack'
    
    
    def doAction(self, entity, paramCode):
        entity.logger.sendMessage(entity, 'Knife attack ')
        if Item.KNIFE not in entity.inventory:
            entity.logger.sendMessage(entity, 'No knife in inventory!')
        else:
            knife = Knife(entity, entity.logger, entity.cell)
            del knife # Циклические ссылки
    
    
    def getParamNames(self):
        return ['None']
    
    
    def getParamCodeFromName(self, paramName):
        return 'NONE'

from .abstractaction import AbstractAction
from ..mapobjects.direction import Direction
from ..mapobjects.entities.grenade import Grenade
from ..mapobjects.item import Item

class GrenadeAction(AbstractAction):
    def __init__(self):
        AbstractAction.__init__(self)
        directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        self.paramNames = [d.name() for d in directions]
        self.paramNameToCode = dict()
        for d in Direction:
            self.paramNameToCode[d.name()] = d.code()


    @staticmethod
    def actionCode():
        return 'GRENADE'
    
    
    @staticmethod
    def actionName():
        return 'Grenade'
    
    
    def doAction(self, entity, paramCode):
        entity.logger.sendMessage(entity, 'Grenade ' + paramCode)
        if Item.GRENADE not in entity.inventory:
            entity.logger.sendMessage(entity, 'No grenade in inventory!')
        else:
            direction = Direction.directionFromCode(paramCode)
            grenade = Grenade(entity.logger, entity.cell, direction) # TODO сообщения что нет стены и разные прочие проврки должны делаться тут
            del grenade # Циклические ссылки
    
    
    def getParamNames(self):
        return self.paramNames
    
    
    def getParamCodeFromName(self, paramName):
        return self.paramNameToCode[paramName]

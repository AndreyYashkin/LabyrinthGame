from .abstractaction import AbstractAction
from ..mapobjects.direction import Direction
from ..mapobjects.entities.bullet import Bullet
from ..mapobjects.item import Item


class FireGunAction(AbstractAction):
    def __init__(self):
        AbstractAction.__init__(self)
        directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        self.paramNames = [d.name() for d in directions]
        self.paramNameToCode = dict()
        for d in Direction:
            self.paramNameToCode[d.name()] = d.code()


    @staticmethod
    def actionCode():
        return 'FIREGUN'
    
    
    @staticmethod
    def actionName():
        return 'Fire gun'
    
    
    def doAction(self, entity, paramCode):
        if Item.GUN not in entity.inventory:
            entity.logger.sendMessage(entity, 'No gun in inventory!')
        else:
            entity.logger.sendMessage(entity, 'Fire gun ' + paramCode)
            direction = Direction.directionFromCode(paramCode)
            bullet = Bullet(entity, entity.logger, entity.cell, direction)
            del bullet # Циклические ссылки
    
    
    def getParamNames(self):
        return self.paramNames
    
    
    def getParamCodeFromName(self, paramName):
        return self.paramNameToCode[paramName]

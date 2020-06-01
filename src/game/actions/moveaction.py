from .abstractaction import AbstractAction
from ..mapobjects.direction import Direction


class MoveAction(AbstractAction):
    def __init__(self):
        AbstractAction.__init__(self)
        self.paramNames = [d.name() for d in Direction]
        self.paramNameToCode = dict()
        for d in Direction:
            self.paramNameToCode[d.name()] = d.code()


    @staticmethod
    def actionCode():
        return 'MOVE'
    
    
    @staticmethod
    def actionName():
        return 'Move'
    
    
    def doAction(self, entity, paramCode):
        entity.logger.sendMessage(entity, 'Move ' + paramCode)
        direction = Direction.directionFromCode(paramCode)
        entity.move(direction)
    
    
    def getParamNames(self):
        return self.paramNames
    
    
    def getParamCodeFromName(self, paramName):
        return self.paramNameToCode[paramName]

from .abstractaction import AbstractAction


class BoatAction(AbstractAction):
    def __init__(self):
        AbstractAction.__init__(self)
        self.paramNames = ['On', 'Off']
        self.paramNameToCode = {'On' : 'ON', 'Off' : 'OFF'}


    @staticmethod
    def actionCode():
        return 'BOAT'
    
    
    @staticmethod
    def actionName():
        return 'Use boat'
    
    
    def doAction(self, entity, paramCode):
        # TODO в rivercell этот момент надо согласовать
        entity.logger.sendMessage('Boat ' + paramCode)
    
    
    def getParamNames(self):
        return self.paramNames
    
    
    def getParamCodeFromName(self, paramName):
        return self.paramNameToCode[paramName]

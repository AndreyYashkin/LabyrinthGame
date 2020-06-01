from .abstractaction import AbstractAction


class PassAction(AbstractAction):
    def __init__(self):
        AbstractAction.__init__(self)


    @staticmethod
    def actionCode():
        return 'PASS'
    
    
    @staticmethod
    def actionName():
        return 'Pass'
    
    
    def doAction(self, entity, paramCode):
        entity.logger.sendMessage(entity, 'Pass')
    
    
    def getParamNames(self):
        return ['None']
    
    
    def getParamCodeFromName(self, paramName):
        return 'NONE'

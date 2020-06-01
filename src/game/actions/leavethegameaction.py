from .abstractaction import AbstractAction


class LeaveTheGameAction(AbstractAction):
    def __init__(self):
        AbstractAction.__init__(self)


    @staticmethod
    def actionCode():
        return 'LEAVE'
    
    
    @staticmethod
    def actionName():
        return 'Leave'
    
    
    def doAction(self, entity, paramCode):
        entity.logger.sendMessage(None, 'NO REALISATION')
        
    
    
    def getParamNames(self):
        return ['None']
    
    
    def getParamCodeFromName(self, paramName):
        return 'NONE'

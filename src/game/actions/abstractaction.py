from abc import ABC, abstractmethod


class AbstractAction(ABC):
    def __init__(self):
        pass
    
    
    @staticmethod
    @abstractmethod
    def actionCode():
        pass
    
    
    @staticmethod
    @abstractmethod
    def actionName():
        pass
    
    
    @abstractmethod
    def doAction(self, entity, paramCode):
        pass
    
    
    @abstractmethod
    def getParamNames(self):
        pass
    
    
    @abstractmethod
    def getParamCodeFromName(self, paramName):
        pass

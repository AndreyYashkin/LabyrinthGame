from abc import ABC, abstractmethod
from ..direction import Direction


class AbstractEntity(ABC):
    # NOTE каждый экземпляр класса должен быть удален через del, т.к. между клеткой и сущностью существуют перекресные ссылки
    # TODO надо переделать, чтобы при создании клетка не задавалась. 
    def __init__(self, name, logger, sendMoveLogs, sendInventoryLogs, cell):
        self.name = name
        self.logger = logger
        self.sendMoveLogs = sendMoveLogs
        self.sendInventoryLogs = sendInventoryLogs
        self.inventory = set()
        self.turnProperties = dict()
        self.permanentProperties = dict()
        self.cell = None
        
        self.putIn(cell) # TODO от этого надо избавиться и делать это вне конструктора
    
    
    def __del__(self):
        try:
            self.cell.entitiesInside.remove(self)
        except ValueError: # если по каким-то причинам в клетке эта сущность не числится
            pass
        self.cell = None
    
    
    @staticmethod
    @abstractmethod
    def entityType(self):
        pass
    
    
    def move(self, direction : Direction):
        self.cell.move(self, direction)
    
    
    # медведь не может собирать, а игрок может
    @abstractmethod
    def onCellEntrance(self):
        pass
    
    
    def removeFromInventory(self, item):
        self.inventory.discard(item)
        if self.sendInventoryLogs:
            self.logger.sendMessage(self, item.name() + ' was removed from inventory')
    
    
    def throwAwayInventory(self):
        # TODO мб тут тоже сообщения нужны
        self.cell.itemInCells.update(self.inventory)
        self.inventory.clear()
    
    
    def kill(self):
        pass
    
    
    # считается, что сущность не находится ни в одной клетке
    def putIn(self, cell):
        self.cell = cell
        cell.entitiesInside.append(self)
        self.onCellEntrance()

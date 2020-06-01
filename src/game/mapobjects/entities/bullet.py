import random
from .abstractentity import AbstractEntity
from ..direction import Direction


class Bullet(AbstractEntity):
    def __init__(self, swapnerName, logger, cell, direction : Direction):
        # FIXME self.permanentProperties инициализруются только в AbstractEntity.__init__
        self.permanentProperties['canBeMovedByCell'] = False
        self.haveKilled = False
        AbstractEntity.__init__(self, swapnerName, logger, True, True, cell)
        self.move(direction)
        
    
    @staticmethod
    def entityType(self):
        return 'Bullet'
    
    
    def onCellEntrance(self):
        candidates = []
        for c in self.cell.entitiesInside:
            if c.name != self.name:
                candidates.append(c)
        if len(candidates) == 0:
            return
        c = random.choice(candidates)
        c.kill()
        self.haveKilled = True
        
    
    def move(self, direction : Direction):
        if self.cell.canMove(self, direction):
            self.cell.move(self, direction)
            if not self.haveKilled:
                self.move(direction)

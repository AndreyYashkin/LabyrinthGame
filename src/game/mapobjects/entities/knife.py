from .abstractentity import AbstractEntity
import random


class Knife(AbstractEntity):
    def __init__(self, swapnerName, logger, cell):
        # FIXME self.permanentProperties инициализруются только в AbstractEntity.__init__
        self.permanentProperties['canBeMovedByCell'] = False
        AbstractEntity.__init__(self, swapnerName, logger, True, True, cell)
    
    
    @staticmethod
    def entityType(self):
        return 'Knife'
    
    
    def onCellEntrance(self):
        candidates = []
        for c in self.cell.entitiesInside:
            if c.name != self.name:
                candidates.append(c)
        if len(candidates) == 0:
            return
        c = random.choice(candidates)
        c.kill()
    
    
    def collectItems(self):
        pass

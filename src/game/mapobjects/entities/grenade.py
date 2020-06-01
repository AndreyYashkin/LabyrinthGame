from .abstractentity import AbstractEntity
from ..direction import Direction


class Grenade(AbstractEntity):
    def __init__(self, logger, cell, direction : Direction):
        self.direction = direction
        # self.permanentProperties['canBeMovedByCell'] = False
        AbstractEntity.__init__(self, 'Grenade', logger, False, False, cell)
    
    
    @staticmethod
    def entityType(self):
        return 'Grenade'
    
    
    def onCellEntrance(self):
        if self.cell.separators[self.direction].wall:
            self.cell.separators[self.direction].wall = False
            self.logger.sendMessage(None, 'A wall was destroyed')
        else:
            self.logger.sendMessage(None, 'There is no wall to destroy')

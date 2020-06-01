from .direction import Direction


class Separator:
    def __init__(self, connectedCells, wall):
        self.connectedCells = connectedCells
        self.wall = wall
        if connectedCells.get(Direction.UP, None):
            connectedCells[Direction.UP].separators[Direction.DOWN] = self
        if connectedCells.get(Direction.DOWN, None):
            connectedCells[Direction.DOWN].separators[Direction.UP] = self
        if connectedCells.get(Direction.RIGHT, None):
            connectedCells[Direction.RIGHT].separators[Direction.LEFT] = self
        if connectedCells.get(Direction.LEFT, None):
            connectedCells[Direction.LEFT].separators[Direction.RIGHT] = self
    
    
    def cell(self, direction : Direction):
        return self.connectedCells.get(direction, None)
    
    
    def canCross(self, entity): #
        if self.wall:
            if entity.sendMoveLogs:
                entity.logger.sendMessage(entity, 'Step impossible, wall')
            return False
        else:
            return True # self.connectedCells[direction].enter(entity)

from enum import Enum


class Direction(Enum):
    NONE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    

    def code(self):
        return self.name().upper()
    

    def name(self):
        if self == Direction.NONE:
            return 'None'
        elif self == Direction.UP:
            return 'Up'
        elif self == Direction.DOWN:
            return 'Down'
        elif self == Direction.LEFT:
            return 'Left'
        elif self == Direction.RIGHT:
            return 'Right'    
    
    
    @staticmethod
    def directionFromCode(directionCode):
        for direction in Direction:
            if directionCode == direction.code():
                return direction

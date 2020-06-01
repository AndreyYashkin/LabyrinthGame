from .mapobjects.cells.arsenalcell import ArsenalCell
from .mapobjects.cells.emptycell import EmptyCell
from .mapobjects.cells.exitcell import ExitCell
from .mapobjects.cells.hospitalcell import HospitalCell
from .mapobjects.cells.monolithcell import MonolithCell
from .mapobjects.cells.rivercell import RiverCell
from .mapobjects.cells.wormholecell import WormholeСell
from .mapobjects.separator import Separator
from .mapobjects.direction import Direction
from .mapobjects.item import Item


class Labyrinth:
    def __init__(self, prop):# , logger): ??? 
        self.size_n = prop['size_n']
        self.size_m = prop['size_m']
        self.cells = dict() # TODO заменить нормальным двухмерном массивом
        self.separators = dict()
        self.hospitals = list()
        self.wormholesCoord = dict()
        self.spawns = dict()
        self.NPCList = list()
        self.starts = list()
        
        for i in range(self.size_n):
            for j in range(self.size_m):
                cell = prop['cell_{}_{}'.format(i, j)]
                cellType = cell.get('cellType', MonolithCell.cellType())
                # TODO сделать чтобы было через список классов в конструкторе, а не прибито гвоздями, как сейчас
                if cellType == ArsenalCell.cellType():
                    itemsInArsenalCodes = cell.get('itemsInArsenal', list())
                    itemsInArsenal = [Item.itemFromCode(itemCode) for itemCode in itemsInArsenalCodes]
                    self.cells[(i, j)] = ArsenalCell(set(itemsInArsenal))
                elif cellType == EmptyCell.cellType():
                    self.cells[(i, j)] = EmptyCell()
                elif cellType == ExitCell.cellType():
                    self.cells[(i, j)] = ExitCell()
                elif cellType == HospitalCell.cellType():
                    self.cells[(i, j)] = HospitalCell()
                    self.hospitals.append((i, j))
                elif cellType == MonolithCell.cellType():
                    self.cells[(i, j)] = MonolithCell()
                elif cellType == RiverCell.cellType():
                    directionCode = cell.get('direction', Direction.UP.code())
                    direction = Direction.directionFromCode(directionCode)
                    self.cells[(i, j)] = RiverCell(direction)
                elif cellType == WormholeСell.cellType():
                    self.wormholesCoord[(i, j)] = (cell['next_i'], cell['next_j']) # TODO не безопасно
                    self.cells[(i, j)] = WormholeСell()
                #else:
                #    print('#', cellType)
                
                itemsInCellCodes = cell.get('itemsInCell', list())
                itemsInCell = [Item.itemFromCode(itemCode) for itemCode in itemsInCellCodes]
                self.cells[(i, j)].itemsInCell.update(set(itemsInCell))
                
                if cell.get('start_point', False) == True:
                    self.starts.append(self.cells[(i, j)])
                # DEBUG
                # self.cells[(i, j)].c1 = str(i)
                # self.cells[(i, j)].c2 = str(j)
        
        for coord in self.wormholesCoord:
            self.cells[coord].nextWormhole = self.cells[self.wormholesCoord[coord]]
        
        for i in range(1, self.size_n): # по другому надо проходить
            for j in range(1, self.size_m):
                cell = prop['cell_{}_{}'.format(i, j)]
                left = ((i, j - 1), (i, j))
                down = ((i - 1, j), (i, j))
                
                connectedCells = {Direction.DOWN : self.cells[(i - 1, j)], Direction.UP : self.cells[(i, j)]}
                self.separators[left] = Separator(connectedCells, cell.get('down_wall', False))
                connectedCells = {Direction.LEFT : self.cells[(i, j - 1)], Direction.RIGHT : self.cells[(i, j)]}
                self.separators[down] = Separator(connectedCells, cell.get('left_wall', False))
                
    
    def __del__(self):
        # надо удалять в ручную или счетчик ссылок сам не станет равен 0 из-за цикличных ссылок
        for i in range(1, self.size_n-1):
            for j in range(1, self.size_m-1):
                left = ((i, j - 1), (i, j))
                down = ((i - 1, j), (i, j))
                del self.separators[left]     
                del self.separators[down]
    
    
    def processNPC(self):
        # TODO
        pass

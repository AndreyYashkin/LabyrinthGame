from PySide2.QtWidgets import QGridLayout, QWidget, QFrame, QAbstractButton, QSizePolicy
from PySide2.QtGui import QPainter, QFont
from PySide2.QtCore import Qt, Signal, Slot

from ..game.mapobjects.cells.arsenalcell import ArsenalCell
from ..game.mapobjects.cells.emptycell import EmptyCell
from ..game.mapobjects.cells.exitcell import ExitCell
from ..game.mapobjects.cells.hospitalcell import HospitalCell
from ..game.mapobjects.cells.monolithcell import MonolithCell
from ..game.mapobjects.cells.rivercell import RiverCell
from ..game.mapobjects.cells.wormholecell import WormholeСell


class CellButton(QAbstractButton):
    def __init__(self, parent=None):
        QAbstractButton.__init__(self, parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.properties = dict()
        self.repaint()
    
    
    def paintEvent(self, event):
        painter = QPainter(self)
        # TODO сделать, чтобы это все не было прибито на гвоздях.
        # Можно как-то обыграть через список классов в качестве параметра конструктора
        cellType = self.properties.get('cellType', MonolithCell.cellType())
        if cellType == ArsenalCell.cellType():
            ArsenalCell.paintCellWidget(painter, event.rect(), self.properties)
        elif cellType == EmptyCell.cellType():
            EmptyCell.paintCellWidget(painter, event.rect(), self.properties)
        elif cellType == ExitCell.cellType():
            ExitCell.paintCellWidget(painter, event.rect(), self.properties)
        elif cellType == HospitalCell.cellType():
            HospitalCell.paintCellWidget(painter, event.rect(), self.properties)
        elif cellType == MonolithCell.cellType():
            MonolithCell.paintCellWidget(painter, event.rect(), self.properties)
        elif cellType == RiverCell.cellType():
            RiverCell.paintCellWidget(painter, event.rect(), self.properties)
        else: # WormholeСell
            WormholeСell.paintCellWidget(painter, event.rect(), self.properties)
    
    
    # TODO
    # size hint & setSizePolicy поменять
    
    
    def setProperties(self, properties : dict):
        self.properties = properties
        
    

class CellWithWalls(QWidget): #TODO мб сделать метод для извечения свойств?
    openEditor = Signal(list) # siglanl(i, j)
    def __init__(self, i, j, parent=None):
        QWidget.__init__(self, parent)
        
        self.i = i
        self.j = j
        
        self.cellButton = CellButton(self)
        self.cellButton.setToolTip('i={}, j={}'.format(i, j))
        
        self.downWall = QFrame(self)
        self.downWall.setFrameShape(QFrame.HLine)
        self.downWall.setLineWidth(3)
        sizePolicy = self.downWall.sizePolicy()
        sizePolicy.setRetainSizeWhenHidden(True)
        self.downWall.setSizePolicy(sizePolicy)
        self.downWall.setVisible(False)
        
        self.leftWall = QFrame(self)
        self.leftWall.setFrameShape(QFrame.VLine)
        self.leftWall.setLineWidth(3)
        sizePolicy = self.leftWall.sizePolicy()
        sizePolicy.setRetainSizeWhenHidden(True)
        self.leftWall.setSizePolicy(sizePolicy)
        self.leftWall.setVisible(False)
        
        layout = QGridLayout()
        layout.addWidget(self.downWall, 1, 1)
        layout.addWidget(self.leftWall, 0, 0)
        layout.addWidget(self.cellButton, 0, 1)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(layout)
        
        self.cellButton.clicked.connect(self.onCellButtonClicked)
        
    
    @Slot() 
    def onCellButtonClicked(self):
        self.openEditor.emit([self.i, self.j])   
        
    
    def setProperties(self, properties : dict):
        self.leftWall.setVisible(properties.get('left_wall', False))
        self.downWall.setVisible(properties.get('down_wall', False))
        self.cellButton.setProperties(properties)
        self.update()
    
    
    def getProperties(self):
        return self.cellButton.properties

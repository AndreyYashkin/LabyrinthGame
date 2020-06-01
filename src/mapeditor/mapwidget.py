from PySide2.QtWidgets import QGridLayout, QWidget
from PySide2.QtGui import QPainter, QFont
from PySide2.QtCore import Qt, Signal, Slot
from .cellwithwalls import CellWithWalls


class MapWidget(QWidget):
    openEditor = Signal(list) # siglanl(i, j)
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.n = 0
        self.m = 0
        self.widgets = dict()
        self.mapProperties = dict()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
    
    
    def resetMap(self, mapProperties):
       
        for index in self.widgets:
            self.widgets[index].deleteLater()
            
        self.widgets.clear()
        self.mapProperties.clear()
        
        self.n = mapProperties.get('size_n', 0)
        self.m = mapProperties.get('size_m', 0)
        for i in range(self.n):
            for j in range(self.m):
                widget = CellWithWalls(i, j, self)
                self.widgets[(i, j)] = widget
                self.layout.addWidget(widget, self.n - 1 -i, j)
                self.updateCell(i, j, mapProperties.get('cell_{}_{}'.format(i, j), dict()))
                self.widgets[(i, j)].openEditor.connect(self.openEditor)
    
    
    def updateCell(self, i, j, cellProperties : dict):
        self.widgets[(i, j)].setProperties(cellProperties)
    
    
    def getCellProperties(self, i, j):
        return self.widgets[(i, j)].getProperties()
        
    
    def getProperties(self):
        mapProperties = dict()
        mapProperties['size_n'] = self.n
        mapProperties['size_m'] = self.m
        for i in range(self.n):
            for j in range(self.m):
                mapProperties['cell_{}_{}'.format(i, j)] = self.getCellProperties(i, j)
        return mapProperties

from PySide2.QtWidgets import QFormLayout, QWidget, QComboBox, QStackedWidget
from PySide2.QtCore import Signal, Slot
from .editwidgets.basecelleditorwidget import BaseCellEditorWidget
from ..game.mapobjects.cells.arsenalcell import ArsenalCell
from ..game.mapobjects.cells.emptycell import EmptyCell
from ..game.mapobjects.cells.exitcell import ExitCell
from ..game.mapobjects.cells.hospitalcell import HospitalCell
from ..game.mapobjects.cells.monolithcell import MonolithCell
from ..game.mapobjects.cells.rivercell import RiverCell
from ..game.mapobjects.cells.wormholecell import WormholeСell


'''
class StackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent)
    
    
    @Slot(int)                                                                                                                 
    def setCurrentIndex(self, index):
        #params = self.currentWidget()
        QStackedWidget.setCurrentIndex(self, index)
        self.currentWidget().setProperties(dict())
'''

    
class CellEditor(QWidget):
    updateCell = Signal()
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        layout = QFormLayout()
        self.setLayout(layout)
        
        self.cellType = QComboBox(self)              
                                
        layout.addRow('Cell type:', self.cellType)
        
        self.baseCellEditorWidget = BaseCellEditorWidget(self)
        layout.addRow(self.baseCellEditorWidget)
        
        self.stackedWidget = QStackedWidget(self)
        layout.addRow(self.stackedWidget)
        
        # TODO как то покрасивее сделать
        self.cellType.addItem(ArsenalCell.cellType())
        self.stackedWidget.addWidget(ArsenalCell.cellEditorWidget())
        self.cellType.addItem(EmptyCell.cellType())
        self.stackedWidget.addWidget(EmptyCell.cellEditorWidget())
        self.cellType.addItem(ExitCell.cellType())
        self.stackedWidget.addWidget(ExitCell.cellEditorWidget())
        self.cellType.addItem(HospitalCell.cellType())
        self.stackedWidget.addWidget(HospitalCell.cellEditorWidget())
        self.cellType.addItem(MonolithCell.cellType())
        self.stackedWidget.addWidget(HospitalCell.cellEditorWidget())
        self.cellType.addItem(RiverCell.cellType())
        self.stackedWidget.addWidget(RiverCell.cellEditorWidget())
        self.cellType.addItem(WormholeСell.cellType())  
        self.stackedWidget.addWidget(WormholeСell.cellEditorWidget())
        
        self.cellType.currentIndexChanged.connect(self.stackedWidget.setCurrentIndex)
        self.cellType.currentIndexChanged.connect(self.updateCell)
        self.baseCellEditorWidget.update.connect(self.updateCell)
        
        for i in range(self.stackedWidget.count()):
            self.stackedWidget.widget(i).update.connect(self.updateCell)
    
    
    def setCellProperties(self, properties : dict) -> None:
        # сбросить все поля
        self.blockSignals(True) # TODO КОСЫЛЬ
        
        self.baseCellEditorWidget.setProperties(properties) 
        for i in range(self.stackedWidget.count()):
            self.stackedWidget.widget(i).setProperties(properties)
        
        index = self.cellType.findText(properties.get('cellType', MonolithCell.cellType()))
        self.cellType.setCurrentIndex(index)
        
        self.blockSignals(False) # TODO КОСЫЛЬ
        
    
    def getCellProperties(self) -> dict:
        properties = dict()
        properties['cellType'] = self.cellType.currentText()
        properties.update(self.baseCellEditorWidget.getCellPropertiesPart())
        properties.update(self.stackedWidget.currentWidget().getCellPropertiesPart())
        return properties

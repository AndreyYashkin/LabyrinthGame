from PySide2.QtWidgets import QCheckBox, QGroupBox, QVBoxLayout, QWidget
from PySide2.QtCore import Signal
from .abstractcelleditor import AbstractCellEditor
from ...game.mapobjects.item import Item


class BaseCellEditorWidget(AbstractCellEditor):
    def __init__(self, parent=None):
        AbstractCellEditor.__init__(self, parent)

        self.start = QCheckBox('Start cell', self)
        self.downWall = QCheckBox('Down wall', self)
        self.leftWall = QCheckBox('Left wall', self)
        
        group = QGroupBox('Items in cell', self)
        
        groupLayout = QVBoxLayout()
        
        self.itemsCheckBox = list()
        
        for item in Item:
            checkBox = QCheckBox(item.name(), group)
            checkBox.setObjectName(item.code()) # QObject.objectName() будет использоваться для храения кода item'а 
            checkBox.stateChanged.connect(self.update)
            groupLayout.addWidget(checkBox)
            self.itemsCheckBox.append(checkBox)
        
        group.setLayout(groupLayout)
        
        layout = QVBoxLayout()
        layout.addWidget(self.start)
        layout.addWidget(self.downWall)
        layout.addWidget(self.leftWall)
        layout.addWidget(group)
        
        self.setLayout(layout)
        
        self.start.stateChanged.connect(self.update)
        self.downWall.stateChanged.connect(self.update)
        self.leftWall.stateChanged.connect(self.update)

        

    def setProperties(self, properties : dict) -> None:
        self.start.setChecked(properties.get('start_point', False))
        self.downWall.setChecked(properties.get('down_wall', False))
        self.leftWall.setChecked(properties.get('left_wall', False))
        itemsCodes = properties.get('itemsInCell', list())
        for checkBox in self.itemsCheckBox:
            checkBox.setChecked(checkBox.objectName() in itemsCodes) # objectName это code
    
    
    def getCellPropertiesPart(self) -> dict:
        prop = dict()
        prop['start_point'] = self.start.isChecked()
        prop['down_wall'] = self.downWall.isChecked()
        prop['left_wall'] = self.leftWall.isChecked()
        itemsCodes = list()
        for checkBox in self.itemsCheckBox:
            if checkBox.isChecked():
                itemsCodes.append(checkBox.objectName())
            checkBox.setChecked(checkBox.objectName() in itemsCodes) # objectName это code
        prop['itemsInCell'] = itemsCodes
        return prop

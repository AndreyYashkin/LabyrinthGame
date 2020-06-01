from PySide2.QtWidgets import (QCheckBox, QGroupBox,
                               QVBoxLayout, QWidget)
from PySide2.QtCore import Signal
from .abstractcelleditor import AbstractCellEditor
from ...game.mapobjects.item import Item


class ArsenalCellEditorWidget(AbstractCellEditor):
    def __init__(self, parent=None):
        AbstractCellEditor.__init__(self, parent)
        
        group = QGroupBox('Items in arsenal', self)
        
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
        layout.addWidget(group)
        
        self.setLayout(layout)
        
    
    def setProperties(self, properties : dict) -> None:
        itemsCodes = properties.get('itemsInArsenal', list())
        for checkBox in self.itemsCheckBox:
            checkBox.setChecked(checkBox.objectName() in itemsCodes) # objectName это code
    
    
    def getCellPropertiesPart(self) -> dict:
        prop = dict()
        itemsCodes = list()
        for checkBox in self.itemsCheckBox:
            if checkBox.isChecked():
                itemsCodes.append(checkBox.objectName())
            checkBox.setChecked(checkBox.objectName() in itemsCodes) # objectName это code
        prop['itemsInArsenal'] = itemsCodes
        return prop

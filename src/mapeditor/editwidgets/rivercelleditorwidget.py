from PySide2.QtWidgets import QComboBox, QFormLayout
from PySide2.QtCore import Signal
from .abstractcelleditor import AbstractCellEditor


class RiverCellEditorWidget(AbstractCellEditor):
    def __init__(self, parent=None):
        AbstractCellEditor.__init__(self, parent)
        
        self.direction = QComboBox(self)
        self.direction.addItems(['Up', 'Down', 'Right', 'Left'])
        
        layout = QFormLayout()
        layout.addRow('Direction:', self.direction)
        
        self.setLayout(layout)
        
        self.direction.currentIndexChanged.connect(self.update)
    
    
    def setProperties(self, properties : dict) -> None:
        directionStr = properties.get('direction', 'UP')
        # TODO можно сделать как-то красивее
        # https://doc.qt.io/qtforpython/PySide2/QtWidgets/QComboBox.html#PySide2.QtWidgets.PySide2.QtWidgets.QComboBox.findText
        directionStr = directionStr[0].upper() + directionStr[1:].lower()
        index = max(self.direction.findText(directionStr), 0)
        self.direction.setCurrentIndex(index)
    
    
    def getCellPropertiesPart(self) -> dict:
        prop = dict()
        prop['direction'] = self.direction.currentText().upper()
        return prop

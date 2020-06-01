from PySide2.QtWidgets import QSpinBox, QFormLayout
from PySide2.QtCore import Signal
from .abstractcelleditor import AbstractCellEditor


class WormholeCellEditorWidget(AbstractCellEditor):
    def __init__(self, parent=None):
        AbstractCellEditor.__init__(self, parent)
        
        self.nextI = QSpinBox(self)
        self.nextJ = QSpinBox(self)
        
        layout = QFormLayout()
        layout.addRow('Next wormhole i coordinate:', self.nextI)
        layout.addRow('Next wormhole j coordinate:', self.nextJ)
        
        self.setLayout(layout)
        
        self.nextI.valueChanged.connect(self.update)
        self.nextJ.valueChanged.connect(self.update)
    
    
    def setProperties(self, properties : dict) -> None:
        self.nextI.setValue(properties.get('next_i', 0))
        self.nextJ.setValue(properties.get('next_j', 0))
    
    
    def getCellPropertiesPart(self) -> dict:
        prop = dict()
        prop['next_i'] = self.nextI.value()
        prop['next_j'] = self.nextJ.value()
        return prop

from PySide2.QtCore import Signal
from .abstractcelleditor import AbstractCellEditor


class EmptyCellEditorWidget(AbstractCellEditor):
    def __init__(self, parent=None):
        AbstractCellEditor.__init__(self, parent)
    
    
    def setProperties(self, properties : dict) -> None:
        pass
    
    
    def getCellPropertiesPart(self) -> dict:
        return dict()

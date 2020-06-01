#from abc import ABC, abstractmethod
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal


# TODO https://stackoverflow.com/questions/46837947/how-to-create-an-abstract-base-class-in-python-which-derived-from-qobject
class AbstractCellEditor(QWidget): #, ABC):
    update = Signal() # TODO а не надо ли его в конструктор внести?
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
    
    
    # WARNING не должен отправлять при этом никаких сигналов! # blockSignals(True)
    #@abstractmethod
    def setProperties(self, properties : dict) -> None:
        pass
    
    
    #@abstractmethod
    def getCellPropertiesPart(self) -> dict: # getCellPropertiesPartPart
        pass

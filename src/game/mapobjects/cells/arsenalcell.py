from PySide2.QtGui import QPainter, QFont
from PySide2.QtCore import Qt, QRect
from .abstractcell import AbstractCell
from ....mapeditor.editwidgets.abstractcelleditor import AbstractCellEditor
from ....mapeditor.editwidgets.arsenalcelleditorwidget import ArsenalCellEditorWidget


class ArsenalCell(AbstractCell):
    def __init__(self, itemsInArsenal : set):
        AbstractCell.__init__(self)
        self.itemsInArsenal = itemsInArsenal
        self.afterEntrance(None)
    
    
    @staticmethod
    def cellType():
        return 'ArsenalCell'
    
    
    def prepareForEntrance(self, entity):
        if entity.sendMoveLogs:
            entity.logger.sendMessage(entity, 'Step executed, arcenal')
        return True
    
    
    def afterEntrance(self, entity):
        self.itemsInCell.update(self.itemsInArsenal)


    @staticmethod
    def canBeStartPoint():
        return True
    
    
    @staticmethod
    def cellEditorWidget(parent = None) -> AbstractCellEditor:
        return ArsenalCellEditorWidget(parent)
    
    
    @staticmethod
    def paintCellWidget(painter : QPainter, rect : QRect, properties : dict) -> None:
        painter.fillRect(rect, Qt.red)
        # TODO это не самый лучший способ. Плохо работает при растягивании
        painter.setPen(Qt.black)
        painter.setFont(QFont('Arial', 30))
        painter.drawText(rect, Qt.AlignCenter, 'A')

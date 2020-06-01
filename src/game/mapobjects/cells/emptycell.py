from PySide2.QtGui import QPainter, QFont
from PySide2.QtCore import Qt, QRect
from .abstractcell import AbstractCell
from ..item import Item
from ....mapeditor.editwidgets.abstractcelleditor import AbstractCellEditor
from ....mapeditor.editwidgets.emptycelleditorwidget import EmptyCellEditorWidget


class EmptyCell(AbstractCell):
    def __init__(self):
        AbstractCell.__init__(self)
    
    
    @staticmethod
    def cellType():
        return 'EmptyCell'
    
    
    def prepareForEntrance(self, entity):
        if entity.sendMoveLogs:
            entity.logger.sendMessage(entity, 'Step executed, empty cell')
        return True
    
    
    def afterEntrance(self, entity):
        pass
    
    
    @staticmethod
    def cellEditorWidget(parent = None) -> AbstractCellEditor:
        return EmptyCellEditorWidget(parent)
    
    
    @staticmethod
    def paintCellWidget(painter : QPainter, rect : QRect, properties : dict) -> None:
        painter.fillRect(rect, Qt.green)
        # TODO это не самый лучший способ. Плохо работает при растягивании
        itemsInCell = properties.get('itemsInCell', list())
        if Item.KEY.code() in itemsInCell:
            painter.setPen(Qt.black)
            painter.setFont(QFont('Arial', 30))
            painter.drawText(rect, Qt.AlignCenter, '🔑')

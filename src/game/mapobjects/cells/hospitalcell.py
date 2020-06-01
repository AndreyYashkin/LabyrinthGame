from PySide2.QtGui import QPainter, QFont
from PySide2.QtCore import Qt, QRect
from .emptycell import EmptyCell
from ....mapeditor.editwidgets.abstractcelleditor import AbstractCellEditor
from ....mapeditor.editwidgets.emptycelleditorwidget import EmptyCellEditorWidget


class HospitalCell(EmptyCell):
    def __init__(self):
        EmptyCell.__init__(self)
    
    
    @staticmethod
    def cellType():
        return 'HospitalCell'


    def prepareForEntrance(self, entity):
        if entity.sendMoveLogs:
            entity.logger.sendMessage(entity, 'Step executed, hospital')
        return True
    
    
    @staticmethod
    def cellEditorWidget(parent = None) -> AbstractCellEditor:
        return EmptyCellEditorWidget(parent)
    
    
    @staticmethod
    def paintCellWidget(painter : QPainter, rect : QRect, properties : dict) -> None:
        painter.fillRect(rect, Qt.darkGreen)
        # TODO это не самый лучший способ. Плохо работает при растягивании
        painter.setPen(Qt.black)
        painter.setFont(QFont('Arial', 30))
        painter.drawText(rect, Qt.AlignCenter, '🏥')

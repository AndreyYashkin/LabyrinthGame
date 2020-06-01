from PySide2.QtGui import QPainter, QFont
from PySide2.QtCore import Qt, QRect
from .abstractcell import AbstractCell
from ..direction import Direction
from ..item import Item
from ....mapeditor.editwidgets.abstractcelleditor import AbstractCellEditor
from ....mapeditor.editwidgets.rivercelleditorwidget import RiverCellEditorWidget


class RiverCell(AbstractCell): # TODO отнаследовать от класса "Перемещающая клетка"
    def __init__(self, direction : Direction):
        AbstractCell.__init__(self)
        self.direction = direction
        #print(direction)
    
    
    @staticmethod
    def cellType():
        return 'RiverCell'
    
    
    def prepareForEntrance(self, entity):
        if entity.sendMoveLogs:
            if entity.turnProperties.get('wasMovedByRiver', False) == False:
                #if self.direction == Direction.NONE:
                    #entity.logger.sendMessage(entity, 'Step executed, river end')
                #else:
                entity.logger.sendMessage(entity, 'Step executed, river')
            else:
                entity.logger.sendMessage(entity, 'river, move ' + entity.turnProperties['wasMovedByRiver'].name())
        return True
    
    
    def afterEntrance(self, entity):
        # TODO лодку надо по необходимости только использовать, это уже есть в флагах
        if (entity.permanentProperties.get('canBeMovedByCell', False) == True
                and entity.turnProperties.get('wasMovedByRiver', False) == False
                and Item.BOAT not in entity.inventory
                and entity.cell.neighborCell(self.direction).cellType() == RiverCell.cellType()
                and self.direction != Direction.NONE):
            entity.turnProperties['wasMovedByRiver'] = self.direction
            entity.move(self.direction)
   
   
    def move(self, entity, direction : Direction):
        if self.canMove(entity, direction):
            if entity.cell.neighborCell(direction).cellType() != RiverCell.cellType():
                if Item.BOAT in entity.inventory:
                    entity.removeFromInventory(Item.BOAT)
            #super().move(entity, direction)
            if direction == Direction.NONE:
                self.enter(entity)
            else:
                self.separators[direction].cell(direction).enter(entity)
    
    
    @staticmethod
    def cellEditorWidget(parent = None) -> AbstractCellEditor:
        return RiverCellEditorWidget(parent)
    
    
    @staticmethod
    def paintCellWidget(painter : QPainter, rect : QRect, properties : dict) -> None:
        direction = properties.get('direction', 'UP')
        if direction == 'UP':
            arrow = '⇑'
        elif direction == 'DOWN':
            arrow = '⇓'
        elif direction == 'LEFT':
            arrow = '⇐'
        else: #if direction == 'RIGHT':
            arrow = '⇒'
        painter.fillRect(rect, Qt.blue)
        # TODO это не самый лучший способ. Плохо работает при растягивании
        painter.setPen(Qt.white)
        painter.setFont(QFont('Arial', 30))
        painter.drawText(rect, Qt.AlignCenter, arrow)

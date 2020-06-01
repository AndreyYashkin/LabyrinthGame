from abc import ABC, abstractmethod
from PySide2.QtGui import QPainter
from PySide2.QtCore import QRect
from ..direction import Direction
from ....mapeditor.editwidgets.abstractcelleditor import AbstractCellEditor
from ....mapeditor.editwidgets.basecelleditorwidget import BaseCellEditorWidget


class AbstractCell(ABC):
    def __init__(self):        
        self.entitiesInside = list() # TODO это в set переделать
        self.separators = dict() # NOTE init will be done in Separator constructors
        self.itemsInCell = set() 
    
    
    @staticmethod
    @abstractmethod
    def cellType():
        pass
    
    
    def neighborCell(self, direction : Direction):
        if direction == Direction.NONE:
            return self
        separator = self.separators.get(direction, None)
        if separator:
            return separator.cell(direction)
        else:
            return None
    
    
    def addEntitiy(self, entity):
        self.entitiesInside.append(entity)
    
    
    def removeEntitiy(self, entity):
        pos = next((i for i, e in enumerate(self.entitiesInside) if e == entity)) #, None))
        self.entitiesInside.pop(pos)
    
    
    def canMove(self, entity, direction : Direction): # TODO нету нормальных проверок на None
        if direction == Direction.NONE:
            return self.prepareForEntrance(entity)
        else:
            separator = self.separators.get(direction, None)
            if separator.canCross(entity):
                return separator.cell(direction).prepareForEntrance(entity)
            else:
                return False
    
    
    def move(self, entity, direction : Direction):
        if self.canMove(entity, direction):
            if direction == Direction.NONE:
                self.enter(entity)
            else:
                self.separators[direction].cell(direction).enter(entity)
    
    
    # Печатает сообщение и возвращает флаг, свидет. о возможности войти в клетку
    @abstractmethod
    def prepareForEntrance(self, entity):
        pass
    
    
    # действие, которые надо предпринять после входа в лкетку. Например, река может снести игрока вниз по течению
    @abstractmethod
    def afterEntrance(self, entity):
        pass
    
    
    def enter(self, entity):
        # DEBUG
        # entity.logger.sendMessage(None, 'DEBUG coord ' + self.cellType() + ' ' + self.c1 + ', ' + self.c2)
        entity.cell.removeEntitiy(entity)
        self.addEntitiy(entity)
        entity.cell = self
        entity.onCellEntrance()
        self.afterEntrance(entity)

    
    # Для редактора
    @staticmethod
    def baseCellEditorWidget(parent = None) -> AbstractCellEditor:
        return BaseCellEditorWidget(parent)
    
    
    # Виджет для редактора, который позволяет редактировать свойства, специфчные для этой клетки
    # Для арсенала - это item'ы в нем
    @staticmethod
    @abstractmethod
    def cellEditorWidget(parent = None) -> AbstractCellEditor:
        pass
    
    
    # TODO см. как надо https://code.woboq.org/qt5/qtbase/src/widgets/widgets/qpushbutton.cpp.html#_ZN11QPushButton10paintEventEP11QPaintEvent
    # или лучше сразу отнаследовать от QPushButton и ничего не рисовать?
    @staticmethod
    @abstractmethod
    def paintCellWidget(painter : QPainter, rect : QRect, properties : dict) -> None:
        pass
    
    
    
    # TODO такого рода условия надо добавить, чтобы создавать рабочие карты. Может, тоже сделать через множество флагов с параметрами?
    #@staticmethod
    #@abstractmethod
    #def canBeStartPoint():
    #   pass

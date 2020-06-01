from PySide2.QtGui import QPainter, QFont
from PySide2.QtCore import Qt, QRect
from .abstractcell import AbstractCell
from ....mapeditor.editwidgets.abstractcelleditor import AbstractCellEditor
from ....mapeditor.editwidgets.wormholecelleditorwidget import WormholeCellEditorWidget


class WormholeСell(AbstractCell): # TODO отнаследовать от класса "Перемещающая клетка"
    def __init__(self, nextWormhole = None):
        AbstractCell.__init__(self)
        self.nextWormhole = nextWormhole
    
    
    @staticmethod
    def cellType():
        return 'WormholeCell'
    
    
    def prepareForEntrance(self, entity):
        if entity.sendMoveLogs:
            if entity.turnProperties.get('wasTeleported', False):
                entity.logger.sendMessage(entity, 'Teleportation, wormhole')
            else:
                entity.logger.sendMessage(entity, 'Step executed, wormhole')
        return True
    
    
    def afterEntrance(self, entity):
        if (entity.permanentProperties.get('canBeMovedByCell', False) == True and
            entity.turnProperties.get('wasTeleported', False) == False):
            entity.turnProperties['wasTeleported'] = True
            self.nextWormhole.prepareForEntrance(entity)
            self.nextWormhole.enter(entity)
    
    
    @staticmethod
    def cellEditorWidget(parent = None) -> AbstractCellEditor:
        return WormholeCellEditorWidget(parent)
    
    
    @staticmethod
    def paintCellWidget(painter : QPainter, rect : QRect, properties : dict) -> None:
        painter.fillRect(rect, Qt.darkCyan)
        # TODO это не самый лучший способ. Плохо работает при растягивании
        painter.setPen(Qt.black)
        painter.setFont(QFont('Arial', 30))
        painter.drawText(rect, Qt.AlignCenter, '🕳')

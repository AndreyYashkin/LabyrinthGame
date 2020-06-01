# 
# WARNING это все временная штука. Часть этого кода должна быть перенесена в серверную часть
# Когда будет сервер, это все надо будет переделать
#
from PySide2.QtCore import QObject, Signal, Slot, QFile, QIODevice, QTextStream
from src.client.gamewidget import GameWidget
from .templogger import TempLogger

from ..game.labyrinth import Labyrinth
from ..game.labyrinthgame import LabyrinthGame

import json


class ClientLogic(QObject):
    def __init__(self, mapPath, parent=None):
        QObject.__init__(self, parent)
        
        self.gameWidget = GameWidget(parent)
        self.logger = TempLogger(self.gameWidget)
        
        self.gameWidget.actionSelected.connect(self.onActionSelected)
        
        # серверная часть с созданием лабиринта
        
        file = QFile(mapPath)
        file.open(QIODevice.ReadOnly | QIODevice.Text)
        map = str(file.readAll(), 'utf-8') # QByteArray -> str
        # print(map)
        properties = json.loads(map)
        
        self.labyrinth = Labyrinth(properties)
        self.labyrinthGame = LabyrinthGame(self.labyrinth, [self], self.logger)
        
        # конец
    
    
    def getGameWidget(self, parent = None): # надо вот над этим подумать
        return self.gameWidget
    
    
    # FIXME эта часть должна относиться к контроллеру 
    def do(self):
        actionCode = self.gameWidget.getActionCode()
        paramCode = self.gameWidget.getParamCode()
        return actionCode, paramCode
    
    def getPlayerInfo(self):
        return 'PLAYER', 'SEX'
        
    
    @Slot()
    def onActionSelected(self):
        if self.labyrinthGame.makeTurn():
            self.gameWidget.switchController(1)

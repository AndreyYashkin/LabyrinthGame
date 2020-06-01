import sys
from PySide2.QtWidgets import QApplication
from src.server.createserverdialog import CreateServerDialog
from src.server.logwidget import LogWidget


'''
from src.game.labyrinth import Labyrinth
from src.game.labyrinthgame import LabyrinthGame
import json
from PySide2.QtWidgets import QMainWindow, QDockWidget, QMenuBar, QMessageBox, QDialog, QFileDialog
from PySide2.QtCore import Signal, Slot, Qt, QFile, QIODevice, QTextStream
'''

if __name__ == "__main__":
    '''
    path = '/home/andrey/Документы/Программирование/Мои проекты/LabyrinthGame/MAP'
    file = QFile(path)
    if file.open(QIODevice.ReadOnly | QIODevice.Text):
        map = str(file.readAll(), 'utf-8') # QByteArray -> str
        properties = json.loads(map)
    
    l = Labyrinth(properties)
    g = LabyrinthGame(l, list(), None)
    
    sys.exit(0)
    '''
    
    app = QApplication(sys.argv)
    widget = LogWidget()
    
    widget.show()
    sys.exit(app.exec_())

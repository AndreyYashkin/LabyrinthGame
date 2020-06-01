from PySide2.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from PySide2.QtCore import Signal, Slot
from .controlwidget import ControlWidget
from ..server.logwidget import LogWidget


class GameWidget(QWidget):
    actionSelected = Signal()
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.controlwidget = ControlWidget()
        layout.addWidget(self.controlwidget)
        
        self.logWidget = LogWidget()
        layout.addWidget(self.logWidget)
        
        self.controlwidget.doAction.connect(self.actionSelected)
    
    
    def getActionCode(self):
        return self.controlwidget.getActionCode()
    
    
    def getParamCode(self):
        return self.controlwidget.getActionParamCode()
    
    
    #@Slot(int)
    def switchController(self, state): # state=0 - off. state=1 - on
        self.controlwidget.setState(state)
    
    
    # TODO тут все еще надо получать entity & str, чтобы можно было делать выделение
    @Slot(str)
    def showMessage(self, name, message):
        self.logWidget.appendMessage(name + ': ' + message)

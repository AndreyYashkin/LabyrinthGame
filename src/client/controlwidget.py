from PySide2.QtWidgets import QStackedWidget, QWidget, QProgressBar, QFormLayout, QComboBox, QPushButton
from PySide2.QtCore import Signal, Slot
from ..game.actioncollection import ActionCollection


class ControlWidget(QStackedWidget):
    doAction = Signal()
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent)
        self.collection = ActionCollection()
        
        waitWidget = QProgressBar()
        waitWidget.setRange(0, 0)
        self.addWidget(waitWidget)
        
        controler = QWidget()
        layout = QFormLayout()
        controler.setLayout(layout)
        self.actionTypeBox = QComboBox()
        self.actionParamBox = QComboBox()
        layout.addRow('Action', self.actionTypeBox)
        layout.addRow('Parameter', self.actionParamBox)
        self.addWidget(controler)
        
        button = QPushButton('Do')
        layout.addWidget(button) # addRow
        
        self.initActionTypeWidget()
        
        button.clicked.connect(self.onActionSelected)
        self.actionTypeBox.currentTextChanged.connect(self.onActionChange)
        self.setCurrentIndex(1) # убрать
    
    
    def getActionCode(self):
        return self.collection.actionFromName(self.actionTypeBox.currentText()).actionCode()
    
    
    def getActionParamCode(self):
        param = self.actionParamBox.currentText()
        return self.collection.actionFromName(self.actionTypeBox.currentText()).getParamCodeFromName(param)
    
    
    #@Slot(int) # Ожидание или ввод в QStackedWidget
    def setState(self, state):
        self.setCurrentIndex(state)
    
    
    @Slot()
    def onActionSelected(self):
        self.setCurrentIndex(0)
        self.doAction.emit()
    
    
    @Slot(str)
    def onActionChange(self, actionName):
        self.resetActionParamWidget(self.actionTypeBox.currentText())
    
    
    @Slot(int)
    def initActionTypeWidget(self):
        self.actionTypeBox.addItems(self.collection.actionNames())
        self.resetActionParamWidget(self.actionTypeBox.currentText())
    
    
    @Slot(int)
    def resetActionParamWidget(self, actionName):
        self.actionParamBox.clear()
        action = self.collection.actionFromName(actionName)
        self.actionParamBox.addItems(action.getParamNames())

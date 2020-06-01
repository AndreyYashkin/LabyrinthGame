from PySide2.QtWidgets import QPlainTextEdit 


# TODO переделать через QPTextEdit, чтобы ник игрока, время выделялся цветом и т.п.
class LogWidget(QPlainTextEdit):
    def __init__(self, parent=None):
        QPlainTextEdit.__init__(self, parent)
        self.setReadOnly(True)
    
    
    def contextMenuEvent(self, event):
        menu = self.createStandardContextMenu()
        menu.addAction('Clear', self.clear)
        menu.exec_(event.globalPos())
    
    
    def appendMessage(self, text):
        self.appendPlainText(text)

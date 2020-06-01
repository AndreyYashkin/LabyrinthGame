from ..game.abstractlogger import AbstractLogger


class TempLogger(AbstractLogger):
    def __init__(self, gameWidget):
        AbstractLogger.__init__(self)
        self.gameWidget = gameWidget
    
    
    def sendMessage(self, entity, message):
        if entity:
            self.gameWidget.showMessage(entity.name, message)
        else:
            self.gameWidget.showMessage('NONE', message)

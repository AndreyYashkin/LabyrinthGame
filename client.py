import sys
from PySide2.QtWidgets import QApplication
from src.client.gamewidget import GameWidget
from src.client.clientlogic import ClientLogic


if __name__ == "__main__":   
    app = QApplication(sys.argv)
    
    logic = ClientLogic('./game_map')
    widget = logic.getGameWidget()
    
    widget.show()
    sys.exit(app.exec_())

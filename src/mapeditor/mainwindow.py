import json
from PySide2.QtWidgets import QMainWindow, QDockWidget, QMenuBar, QMessageBox, QDialog, QFileDialog
from PySide2.QtCore import Signal, Slot, Qt, QFile, QIODevice, QTextStream
from .celleditor import CellEditor
from .mapwidget import MapWidget
from .newmapdialog import NewMapDialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        
        self.unsavedChanges = False
        self.path = ''
        
        self.mapWidget = MapWidget()
        self.cellEditor = CellEditor()
        
        self.i = -1
        self.j = -1
        
        self.setCentralWidget(self.mapWidget)
        
        self.dockWidget = QDockWidget('Cell editor')
        self.dockWidget.setFloating(False)
        self.dockWidget.setWidget(self.cellEditor)
        self.dockWidget.setVisible(False)
        
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget)
        
        self.mapWidget.openEditor.connect(self.onOpenEditor)
        self.cellEditor.updateCell.connect(self.onUpdateCell)
        
        menuBar = QMenuBar()
        fMenu = menuBar.addMenu('File')
        actionNew = fMenu.addAction('New')
        actionNew.triggered.connect(self.onActionNew)
        
        actionOpen = fMenu.addAction('Open')
        actionOpen.triggered.connect(self.onActionOpen)
        
        self.actionSave = fMenu.addAction('Save')
        self.actionSave.triggered.connect(self.onActionSave)
        
        self.actionSaveAs = fMenu.addAction('Save as ...')
        self.actionSaveAs.triggered.connect(self.onActionSaveAs)
        
        self.actionClose = fMenu.addAction('Close')
        self.actionClose.triggered.connect(self.onActionClose)
        
        actionExit = fMenu.addAction('Exit')
        actionExit.triggered.connect(self.onActionExit)
        
        fMenu.insertSeparator(actionExit)
        
        menuBar.addMenu('About')
        
        self.setMenuBar(menuBar)
        
        # TODO status bar
        
        self.setHaveOpenedMap(False)
    
    
    @Slot()
    def onActionNew(self):
        if not self.canClose():
            return
        dialog = NewMapDialog()
        if dialog.exec() == QDialog.Accepted:
            rows, cells = dialog.dim()
            properties = dict()
            properties['size_n'] = rows
            properties['size_m'] = cells
            self.mapWidget.resetMap(properties)
            self.setHaveOpenedMap(True)
            self.path = ''
        
    
    @Slot()
    def onActionOpen(self):
        if self.canClose():
            path, selectedFilter = QFileDialog.getOpenFileName(self, 'Open map') #, '', 'Maps (*.lMap)') # TODO
            if len(path) > 0:
                file = QFile(path)
                if file.open(QIODevice.ReadOnly | QIODevice.Text):
                    map = str(file.readAll(), 'utf-8') # QByteArray -> str
                    self.path = path
                    properties = json.loads(map)
                    self.mapWidget.resetMap(properties)
                    self.setHaveOpenedMap(True)
    
    
    @Slot()
    def onActionSave(self) -> bool:
        if len(self.path) > 0:
            return self.save(self.path)
        else:
            return self.onActionSaveAs()
    
    
    @Slot()
    def onActionSaveAs(self) -> bool:
        path, selectedFilter = QFileDialog.getSaveFileName(self, 'Save map') #, '', 'Maps (*.lMap)') # TODO
        if len(path) > 0:
            if self.save(path):
                self.path = path
                return True
        return False
    
    
    @Slot()
    def onActionClose(self) -> bool:
        if self.canClose():
            self.setHaveOpenedMap(False)
            
    @Slot()
    def onActionExit(self):
        if self.canClose():
            self.close()
    
    
    def save(self, path) -> bool:
        jsonData = json.dumps(self.mapWidget.getProperties())
        file = QFile(path)
        if not file.open(QIODevice.WriteOnly | QIODevice.Text):
            return False
        ts = QTextStream(file)
        ts << jsonData
        self.unsavedChanges = False
        return True
        
    
    
    def canClose(self) -> bool:
        if self.unsavedChanges:
            res = QMessageBox.question(self, 'Unsaved changes', 'Want to save your changes?', QMessageBox.Save | QMessageBox.Discard
                                                                                                               | QMessageBox.Cancel)
            if res == QMessageBox.Save:
                if self.onActionSave():
                    return True
                else:
                    return False
            elif res == QMessageBox.Cancel:
                return False
        return True
        
    
    def setHaveOpenedMap(self, flag):
        self.unsavedChanges = False
        # TODO это бы как-то заменить
        if flag == False:
            self.mapWidget.resetMap(dict())
            self.path = ''
        self.mapWidget.setDisabled(not flag)
        self.dockWidget.setVisible(self.dockWidget.isVisible() and flag)
        
        self.actionSave.setEnabled(flag)
        self.actionSaveAs.setEnabled(flag)
        self.actionClose.setEnabled(flag)
    
    
    @Slot(list)
    def onOpenEditor(self, list):
        self.i = list[0]
        self.j = list[1]
        
        self.cellEditor.setCellProperties(self.mapWidget.getCellProperties(self.i, self.j))
        
        self.dockWidget.setVisible(True)
    
    
    @Slot()
    def onUpdateCell(self):
        properties = self.cellEditor.getCellProperties()
        self.mapWidget.updateCell(self.i, self.j, properties)
        self.unsavedChanges = True

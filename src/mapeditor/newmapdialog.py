from PySide2.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QSpinBox
from PySide2.QtCore import Qt


class NewMapDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        
        layout = QFormLayout()
        self.setLayout(layout)
        
        self.rowSpinBox = QSpinBox(self)
        self.rowSpinBox.setMinimum(5)
        layout.addRow('Rows', self.rowSpinBox)
        
        self.columnSpinBox = QSpinBox(self)
        self.columnSpinBox.setMinimum(5)
        layout.addRow('Columns', self.columnSpinBox)
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        layout.addWidget(self.buttonBox)
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
    def dim(self) -> (int, int):
        return self.rowSpinBox.value(), self.columnSpinBox.value() 

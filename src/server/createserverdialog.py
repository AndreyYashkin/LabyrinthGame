from PySide2.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QSpinBox, QLineEdit
from PySide2.QtCore import Qt


class CreateServerDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        
        layout = QFormLayout()
        self.setLayout(layout)
        
        self.playersNSpinBox = QSpinBox(self)
        self.playersNSpinBox.setMinimum(1)
        layout.addRow('Number of players', self.playersNSpinBox)
        
        self.passwordLine = QLineEdit(self)
        layout.addRow('Password', self.passwordLine)
        # TODO setValidator() вида пароля
        
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        layout.addWidget(self.buttonBox)
    
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
    
    
    def players(self) -> int:
        return self.playersNSpinBox.value()
    
    
    def password(self) -> str:
        return self.passwordLine.text ()

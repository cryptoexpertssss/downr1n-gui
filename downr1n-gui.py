import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox
from PyQt5.QtGui import QColor
import subprocess

class Downr1nGui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Downr1n Gui')
        self.setGeometry(0, 0, 1280, 720)
        self.setFixedSize(1280, 720)
        
        # Checkbox for boot
        self.boot_checkbox = QCheckBox('Boot', self)
        self.boot_checkbox.move(100, 100)
        self.boot_checkbox.stateChanged.connect(self.boot_checkbox_changed)
        
        # Checkbox for downgrade
        self.downgrade_checkbox = QCheckBox('Downgrade', self)
        self.downgrade_checkbox.move(100, 150)
        self.downgrade_checkbox.stateChanged.connect(self.downgrade_checkbox_changed)
        
        # Dropdown menu for iOS versions
        self.version_label = QLabel('Select iOS version:', self)
        self.version_label.move(100, 200)
        
        self.version_dropdown = QComboBox(self)
        self.version_dropdown.move(250, 200)
        self.version_dropdown.addItem('14.1')
        self.version_dropdown.addItem('14.2')
        self.version_dropdown.addItem('14.3')
        self.version_dropdown.addItem('14.4')
        self.version_dropdown.addItem('14.5')
        self.version_dropdown.addItem('14.6')
        self.version_dropdown.addItem('14.7')
        self.version_dropdown.addItem('14.8')
        self.version_dropdown.addItem('15.0')
        self.version_dropdown.addItem('15.1')
        self.version_dropdown.addItem('15.2')
        self.version_dropdown.addItem('15.3')
        self.version_dropdown.addItem('15.4')
        self.version_dropdown.addItem('15.5')
        self.version_dropdown.addItem('15.6')
        self.version_dropdown.addItem('15.7')
        
        # Default to 14.8
        self.version_dropdown.setCurrentText('14.8')
        
        # Message labels
        self.message_label = QLabel('Made By Aditya,Uckermark\nSome code of Edwin', self)
        self.message_label.move(100, 500)
        
        # Execute button
        self.execute_button = QPushButton('Execute', self)
        self.execute_button.move(100, 400)
        self.execute_button.clicked.connect(self.execute_button_clicked)
        
        self.show()
    
    def boot_checkbox_changed(self):
        if self.boot_checkbox.isChecked():
            self.version_label.hide()
            self.version_dropdown.hide()
    
    def downgrade_checkbox_changed(self):
        if self.downgrade_checkbox.isChecked():
            self.version_label.show()
            self.version_dropdown.show()
    
    def execute_button_clicked(self):
        if self.boot_checkbox.isChecked():
            subprocess.run(['sudo', './downr1n.sh', '--boot'])
        elif self.downgrade_checkbox.isChecked():
            version = self.version_dropdown.currentText()
            subprocess.run(['sudo', './downr1n.sh', '--downgrade', version])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Downr1nGui()
    sys.exit(app.exec_())


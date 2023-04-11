import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Downr1nGui(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set the window dimensions
        self.width = 1280
        self.height = 720
        self.setFixedSize(self.width, self.height)
        
        # Set the window title
        self.setWindowTitle("Downr1n Gui")
                
        # Create the Boot checkbox
        self.boot_checkbox = QCheckBox('Boot', self)
        self.boot_checkbox.move(20, 20)
        self.boot_checkbox.stateChanged.connect(self.boot_checkbox_changed)
        
        # Create the Downgrade checkbox
        self.downgrade_checkbox = QCheckBox('Downgrade', self)
        self.downgrade_checkbox.move(20, 50)
        self.downgrade_checkbox.stateChanged.connect(self.downgrade_checkbox_changed)
        
        # Create the message label
        self.message_label = QLabel("Made By Aditya ,Uckermark\nhttps://github.com/Aditya20110/\nhttps://github.com/Uckermark", self)
        self.message_label.move(20, 90)
        
        # Hide the dropdown menu when boot checkbox is selected
        self.version_dropdown = QComboBox(self)
        self.version_dropdown.addItems(['14.1', '14.2', '14.3', '14.4', '14.5', '14.6', '14.7', '14.8', '15.0', '15.1', '15.2', '15.3', '15.4', '15.5', '15.6', '15.7'])
        self.version_dropdown.move(150, 20)
        self.version_dropdown.hide()
        
        # Create the Execute button
        self.execute_button = QPushButton('Execute', self)
        self.execute_button.move(150, 50)
        self.execute_button.clicked.connect(self.execute_button_clicked)
        
        # Initialize the command variable
        self.command = ""
    
    def boot_checkbox_changed(self):
        if self.boot_checkbox.isChecked():
            self.version_dropdown.hide()
        else:
            self.version_dropdown.show()
    
    def downgrade_checkbox_changed(self):
        if self.downgrade_checkbox.isChecked():
            self.command = "sudo ./downr1n.sh --downgrade"
        else:
            self.command = ""
    
    def execute_button_clicked(self):
        if self.boot_checkbox.isChecked():
            command = "sudo ./downr1n.sh --boot"
        elif self.downgrade_checkbox.isChecked():
            command = self.command + " " + str(self.version_dropdown.currentText())
        
        if command:
            os.system(command)
            self.close()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #print "made by Aditya,Uckermark"
    #print "some code of edwin"
    gui = Downr1nGui()
    gui.show()
    sys.exit(app.exec_())

import subprocess
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QWidget

class JailbreakGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Jailbreak GUI')
        self.setGeometry(100, 100, 1280, 720)
        self.init_ui()
        
    def init_ui(self):
        # Create the UI components
        self.version_dropdown = QComboBox(self)
        self.version_dropdown.addItems(['iOS 14.1', 'iOS 14.2', 'iOS 14.3', 'iOS 14.4', 'iOS 14.5', 'iOS 14.6', 'iOS 14.7', 'iOS 14.8', 'iOS 15.0', 'iOS 15.1', 'iOS 15.2', 'iOS 15.3', 'iOS 15.4', 'iOS 15.5', 'iOS 15.6', 'iOS 15.7'])
        self.jailbreak_button = QPushButton('Jailbreak!', self)
        self.message_label = QLabel('Made By Aditya ,Uckermark\nsome code of edwin', self)
        
        # Create the layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.version_dropdown)
        vbox.addWidget(self.jailbreak_button)
        vbox.addStretch(1)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.message_label)
        hbox.addStretch(1)
        
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        
        # Connect the button click to the jailbreak function
        self.jailbreak_button.clicked.connect(self.jailbreak)
        
    def jailbreak(self):
        version = self.version_dropdown.currentText()
        command = f'sudo ./downr1n.sh --jailbreak {version}'
        subprocess.call(command, shell=True)
        
if __name__ == '__main__':
    app = QApplication([])
    gui = JailbreakGUI()
    gui.show()
    app.exec_()

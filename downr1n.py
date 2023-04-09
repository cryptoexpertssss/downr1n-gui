import cmd
import os
import sys
import platform


try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
    from gui import Ui_MainWindow
    from applescript import tell
except ImportError:
    if input("Requirements not satisfied, please install the pip requirements.\nTry and install automatically? (y/n) ") == "y":
        try:
            os.system("pip3 install -r requirements.txt")
        except Exception:
            print("Error automatically installing requirements, please install them manually.")
            quit()
    print("Please restart downr1n-gui")

def run_command(command):
    if platform.system() == "Darwin":
        tell.app('Terminal', 'do script "' + command + '"')
    else:
        os.system(command)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.StartButton.clicked.connect(self.StartButton_clicked)
        self.ui.IPSWButton.clicked.connect(self.IPSWPath_clicked)
        self.path = os.path.dirname(os.path.abspath(__file__))
    
    def StartButton_clicked(self):
        ipsw = self.ui.IPSWLineEdit.text()
        
        if self.ui.RestoreMode.isChecked():
            if ipsw == "":
                QMessageBox.critical(self, "Error!", "No IPSW file specified")
                return
            
            file_exists = os.path.exists(ipsw)
            if not file_exists:
                QMessageBox.critical(self, "Error!", "The specified IPSW file does not exist.")
                return
            if not ipsw.endswith(".ipsw"):
                QMessageBox.warning(self, "Warning!", "Your IPSW file is not a file ending in .ipsw\nThis can cause errors in the execution and it is recommended to choose a file ending in .ipsw")

            args = f"sudo ./downr1n.sh --downgrade 15.6"
            
            path = os.path.abspath(os.getcwd())

            if not os.path.exists(f"{self.path}/downr1n.sh"):
                QMessageBox.critical(self, "Error!", "downr1n was not found in current path.")
                return

            command = f"cd {self.path} && {sys.executable} {path}/downr1n.sh {args}"

            QMessageBox.critical(self, "Warning!", "Connect your device already in DFU mode with sigchecks removed before proceeding")

            run_command(command)


        elif self.ui.BootMode.isChecked():

            if ipsw == "":
                QMessageBox.critical(self, "Error!", "No IPSW file specified")
                return

            file_exists = os.path.exists(ipsw)
            if not file_exists:
                QMessageBox.critical(self, "Error!", "The specified IPSW file does not exist.")
                return
            if not ipsw.endswith(".ipsw"):
                QMessageBox.warning(self, "Warning!", "Your IPSW file is not a file ending in .ipsw\nThis can cause errors in the execution and it is recommended to choose a file ending in .ipsw")

            args = f"sudo ./downr1n.sh --boot"

            command = f"cd {self.path} && {sys.executable} {os.path.abspath(os.getcwd())}/downr1n.sh {args}"

            if not os.path.exists(f"{self.path}/downr1n.sh"):
                QMessageBox.critical(self, "Error!", "dualra1n-gui was not found in current path.")
                return
      
            run_command(command)

    def IPSWPath_clicked(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","IPSW Files (*.ipsw);;All Files (*)", options=options)
        if fileName:
            self.ui.IPSWLineEdit.setText(fileName)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

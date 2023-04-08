import cmd
import os
import sys


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

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.StartButton.clicked.connect(self.StartButton_clicked)
        self.ui.IPSWButton.clicked.connect(self.IPSWPath_clicked)
    
    def StartButton_clicked(self):
        ipsw = self.ui.IPSWLineEdit.text()
        boardconfig = self.ui.BoardConfigLineEdit.text().lower()
        
        if self.ui.RestoreMode.isChecked():
            if ipsw == "":
                QMessageBox.critical(self, "Error!", "No IPSW file specified")
                return
            elif boardconfig == "":
                QMessageBox.critical(self, "Error!", "No BoardConfig specified.")
                return


            file_exists = os.path.exists(ipsw)
            if not file_exists:
                QMessageBox.critical(self, "Error!", "The specified IPSW file does not exist.")
                return
            if not ipsw.endswith(".ipsw"):
                QMessageBox.warning(self, "Warning!", "Your IPSW file is not a file ending in .ipsw\nThis can cause errors in the execution and it is recommended to choose a file ending in .ipsw")

            args = f"--downgrade"
            
            path = os.path.abspath(os.getcwd())

            if not os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/"):
                QMessageBox.critical(self, "Error!", "downr1n was not found in current path.")
                return

            command = f"cd {os.path.dirname(os.path.abspath(__file__))} && {sys.executable} {path}/downr1n.sh {args}"

            QMessageBox.critical(self, "Warning!", "Connect your device already in DFU mode with sigchecks removed before proceeding")

            tell.app( 'Terminal', 'do script "' + command + '"') 


        elif self.ui.BootMode.isChecked():
            identifier = self.ui.IdentifierLineEdit.text()

            if ipsw == "":
                QMessageBox.critical(self, "Error!", "No IPSW file specified")
                return


            file_exists = os.path.exists(ipsw)
            if not file_exists:
                QMessageBox.critical(self, "Error!", "The specified IPSW file does not exist.")
                return
            if not ipsw.endswith(".ipsw"):
                QMessageBox.warning(self, "Warning!", "Your IPSW file is not a file ending in .ipsw\nThis can cause errors in the execution and it is recommended to choose a file ending in .ipsw")


          

            args = f"--downgrade"

            command = f"cd {os.path.dirname(os.path.abspath(__file__))} && {sys.executable} {os.path.abspath(os.getcwd())}/downr1n.sh {args}"

            if not os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/downr1n.sh"):
                QMessageBox.critical(self, "Error!", "dualra1n-gui was not found in current path.")
                return
            
            QMessageBox.critical(self, "Warning!", "After this script finishes, put your device into pwndfu with sigchecks removed again and run \"boot.sh\"")

            tell.app( 'Terminal', 'do script "' + command + '"') 
        

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

import cmd
import os
import sys
import platform
import threading


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

class CommandRunner(threading.Thread):
    def __init__(self):
        super().__init__()
        self.command = None

    def set_command(self, command):
        self.command = command

    def start(self):
        if platform.system() == "Darwin":
            tell.app('Terminal', 'do script "' + self.command + '"')
        else:
            log = os.system(self.command)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.StartButton.clicked.connect(self.StartButton_clicked)
        self.ui.IPSWButton.clicked.connect(self.IPSWPath_clicked)
        self.path = os.path.abspath(os.getcwd())
        self.command_thread = CommandRunner()
    
    def StartButton_clicked(self):
        if self.command_thread and self.command_thread.is_alive():
            QMessageBox.critical(self, "Error!", "A command is already running. Please wait for it to finish.")
            return

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

            command = f"{path}/downr1n.sh {args}"

            QMessageBox.critical(self, "Warning!", "Connect your device already in DFU mode with sigchecks removed before proceeding")

            self.command_thread.set_command(command)
            self.command_thread.start()


        elif self.ui.BootMode.isChecked():

            args = "--boot"

            command = f"{self.path}/downr1n.sh {args}"

            if not os.path.exists(f"{self.path}/downr1n.sh"):
                QMessageBox.critical(self, "Error!", "dualra1n-gui was not found in current path.")
                return
      
            self.command_thread.set_command(command)
            self.command_thread.start()

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

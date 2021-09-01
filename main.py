# Author: duxeph
# Release date: 2021/9/1 (y.m.d)
# Version: 1.0
# Contact mail: furieuxx13@gmail.com
# Contact github: https://github.com/duxeph

from PyQt5 import QtWidgets
from fast_form import Ui_Form
import sys
from control.basics import Basics

"""NEARLY UPDATES"""
# CONTROLLABLE DOWNLOAD ALTERNATIVE FOR JAVA, JAVAC, JAR PACKAGES FOR BOTH UBUNTU/ANY LINUX AND WINDOWS
# SOLVING CHMOD PROBLEM IN WINDOWS
# CHANGABLE MAIN CLASS NAME

class window(QtWidgets.QWidget):
    def __init__(self):
        super(window, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        Basics().checkVersions(self.ui)

        print("[INFO] App configured.")
        self.ui.buttonPath.clicked.connect(self.mainFilePathSelection)
        self.ui.buttonStart.clicked.connect(self.takeConvertionAsk)
        self.ui.buttonExit.clicked.connect(self.close)

        self.ui.lineEditPath.keyReleaseEvent = self.pathControlDirector
        self.ui.lineEditPath.mouseReleaseEvent = self.pathControlDirector

    def mainFilePathSelection(self):
        self.main_path = str(QtWidgets.QFileDialog.getOpenFileName(self, "Select Main.java path")[0])
        if self.main_path != "" and self.main_path.split('/')[-1] == "Main.java":
            Basics().mainFilePathSelection(self.main_path, self.ui)

    def pathControlDirector(self, e):
        Basics().pathControlDirector(self.main_path, self.ui)

    def takeConvertionAsk(self):
        Basics().takeConvertionAsk(self.main_path, self.ui)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())
app()

# -*- coding: utf-8 -*-

# @author bl4ckvghost
#
# Copyright (C) 2017 Youssef Hesham
#
# License <http://www.gnu.org/licenses/gpl-3.0.html>

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 516)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 16777215, 16777214))
        self.frame.setMinimumSize(QtCore.QSize(16777214, 16777214))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(310, 10, 161, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(28)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.scriptPath = QtGui.QTextEdit(self.frame)
        self.scriptPath.setGeometry(QtCore.QRect(100, 80, 501, 31))
        self.scriptPath.setObjectName(_fromUtf8("scriptPath"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.choose_archive = QtGui.QPushButton(self.frame)
        self.choose_archive.setGeometry(QtCore.QRect(610, 80, 94, 32))
        self.choose_archive.setObjectName(_fromUtf8("choose_archive"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 131, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Impact"))
        font.setPointSize(18)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.check_Bruteforce = QtGui.QCheckBox(self.frame)
        self.check_Bruteforce.setGeometry(QtCore.QRect(40, 230, 101, 25))
        self.check_Bruteforce.setObjectName(_fromUtf8("check_Bruteforce"))
        self.check_dict = QtGui.QCheckBox(self.frame)
        self.check_dict.setGeometry(QtCore.QRect(40, 270, 93, 25))
        self.check_dict.setObjectName(_fromUtf8("check_dict"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.DictPath = QtGui.QTextEdit(self.frame)
        self.DictPath.setGeometry(QtCore.QRect(100, 120, 501, 31))
        self.DictPath.setObjectName(_fromUtf8("DictPath"))
        self.choose_dict = QtGui.QPushButton(self.frame)
        self.choose_dict.setGeometry(QtCore.QRect(610, 120, 94, 32))
        self.choose_dict.setObjectName(_fromUtf8("choose_dict"))
        self.check_Symboles = QtGui.QCheckBox(self.frame)
        self.check_Symboles.setGeometry(QtCore.QRect(200, 230, 121, 25))
        self.check_Symboles.setObjectName(_fromUtf8("check_Symboles"))
        self.check_Kali = QtGui.QCheckBox(self.frame)
        self.check_Kali.setGeometry(QtCore.QRect(200, 270, 161, 25))
        self.check_Kali.setObjectName(_fromUtf8("check_Kali"))
        self.start_cracking = QtGui.QPushButton(self.frame)
        self.start_cracking.setGeometry(QtCore.QRect(623, 280, 161, 32))
        self.start_cracking.setObjectName(_fromUtf8("start_cracking"))
        self.themeChanger = QtGui.QComboBox(self.frame)
        self.themeChanger.setGeometry(QtCore.QRect(445, 280, 161, 31))
        self.themeChanger.setObjectName(_fromUtf8("themeChanger"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, 319, 801, 181))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.output = QtGui.QTextEdit(self.widget)
        self.output.setGeometry(QtCore.QRect(0, 10, 801, 131))
        self.output.setObjectName(_fromUtf8("output"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuWelcome = QtGui.QMenu(self.menubar)
        self.menuWelcome.setObjectName(_fromUtf8("menuWelcome"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionHow_To_Use = QtGui.QAction(MainWindow)
        self.actionHow_To_Use.setObjectName(_fromUtf8("actionHow_To_Use"))
        self.menuWelcome.addAction(self.actionAbout)
        self.menuWelcome.addAction(self.actionQuit)
        self.menuWelcome.addAction(self.actionHow_To_Use)
        self.menubar.addAction(self.menuWelcome.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Obevilion", None))
        self.label.setText(_translate("MainWindow", "Obevilion", None))
        self.scriptPath.setStatusTip(_translate("MainWindow", "Enter the archive path to crack", None))
        self.label_2.setText(_translate("MainWindow", "Arhive Path", None))
        self.choose_archive.setStatusTip(_translate("MainWindow", "Choose archive from file system", None))
        self.choose_archive.setText(_translate("MainWindow", "Choose", None))
        self.label_3.setText(_translate("MainWindow", "What To Use", None))
        self.check_Bruteforce.setStatusTip(_translate("MainWindow", "Use bruteforce attack method", None))
        self.check_Bruteforce.setText(_translate("MainWindow", "BruteForce", None))
        self.check_dict.setStatusTip(_translate("MainWindow", "Use dictionary attack method", None))
        self.check_dict.setText(_translate("MainWindow", "Dictionary", None))
        self.label_4.setText(_translate("MainWindow", "Dictionary", None))
        self.DictPath.setStatusTip(_translate("MainWindow", "Enter the path of the password list", None))
        self.choose_dict.setStatusTip(_translate("MainWindow", "Choose password list from file system", None))
        self.choose_dict.setText(_translate("MainWindow", "Choose", None))
        self.check_Symboles.setStatusTip(_translate("MainWindow", "Use Symboles in the cracking process", None))
        self.check_Symboles.setText(_translate("MainWindow", "Use Symboles", None))
        self.check_Kali.setStatusTip(_translate("MainWindow", "Check if you are using kali linux", None))
        self.check_Kali.setText(_translate("MainWindow", "Use External Scripts", None))
        self.start_cracking.setStatusTip(_translate("MainWindow", "Begin The Cracking Process", None))
        self.start_cracking.setText(_translate("MainWindow", "Lets Go!", None))
        self.themeChanger.setStatusTip(_translate("MainWindow", "Change The Window Theme", None))
        self.widget.setStatusTip(_translate("MainWindow", "The output shows here", None))
        self.menuWelcome.setTitle(_translate("MainWindow", "Obevilion", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About The Programmer", None))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+B", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Close the application", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionHow_To_Use.setText(_translate("MainWindow", "How To Use?", None))
        self.actionHow_To_Use.setStatusTip(_translate("MainWindow", "How to use Obevilion", None))
        self.actionHow_To_Use.setShortcut(_translate("MainWindow", "Ctrl+H", None))


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

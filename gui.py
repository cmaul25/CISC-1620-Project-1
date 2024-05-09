# Form implementation generated from reading ui file 'accounts-gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 450)
        MainWindow.setMinimumSize(QtCore.QSize(400, 450))
        MainWindow.setMaximumSize(QtCore.QSize(400, 450))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PythonBanking = QtWidgets.QLabel(parent=self.centralwidget)
        self.PythonBanking.setGeometry(QtCore.QRect(30, 20, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PythonBanking.setFont(font)
        self.PythonBanking.setObjectName("PythonBanking")
        self.FNLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.FNLabel.setGeometry(QtCore.QRect(4, 80, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FNLabel.setFont(font)
        self.FNLabel.setObjectName("FNLabel")
        self.LNLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.LNLabel.setGeometry(QtCore.QRect(4, 110, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LNLabel.setFont(font)
        self.LNLabel.setObjectName("LNLabel")
        self.PINLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.PINLabel.setGeometry(QtCore.QRect(10, 140, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PINLabel.setFont(font)
        self.PINLabel.setObjectName("PINLabel")
        self.EntryFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.EntryFrame.setGeometry(QtCore.QRect(100, 70, 131, 101))
        self.EntryFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.EntryFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.EntryFrame.setObjectName("EntryFrame")
        self.PINEntry = QtWidgets.QLineEdit(parent=self.EntryFrame)
        self.PINEntry.setGeometry(QtCore.QRect(10, 70, 113, 20))
        self.PINEntry.setObjectName("PINEntry")
        self.LNEntry = QtWidgets.QLineEdit(parent=self.EntryFrame)
        self.LNEntry.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.LNEntry.setObjectName("LNEntry")
        self.FNEntry = QtWidgets.QLineEdit(parent=self.EntryFrame)
        self.FNEntry.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.FNEntry.setObjectName("FNEntry")
        self.LoginLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.LoginLabel.setGeometry(QtCore.QRect(250, 50, 131, 161))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LoginLabel.setWordWrap(True)
        self.LoginLabel.setObjectName("LoginLabel")
        self.EnterButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.EnterButton.setGeometry(QtCore.QRect(140, 170, 56, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EnterButton.setFont(font)
        self.EnterButton.setObjectName("EnterButton")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 260, 371, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.HistDisplayLabel = QtWidgets.QLabel(parent=self.frame)
        self.HistDisplayLabel.setGeometry(QtCore.QRect(0, 30, 161, 91))
        self.HistDisplayLabel.setText("")
        self.HistDisplayLabel.setObjectName("HistDisplayLabel")
        self.AccDisplayLabel = QtWidgets.QLabel(parent=self.frame)
        self.AccDisplayLabel.setGeometry(QtCore.QRect(190, 30, 161, 91))
        self.AccDisplayLabel.setText("")
        self.AccDisplayLabel.setObjectName("AccDisplayLabel")
        self.TransHistLabel = QtWidgets.QLabel(parent=self.frame)
        self.TransHistLabel.setGeometry(QtCore.QRect(0, 0, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TransHistLabel.setFont(font)
        self.TransHistLabel.setObjectName("TransHistLabel")
        self.AccountInfoLabel = QtWidgets.QLabel(parent=self.frame)
        self.AccountInfoLabel.setGeometry(QtCore.QRect(190, 0, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.AccountInfoLabel.setFont(font)
        self.AccountInfoLabel.setObjectName("AccountInfoLabel")
        self.DespoitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.DespoitButton.setGeometry(QtCore.QRect(100, 220, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DespoitButton.setFont(font)
        self.DespoitButton.setObjectName("DespoitButton")
        self.WithdrawlButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.WithdrawlButton.setGeometry(QtCore.QRect(170, 220, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WithdrawlButton.setFont(font)
        self.WithdrawlButton.setObjectName("WithdrawlButton")
        self.wdEntry = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.wdEntry.setGeometry(QtCore.QRect(100, 200, 141, 21))
        self.wdEntry.setObjectName("wdEntry")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PythonBanking.setText(_translate("MainWindow", "Python Banking"))
        self.FNLabel.setText(_translate("MainWindow", "First Name"))
        self.LNLabel.setText(_translate("MainWindow", "Last Name"))
        self.PINLabel.setText(_translate("MainWindow", "PIN"))
        self.LoginLabel.setText(_translate("MainWindow", "Enter First Name, Last Name, and PIN to login. (Case Sensitive)"))
        self.EnterButton.setText(_translate("MainWindow", "Enter"))
        self.TransHistLabel.setText(_translate("MainWindow", "Transaction History"))
        self.AccountInfoLabel.setText(_translate("MainWindow", "Account Info"))
        self.DespoitButton.setText(_translate("MainWindow", "Deposit"))
        self.WithdrawlButton.setText(_translate("MainWindow", "Withdrawl"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

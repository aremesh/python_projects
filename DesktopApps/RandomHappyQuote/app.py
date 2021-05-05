# Form implementation generated from reading ui file 'happy.ui'

import os
import random

from PyQt6 import QtCore, QtGui, QtWidgets

path = os.path.dirname(__file__)
textfile = path + "/happyquotes.txt"

happy_quotes = []
with open(textfile, 'r') as f:
    for line in f:
        happy_quotes.append(line)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 300)
        MainWindow.setMinimumSize(QtCore.QSize(550, 300))
        MainWindow.setMaximumSize(QtCore.QSize(550, 300))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(205, 202, 207);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.happy_quote = QtWidgets.QLabel(self.centralwidget)
        self.happy_quote.setGeometry(QtCore.QRect(20, 60, 511, 121))
        font = QtGui.QFont()
        font.setFamily(".Savoye LET CC.")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.happy_quote.setFont(font)
        self.happy_quote.setText("")
        self.happy_quote.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.happy_quote.setObjectName("happy_quote")
        self.happy_quote.setWordWrap(1)
        self.happy_quote.setStyleSheet("QLabel{ color:rgb(75,75,75);}")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 220, 151, 32))
        self.pushButton.clicked.connect(self.buttonPush)
        self.pushButton.setStyleSheet("QPushButton{\n"
        "  background: #333;\n"
        "  color:white;\n"
        "  border-radius:10px;\n"
        "}\n"
        "QPushButton:hover:!pressed\n"
        "{\n"
        "  background: #AAA;\n"
        "}"
        )
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Random Happy Quote"))
        self.pushButton.setText(_translate("MainWindow", "Next Quote"))

    def buttonPush(self):
        max_len = len(happy_quotes) - 1
        randint = random.randint(0, max_len)
        self.happy_quote.setText(happy_quotes[randint])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

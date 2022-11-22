from sys import argv, exit
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(160, 200, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "Start drawing circles"))


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(600, 600)
        self.btn.clicked.connect(self.start_drawing)

    def start_drawing(self):
        self.btn.hide()
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.btn.isHidden():
            self.btn.hide()
            for i in range(5000):
                qp.setBrush(QColor.fromRgb(randint(0, 255), randint(0, 255), randint(0, 255)))
                self.drawing(qp)
            qp.end()

    def drawing(self, qp):
        a = randint(1, 100)
        x, y = randint(0, 500), randint(0, 500)
        qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main_Window()
    ex.show()
    exit(app.exec())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal_user.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QLabel,
                              QMainWindow, QMenu, QMessageBox, QScrollArea, QSizePolicy)
from PyQt5.QtCore import QDir, Qt
from parts import parts
import mysql.connector
class Normal(object):
    itr=int(0)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 100, 491, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnPrev = QtWidgets.QPushButton(self.frame)
        self.btnPrev.setGeometry(QtCore.QRect(0, 130, 51, 51))
        self.btnPrev.setObjectName("btnPrev")
        self.btnPrev.clicked.connect(self.prevImgLoad)
        self.btnNext = QtWidgets.QPushButton(self.frame)
        self.btnNext.setGeometry(QtCore.QRect(440, 140, 51, 51))
        self.btnNext.setObjectName("btnNext")
        self.btnNext.clicked.connect(self.nextImagLoad)
        self.logoutBtn = QtWidgets.QPushButton(self.frame)
        self.logoutBtn.setGeometry(QtCore.QRect(400, 330, 91, 31))
        self.logoutBtn.setObjectName("logoutBtn")
        self.imgView = QtWidgets.QLabel(self.frame)
        self.imgView.setGeometry(QtCore.QRect(60, 20, 371, 301))

        self.imgView.setObjectName("imgView")

        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(40, 40, 91, 41))
        self.openBtn.setObjectName("openBtn")
        self.openBtn.clicked.connect(self.openBtnClickMethod)
        self.trainBtn = QtWidgets.QPushButton(self.centralwidget)
        self.trainBtn.setGeometry(QtCore.QRect(160, 40, 101, 41))
        self.trainBtn.setObjectName("trainBtn")
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(290, 40, 101, 41))
        self.searchBtn.setObjectName("searchBtn")
        self.createbtn = QtWidgets.QPushButton(self.centralwidget)
        self.createbtn.setGeometry(QtCore.QRect(420, 40, 101, 41))
        self.createbtn.setObjectName("createbtn")
        self.createbtn.clicked.connect(self.makeGANgogh)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def openBtnClickMethod(self):
       fileName, _ = QFileDialog.getOpenFileName(self, "Open File",
                                                  QDir.currentPath())


    def makeGANgogh(self):
        parts.run(self)

    def nextImagLoad(self):
        root='C:/Users/Priyotuli/Desktop/pl/spl.png.'
        Normal.itr+=1

        root+=str(Normal.itr)
        root+=".jpg"
        print(root)
        pixmap = QtGui.QPixmap(root)
        self.imgView.setPixmap(pixmap)

    def prevImgLoad(self):
        root='C:/Users/Priyotuli/Desktop/pl/spl.png.'
        Normal.itr-=1

        root+=str(Normal.itr)
        root+=".jpg"
        print(root)
        pixmap = QtGui.QPixmap(root)
        self.imgView.setPixmap(pixmap)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPrev.setText(_translate("MainWindow", "<"))
        self.btnNext.setText(_translate("MainWindow", ">"))
        self.logoutBtn.setText(_translate("MainWindow", "Logout"))
        self.openBtn.setText(_translate("MainWindow", "Open"))
        self.trainBtn.setText(_translate("MainWindow", "Train"))
        self.searchBtn.setText(_translate("MainWindow", "Search"))
        self.createbtn.setText(_translate("MainWindow", "Create"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Normal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

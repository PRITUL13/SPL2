# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'artist.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
class Artist(object):
    itr=int(0)
    myresult=list()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(989, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(590, 20, 371, 451))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 449))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, 230, 81, 16))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(10, 340, 81, 21))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setGeometry(QtCore.QRect(100, 90, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 220, 261, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 330, 261, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 80, 461, 320))
        self.frame.setStyleSheet("border-color: rgb(0, 0,0);\n"
                                "background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.rateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.rateBtn.setGeometry(QtCore.QRect(80, 20, 91, 41))
        self.rateBtn.setObjectName("rateBtn")
        self.rateBtn.clicked.connect(self.setDB)
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(190, 20, 101, 41))
        self.searchBtn.setObjectName("searchBtn")
        self.searchBtn.clicked.connect(self.rateInsert)
        self.frame.setObjectName("frame")
        self.btnPrev = QtWidgets.QPushButton(self.frame)
        self.btnPrev.setGeometry(QtCore.QRect(0, 130, 51, 51))
        self.btnPrev.setObjectName("btnPrev")
        self.btnPrev.clicked.connect(self.prevImgLoad)
        self.btnNext = QtWidgets.QPushButton(self.frame)
        self.btnNext.setGeometry(QtCore.QRect(410, 140, 51, 51))
        self.btnNext.setObjectName("btnNext")
        self.btnNext.clicked.connect(self.nextImagLoad)
        self.logoutBtn = QtWidgets.QPushButton(self.frame)
        self.logoutBtn.setGeometry(QtCore.QRect(400, 330, 91, 31))
        self.logoutBtn.setObjectName("logoutBtn")
        self.imgView = QtWidgets.QLabel(self.frame)
        self.imgView.setGeometry(QtCore.QRect(60, 20, 371, 301))

        self.imgView.setObjectName("imgView")

        self.logoutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.logoutBtn.setGeometry(QtCore.QRect(430, 430, 91, 31))
        self.logoutBtn.setObjectName("logoutBtn")
        '''self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(6, 230, 51, 41))
        self.toolButton.setStyleSheet("")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(530, 230, 51, 41))
        self.toolButton_2.setStyleSheet("")
        self.toolButton_2.setObjectName("toolButton_2")'''
        self.frame.raise_()
        self.rateBtn.raise_()
        self.searchBtn.raise_()
        self.scrollArea.raise_()
        self.logoutBtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def openBtnClickMethod(self):
           fileName,_=QFileDialog.getOpenFileName(self,"OpenFile",QDir.currentPath())


    def rateInsert(self):
        print("sajhdfsajhfd")
        mydb = mysql.connector.connect(
                     host="localhost",
                     user="saiba",
                     passwd="1110235361",
                     database="priotuli"
         )
        mycursor = mydb.cursor()
        rates=self.lineEdit_3.text()
        print(rates)
        sql = "update arts set art_rate=%s where art_id=%s"
        print(Artist.myresult[Artist.itr][2])
        val=(float(rates),int(Artist.myresult[Artist.itr][2]))
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()

    def setDB(self):


        mydb = mysql.connector.connect(
                     host="localhost",
                     user="saiba",
                     passwd="1110235361",
                     database="priotuli"
         )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT art_name, art_rate, art_id FROM arts")
        Artist.myresult = mycursor.fetchall()

        print(Artist.myresult)
        mycursor.close()
        mydb.close()


    def makeGANgogh(self):
        parts.run(self)

    def nextImagLoad(self):
        root='C:/Users/Priyotuli/Desktop/pl/spl.png.'
        Artist.itr+=1
        print(Artist.itr)
        print(Artist.myresult[Artist.itr][1])
        root+=str(Artist.itr)
        root+=".jpg"
        print(root)
        pixmap = QtGui.QPixmap(Artist.myresult[Artist.itr][0])
        self.imgView.setPixmap(pixmap)
        self.lineEdit.setText(Artist.myresult[Artist.itr][0])
        self.lineEdit_2.setText(str(Artist.myresult[Artist.itr][2]))

    def prevImgLoad(self):
        root='C:/Users/Priyotuli/Desktop/pl/spl.png.'
        Artist.itr-=1

        root+=str(Artist.itr)
        root+=".jpg"
        print(root)
        pixmap = QtGui.QPixmap(root)
        self.imgView.setPixmap(pixmap)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Art Name"))
        self.label_2.setText(_translate("MainWindow", "Art ID"))
        self.label_3.setText(_translate("MainWindow", "Rating"))
        self.rateBtn.setWhatsThis(_translate("MainWindow", "print(\'i am labonno\')"))
        self.rateBtn.setText(_translate("MainWindow", "Rate art"))
        self.searchBtn.setText(_translate("MainWindow", "submit rate"))
        self.logoutBtn.setText(_translate("MainWindow", "Logout"))
        self.btnNext.setText(_translate("MainWindow", "<"))
        self.btnPrev.setText(_translate("MainWindow", ">"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Artist()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

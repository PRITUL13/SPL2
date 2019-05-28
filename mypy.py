import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QRadioButton,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import mysql.connector
from artist import Artist
from normal_user import Normal
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left =100
        self.top = 40
        self.width =600
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.label=QLabel(self)
        self.label.move(50,20)
        self.label.setText("UserName:")
        self.uname = QLineEdit(self)
        self.uname.move(50, 50)
        self.uname.resize(280,40)


        self.label2=QLabel(self)
        self.label2.move(50,100)
        self.label2.setText("password:")
        self.passw = QLineEdit(self)
        self.passw.move(50, 140)
        self.passw.resize(280,40)


        ''' self.user = QLineEdit(self)
        self.user.move(260, 250)
        self.user.resize(100,40)'''


        # Create a button in the window
        self.button = QPushButton('Login', self)
        self.button.move(150,400)

        # connect button to function on_click
        self.button.clicked.connect(self.setDB)
        self.show()




    def setDB(self):


        mydb = mysql.connector.connect(
                     host="localhost",
                     user="saiba",
                     passwd="1110235361",
                     database="priotuli"
         )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT name, password, usertype FROM user")
        myresult = mycursor.fetchall()
        print(myresult)
        mycursor.close()
        mydb.close()

        name = self.uname.text()
        pwd = self.passw.text()
        print(name, " ", pwd)
        for row in myresult:
            #print(row[2])
            if name == row[0] and pwd == row[1]:
                if row[2] == "normal":
                    print("noraml")
                    self.normalUser = QtWidgets.QMainWindow()
                    self.ui = Normal()
                    self.ui.setupUi(self.normalUser)
                    self.normalUser.show()
                if row[2] == "artist":
                    print("artist")
                    self.artistWindow = QtWidgets.QMainWindow()
                    self.ui = Artist()
                    self.ui.setupUi(self.artistWindow)
                    self.artistWindow.show()
                           #loadStartingPage()


    @pyqtSlot()
    def on_click(self):
        textboxValue = self.uname.text()
        print(textboxValue)
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.uname.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import requests


class SignUpMainWindow(QDialog):

    def __init__ (self):
        super().__init__()


        ##Use QFormLayout
        self.qbox = QFormLayout()

        ##All labels
        self.label1 = QLabel("Name: ")
        self.label2 = QLabel("Username: ")
        self.label3 = QLabel("Password: ")
        ##self.label4 = QLabel("Confirm Password: ")
        self.label5 = QLabel("E-mail: ")
        self.label6 = QLabel("Phone No: ")



        ##All QlineEdits
        self.nameLine = QLineEdit()
        self.usernameLine = QLineEdit()
        self.passwordLine = QLineEdit()
        self.conpassLine = QLineEdit()
        self.emailLine = QLineEdit()
        self.phoneLine = QLineEdit()



        ##All QlineEdits setup
        self.passwordLine.setEchoMode(QLineEdit.Password)
        self.conpassLine.setEchoMode(QLineEdit.Password)
        self.phoneLine.setInputMask('+669-999-9999')

        '''
        ##In case want to add Stretch between label and lineEdit to align label left
        self.tempLay = QHBoxLayout()
        self.tempLay.addWidget(self.label1)
        self.tempLay.addStretch()
        self.tempLay.addWidget(self.nameLine)

        '''

        ##Submit Button
        self.butSubmit = QPushButton("Submit")


        ##sub-Layout setup
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.passwordLine)
        vlayout.addWidget(self.conpassLine)



        ##Add all widget to Form layout
        self.vlayout = QFormLayout()
        ##self.vlayout.addRow(self.tempLay)
        self.vlayout.addRow(self.label1,self.nameLine)
        self.vlayout.addRow(self.label2, self.usernameLine)
        self.vlayout.addRow(self.label3, vlayout)
        ##self.vlayout.addRow(self.label4, self.conpassLine)
        self.vlayout.addRow(self.label5, self.emailLine)
        self.vlayout.addRow(self.label6, self.phoneLine)
        self.vlayout.addRow(self.butSubmit)


        ##All signal handling function call
        self.usernameLine.editingFinished.connect(self.validateUsername)
        self.butSubmit.clicked.connect(self.submitButClicked)
        self.conpassLine.editingFinished.connect(self.validatePassword)

        ##Set QWidget Mainwindow Layout to QFormLayout
        self.setLayout(self.vlayout)
        self.show()


    def validateUsername(self):
        print("Validating..." + self.usernameLine.text())


    def validatePassword(self):

        matched = self.passwordLine.text() == self.conpassLine.text()
        print("Password Match? " + str(matched))



    def submitButClicked(self):
        infoList = []
        infoList.append(self.nameLine.text())
        infoList.append(self.usernameLine.text())
        infoList.append(self.passwordLine.text())
        infoList.append(self.emailLine.text())
        infoList.append(self.phoneLine.text())
        print(infoList)
        print(infoList[0])
        data = {'id':'123',
        'name':infoList[0],
        'username':infoList[1],
        'password':infoList[2],
        'email':infoList[3],
        'phone':infoList[4]}
        y = requests.post('http://127.0.0.1:8000/test2/', data)
        print(y.text)





























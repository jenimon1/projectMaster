import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import requests
import json


from sign_up import *


class LogInMainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.vlayout = QVBoxLayout()


        ##All neccessary Labels
        self.appNameLabel = QLabel("Engineer Hub")
        self.usernameLabel = QLabel("Username: ")
        self.passwordLabel = QLabel("Password: ")
        self.signUpLabel = QLabel("<A href='www.TutorialsPoint.com'>Sign Up</A>")

        ##All LineEdits
        self.usernameLine = QLineEdit()
        self.passwordLine = QLineEdit()

        ##All button
        self.loginBut = QPushButton("Login")




        ##All LineEdits setup
        self.passwordLine.setEchoMode(QLineEdit.Password)


        ##Frame1 below Stretch() ,contain username Label and username line edit,with HorizontalBoxLayout as its layout
        row1hlayout = QHBoxLayout()
        row1hlayout.addStretch()
        row1hlayout.addWidget(self.usernameLabel)
        row1hlayout.addWidget(self.usernameLine)
        row1hlayout.addStretch()

        frame1 = QFrame()
        frame1.setLayout(row1hlayout)

        ##Frame2 below Stretch() ,contain password Label and password line edit,with HorizontalBoxLayout as its layout
        row2hlayout = QHBoxLayout()
        row2hlayout.addStretch()
        row2hlayout.addWidget(self.passwordLabel)
        row2hlayout.addWidget(self.passwordLine)
        row2hlayout.addStretch()

        frame2 = QFrame()
        frame2.setLayout(row2hlayout)



        ##Frame3 below Stretch() ,contain Signup Label and login button,with HorizontalBoxLayout as its layout
        row3hlayout = QHBoxLayout()
        row3hlayout.addStretch()
        row3hlayout.addWidget(self.signUpLabel)
        row3hlayout.addWidget(self.loginBut)
        row3hlayout.addStretch()

        frame3 = QFrame()
        frame3.setLayout(row3hlayout)


        ##Vertical layout as Login page main layout adding 1 stretch and all the 3 frames to its layout
        self.vlayout.addStretch()
        self.vlayout.addWidget(frame1)
        self.vlayout.addWidget(frame2)
        self.vlayout.addWidget(frame3)


        ##All Signal Handling function
        self.signUpLabel.linkActivated.connect(self.signUpLabelClicked)  ##when signup is clicked new SignUpPage(QDialog PopUpP)
        self.loginBut.clicked.connect(self.loginButClicked)



        ##LoginInPage window setup
        self.setGeometry(250,0,1000,800)
        self.setLayout(self.vlayout)

        self.show()

    def signUpLabelClicked(self):
        signUpWindow = SignUpMainWindow()
        signUpWindow.exec_()



    def loginButClicked(self):
        print("Login button clicked")
        x = requests.get('http://127.0.0.1:8000/test2/')
        a = json.loads(x.text)
        db = []
        count = 0
        print((self.usernameLine).text())
        print((self.passwordLine).text())
        

        for i in a:
    
            db.append(i['fields']['user_username'])
            db.append(i['fields']['user_password'])

            print(db)
            
            if (self.usernameLine).text() == db[0] and (self.passwordLine).text() == db[1]:
                print("to menu page")
                break
            
    
            
            db.clear()
 

            













if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LogInMainWindow()
    sys.exit(app.exec_())

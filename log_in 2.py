import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


from SignUpPage import *
from CreateOrViewProjectPage import *


class LogInMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.widget = QWidget()
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




        # self.backgroundPic = QLabel()
        # self.backgroundPic.setPixmap(QPixmap("/Users/Chieh/Desktop/EngineerHub/loginPageBackEdit.jpg"))
        # # self.loginBut.setStyleSheet("QWidget {border: 20px; border-radius: 0px; background-color: #00FF00; left: -600px;}")
        # self.loginBut.setStyleSheet("QWidget {background-image: url(loginPageBackEdit.png)}")
        #
        self.setStyleSheet("LogInMainWindow {background-image: url(/Users/Chieh/Desktop/EngineerHub/Images/LogInBack.jpg)}")






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
        #self.setLayout(self.vlayout)
        self.widget.setLayout(self.vlayout)



        self.setCentralWidget(self.widget)


        self.show()

    def signUpLabelClicked(self):
        signUpWindow = SignUpMainWindow()
        signUpWindow.exec_()



    def loginButClicked(self):
        createOrViewProjWindow = CreateOrViewProjectMainWindow(self)
        self.setStyleSheet("LogInMainWindow {background-image: url(/Users/Chieh/Desktop/EngineerHub/Images/MenuBack.jpg)}")


        self.profileAction = QAction(QIcon("/Users/Chieh/Desktop/EngineerHub/Images/profileIcon.jpg"),'Profile',self)
        self.profileAction.triggered.connect(self.profileActionClicked)
        self.notiAction = QAction(QIcon("/Users/Chieh/Desktop/EngineerHub/Images/profileIcon.jpg"),'Noti',self)
        self.notiAction.triggered.connect(self.notiActionClicked)
        self.leftSpacer = QWidget()
        self.leftSpacer.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)


        self.toolBar = self.addToolBar('toolbar')
        self.toolBar.addWidget(self.leftSpacer)
        self.toolBar.addAction(self.notiAction)
        self.toolBar.addAction(self.profileAction)



        self.toolBar.setStyleSheet("background-color: black;")
        # self.toolBar.setOrientation(Qt.Horizontal)

        self.setCentralWidget(createOrViewProjWindow)


    def profileActionClicked(self):
        print("profile action clicked")

    def notiActionClicked(self):
        print("notification action clicked")






if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LogInMainWindow()
    sys.exit(app.exec_())






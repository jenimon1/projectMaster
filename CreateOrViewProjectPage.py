import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

from CreateProjectPage import *
from LoginPage import *

class CreateOrViewProjectMainWindow(QWidget):


    def __init__(self,mainwindow):
        super().__init__()

        self.mainWindow = mainwindow

        ##initialise button to absolute positioning
        self.initUI()

        ##set central widget size
        self.setGeometry(250, 0, 1000, 800)
        self.show()




    def initUI(self):
        ##Add all button to createprViewProjectMainWindow widget
        self.createBut = QPushButton("", self)
        self.viewBut = QPushButton("", self)

        ##All buttons stylesheet setup
        self.createBut.setStyleSheet("background: rgba(0,0,0,0%); border-style: outset; border-radius: 175px;")
        self.viewBut.setStyleSheet("background: rgba(0,0,0,0%); border-style: outset; border-radius: 175px;")

        ##Absolute positioning all buttons to desired postision
        self.createBut.setGeometry(50, 300, 400, 350)
        self.viewBut.setGeometry(560, 300, 400, 350)

        ##Signal handling for all button
        self.createBut.clicked.connect(self.createProjButClicked)
        self.viewBut.clicked.connect(self.viewProjButClicked)



    def createProjButClicked(self):
        print("Create project button has been clicked")



        createProjectPage = CreateProjectPage(self.mainWindow)

        self.mainWindow.setStyleSheet("LogInMainWindow {Background-image: url(/Users/Chieh/Desktop/EngineerHub/Images/CreateProjBack.jpg)}")
        self.mainWindow.setCentralWidget(createProjectPage)
        self.mainWindow.toolBar.hide()
        createProjectPage.show()


    def viewProjButClicked(self):
        print("View project button has been clicked")
























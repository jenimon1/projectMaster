import  os
import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

from projectMaster.DragAndDrop import *
import projectMaster.ViewProjectPage

class myProjectMemberPageMainWindow(QWidget):

    def __init__(self,mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

        self.initUI()




    def initUI(self):

        ##ALL neccessary widgets set up
        self.toDoFrame = MyFrame(self,"ToDo")
        self.doingFrame = MyFrame(self,"Doing")
        self.doneFrame = MyFrame(self,"Done")
        self.updateBut = QPushButton("Update",self)
        self.cancelBut = QPushButton("Cancel",self)




        ##Absolute Positioning of all widgets
        self.toDoFrame.setGeometry(50,180,300,400)
        self.doingFrame.setGeometry(375, 180, 300, 400)
        self.doneFrame.setGeometry(700, 180, 300, 400)
        self.updateBut.setGeometry(820,620,80,50)
        self.cancelBut.setGeometry(900,620,80,50)



        self.initialiseAllFrame()




        ##All signal Handling widget attatch to function
        self.updateBut.clicked.connect(self.updateButClicked)
        self.cancelBut.clicked.connect(self.cancelButClicked)


    def updateButClicked(self):
        print("Update Button has been clicked...")

        listo1 = self.toDoFrame.getPhaseList()
        print("To Do: ")
        for i in listo1:
            print(i.text())

        listo2 = self.doingFrame.getPhaseList()
        print("Doing: ")
        for i in listo2:
            print(i.text())

        listo3 = self.doneFrame.getPhaseList()
        print("Done: ")
        for i in listo3:
            print(i.text())

    def cancelButClicked(self):
        viewProjWidget = projectMaster.ViewProjectPage.ViewProjectPageMainWindow(self.mainWindow)
        self.mainWindow.setStyleSheet(
            "LogInMainWindow {Background-image: url(projectMaster/Images/ViewProjBack.jpg)}")
        # self.mainWindow.toolBar.hide()

        self.mainWindow.setCentralWidget(viewProjWidget)



    def initialiseAllFrame(self):
        for i in range(5):
            self.toDoFrame.addPhase("Items",i)

        for i in range(5,10):
            self.doingFrame.addPhase("Items", i)

        for i in range(10,15):
            self.doneFrame.addPhase("Items",i)














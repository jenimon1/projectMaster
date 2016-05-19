import  os
import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *

from projectMaster.DragAndDrop import *
import projectMaster.ViewProjectPage

class OtherProjectPageMainWindow(QWidget):


    def __init__(self,mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.initUI()




    def initUI(self):
        ##ALL neccessary widgets set up
        self.toDoFrame = MyFrame(self,"ToDo")
        self.doingFrame = MyFrame(self,"Doing")
        self.doneFrame = MyFrame(self,"Done")
        self.cancelBut = QPushButton("Cancel",self)
        self.projDetailBut = QPushButton("Detail",self)
        self.progressBar = QProgressBar(self)



        ##Absolute Positioning of all widgets
        self.toDoFrame.setGeometry(50,180,300,400)
        self.doingFrame.setGeometry(375, 180, 300, 400)
        self.doneFrame.setGeometry(700, 180, 300, 400)
        self.cancelBut.setGeometry(900,620,80,50)
        self.projDetailBut.setGeometry(50,620,80,50)
        self.progressBar.setGeometry(80,655,840,100)


        ##Populate all Frames and update Progress bar accordingly
        self.initialiseAllFrame()
        self.updateProgressBar()




        ##All signal Handling widget attatch to function
        self.cancelBut.clicked.connect(self.cancelButClicked)
        self.projDetailBut.clicked.connect(self.projectDetailButClicked)
        self.doneFrame.dropped.connect(self.updateProgressBar)

    def projectDetailButClicked(self):
        print("project detail button has been clicked")




    def cancelButClicked(self):
        viewProjWidget = projectMaster.ViewProjectPage.ViewProjectPageMainWindow(self.mainWindow)
        self.mainWindow.setStyleSheet(
            "LogInMainWindow {Background-image: url(projectMaster/Images/ViewProjBack.jpg)}")
        # self.mainWindow.toolBar.hide()

        self.mainWindow.setCentralWidget(viewProjWidget)



    def initialiseAllFrame(self):
        ##Initialising all Frames with phases
        for i in range(5):
            self.toDoFrame.addPhase("Items",i)

        for i in range(5,10):
            self.doingFrame.addPhase("Items", i)

        for i in range(10,15):
            self.doneFrame.addPhase("Items",i)

    def updateProgressBar(self):
        ##Get number of phase from each frame
        toDoPhaseNo = len(self.toDoFrame.getPhaseList())
        doingPhaseNo = len(self.doingFrame.getPhaseList())
        donePhaseNo = len(self.doneFrame.getPhaseList())

        ##Get Percentage of phase that are in the done state over total phases in the project
        doneLength = int((donePhaseNo/(toDoPhaseNo + doingPhaseNo + donePhaseNo))*100)
        self.progressBar.setValue(doneLength)






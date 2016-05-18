import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

from projectMaster.myProjectMemberPage import *

class ViewProjectPageMainWindow(QWidget):

    def __init__(self,mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

        self.initUI()

        self.show()

    def initUI(self):



        ##All Widgets setup
        self.myProjList = QListWidget(self)
        self.otherProjList = QListWidget(self)
        self.goButton = QPushButton(self)



        self.populateAllLists()

        #Absolute position all widgets
        self.myProjList.setGeometry(50,100,400,500)
        self.otherProjList.setGeometry(550, 100, 400, 500)
        self.goButton.setGeometry(420,640,100,80)


        ##All widgets signal Handling event
        self.goButton.clicked.connect(self.goButClicked)
        self.myProjList.itemClicked.connect(self.isOtherListClicked)
        self.otherProjList.itemClicked.connect(self.isProjectListClicked)


        ##All Widget styesheet set up
        self.goButton.setStyleSheet("Background-color: rgba(0,0,0,0%)")

    def populateAllLists(self):
        ##Jane create list of project too
        for i in range(20):
            self.myProjList.addItem("Item " + str(i))

        for i in range(21,60):
            self.otherProjList.addItem("Item " + str(i) )


    def isOtherListClicked(self):
        ##Deselect other project list item if it is selected while item in my project list is clicked
        if (len(self.otherProjList.selectedItems()) != 0):
            for item in self.otherProjList.selectedItems():
                item.setSelected(False)


    def isProjectListClicked(self):
        ##Deselect my project list item if it is selected while item in other project list is clicked
        if (len(self.myProjList.selectedItems()) != 0):
            for item in self.myProjList.selectedItems():
                item.setSelected(False)





    def goButClicked(self):
        # print("go button has been clicked!!!")
        # for i in self.myProjList.selectedItems():
        #     print("hey")
        #
        # for i in self.otherProjList.selectedItems():
        #     print("hey21")

        ###if user is head of Project
        # self.mainWindow.setStyleSheet("LogInMainWindow {Background-image: url(projectMaster/Images/CreateProjBack.jpg)}")
        centralWidget = myProjectMemberPageMainWindow(self.mainWindow)
        self.mainWindow.setCentralWidget(centralWidget)
        self.mainWindow.setStyleSheet("LogInMainWindow {Background-Image: url(Images/UpdateProjMemBack.jpg)}")








import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

from projectMaster.myProjectMemberPage import *
from projectMaster.CreateProjectPage2 import *



class MyProjectHeaderPageMainWindow(MyProjectMemberPageMainWindow):

    def __init__(self,mainWindow):
        super().__init__(mainWindow)
        ##All widgets set up
        self.editBut = QPushButton("Edit",self)
        self.editBut.setGeometry(740,620,80,50)

        ##All Widget signal  function
        self.editBut.clicked.connect(self.editButClicked)

    def editButClicked(self):
        print("Edit Button has been clicked..")
        ##CreatingProjectPage Widget to be set as MainWindow's central widget
        createProjectPage = CreateProjectPage(self.mainWindow)

        ''''''
        createProjectPage.setParentWidget("myProjectHeaderPage")
        ''''''

        ##MainWindow stylesheet setup
        self.mainWindow.setStyleSheet(
            "LogInMainWindow {Background-image: url(projectMaster/Images/CreateProjBack.jpg)}")

        ##MainWindow setting up its central widget
        self.mainWindow.setCentralWidget(createProjectPage)
        createProjectPage.show()











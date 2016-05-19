
import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

from projectMaster.myProjectMemberPage import *



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









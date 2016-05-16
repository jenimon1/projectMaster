import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *



from Phase import *
import CreateOrViewProjectPage



class CreateProjectPage(QWidget):

    def __init__(self,mainwindow):
        super().__init__()
        self.mainWindow = mainwindow

        self.initUI()



    def initUI(self):
        self.layout = QVBoxLayout()

        scrollWidget = QWidget()
        scrollWidgetLayout = QVBoxLayout()


        ##Frame 1 setup, project name label and lineEdit
        self.projNameLabel = QLabel("Project Title: ")
        self.projNameLine = QLineEdit()
        frame1Layout = QHBoxLayout()
        frame1Layout.addWidget(self.projNameLabel)
        frame1Layout.addWidget(self.projNameLine)
        frame1 = QFrame()
        frame1.setLayout(frame1Layout)

        ##Frame 1 signal handling
        self.projNameLine.editingFinished.connect(self.projectTitleValidation)




        ##Frame2 all widgets set up
        self.siteNameLabel = QLabel("Site Name: ")
        self.codeLabel = QLabel("Site Code: ")
        self.regionLabel = QLabel("Region: ")
        self.sContractLabel = QLabel("Servey Subcontract: ")
        self.cContractLabel = QLabel("Construction Subcontract: ")
        self.typeLabel = QLabel("Type: ")
        self.sConfigLabel = QLabel("Site Configuration: ")
        self.heightLabel = QLabel("Height: ")
        self.clientLabel = QLabel("Client: ")


        self.siteNameLine = QLineEdit()
        self.codeLine = QLineEdit()
        self.regionLine = QLineEdit()
        self.sContractLine = QLineEdit()
        self.cContractLine = QLineEdit()
        self.typeLine = QLineEdit()
        self.sConfigLine = QLineEdit()
        self.heightLine = QLineEdit()
        self.clientLine = QLineEdit()

        #Frame2 sub-frame layout setup
        minif1Layout = QHBoxLayout()
        minif2Layout = QHBoxLayout()
        minif3Layout = QHBoxLayout()
        minif4Layout = QHBoxLayout()

        #Frame2 sub-frame layout add widgets
        minif1Layout.addWidget(self.siteNameLabel)
        minif1Layout.addWidget(self.siteNameLine)
        minif1Layout.addWidget(self.codeLabel)
        minif1Layout.addWidget(self.codeLine)

        minif2Layout.addWidget(self.regionLabel)
        minif2Layout.addWidget(self.regionLine)
        minif2Layout.addWidget(self.sContractLabel)
        minif2Layout.addWidget(self.sContractLine)
        minif2Layout.addWidget(self.cContractLabel)
        minif2Layout.addWidget(self.cContractLine)

        minif3Layout.addWidget(self.typeLabel)
        minif3Layout.addWidget(self.typeLine)
        minif3Layout.addWidget(self.sConfigLabel)
        minif3Layout.addWidget(self.sConfigLine)

        minif4Layout.addWidget(self.heightLabel)
        minif4Layout.addWidget(self.heightLine)
        minif4Layout.addWidget(self.clientLabel)
        minif4Layout.addWidget(self.clientLine)




        #Frame2 sub-frame setup
        minif1 = QFrame()
        minif2 = QFrame()
        minif3 = QFrame()
        minif4 = QFrame()

        minif1.setLayout(minif1Layout)
        minif2.setLayout(minif2Layout)
        minif3.setLayout(minif3Layout)
        minif4.setLayout(minif4Layout)


        #Frame2 main-layout add all sub-frames
        frame2Layout = QFormLayout()
        frame2Layout.addRow(minif1)
        frame2Layout.addRow(minif2)
        frame2Layout.addRow(minif3)
        frame2Layout.addRow(minif4)



        #Frame2 set its main layout
        frame2 = QFrame()
        frame2.setLayout(frame2Layout)

        ##Frame2 widgets Signal Handling
        self.codeLine.editingFinished.connect(self.siteCodeValidation)



        ##All Frame3 widgets set up
        self.memberLabel = QLabel("Add/Remove Members : ")
        self.search1Line = QLineEdit()
        self.search2Line = QLineEdit()
        self.addBut = QPushButton("+")
        self.subBut = QPushButton("-")
        self.listAll = QListWidget()
        self.listMembers = QListWidget()


        ##Populate both list of all users and list of all recruiting members
        self.populateAllLists()



        ##Frame3 sub-frame layout, frame3Extra(add/remove member label) and frame3Extra2 search box and list
        ##frameExtra2 contains 3 sub-frames 1st contain searchLineEdit and list,2nd add/removeButton,3rd searchLineEdit2 and list2
        minif31Layout = QVBoxLayout()
        minif32Layout = QVBoxLayout()
        minif33Layout = QVBoxLayout()

        minif31Layout.addWidget(self.search1Line)
        minif31Layout.addWidget(self.listAll)

        minif32Layout.addWidget(self.addBut)
        minif32Layout.addWidget(self.subBut)

        minif33Layout.addWidget(self.search2Line)
        minif33Layout.addWidget(self.listMembers)


        minif31 = QFrame()
        minif32 = QFrame()
        minif33 = QFrame()


        minif31.setLayout(minif31Layout)
        minif32.setLayout(minif32Layout)
        minif33.setLayout(minif33Layout)



        ##Add all frame3Extra2 sub-frame into its layout
        frame3Layout = QHBoxLayout()
        frame3Layout.addWidget(minif31)
        frame3Layout.addWidget(minif32)
        frame3Layout.addWidget(minif33)

        frame3Extra2 = QFrame()
        frame3Extra2.setLayout(frame3Layout)

        ## Frame3Extra for add/remove member label
        frame3Extra = QFrame()
        frame3ExtraLayout = QVBoxLayout()
        frame3ExtraLayout.addWidget(self.memberLabel)
        frame3Extra.setLayout(frame3ExtraLayout)

        ##Frame3 main-layout add all the two sub-frames
        frame3BigFrame = QFrame()
        frame3BigFrameLayout = QVBoxLayout()
        frame3BigFrameLayout.addWidget(frame3Extra)
        frame3BigFrameLayout.addWidget(frame3Extra2)

        frame3 = QFrame()
        frame3.setLayout(frame3BigFrameLayout)


        ##Frame3 all signal Handling
        self.search1Line.editingFinished.connect(self.scrollToItem)
        self.search2Line.editingFinished.connect(self.scrollToItem)
        self.addBut.clicked.connect(self.addMemberButClicked)
        self.subBut.clicked.connect(self.delMemberButClicked)




        ##frame4 Add/Remove phase:
        self.phaseLabel = QLabel("Add/Remove Phase: ")
        self.phaseTitleLabel = QLabel("Title: ")
        self.phaseIDLabel = QLabel("PhaseID: ")
        self.phaseIDLine = QLineEdit()
        self.phaseTitleLine = QLineEdit()
        self.precendentLabel = QLabel("Precendent: ")
        self.precendentLine = QLineEdit()
        self.addPhaseBut = QPushButton("Add Phase")
        self.removePhaseBut = QPushButton("Remove Phase")
        self.phaseList= QListWidget()

        ##Publish and Cancel Button
        self.publishBut = QPushButton("Publish")
        self.cancelBut = QPushButton("Cancel")


        ##Phase Table setUP
        # self.phaseTable.setColumnCount(3)
        # self.phaseTable.setRowCount(10)
        # self.rCount = 0
        # self.cCount = 0


        ##Al frame4 sub-frame layout set-up
        minif41Layout = QVBoxLayout()
        minif42Layout = QHBoxLayout()
        minif43Layout = QVBoxLayout()
        minif44Layout = QHBoxLayout()

        ##Add widget to frame4 sub-frame1 layout
        minif41Layout.addWidget(self.phaseLabel)


        ##Add widget to frame4 sub-frame2 layout
        minif42Layout.addWidget(self.phaseTitleLabel)
        minif42Layout.addWidget(self.phaseTitleLine)
        minif42Layout.addWidget(self.phaseIDLabel)
        minif42Layout.addWidget(self.phaseIDLine)
        minif42Layout.addWidget(self.precendentLabel)
        minif42Layout.addWidget(self.precendentLine)
        minif42Layout.addWidget(self.addPhaseBut)


        ##ADD widgets to frame4 sub-frame3 layout
        minif43Layout.addWidget(self.phaseList)
        minif43Layout.addWidget(self.removePhaseBut)


        ##Add button to frame4 sub-frame3 layout
        minif44Layout.addWidget(self.publishBut)
        minif44Layout.addWidget(self.cancelBut)



        ##All frame4 sub-frame layout setup
        minif41 = QFrame()
        minif42 = QFrame()
        minif43 = QFrame()
        minif44 = QFrame()

        minif41.setLayout(minif41Layout)
        minif42.setLayout(minif42Layout)
        minif43.setLayout(minif43Layout)
        minif44.setLayout(minif44Layout)



        ##Frame4 Layout add all frame4 sub-frames
        frame4Layout = QVBoxLayout()
        frame4Layout.addWidget(minif41)
        frame4Layout.addWidget(minif42)
        frame4Layout.addWidget(minif43)
        frame4Layout.addWidget(minif44)



        ##Frame4 set main layout
        frame4 = QFrame()
        frame4.setLayout(frame4Layout)

        ##All Signal Handling of widgets attached to handling function
        self.phaseIDLine.editingFinished.connect(self.phaseIDValidation)
        self.precendentLine.editingFinished.connect(self.phasePrecendentValidation)
        self.addPhaseBut.clicked.connect(self.addPhaseButClicked)
        self.removePhaseBut.clicked.connect(self.removePhaseButClicked)
        self.publishBut.clicked.connect(self.publishButClicked)
        self.cancelBut.clicked.connect(self.cancelButClicked)






        scrollWidgetLayout.addWidget(frame1)
        scrollWidgetLayout.addWidget(frame2)
        scrollWidgetLayout.addWidget(frame3)
        scrollWidgetLayout.addWidget(frame4)
        scrollWidget.setLayout(scrollWidgetLayout)



        ##Scroll Area set up
        scrollArea = QScrollArea()
        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setWidgetResizable(False)
        scrollArea.setWidget(scrollWidget)




        scrollArea.setStyleSheet("QScrollArea {Background-color: rgba(0,0,0,0%)}")

        self.layout.addWidget(scrollArea)

        self.setLayout(self.layout)




    def addMemberButClicked(self):
        for i in self.listAll.selectedItems():
            self.listMembers.addItem(self.listAll.takeItem(self.listAll.row(i)))


    def delMemberButClicked(self):
        for i in self.listMembers.selectedItems():
            self.listAll.addItem(self.listMembers.takeItem(self.listMembers.row(i)))


    def addPhaseButClicked(self):
        phase = Phase(self.phaseTitleLine.text(),self.phaseIDLine.text(),self.precendentLine.text())
        self.phaseList.addItem(phase.getPhaseTitle() + " " + phase.getPhaseID() + " " + phase.getPhasePrecendentString())

        ##Phase TAble
        # name = phase.getPhaseTitle()
        # id = phase.getPhaseID()
        # pres = phase.getPhasePrecendentString()
        # item = QTableWidgetItem(name)
        # self.phaseTable.setItem(self.rCount,self.cCount,item)
        # self.cCount = (self.cCount + 1) % self.phaseTable.columnCount()
        #
        #
        # item = QTableWidgetItem(id)
        # self.phaseTable.setItem(self.rCount, self.cCount, item)
        # self.cCount = (self.cCount + 1) % self.phaseTable.columnCount()
        #
        #
        # item = QTableWidgetItem(pres)
        # self.phaseTable.setItem(self.rCount, self.cCount, item)
        # self.cCount = (self.cCount + 1) % self.phaseTable.columnCount()
        #
        # if (self.rCount + 1 == self.phaseTable.currentRow()):
        #     self.phaseTable.setRowCount(self.phaseTable.rowCount() + 10)
        # self.rCount += 1
#######
    def siteCodeValidation(self):
        print("Validating site code" + self.codeLine.text())
        self.codeLine.setStyleSheet("color: red;")
        ##Comparison,initialise condition to True
        condition = False
        if (not condition):
            self.codeLine.setText("Site code already existed")
########
    def projectTitleValidation(self):
        print("Validating project name..." + self.projNameLine.text())
        self.projNameLine.setStyleSheet("color: red;")
        condition = False
        if (not condition):
            self.projNameLine.setText("This project already existed")
#######
    def phaseIDValidation(self):
        print("Validating id >>> " + self.phaseIDLine.text())
        self.phaseIDLine.setStyleSheet("color: red")
        condition = False
        if (not condition):
            self.phaseIDLine.setText("Phase ID duplicated")

######
    def phasePrecendentValidation(self):
        print("Validating precendt id: ")
        self.precendentLine.setStyleSheet("color: red")
        condition = False
        if (not condition):
            self.precendentLine.setText("Phase Id does not existed!")

    def removePhaseButClicked(self):
        for i in self.phaseList.selectedItems():
            self.phaseList.takeItem(self.phaseList.row(i))





#######
    def populateAllLists(self):
        for i in range(10):
            self.listAll.addItem("item " + str(i))

        for i in range(11, 14):
            self.listMembers.addItem("item " + str(i))

    def scrollToItem(self):
        # for i in self.listAll.findItems(self.search1Line.text(),Qt.MatchExactly):
            # self.listAll.scrollTo(self.listAll.row(i))
        print("Scrolling..")


#########
    def publishButClicked(self):
        print('published button has been clicked')
        createOrViewProjWindow = CreateOrViewProjectPage.CreateOrViewProjectMainWindow(self.mainWindow)
        self.mainWindow.setCentralWidget(createOrViewProjWindow)
        self.mainWindow.setStyleSheet("LogInMainWindow {background-image: url(/Users/Chieh/Desktop/EngineerHub/Images/MenuBack.jpg)}")




    def cancelButClicked(self):
        print('cancel button has been clicked')
        createOrViewProjWindow = CreateOrViewProjectPage.CreateOrViewProjectMainWindow(self.mainWindow)
        self.mainWindow.setCentralWidget(createOrViewProjWindow)
        self.mainWindow.setStyleSheet(
            "LogInMainWindow {background-image: url(/Users/Chieh/Desktop/EngineerHub/Images/MenuBack.jpg)}")





























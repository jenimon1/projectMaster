import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *

class DraggableLabel(QLabel):

    def __init__(self,parent = None):
        super(DraggableLabel,self).__init__(parent)
        self.myMimeType = 'application/MyWindow'

        self.setStyleSheet("""
            background-color: black;
            color: white;
            font: bold;
            padding: 6px;
            border-width: 2px;
            border-style: solid;
            border-radius: 16px;
            border-color: white;
        """)


    def mousePressEvent(self,event):
        itemData = QByteArray()
        # texto = QString(self.text())
        # dataStream.writeString(texto)
        dataStream = QDataStream(itemData,QIODevice.WriteOnly)
        dataStream << QPoint(event.pos() - self.rect().topLeft())

        mimeData = QMimeData()
        mimeData.setData(self.myMimeType,itemData)
        mimeData.setText(self.text())

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - self.rect().topLeft())

        self.hide()

        if drag.exec_(Qt.MoveAction, Qt.CopyAction) == Qt.MoveAction:
            self.close()
        else:
            self.show()

class MyFrame(QFrame):
    dropped = pyqtSignal()
    def __init__(self, parent, stat):
        super(MyFrame, self).__init__(parent)
        self.status = stat

        self.setStyleSheet("""
            background-color: lightgray;
            border-width: 2px;
            border-style: solid;
            border-color: black;
            margin: 2px;
        """)
        self.phaseList = []

        self.myMimeType = 'application/MyWindow'

        self.plusValue = 6

        # self.initUI()

        # y = 6
        # for labelNumber in range(6):
        #     label = DraggableLabel(self)
        #     label.setText("Label #{0}".format(labelNumber))
        #     label.move(6, y)
        #     label.show()
        #     self.phaseList.append(label)
        #
        #     y += label.height() + 2

        self.setAcceptDrops(True)


    def initUI(self):
        y = 6
        for p in self.phaseList:
            label = DraggableLabel(self)
            label.setText(p.getPhaseTitle() + " " + str(p.getPhaseID()))
            label.move(6,y)
            label.show()
            y += label.height() + 2





    def addPhase(self,phaseName,phaseId):
        phase = DraggableLabel(self)
        phase.setText(phaseName + " " + str(phaseId))
        self.phaseList.append(phase)
        phase.move(6,self.plusValue)
        phase.show()
        self.plusValue += phase.height() + 2

    def removePhase(self,phase):
        for i in self.phaseList:
            if (i.text() == phase):
                self.phaseList.remove(i)
                break


    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat(self.myMimeType):

            if event.source() in self.children():
                event.setDropAction(Qt.MoveAction)
                event.accept()
            else:
                event.acceptProposedAction()

        else:
            event.ignore()

    def dropEvent(self, event):

        if event.mimeData().hasFormat(self.myMimeType):
            if (self.isPhaseInPhaseList(event.mimeData().text()) == False):
                self.phaseList.append(DraggableLabel(event.mimeData().text()))
                self.drop.emit()
            mime = event.mimeData()
            itemData = mime.data(self.myMimeType)
            dataStream = QDataStream(itemData, QIODevice.ReadOnly)

            text = QByteArray()
            offset = QPoint()
            dataStream >> text >> offset

            newLabel = DraggableLabel(self)
            newLabel.setText(event.mimeData().text())
            newLabel.move(event.pos())
            newLabel.show()

            if event.source() in self.children():
                event.setDropAction(Qt.MoveAction)
                event.accept()

            else:
                event.acceptProposedAction()
        else:
            event.ignore()


    def dragMoveEvent(self,event):
        if event.mimeData().hasFormat(self.myMimeType):
            self.removePhase(event.mimeData().text())
            event.accept()
        else:
            event.ignore()




    def getPhaseList(self):
        return self.phaseList

    def isPhaseInPhaseList(self,string):
        for i in self.phaseList:
            if i.text() == string:##if that phase is already in the list
                return True
        return False ##if that phase is not in the list



    def printAllElements(self):
        print(len(self.phaseList))
        for i in self.phaseList:
            print(i.text())




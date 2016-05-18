import  os
import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *



class myProjectMemberPageMainWindow(QWidget):

    def __init__(self,mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.initUI()




    def initUI(self):

        ##ALL neccessary widgets set up
        self.toDoList = DragDropListWidget(self)
        self.doingList = DragDropListWidget(self)
        self.doneList = DragDropListWidget(self)
        self.updateBut = QPushButton("Update",self)
        self.cancelBut = QPushButton("Cancel",self)

        ##All widget set up
        self.populateList()


        ##Absolute Positioning of all widgets
        self.toDoList.setGeometry(50,180,300,400)
        self.doingList.setGeometry(375, 180, 300, 400)
        self.doneList.setGeometry(700, 180, 300, 400)
        self.updateBut.setGeometry(820,620,80,50)
        self.cancelBut.setGeometry(900,620,80,50)




        ##All signal Handling widget attatch to function
        # self.doingList.clicked.connect(self.pictureDropped)




    def populateList(self):
        for i in range(5):
            self.toDoList.addItem("Item " + str(i))

        for i in range(5,10):
            self.doingList.addItem("Item " + str(i))

        for i in range(10,15):
            self.doneList.addItem("Item " + str(i))

    def pictureDropped(self, l):
        for url in l:
            if os.path.exists(url):
                picture = Image.open(url)
                picture.thumbnail((72, 72), Image.ANTIALIAS)
                icon = QIcon(QPixmap.fromImage(ImageQt.ImageQt(picture)))
                item = QListWidgetItem(os.path.basename(url)[:20] + "...", self.doingList)
                item.setStatusTip(url)
                item.setIcon(icon)



class DragDropListWidget(QListWidget):

    def __init__(self, parent = None):
        super(DragDropListWidget,self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)


    def dragEnterEvent(self,event):
        event.accept()



    def dropEvent(self,e):
        print("enter la na")
        print(e.)






# class DragDropListWidget(QListWidget):
#     def __init__(self, parent=None):
#         super(DragDropListWidget, self).__init__(parent)
#         self.setAcceptDrops(True)
#         self.setIconSize(QSize(72, 72))
#
#     def dragEnterEvent(self, event):
#         if event.mimeData().hasUrls():
#             event.accept()
#         else:
#             event.ignore()
#
#     def dragMoveEvent(self, event):
#         if event.mimeData().hasUrls():
#             event.setDropAction(Qt.CopyAction)
#             event.accept()
#         else:
#             event.ignore()
#
#
#     def dropEvent(self,event):
#         if event.mimeData().hasUrls():
#             event.setDropAction(Qt.CopyAction)
#             event.accept()
#             listo = []
#             for url in listo:
#                 listo.append(str(url.toLocalFile()))
#                 self.emit(SIGNAL("dropped"),listo)
#         else:
#             event.ignore()











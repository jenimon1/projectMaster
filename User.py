
class User:

    def __init__(self,name,usern,passs,email,phoneNo):
        self.__name = name
        self.__userName = usern
        self.__password = passs
        self.__email = email
        self.__phoneNo = phoneNo
        self.__projectList = []


    def addProject(self,proj):
        self.__projectList.append(proj)

    def removeProject(self,proj):
        self.__projectList.remove(proj)


    def setName(self,n):
        self.__name = n

    def getName(self):
        return self.__name

    def setPassword(self,np):
        self.__password = np

    def getPassword(self):
        return self.__password

    def setEmail(self,e):
        self.__email = e

    def getEmail(self):
        return self.__email

    def setPhoneNo(self,phone):
        self.__phoneNo = phone

    def getPhoneNo(self):
        return self.__phoneNo
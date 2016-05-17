
from LoginPage import *
class Project:

    def __init__(self,projTitle,code,re,ss,cs,type,sc,height,client,projH):
        self.__projTitle = projTitle
        self.__siteCode = code
        self.__region = re
        self.__surveySubcontract = ss
        self.__constructionSubcontract = cs
        self.__type = type
        self.__siteConfiguration = sc
        self.__height = height
        self.__client = client
        self.__projectHead = projH
        self.__memberList = []


    def getProjectHead(self):
        return self.__p


    def addMember(self,user):
        self.__memberList.append(user)

    def remove(self,user):
        self.__memberList.remove(user)


    def newlyTrial(self):
        print("try1")
        print("try1")
        print("try1")




    def getProjectTitle(self):
        return self.__projTitle


    def getSiteCode(self):
        return self.__siteCode

    def getRegion(self):
        return self.__region

    def setSurveySubcontract(self,data):
        self.__surveySubcontract = data

    def getSurveySubcontract(self):
        return self.__surveySubcontract

    def setConstructionSubContract(self,data):
        self.__constructionSubcontract = data

    def getConstructionSubContract(self):
        return self.__constructionSubcontract

    def setType(self,type):
        self.__type = type

    def getType(self):
        return self.__type

    def setSiteConfiguration(self,data):
        self.__siteConfiguration = data

    def getSiteConfiguration(self):
        return self.__siteConfiguration

    def setHeight(self,height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def setClient(self,c):
        self.__client = c

    def getClient(self):
        return self.__height


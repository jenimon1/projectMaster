



class Phase:

    def __init__(self,phaseName,phaseId,phasePresString):
        self.__phaseTitle = phaseName
        self.__phaseId = phaseId
        self.__phasePrecendentTuple = tuple(self.stringManipulate(phasePresString))
        self.__phasePrecendentString = phasePresString



    def setPhaseTitle(self,name):
        self.__phaseTitle = name

    def getPhaseTitle(self):
        return self.__phaseTitle

    def setPhasePrecendent(self,tub):
        self.__phasePrecendentTuple = tub

    def getPhasePrecendent(self):
        return self.__phasePrecendentTuple

    def getPhasePrecendentString(self):
        return self.__phasePrecendentString

    def getPhaseID(self):
        return self.__phaseId

    def stringManipulate(self,string):
        tempList = []
        for ch in string:
            if (ch != ','):
                tempList.append(ch)

        return tempList




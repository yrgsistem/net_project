class Bina:

    def __init__(self,id,ad,backboneip):
        self.__id = id
        self.__ad = ad
        self.__backboneip = backboneip

    def getId(self):
        return self.__id

    def setId(self,id):
        self.__id = id

    def getAd(self):
        return self.__ad

    def setAd(self,ad):
        self.__ad = ad

    def getBackboneip(self):
        return self.__backboneip

    def setBackboneip(self,backboneip):
        self.__backboneip = backboneip

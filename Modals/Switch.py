from Tools.SnmpConnections import SnmpProtocol

class Switch:

    def __init__(self,ip,status,Bina,SnmpProtocol):
        #self.__id = id
        self.__ad = ""
        self.__ip = ip
        self.__Bina = Bina
        self.__status = status
        try:
            stmt = SnmpProtocol.execute(ip, '1.3.6.1.2.1.1', '"3.6.1.2.1.1.5.0"')
            eachline = stmt.splitlines()
            for i in eachline:
                ad = i.split(' ')[3]
                self.setAd(ad)
        except:
            print("hata")

    def getAd(self):
        return self.__ad

    def setAd(self,ad):
        self.__ad = ad

    def getIp(self):
        return self.__ip

    def setIp(self, ip):
        self.__ip = ip

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status

    def getBina(self):
        return self.__Bina

    def setBina(self, Bina):
        self.__Bina = Bina

from SnmpConnections import SnmpProtocol

class Switch:

    def __init__(self,ip):
        self.ip = ip
        self.ad = "Yok"
        SnmpProtocol2 = SnmpProtocol()
        try:
            stmt = SnmpProtocol2.execute (ip, '1.3.6.1.2.1.1', '"3.6.1.2.1.1.5.0"')
            eachline = stmt.splitlines ()
            for i in eachline:
                ad = i.split (' ')[3]
                self.ad = ad
        except:
            print("hata")

    def setClients(self,clients):
        self.clients = clients

from SnmpConnections import SnmpProtocol
from Switch import Switch

class Backbone:

    switches = []

    def __init__(self,id,ip,binaad,binaid):
        self.id = id
        self.ip = ip
        self.binaid = binaid
        self.binaad = binaad

        SnmpProtocol2 = SnmpProtocol()
        switches = []
        stmt = SnmpProtocol2.execute(ip, '1.3.6.1.2.1.4.22.1.1', '"INTEGER: 28"')
        eachline = stmt.splitlines ()
        for i in eachline:
            a = (i.split ('.'))
            if (a[14].split (' ')[0] != '1'):
                ip =a[11] + "." + a[12] + "." + a[13] + "." + a[14].split (' ')[0]
                switch = Switch(ip)
                switches.append(switch)
        self.switches = switches


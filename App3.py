from Controllers.BinaController import BinaController
from Modals.Bina import Bina
from Modals.Switch import Switch
from Tools.SnmpConnections import SnmpProtocol
from Tools.QueryExecuter import QueryExecuter

bc = BinaController()
qe = QueryExecuter()
binalar = bc.getBinas
SnmpProtocol = SnmpProtocol()
for bina in binalar:
    switches = []
    stmt = SnmpProtocol.execute(bina.getBackboneip(), '1.3.6.1.2.1.4.22.1.1', '"INTEGER: 28"')
    eachline = stmt.splitlines()
    for i in eachline:
        a = (i.split('.'))
        if (a[14].split(' ')[0] != '1'):
            ip = a[11] + "." + a[12] + "." + a[13] + "." + a[14].split(' ')[0]
            switch = Switch(ip,1,bina,SnmpProtocol)
            print(switch.getBina().getAd()+"-"+switch.getIp()+"-"+str(switch.getStatus())+"-"+switch.getAd())
            flag = qe.insertdeletequery("INSERT INTO switch (ad,ip,bina_id,status) VALUES (%s,%s,%s,%s)",[switch.getAd(),switch.getIp(),switch.getBina().getId(),switch.getStatus()])

from SnmpConnections import SnmpProtocol
from QueryExecuter import querytrigger
from Backbone import Backbone
from Switch import Switch
from Client import Client
from Helper import Helper

dbclass = querytrigger()

sql = "SELECT backbone.id as id, backbone.ip as ip, bina.ad as binaad,bina.id as binaid FROM backbone INNER JOIN bina ON (backbone.binaid = bina.id) WHERE backbone.switchkontrol = 1 ORDER BY backbone.id ASC"
records = dbclass.simpleselectquery(sql)

if(len(records) > 0):
    backbones = []
    SnmpProtocol = SnmpProtocol()
    for record in records:
        switches = []
        backbone = Backbone(str(record[0]), record[1], record[2], record[3])
        backbones.append(backbone)

for backbone in backbones:
    print(backbone.id)
    print(backbone.binaad)
    print(backbone.ip)
    switches = backbone.switches
    for switchsingle in switches:
        stmt2 = SnmpProtocol.execute(switchsingle.ip,'1.3.6.1.2.1.17.7.1.2.2.1.2','-v "INTEGER: 418"')
        eachline = stmt2.splitlines()
        print("SwitchIp:"+switchsingle.ip)
        for i in eachline:
            clients = []
            #maci convert et ve vlan çek
            rtr = Helper.decimaltohex(i)
            mac = rtr[0]
            vlan = str(rtr[1])
            #port string olarak bul
            port = Helper.findport(i,switchsingle.ip,SnmpProtocol)
            client = Client(mac,port,vlan)
            clients.append(client)
            switchsingle.setClients(clients)
            for client in clients:
                print("Mac: "+client.mac + " Port: "+client.port+ " Vlan: "+client.vlan)


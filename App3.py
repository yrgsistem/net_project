from typing import List

from Controllers.BinaController import BinaController
from Modals.Bina import Bina
from Modals.Client import Client
from Modals.Switch import Switch
from Tools.SnmpConnections import SnmpProtocol
from Tools.QueryExecuter import QueryExecuter
from Tools.Helper import Helper

bc = BinaController()
qe = QueryExecuter()
binalar = bc.getBinas
SnmpProtocol = SnmpProtocol()

for bina in binalar:
    print(bina.getAd())
    print("___________________________________________")
    stmt = SnmpProtocol.execute(bina.getBackboneip(), '1.3.6.1.2.1.4.22.1.1', '"INTEGER: 28"')
    eachline = stmt.splitlines()
    for i in eachline:
        a = (i.split('.'))
        if (a[14].split(' ')[0] != '1'):
            ip = a[11] + "." + a[12] + "." + a[13] + "." + a[14].split(' ')[0]
            switch = Switch(ip,1,bina,SnmpProtocol)
            #print(switch.getBina().getAd()+"-"+switch.getIp()+"-"+str(switch.getStatus())+"-"+switch.getAd())
            #flag = qe.insertdeletequery("INSERT INTO switch (ad,ip,bina_id,status) VALUES (%s,%s,%s,%s)",[switch.getAd(),switch.getIp(),switch.getBina().getId(),switch.getStatus()])
            #GETCLIENTS
            print(switch.getAd())
            clients: List[Client] = []
            stmt2 = SnmpProtocol.execute(switch.getIp(), '1.3.6.1.2.1.17.7.1.2.2.1.2', '-Ev "INTEGER: 419|INTEGER: 418"')
            eachline = stmt2.splitlines()
            for i in eachline:
                rtr = Helper.findmacvlan(i)
                mac = rtr[0]
                vlaninfo = str(rtr[1])
                mac = mac[0] + mac[1] + " " + mac[2] + mac[3] + " " + mac[4] + mac[5] + " " + mac[6] + mac[
                        7] + " " + mac[8] + mac[9] + " " + mac[10] + mac[11]

                client = Client(mac, vlaninfo, bina.getBackboneip(),switch.getIp(), i, SnmpProtocol)
                clients.append(client)
                #print("PORT:" + client.port + "-Mac: " + client.mac + " Vlan: " + str(
                  #  client.vlaninfo) + "IP:" + client.ip + "-Switchip: " + client.switchip)
            for cl in clients:
                flag = qe.insertdeletequery("INSERT INTO client (port,mac,vlan,ip,backbone_ip) VALUES (%s,%s,%s,%s,%s)",[cl.port,cl.mac,cl.vlaninfo,cl.ip,switch.getIp()])

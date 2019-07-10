from SnmpConnections import SnmpProtocol
from BackboneController import BackboneController
from Client import Client
from Helper import Helper

bc = BackboneController()
coming = bc.whichbackbone()
backboneidlist = coming[1]
soru = coming[0]
print(soru)

while True:
    backboneid = input("Bina Seçiniz...")
    if(backboneid=="q"):
        print("Program sonlanıyor...")
        break
    elif (backboneid in backboneidlist):
        while True:
            macsearch = input("Mac Adresi Giriniz... \nÇıkmak İçin Q...")
            if (len(macsearch) == 12):
                sc = SnmpProtocol()
                clients = []
                flag = 'false'
                backbone = bc.findbyid(backboneid)
                for switchsingle in backbone.switches:
                    stmt2 = sc.execute (switchsingle.ip, '1.3.6.1.2.1.17.7.1.2.2.1.2', '-v "INTEGER: 418"')
                    eachline = stmt2.splitlines ()
                    for i in eachline:
                        rtr = Helper.findmacvlan (i)
                        mac = rtr[0]
                        if(macsearch == mac):
                            flag = 'true'
                            vlaninfo = str (rtr[1])
                            mac = mac[0]+mac[1]+" "+mac[2]+mac[3]+" "+mac[4]+mac[5]+" "+mac[6]+mac[7]+" "+mac[8]+mac[9]+" "+mac[10]+mac[11]
                            client = Client(mac,vlaninfo,backbone.ip,switchsingle.ip,i,sc)
                            clients.append(client)
                            #switchsingle.setClients(clients)
                for client in clients:
                    print ("Mac: " + client.mac + " Port: " + client.port + " Vlan: " + client.vlaninfo + " Ip: " + client.ip + "switchi" + client.switchip+" line" + client.line)
                if (flag != 'true'):
                    print ("Sonuç Bulunamadı")
            elif(mac == "q"):
                print("Program sonlanıyor...")
                break
    else:
        print("geçersiz")


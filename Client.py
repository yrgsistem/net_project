from Helper import Helper
class Client:


    def __init__(self, mac, vlaninfo, backboneip, switchip, line, sc):
        mac = mac.upper ()
        port = Helper.findport (line, switchip, sc)
        ip = Helper.findip (mac, backboneip, sc)
        self.mac = mac
        self.vlaninfo = vlaninfo
        self.ip = ip
        self.port = port
        self.switchip = switchip
        self.line = line



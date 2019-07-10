from QueryExecuter import querytrigger
from Backbone import Backbone

class BackboneController:

    def findbyid(self,backboneid):
        dbclass = querytrigger()
        sql = "SELECT backbone.id as id, backbone.ip as ip, bina.ad as binaad,bina.id as binaid FROM backbone INNER JOIN bina ON (backbone.binaid = bina.id) WHERE backbone.id = %s ORDER BY backbone.id ASC"
        records = dbclass.selectquery (sql, backboneid)
        if (len (records) > 0):
            for record in records:
                backbone = Backbone (str (record[0]), record[1], record[2], record[3])
        return backbone

    def whichbackbone(self):
        dbclass = querytrigger()
        sql = "SELECT backbone.id as id, backbone.ip as ip, bina.ad as binaad FROM backbone INNER JOIN bina ON (backbone.binaid = bina.id) WHERE backbone.switchkontrol = 1 ORDER BY backbone.id ASC"
        records = dbclass.simpleselectquery (sql)
        backboneidlist = []
        soru1 = ""
        if (len (records) > 0):
            for record in records:
                soru1 = soru1 + str (record[0]) + ". " + record[2] + " - " + record[1] + "\n"
                backboneidlist.append (str (record[0]))
        soru1 = soru1 + "Q. Programdan çıkmak için."
        return soru1,backboneidlist
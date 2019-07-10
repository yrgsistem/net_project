from Tools.QueryExecuter import QueryExecuter
from Modals.Bina import Bina

class BinaController:

    def findBina(self,binaid):
        dbclass = QueryExecuter()
        sql = "SELECT id,ad,backboneip FROM bina WHERE id = %s ORDER BY id ASC"
        records = dbclass.selectquery (sql, binaid)
        if (len (records) > 0):
            for record in records:
                bina = Bina(str (record[0]), record[1], record[2])
        return bina

    @property
    def getBinas(self):
        dbclass = QueryExecuter()
        sql = "SELECT id,ad,backboneip FROM bina ORDER BY id ASC"
        records = dbclass.simpleselectquery (sql)
        binalist = []
        if (len (records) > 0):
            for record in records:
                bina = Bina(record[0], str(record[1]),record[2])
                binalist.append (bina)
        return binalist
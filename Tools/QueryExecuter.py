from Tools.ConnectionSingleton import uniqueconn

class QueryExecuter:

    def getcon(self):
        dbclass = uniqueconn()
        baglanti = dbclass.conn()
        cur = baglanti.cursor()
        return cur, baglanti

    def selectquery(self, sorgu, vars):
        array_source = self.getcon()
        stmt = array_source[0]
        baglanti = array_source[1]
        stmt.execute(sorgu, vars)
        records = stmt.fetchall()
        stmt.close()
        del stmt
        baglanti.close()
        return records

    def simpleselectquery(self, sorgu):
        array_source = self.getcon()
        stmt = array_source[0]
        baglanti = array_source[1]
        stmt.execute(sorgu)
        records = stmt.fetchall()
        stmt.close()
        del stmt
        baglanti.close()
        return records

    def insertdeletequery(self, sorgu, vars):
        array_source = self.getcon()
        stmt = array_source[0]
        baglanti = array_source[1]
        stmt.execute(sorgu, vars)
        baglanti.commit()
        stmt.close()
        del stmt
        baglanti.close()













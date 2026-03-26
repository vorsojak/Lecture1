
from dao.db_connect import dbConnect
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord


class DAO:

    def getAllProdotti(self):
        cnx = dbConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("select * from prodotti")
        row = cursor.fetchall()
        res = []

        for p in row:
            res.append(ProdottoRecord(p["nome"], p["prezzo"], 1))

        cursor.close()
        cnx.close()
        return res

    def getAllClienti(self):
        cnx = dbConnect().getConnection()

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("select * from clienti")
        row = cursor.fetchall()
        res = []

        for p in row:
            res.append(ClienteRecord(p["nome"], p["mail"], p["categoria"]))

        cursor.close()
        cnx.close()
        return res

    def add_prodotto(self, prodotto):
        cnx = dbConnect().getConnection()

        cursor = cnx.cursor()
        query = """insert into prodotti
                    (nome, prezzo, quantita) values (%s, %s, %s)"""
        cursor.execute(query,(prodotto.name, prodotto.prezzo_unitario, prodotto.quantity))

        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def add_cliente(self, cliente):
        cnx = dbConnect.getConnection()

        cursor = cnx.cursor()
        query = """insert into clienti
                    (nome, mail, categoria) values (%s,%s,%s)"""

        cursor.execute(query, (cliente.name, cliente.mail, cliente.categoria))

        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def hasProdotto(self, prodotto):
        cnx = dbConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = "Select * from prodotti where nome = %s"
        cursor.execute(query, (prodotto.name,))
        row =cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0

    def hasCliente(self, cliente):
        cnx = dbConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = "Select * from clienti where mail = %s"
        cursor.execute(query, (cliente.mail,))
        row =cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0





if __name__ == "__main__":
    myDAO = DAO()
    myDAO.getAllProdotti()
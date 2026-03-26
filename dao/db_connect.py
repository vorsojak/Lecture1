import mysql.connector



class dbConnect:

    @classmethod
    def getConnection(cls):

        try:
            cnx = mysql.connector.connect(
                user = "root",
                password = "root1",
                host="127.0.0.1",
                database="sw_gestionale"
            )
            return cnx
        except mysql.connector.Error as err:
            print("Non sono riuscito a stabilire la connessione")
            print(err)
            return None
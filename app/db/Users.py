import json
import mysql.connector
from .DBConnection import DBUtility
# qui creo la classe User dove metto i metodi che andrò a richiamare nelle API
class User:
    @staticmethod
    def getAllUsers():
        connessione = DBUtility.getConnection()
        allUsers = []
        try:
            # Generazione del cursore
            cursore = connessione.cursor()
            # Comando SQL per la visualizzazione dei database in formato SQL
            cursore.execute("select U.username, U.password from utente U")
            # get all records
            records = cursore.fetchall()
            # salva tutti gli elementi del record in una lista 
            for elem in records:
                allUsers.append(elem)
        except mysql.connector.Error as e:
                    print("Error reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()
                cursore.close()
        
        return json.dumps(allUsers)

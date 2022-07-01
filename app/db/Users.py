from fastapi.responses import JSONResponse
import mysql.connector
from .DBConnection import DBUtility
# qui creo la classe User dove metto i metodi che andrò a richiamare nelle API
class User:
    @staticmethod
    def getAllUsers():
        connessione = DBUtility.getConnection()
        user = []
        password = []
        try:
            # Generazione del cursore
            cursore = connessione.cursor()
            # Comando SQL per la visualizzazione dei database in formato SQL
            cursore.execute("select U.username, U.password from utente U")
            # get all records
            records = cursore.fetchall()
            # salva tutti gli elementi del record in una lista 
            for elem in records:
                user.append(elem[0])
                password.append(elem[1])
            dict_users = dict(zip(user, password))
        except mysql.connector.Error as e:
                    print("Error reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()
                cursore.close()
        
        return dict_users

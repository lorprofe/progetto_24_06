import json
import mysql.connector
from .DBConnection import DBUtility
from fastapi.responses import JSONResponse
# creo la classe Questions in cui metto tutti i metodi che mi serviranno come api
class Questions:
    # metodo che restituisce tutta la lista delle domande
    @staticmethod
    def getAllQuestions():
        connessione = DBUtility.getConnection()
        key = list()
        value = list()
        try:
            # Generazione del cursore
            cursore = connessione.cursor()
            # Comando SQL per la visualizzazione dei database in formato SQL
            cursore.execute("select id_domanda, domanda from domanda")
            # get all records
            records = cursore.fetchall()
            # salva tutti gli elementi del record in una lista 
            for elem in records:
                key.append(elem[0])
                value.append(elem[1])
            dict_questions = dict(zip(key, value))
        except mysql.connector.Error as e:
                    print("Error reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()
                cursore.close()
        
        return dict_questions




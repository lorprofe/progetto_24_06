import json
import mysql.connector
from .DBConnection import DBUtility
# in questo file creo la classe Answers dove inserisco tutti i metodi che andrò ad utilizzare nell'API
class Answers:
    # metodo che restituisce tutte le risposte di ogni domanda
    @staticmethod
    def getAllAnswers():
        connessione = DBUtility.getConnection()
        allAnswers = []
        try:
            # Generazione del cursore
            cursore = connessione.cursor()
            # Comando SQL per la visualizzazione dei database in formato SQL
            cursore.execute("select R.risposta, R.esito, D.id_domanda from risposte R, domanda D where R.id_domanda = D.id_domanda")
            # get all records
            records = cursore.fetchall()
            # salva tutti gli elementi del record in una lista 
            for elem in records:
                allAnswers.append(elem)
        except mysql.connector.Error as e:
                    print("Error reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()
                cursore.close()
        
        return json.dumps(allAnswers)

    
import mysql.connector
from datetime import datetime
from .DBConnection import DBUtility
# creo la classe RisultatiTes che è quella che andrà a gestire la stampa a schermo e l'inserimento nel db dei risultati del quiz
class RisultatiTest:
    @staticmethod
    def getClassificaFinale():
        connessione = DBUtility.getConnection()
        classificaFinale = []
        try:
            # Generazione del cursore
            cursore = connessione.cursor()
            # Comando SQL per la visualizzazione dei database in formato SQL
            cursore.execute("select U.nome, U.cognome, TR.score, TR.data_test from utente U, test_risultati TR where TR.fk_utente = U.id_utente ")
            # get all records
            records = cursore.fetchall()
            # salva tutti gli elementi del record in una lista 
            for elem in records:
                classificaFinale.append(elem)
        except mysql.connector.Error as e:
                    print("Error reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()
                cursore.close()
        
        return classificaFinale

    @staticmethod 
    def addValuesInClassifica(id_utente, score, data):
        connessione = DBUtility.getConnection()
        somma = 0
        try:
            # Generazione del cursore
            cursore = connessione.cursor()
            # Query SQL per ottenere lo score da sommare
            query1 = """SELECT score FROM test_risultati WHERE fk_utente = %s;"""
            cursore.execute(query1, (id_utente, ))
            # prendo il record dal cursore con il fetchall() e accedo all'int mediante un doppio indice, in quanto all'interno della lista dei records ho una tupla contenente il valore del campo score
            records = cursore.fetchall()
            somma = records[0][0] + score
            # Query SQL per l'inserimento dei valori nel database in formato SQL
            query2 = """UPDATE test_risultati SET score = %s, data_test = %s WHERE fk_utente = %s;COMMIT;"""
            cursore.execute(query2, (somma, data, id_utente))
            return print(f"""Modifica avvenuta con successo, aggiunti {score} punti, in data {data}, all'utente {id_utente}, ora ha {somma} punti""")
        except mysql.connector.Error as e:
                    print("Error reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()
                cursore.close()
    

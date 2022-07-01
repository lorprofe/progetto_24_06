import mysql.connector
from .DBConnection import DBUtility
from fastapi.responses import JSONResponse
# creo la classe RisultatiTes che è quella che andrà a gestire la stampa a schermo e l'inserimento nel db dei risultati del quiz
class RisultatiTest:
    @staticmethod
    def getClassificaFinale():
        connessione = DBUtility.getConnection()
        id_utente = []
        nome = []
        cognome = []
        score = []
        try:
            # Generazione del cursore
            cursore = connessione.cursor()
            # Comando SQL per la visualizzazione dei database in formato SQL
            cursore.execute("select U.id_utente, U.nome, U.cognome, TR.score, TR.data_test from utente U, test_risultati TR where TR.fk_utente = U.id_utente ")
            # get all records
            records = cursore.fetchall()
            # salva tutti gli elementi del record in una lista 
            for elem in records:
                id_utente.append(elem[0])
                nome.append(elem[1])
                cognome.append(elem[2])
                score.append(elem[3])
            zipped = zip(nome, cognome, score)
            dict_classifica = dict(zip(id_utente, zipped))
        except mysql.connector.Error as e:
                    print("Error reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()
                cursore.close()
        return dict_classifica

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
        except mysql.connector.Error as e:
                    print("Error reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()
                cursore.close()
    

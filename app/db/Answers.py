import mysql.connector
from .DBConnection import DBUtility
from .Questions import Questions
# in questo file creo la classe Answers dove inserisco tutti i metodi che andrò ad utilizzare nell'API
class Answers:
    # metodo che restituisce tutte le risposte di ogni domanda
    @staticmethod
    def getAllAnswers():
        connessione = DBUtility.getConnection()
        id_risposta = list()
        risposta = list()
        esito = list()
        id_domandaR = list()
        try:
            # Generazione del cursore
            cursore = connessione.cursor()
            # Comando SQL per la visualizzazione dei database in formato SQL
            cursore.execute("select R.id_risposta, R.risposta, R.esito, R.id_domanda from risposte R, domanda D where R.id_domanda = D.id_domanda")
            # get all records
            risposte = cursore.fetchall()
            # salva tutti gli elementi del record in una lista 
            for elem in risposte:
                id_risposta.append(elem[0])
                risposta.append(elem[1])
                esito.append(elem[2])
                id_domandaR.append(elem[3])
            zipped = zip(risposta, esito, id_domandaR)
            dict_risposta = dict(zip(id_risposta, zipped))
        except mysql.connector.Error as e:
                    print("Error reading data from MySQL table", e)
        finally:
            if connessione.is_connected():
                connessione.close()
                cursore.close()
        
        return dict_risposta
    
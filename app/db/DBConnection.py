import mysql.connector
import json

class DBUtility:
    @staticmethod
    def __connectToDB__():
        # specifiche di backup del DB in caso il try fallisca
        data = {
            "endpoint" : "localhost",
            "user" : "root",
            "password" : "Vale2002",
            "database" : "task2406"
        }
        try:  
            with open('DBConfig.json') as f:
                data = json.load(f)
                return data
        except:
            return data
    
    @staticmethod
    def getConnection(data = __connectToDB__()):
        connessione = None
        try:
            # Connessione a MySQL
            connessione = mysql.connector.connect(
            # Parametri per la connessione
            host=data["endpoint"],
            user=data["user"],
            password=data["password"],
            database=data["database"])
            print(connessione)
        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            return connessione

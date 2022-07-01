import json
import requests
import random
from ..db.Answers import Answers
from ..db.Questions import Questions
from ..db.Users import User
from ..db.RisultatiTest import RisultatiTest
# API che ritorna tutte le domande presenti nel DB, il risultato è formato da una lista
# contenente tutte le domande
def getAllQuestions():
    return Questions.getAllQuestions()

def getQuestion(index: int):
    AllQuestions = Questions.getAllQuestions()
    return AllQuestions.get(index)

def getRandomQuestion():
    AllQuestions = Questions.getAllQuestions()
    indexQ = random.randint(1,12)
    return AllQuestions.get(indexQ)

def getAnswer(id_question: int):
    allAnswers = Answers.getAllAnswers()
    fourAnswers = []
    if id_question != 1:
        for index in range(4*id_question - 3 , 4*id_question + 1):
            fourAnswers.append(allAnswers.get(index))
    return fourAnswers
    
def getAllUser():
    return User.getAllUsers()

def getClassificaFinale():
    return RisultatiTest.getClassificaFinale()

def add_values_in_classifica(id_utente, score, data):
    return RisultatiTest.addValuesInClassifica(id_utente, score, data)
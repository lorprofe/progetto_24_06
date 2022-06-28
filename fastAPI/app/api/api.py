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
    
    for elem in AllQuestions:
        if elem == AllQuestions[index - 1]:
            return elem

def getRandomQuestion():
    allQuestions = Questions.getAllQuestions()
    indexQ = random.randint(0,11)

    for question in allQuestions:
        if question == allQuestions[indexQ]:
            return question

def getAnswer(id_question: int):
    allAnswer = Answers.getAllAnswers()
    fourAnswer = []
    for answer in allAnswer:
        if answer[2] == id_question:
            fourAnswer.append(answer)

    return fourAnswer
    
def getAllUser():
    return User.getAllUsers()

def getClassificaFinale():
    return RisultatiTest.getClassificaFinale()

def add_values_in_classifica(id_utente, score, data):
    return RisultatiTest.addValuesInClassifica(id_utente, score, data)
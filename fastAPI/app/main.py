from fastapi import FastAPI, HTTPException
from app.api import api
from app.db.models import dataForResult
app = FastAPI()

@app.get("/questions")
def read_all_questions():
    return api.getAllQuestions()

@app.get("/questions/{id_question}", status_code=200)
def get_question(id_question: int):
    question = api.getQuestion(id_question)

    if not question:
        raise HTTPException(status_code=400, detail="Error, out of index")

    return question

@app.get("/random_question")
def get_random_question():
    question = api.getRandomQuestion()
    return question

@app.get("/answers/{id_question}")
def get_answer(id_question: int):
    return api.getAnswer(id_question)

@app.get("/user")
def get_all_Users():
    return api.getAllUser()

@app.get("/result")
def get_classifica_finale():
    return api.getClassificaFinale()

@app.post("/result/push", status_code=201)
async def add_risultati_test(dati: dataForResult):
    
    return api.add_values_in_classifica(dati.fk_utente, dati.score, dati.data_test)


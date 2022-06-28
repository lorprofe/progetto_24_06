from datetime import date
from pydantic import BaseModel

class dataForResult(BaseModel):
    fk_utente: int
    score: int
    data_test: date


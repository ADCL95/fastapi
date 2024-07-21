from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()
counter = 0  # Contador global para contar las llamadas a los endpoints

class DateRequest(BaseModel):
    return_full_datetime: bool  # Parámetro booleano en la solicitud

@app.post("/date")
async def get_date(request: DateRequest):
    global counter
    counter += 1  # Incrementa el contador cada vez que se llama este endpoint
    current_datetime = datetime.now()
    if request.return_full_datetime:
        # Devuelve la fecha y hora completas
        return {"date": current_datetime.strftime("%Y-%m-%d %H:%M:%S")}
    else:
        # Devuelve solo la fecha en formato aaaa-dd-mm
        return {"date": current_datetime.strftime("%Y-%d-%m")}

@app.get("/count")
async def get_count():
    global counter
    return {"count": counter}  # Devuelve el valor del contador


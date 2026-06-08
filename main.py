from fastapi import FastAPI, HTTPException, status
from typing import List, Optional

# Импортируем наши модули (пока будут пустыми, но мы их заполним)
import models
import crud # Будет использоваться позже
import uvicorn

app = FastAPI(title="CryptoLedger API")

#  Главный маршрут
@app.get("/", summary="Приветствие API", response_description="Сообщение с приветствием")
def read_root():
    return {"message": "Добро пожаловать в CryptoLedger API!"}

@app.post("/transactions/", summary = "Создание транзакции", response_description="Детали созданной транзакции")
def create_transactions(transaction:models.TransactionCreate):
    ans = crud.create_transaction(transaction)
    ans.update({"message":"Транзакция успешно создана!"})
    return ans

@app.get("/transactions/", summary = "Создание транзакции", response_description="Детали созданной транзакции")
def get_transactions():
    return crud.get_transactions()

@app.post("/blocks/",summary = "Создание транзакции", response_description="Детали созданной транзакции")
def creat_block(block:models.BlockCreate):
    ans = crud.create_block(block)
    ans.update({"message":"блок успешно создан!"})
    return ans


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)
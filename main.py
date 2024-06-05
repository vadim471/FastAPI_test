from typing import Union
import requests
from sqlalchemy.orm import Session
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from . import schemas, crud, models
from .database import SessionLocal, engine
import uvicorn

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_session():  
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.post("/products")
def add_product(product:schemas.ProductCreate, session: Session = Depends(get_session)):
    return crud.add_product(session, product.nm_id)

@app.get("/products/{id}")
def get_product(id:int):
    return crud.get_product(get_session(), id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
from fastapi import  Depends,APIRouter, HTTPException
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.transacciones
import crud.transacciones, config.db, schemas.transacciones, models.transacciones
from typing import List
from portadortoken import Portador


key=Fernet.generate_key()
f = Fernet(key)

transacciones = APIRouter()

models.transacciones.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@transacciones.get("/transacciones/", response_model=List[schemas.transacciones.Transaccion], tags=["Transacciones"],dependencies=[Depends(Portador())] )
def read_transacciones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users= crud.transacciones.get_transacciones(db=db, skip=skip, limit=limit)
    return db_users

@transacciones.post("/transaccion/{id}", response_model=schemas.transacciones.Transaccion, tags=["Transacciones"],dependencies=[Depends(Portador())])
def read_transaccion(id: int, db: Session = Depends(get_db)):
    db_user= crud.transacciones.get_transaccion(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Transaccion not found")
    return db_user

@transacciones.post("/transaccion/", response_model=schemas.transacciones.Transaccion, tags=["Transacciones"],dependencies=[Depends(Portador())])
def create_transaccion(transaccion: schemas.transacciones.TransaccionCreate, db: Session = Depends(get_db)):
    return crud.transacciones.create_transacciones(db=db, nom=transaccion)

@transacciones.put("/transaccion/{id}", response_model=schemas.transacciones.Transaccion, tags=["Transacciones"],dependencies=[Depends(Portador())])
def update_transaccion(id: int, persona: schemas.transacciones.TransaccionUpdate, db: Session = Depends(get_db)):
    db_user = crud.transacciones.update_transacciones(db=db, id=id, person=persona)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Transaccion no existe, no actualizado")
    return db_user

@transacciones.delete("/transaccion/{id}", response_model=schemas.transacciones.Transaccion, tags=["Transacciones"],dependencies=[Depends(Portador())])
def delete_transaccion(id: int, db: Session = Depends(get_db)):
    db_user = crud.transacciones.delete_transacciones(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Transaccion no existe, no se pudo eliminar")
    return db_user
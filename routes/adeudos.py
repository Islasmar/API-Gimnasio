from fastapi import APIRouter,HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import json
import crud.adeudos, config.db, schemas.adeudos, models.adeudos
from typing import List
from jwt_config import solicita_token 
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

adeudo = APIRouter()
models.adeudos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Ruta de bienvenida
@adeudo.get('/')
def bienvenido():
    return 'Bienvenido al sistema de APIs'

# Ruta para obtener todos los usuarios
@adeudo.get('/adeudo/', response_model=List[schemas.adeudos.Adeudo],tags=['Adeudo'], dependencies=[Depends(Portador())])
def read_adeudo(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_adeudo = crud.adeudos.get_adeudos(db=db,skip=skip, limit=limit)
    return db_adeudo

# Ruta para obtener un usuario por ID
@adeudo.post("/adeudo/{id}", response_model=schemas.adeudos.Adeudo, tags=["Adeudo"], dependencies=[Depends(Portador())])
def read_adeudo(id: int, db: Session = Depends(get_db)):
    db_adeudo= crud.adeudos.get_adeudo(db=db, id=id)
    if db_adeudo is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_adeudo

# Ruta para crear un usurio
@adeudo.post('/adeudo/', response_model=schemas.adeudos.Adeudo,tags=['Adeudo'], dependencies=[Depends(Portador())])
def create_adeudo(adeudo: schemas.adeudos.AdeudoCreate, db: Session=Depends(get_db)):
    db_adeudo = crud.adeudos.get_adeudo_by_nombre(db,adeudo=adeudo.Area)
    if db_adeudo:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.adeudos.create_adeudo(db=db, adeudo=adeudo)

# Ruta para actualizar un usuario
@adeudo.put('/adeudo/{id}', response_model=schemas.adeudos.Adeudo,tags=['Adeudo'], dependencies=[Depends(Portador())])
def update_adeudo(id:int,adeudo: schemas.adeudos.AdeudoUpdate, db: Session=Depends(get_db)):
    db_adeudo = crud.adeudos.update_adeudo(db=db, id=id, adeudo=adeudo)
    if db_adeudo is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo actualizar ")
    return db_adeudo

# Ruta para eliminar un usuario
@adeudo.delete('/adeudo/{id}', response_model=schemas.adeudos.Adeudo,tags=['Adeudo'], dependencies=[Depends(Portador())])
def delete_adeudo(id:int, db: Session=Depends(get_db)):
    db_adeudo = crud.adeudos.delete_adeudo(db=db, id=id)
    if db_adeudo is None:
        raise HTTPException(status_code=404, detail="Sucursal no existe, no se pudo eliminar ")
    return db_adeudo

from fastapi import APIRouter,HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import json
import crud.sucursales, config.db, schemas.sucursales, models.sucursales
from typing import List
from jwt_config import solicita_token 
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

sucursales = APIRouter()
models.sucursales.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Ruta de bienvenida
@sucursales.get('/')
def bienvenido():
    return 'Bienvenido al sistema de APIs'

# Ruta para obtener todos los usuarios
@sucursales.get('/sucursales/', response_model=List[schemas.sucursales.Sucursal],tags=['Sucursal'], dependencies=[Depends(Portador())])
def read_sucursales(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_sucursales = crud.sucursales.get_sucursales(db=db,skip=skip, limit=limit)
    return db_sucursales

# Ruta para obtener un usuario por ID
@sucursales.post("/sucursales/{id}", response_model=schemas.sucursales.Sucursal, tags=["Sucursal"], dependencies=[Depends(Portador())])
def read_sucursal(id: int, db: Session = Depends(get_db)):
    db_sucursales= crud.sucursales.get_sucursal(db=db, id=id)
    if db_sucursales is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_sucursales

# Ruta para crear un usurio
@sucursales.post('/sucursales/', response_model=schemas.sucursales.Sucursal,tags=['Sucursal'], dependencies=[Depends(Portador())])
def create_sucursal(sucursal: schemas.sucursales.SucursalCreate, db: Session=Depends(get_db)):
    db_sucursales = crud.sucursales.get_sucursal_by_sucursal(db,sucursal=sucursal.Nombre)
    if db_sucursales:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.sucursales.create_sucursal(db=db, sucursal=sucursal)

# Ruta para actualizar un usuario
@sucursales.put('/sucursales/{id}', response_model=schemas.sucursales.Sucursal,tags=['Sucursal'], dependencies=[Depends(Portador())])
def update_sucursal(id:int,sucursal: schemas.sucursales.SucursalUpdate, db: Session=Depends(get_db)):
    db_sucursal = crud.sucursales.update_sucursal(db=db, id=id, sucursal=sucursal)
    if db_sucursal is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo actualizar ")
    return db_sucursal

# Ruta para eliminar un usuario
@sucursales.delete('/sucursal/{id}', response_model=schemas.sucursales.Sucursal,tags=['Sucursal'], dependencies=[Depends(Portador())])
def delete_sucursal(id:int, db: Session=Depends(get_db)):
    db_sucursal = crud.sucursales.delete_sucursal(db=db, id=id)
    if db_sucursal is None:
        raise HTTPException(status_code=404, detail="Sucursal no existe, no se pudo eliminar ")
    return db_sucursal

from fastapi import APIRouter,HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import json
import crud.mantenimiento, config.db, schemas.mantenimiento, models.mantenimiento
from typing import List
from jwt_config import solicita_token 
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

mantenimiento = APIRouter()
models.mantenimiento.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Ruta de bienvenida
@mantenimiento.get('/')
def bienvenido():
    return 'Bienvenido al sistema de APIs'

# Ruta para obtener todos los usuarios
@mantenimiento.get('/mantenimiento/', response_model=List[schemas.mantenimiento.Mantenimiento],tags=['Mantenimiento'], dependencies=[Depends(Portador())])
def read_equipamiento(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_mantenimiento = crud.mantenimiento.get_mantenimientos(db=db,skip=skip, limit=limit)
    return db_mantenimiento

# Ruta para obtener un usuario por ID
@mantenimiento.post("/mantenimiento/{id}", response_model=schemas.mantenimiento.Mantenimiento, tags=["Mantenimiento"], dependencies=[Depends(Portador())])
def read_equipamiento(id: int, db: Session = Depends(get_db)):
    db_mantenimiento= crud.mantenimiento.get_mantenimiento(db=db, id=id)
    if db_mantenimiento is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_mantenimiento

# Ruta para crear un usurio
@mantenimiento.post('/mantenimiento/', response_model=schemas.mantenimiento.Mantenimiento,tags=['Mantenimiento'], dependencies=[Depends(Portador())])
def create_equipamiento(mantenimiento: schemas.mantenimiento.MantenimientoCreate, db: Session=Depends(get_db)):
    db_mantenimiento = crud.mantenimiento.get_mantenimiento_by_mantenimiento(db,mantenimiento=mantenimiento.Equipo)
    if db_mantenimiento:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.mantenimiento.create_mantenimiento(db=db, mantenimiento=mantenimiento)

# Ruta para actualizar un usuario
@mantenimiento.put('/mantenimiento/{id}', response_model=schemas.mantenimiento.Mantenimiento,tags=['Mantenimiento'], dependencies=[Depends(Portador())])
def update_equipamiento(id:int,mantenimiento: schemas.mantenimiento.MantenimientoUpdate, db: Session=Depends(get_db)):
    db_mantenimiento = crud.mantenimiento.update_mantenimiento(db=db, id=id, mantenimiento=mantenimiento)
    if db_mantenimiento is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo actualizar ")
    return db_mantenimiento

# Ruta para eliminar un usuario
@mantenimiento.delete('/mantenimiento/{id}', response_model=schemas.mantenimiento.Mantenimiento,tags=['Mantenimiento'], dependencies=[Depends(Portador())])
def delete_equipamiento(id:int, db: Session=Depends(get_db)):
    db_mantenimiento = crud.mantenimiento.delete_mantenimiento(db=db, id=id)
    if db_mantenimiento is None:
        raise HTTPException(status_code=404, detail="Sucursal no existe, no se pudo eliminar ")
    return db_mantenimiento

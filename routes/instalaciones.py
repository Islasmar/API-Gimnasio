from fastapi import APIRouter,HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import json
import crud.instalacion, config.db, schemas.instalaciones, models.instalaciones
from typing import List
from jwt_config import solicita_token 
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

instalacion = APIRouter()
models.instalaciones.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Ruta de bienvenida
@instalacion.get('/')
def bienvenido():
    return 'Bienvenido al sistema de APIs'

# Ruta para obtener todos los usuarios
@instalacion.get('/instalacion/', response_model=List[schemas.instalaciones.Instalacion],tags=['Instalacion'], dependencies=[Depends(Portador())])
def read_equipamiento(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_instalacion = crud.instalacion.get_instalaciones(db=db,skip=skip, limit=limit)
    return db_instalacion

# Ruta para obtener un usuario por ID
@instalacion.post("/instalacion/{id}", response_model=schemas.instalaciones.Instalacion, tags=["Instalacion"], dependencies=[Depends(Portador())])
def read_equipamiento(id: int, db: Session = Depends(get_db)):
    db_instalacion= crud.instalacion.get_instalacion(db=db, id=id)
    if db_instalacion is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_instalacion

# Ruta para crear un usurio
@instalacion.post('/instalacion/', response_model=schemas.instalaciones.Instalacion,tags=['Instalacion'], dependencies=[Depends(Portador())])
def create_equipamiento(instalacion: schemas.instalaciones.InstalacionesCreate, db: Session=Depends(get_db)):
    db_instalacion = crud.instalacion.get_instalacion_by_instalacion(db,instalacion=instalacion.Sucursal_Id)
    if db_instalacion:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.instalacion.create_instalacion(db=db, instalacion=instalacion)

# Ruta para actualizar un usuario
@instalacion.put('/instalacion/{id}', response_model=schemas.instalaciones.Instalacion,tags=['Instalacion'], dependencies=[Depends(Portador())])
def update_equipamiento(id:int,instalacion: schemas.instalaciones.InstalacionUpdate, db: Session=Depends(get_db)):
    db_instalacion = crud.instalacion.update_instalacion(db=db, id=id, instalacion=instalacion)
    if db_instalacion is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo actualizar ")
    return db_instalacion

# Ruta para eliminar un usuario
@instalacion.delete('/instalacion/{id}', response_model=schemas.instalaciones.Instalacion,tags=['Instalacion'], dependencies=[Depends(Portador())])
def delete_equipamiento(id:int, db: Session=Depends(get_db)):
    db_instalacion = crud.instalacion.delete_instalacion(db=db, id=id)
    if db_instalacion is None:
        raise HTTPException(status_code=404, detail="Sucursal no existe, no se pudo eliminar ")
    return db_instalacion

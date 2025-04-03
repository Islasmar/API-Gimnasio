from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import crud.instalaciones, config.db, schemas.instalaciones, models.instalaciones
from typing import List
from portadortoken import Portador

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
    return JSONResponse(content={"message": "Bienvenido al sistema de APIs"})

<<<<<<< HEAD
# Obtener todas las instalaciones
@instalacion.get('/instalacion/', response_model=List[schemas.instalaciones.InstalacionResponse], tags=['Instalación'], dependencies=[Depends(Portador())])
def read_instalaciones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.instalaciones.get_instalaciones(db=db, skip=skip, limit=limit)

# Obtener una instalación por ID
@instalacion.get("/instalacion/{id}", response_model=schemas.instalaciones.InstalacionResponse, tags=["Instalación"], dependencies=[Depends(Portador())])
def read_instalacion(id: int, db: Session = Depends(get_db)):
    instalacion = crud.instalaciones.get_instalacion(db=db, instalacion_id=id)
    if not instalacion:
        raise HTTPException(status_code=404, detail="Instalación no encontrada")
    return instalacion

# Crear una instalación
@instalacion.post('/instalacion/', response_model=schemas.instalaciones.InstalacionResponse, tags=['Instalación'], dependencies=[Depends(Portador())])
def create_instalacion(instalacion: schemas.instalaciones.InstalacionCreate, db: Session = Depends(get_db)):
    return crud.instalaciones.create_instalacion(db=db, instalacion=instalacion)

# Actualizar una instalación
@instalacion.put('/instalacion/{id}', response_model=schemas.instalaciones.InstalacionResponse, tags=['Instalación'], dependencies=[Depends(Portador())])
def update_instalacion(id: int, instalacion: schemas.instalaciones.InstalacionUpdate, db: Session = Depends(get_db)):
    updated_instalacion = crud.instalaciones.update_instalacion(db=db, instalacion_id=id, instalacion=instalacion)
    if not updated_instalacion:
        raise HTTPException(status_code=404, detail="Instalación no encontrada, no se pudo actualizar")
    return updated_instalacion

# Eliminar una instalación
@instalacion.delete('/instalacion/{id}', response_model=schemas.instalaciones.InstalacionResponse, tags=['Instalación'], dependencies=[Depends(Portador())])
def delete_instalacion(id: int, db: Session = Depends(get_db)):
    deleted_instalacion = crud.instalaciones.delete_instalacion(db=db, instalacion_id=id)
    if not deleted_instalacion:
        raise HTTPException(status_code=404, detail="Instalación no encontrada, no se pudo eliminar")
    return deleted_instalacion
=======
# Ruta para obtener todos los instalaciones
@instalacion.get('/instalacion/', response_model=List[schemas.instalaciones.Instalacion],tags=['Instalacion'], dependencies=[Depends(Portador())])
def read_equipamiento(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_instalacion = crud.instalacion.get_instalaciones(db=db,skip=skip, limit=limit)
    return db_instalacion

# Ruta para obtener un instalación por ID
@instalacion.post("/instalacion/{id}", response_model=schemas.instalaciones.Instalacion, tags=["Instalacion"], dependencies=[Depends(Portador())])
def read_equipamiento(id: int, db: Session = Depends(get_db)):
    db_instalacion= crud.instalacion.get_instalacion(db=db, id=id)
    if db_instalacion is None:
        raise HTTPException(status_code=404, detail="Insatalación no encontrada")
    return db_instalacion

# Ruta para crear una instalación
@instalacion.post('/instalacion/', response_model=schemas.instalaciones.Instalacion,tags=['Instalacion'], dependencies=[Depends(Portador())])
def create_equipamiento(instalacion: schemas.instalaciones.InstalacionesCreate, db: Session=Depends(get_db)):
    db_instalacion = crud.instalacion.get_instalacion_by_instalacion(db,instalacion=instalacion.Sucursal_Id)
    if db_instalacion:
        raise HTTPException(status_code=400, detail="Instalación no existente intenta nuevamente")
    return crud.instalacion.create_instalacion(db=db, instalacion=instalacion)

# Ruta para actualizar una instalación
@instalacion.put('/instalacion/{id}', response_model=schemas.instalaciones.Instalacion,tags=['Instalacion'], dependencies=[Depends(Portador())])
def update_equipamiento(id:int,instalacion: schemas.instalaciones.InstalacionUpdate, db: Session=Depends(get_db)):
    db_instalacion = crud.instalacion.update_instalacion(db=db, id=id, instalacion=instalacion)
    if db_instalacion is None:
        raise HTTPException(status_code=404, detail="Instalación no existe, no se pudo actualizar ")
    return db_instalacion

# Ruta para eliminar una instalación
@instalacion.delete('/instalacion/{id}', response_model=schemas.instalaciones.Instalacion,tags=['Instalacion'], dependencies=[Depends(Portador())])
def delete_equipamiento(id:int, db: Session=Depends(get_db)):
    db_instalacion = crud.instalacion.delete_instalacion(db=db, id=id)
    if db_instalacion is None:
        raise HTTPException(status_code=404, detail="la instalación no existe, no se pudo eliminar ")
    return db_instalacion
>>>>>>> 9a61c8b (Modificando archivos para realizar el CRUD de equipamiento y mantenimiento)

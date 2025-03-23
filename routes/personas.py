from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.personas, config.db, schemas.personas, models.personas
from typing import List
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

person = APIRouter()
models.personas.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los Personas
@person.get('/personas/', response_model=List[schemas.personas.Persona],tags=['Personas'],dependencies=[Depends(Portador())])
def read_persons(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_persons = crud.personas.get_person(db=db,skip=skip, limit=limit)
    return db_persons

# Ruta para obtener un Persona por ID
@person.post("/person/{id}", response_model=schemas.personas.Persona, tags=["Personas"], dependencies=[Depends(Portador())])
def read_person(id: int, db: Session = Depends(get_db)):
    db_person= crud.personas.get_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona not found")
    return db_person

# Ruta para crear un usurio
@person.post('/personas/', response_model=schemas.personas.Persona,tags=['Personas'])
def create_person(person: schemas.personas.PersonCreate, db: Session=Depends(get_db)):
    db_persons = crud.personas.get_person_by_nombre(db,nombre=person.Nombre)
    if db_persons:
        raise HTTPException(status_code=400, detail="Persona existente intenta nuevamente")
    return crud.personas.create_person(db=db, person=person)

# Ruta para actualizar un Persona
@person.put('/personas/{id}', response_model=schemas.personas.Persona,tags=['Personas'], dependencies=[Depends(Portador())])
def update_person(id:int,person: schemas.personas.PersonUpdate, db: Session=Depends(get_db)):
    db_persons = crud.personas.update_person(db=db, id=id, person=person)
    if db_persons is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo actualizar ")
    return db_persons

# Ruta para eliminar un Persona
@person.delete('/personas/{id}', response_model=schemas.personas.Persona,tags=['Personas'], dependencies=[Depends(Portador())])
def delete_person(id:int, db: Session=Depends(get_db)):
    db_persons = crud.personas.delete_person(db=db, id=id)
    if db_persons is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar ")
    return db_persons
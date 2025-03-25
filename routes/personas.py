from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.personas, config.db, schemas.personas, models.personas
from typing import List
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

persona = APIRouter()
models.personas.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los Personas
@persona.get('/personas/', response_model=List[schemas.personas.Persona],tags=['Personas'],dependencies=[Depends(Portador())])
def read_personas(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_personas = crud.personas.get_personas(db=db,skip=skip, limit=limit)
    return db_personas

# Ruta para obtener un Persona por ID
@persona.post("/persona/{id}", response_model=schemas.personas.Persona, tags=["Personas"], dependencies=[Depends(Portador())])
def read_persona(id: int, db: Session = Depends(get_db)):
    db_persona= crud.personas.get_personas(db=db, id=id)
    if db_persona is None:
        raise HTTPException(status_code=404, detail="Persona not found")
    return db_persona

# Ruta para crear una persona
@persona.post('/personas/', response_model=schemas.personas.PersonaCreate, tags=['Personas'])
def create_persona(persona: schemas.personas.PersonaCreate, db: Session = Depends(get_db)):
    print(f"📌 Datos recibidos: {persona}")  # 👈 Verifica qué valores llegan
    db_personas = crud.personas.get_persona_by_nombre(db, nombre=persona.Nombre)
    if db_personas:
        raise HTTPException(status_code=400, detail="Persona existente intenta nuevamente")

    return crud.personas.create_persona(db=db, persona=persona)


# Ruta para actualizar un Persona
@persona.put('/personas/{id}', response_model=schemas.personas.Persona,tags=['Personas'], dependencies=[Depends(Portador())])
def update_persona(id:int,persona: schemas.personas.PersonaUpdate, db: Session=Depends(get_db)):
    db_personas = crud.personas.update_persona(db=db, id=id, persona=persona)
    if db_personas is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo actualizar ")
    return db_personas

# Ruta para eliminar un Persona
@persona.delete('/personas/{id}', response_model=schemas.personas.Persona,tags=['Personas'], dependencies=[Depends(Portador())])
def delete_persona(id:int, db: Session=Depends(get_db)):
    db_personas = crud.personas.delete_persona(db=db, id=id)
    if db_personas is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar ")
    return db_personas
import models.personas
import schemas.personas
from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException


# Busqueda por id
def get_persona(db:Session, id: int):
    return db.query(models.personas.Persona).filter(models.personas.Persona.ID == id).first()

# Busqueda por Nombre
def get_persona_by_nombre(db:Session, nombre: str):
    return db.query(models.personas.Persona).filter(models.personas.Persona.Nombre == nombre).first()

# Buscar todos las personas
def get_personas(db:Session, skip: int=0, limit:int=10):
    return db.query(models.personas.Persona).offset(skip).limit(limit).all()

# Crear una nueva personas
def create_persona(db:Session, persona: schemas.personas.PersonaCreate):
    db_persona = models.personas.Persona(Titulo_Cortesia=persona.Titulo_Cortesia,
                                      Nombre=persona.Nombre, 
                                      Primer_Apellido=persona.Primer_Apellido, 
                                      Segundo_Apellido=persona.Segundo_Apellido, 
                                      Fecha_Nacimiento=persona.Fecha_Nacimiento, 
                                      Fotografia=persona.Fotografia, 
                                      Genero=persona.Genero,
                                      Tipo_Sangre=persona.Tipo_Sangre, 
                                      Estatus=persona.Estatus,
                                      Fecha_Registro=persona.Fecha_Registro,
                                      Fecha_Actualizacion=persona.Fecha_Actualizacion)
    try:
        db.add(db_persona)
        db.commit()
        db.refresh(db_persona)
        return db_persona
    except Exception as e:
        db.rollback()
        print(f"Error al insertar persona: {str(e)}")  # 👈 Verifica la consola
        raise HTTPException(status_code=500, detail=f"Error al insertar persona: {str(e)}")


# Actualizar una personas por id
def update_persona(db:Session, id:int, persona:schemas.personas.PersonaUpdate):
    db_persona = db.query(models.personas.Persona).filter(models.personas.Persona.ID == id).first()
    if db_persona:
        for var, value in vars(persona).items():
            setattr(db_persona, var, value) if value else None
        db.commit()
        db.refresh(db_persona)
    return db_persona

# Eliminar una personas por id
def delete_persona(db:Session, id:int):
    db_persona = db.query(models.personas.Persona).filter(models.personas.Persona.ID == id).first()
    if db_persona:
        db.delete(db_persona)
        db.commit()
    return db_persona
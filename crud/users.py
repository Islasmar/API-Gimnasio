from fastapi import HTTPException
import models.users
import schemas.users
from sqlalchemy.orm import Session
import models, schemas
import models.personas
import schemas.personas

# Busqueda por id
def get_user(db:Session, id: int):
    return db.query(models.users.User).filter(models.users.User.ID == id).first()

# Busqueda por USUARIO
def get_user_by_usuario(db:Session, usuario: str):
    return db.query(models.users.User).filter(models.users.User.Nombre_Usuario == usuario).first()

def get_user_by_creentials(db:Session, username: str, correo:str, telefono:str, password:str):
    return db.query(models.users.User).filter((models.users.User.Nombre_Usuario == username) |
                                               (models.users.User.Correo_Electronico == correo) |
                                               (models.users.User.Numero_Telefonico_Movil == telefono),
                                                 models.users.User.Contrasena == password).first()

# Buscar todos los usuarios
def get_users(db:Session, skip: int=0, limit:int=10):
    return db.query(models.users.User).offset(skip).limit(limit).all()

# Crear nuevo usuario
def create_user(db: Session, user_data: schemas.users.UserCreate, persona_data: schemas.personas.PersonaCreate):
    try:
        # Crear la persona
        db_persona = models.personas.Persona(
            Titulo_Cortesia=persona_data.Titulo_Cortesia,
            Nombre=persona_data.Nombre,
            Primer_Apellido=persona_data.Primer_Apellido,
            Segundo_Apellido=persona_data.Segundo_Apellido,
            Fecha_Nacimiento=persona_data.Fecha_Nacimiento,
            Fotografia=persona_data.Fotografia,
            Genero=persona_data.Genero,
            Tipo_Sangre=persona_data.Tipo_Sangre,
            Estatus=persona_data.Estatus,
            Fecha_Registro=persona_data.Fecha_Registro,
            Fecha_Actualizacion=persona_data.Fecha_Actualizacion
        )
        db.add(db_persona)
        db.commit()
        db.refresh(db_persona)

        # Crear el usuario con el ID de la persona creada
        db_user = models.users.User(
            ID_Persona=db_persona.ID,
            Nombre_Usuario=user_data.Nombre_Usuario,
            Correo_Electronico=user_data.Correo_Electronico,
            Contrasena=user_data.Contrasena,
            Numero_Telefonico_Movil=user_data.Numero_Telefonico_Movil,
            Estatus=user_data.Estatus,
            Fecha_Registro=user_data.Fecha_Registro,
            Fecha_Actualizacion=user_data.Fecha_Actualizacion
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear usuario con persona: {str(e)}")



# Actualizar un usuario por id
def update_user(db:Session, id:int, user:schemas.users.UserUpdate):
    db_user = db.query(models.users.User).filter(models.users.User.ID == id).first()
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

# Eliminar un usuario por id
def delete_user(db: Session, id: int):
    user = db.query(models.users.User).filter(models.users.User.ID == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    persona = db.query(models.personas.Persona).filter(models.personas.Persona.ID == user.ID_Persona).first()

    db.delete(user)
    if persona:
        db.delete(persona)  # Eliminar la persona si existe
    db.commit()

    return {"message": "Usuario y persona eliminados correctamente"}

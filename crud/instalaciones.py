import models.instalaciones
import schemas.instalaciones
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por id
def get_instalacion(db:Session, id: int):
    return db.query(models.instalaciones.Instalacion).filter(models.instalaciones.Instalacion.Id == id).first()

# Busqueda por USUARIO
def get_instalacion_by_instalacion(db:Session, instalacion : str):
    return db.query(models.instalaciones.Instalacion).filter(models.instalaciones.Instalacion.Id == instalacion).first()

# Buscar todos los usuarios
def get_instalaciones(db:Session, skip: int=0, limit:int=10):
    return db.query(models.instalaciones.Instalacion).offset(skip).limit(limit).all()

# Crear nuevo usuario
def create_instalacion(db:Session, instalacion: schemas.instalaciones.InstalacionesCreate):
    db_instalacion = models.instalaciones.Instalacion(
                                            Sucursal_Id=instalacion.Sucursal_Id,
                                             Descripcion=instalacion.Descripcion,
                                             Tipo=instalacion.Tipo,
                                             Calificacion=instalacion.Calificacion,
                                             Horario_Disponible=instalacion.Horario_Disponible,
                                             Servicio=instalacion.Servicio,
                                             Observaciones=instalacion.Observaciones,
                                             Estatus=instalacion.Estatus,
                                             Fecha_Registro=instalacion.Fecha_Registro,
                                             Fecha_Actualizacion=instalacion.Fecha_Actualizacion)
    
    
    db.add(db_instalacion)
    db.commit()
    db.refresh(db_instalacion)
    print(db_instalacion)
    return db_instalacion

# Actualizar un usuario por id
def update_instalacion(db:Session, id:int, instalacion:schemas.instalaciones.InstalacionUpdate):
    db_instalacion = db.query(models.instalaciones.Instalacion).filter(models.instalaciones.Instalacion.Id == id).first()
    if db_instalacion:
        for var, value in vars(instalacion).items():
            setattr(db_instalacion, var, value) if value else None
        db.commit()
        db.refresh(db_instalacion)
    return db_instalacion

# Eliminar un usuario por id
def delete_instalacion(db:Session, id:int):
    db_instalacion = db.query(models.instalaciones.Instalacion).filter(models.instalaciones.Instalacion.Id == id).first()
    if db_instalacion:
        db.delete(db_instalacion)
        db.commit()
    return db_instalacion
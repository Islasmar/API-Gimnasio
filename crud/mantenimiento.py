import models.mantenimiento
import schemas.mantenimiento
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por id
def get_mantenimiento(db:Session, id: int):
    return db.query(models.mantenimiento.Mantenimiento).filter(models.mantenimiento.Mantenimiento.Id == id).first()

# Busqueda por USUARIO
def get_mantenimiento_by_mantenimiento(db:Session, mantenimiento : str):
    return db.query(models.mantenimiento.Mantenimiento).filter(models.mantenimiento.Mantenimiento.Equipo == mantenimiento).first()

# Buscar todos los usuarios
def get_mantenimientos(db:Session, skip: int=0, limit:int=10):
    return db.query(models.mantenimiento.Mantenimiento).offset(skip).limit(limit).all()

# Crear nuevo usuario
def create_mantenimiento(db:Session, mantenimiento: schemas.mantenimiento.MantenimientoCreate):
    db_mantenimiento = models.mantenimiento.Mantenimiento(
                                            Equipo=mantenimiento.Equipo,
                                             Descripcion=mantenimiento.Descripcion,
                                             Responsable=mantenimiento.Responsable,
                                             Costo=mantenimiento.Costo,
                                             Estatus=mantenimiento.Estatus,
                                             Fecha_mantenimiento=mantenimiento.Fecha_mantenimiento,
                                             Fecha_Actualizacion=mantenimiento.Fecha_Actualizacion)
    
    db.add(db_mantenimiento)
    db.commit()
    db.refresh(db_mantenimiento)
    print(db_mantenimiento)
    return db_mantenimiento

# Actualizar un usuario por id
def update_mantenimiento(db:Session, id:int, mantenimiento:schemas.mantenimiento.Mantenimiento):
    db_mantenimiento = db.query(models.mantenimiento.Mantenimiento).filter(models.mantenimiento.Mantenimiento.Id == id).first()
    if db_mantenimiento:
        for var, value in vars(mantenimiento).items():
            setattr(db_mantenimiento, var, value) if value else None
        db.commit()
        db.refresh(db_mantenimiento)
    return db_mantenimiento

# Eliminar un usuario por id
def delete_mantenimiento(db:Session, id:int):
    db_mantenimiento = db.query(models.mantenimiento.Mantenimiento).filter(models.mantenimiento.Mantenimiento.Id == id).first()
    if db_mantenimiento:
        db.delete(db_mantenimiento)
        db.commit()
    return db_mantenimiento
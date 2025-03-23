import models.adeudos
import schemas.adeudos
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por id
def get_adeudo(db:Session, id: int):
    return db.query(models.adeudos.Adeudos).filter(models.adeudos.Adeudos.ID == id).first()

# Busqueda por USUARIO
def get_adeudo_by_nombre(db:Session, adeudo : str):
    return db.query(models.adeudos.Adeudos).filter(models.adeudos.Adeudos == adeudo).first()

# Buscar todos los usuarios
def get_adeudos(db:Session, skip: int=0, limit:int=10):
    return db.query(models.adeudos.Adeudos).offset(skip).limit(limit).all()

# Crear nuevo usuario
def create_adeudo(db:Session, adeudo: models.adeudos.Adeudos):
    db_adeudo = models.adeudos.Adeudos(
                                            Area=adeudo.Area,
                                            Cliente=adeudo.Cliente,
                                            Descripcion=adeudo.Descripcion,
                                            Tipo=adeudo.Tipo,
                                            Detalle=adeudo.Detalle,
                                            Estatus=adeudo.Estatus,
                                            Fecha_Registro=adeudo.Fecha_Registro,
                                            Fecha_Actualizacion=adeudo.Fecha_Actualizacion)
    
    
    db.add(db_adeudo)
    db.commit()
    db.refresh(db_adeudo)
    print(db_adeudo)
    return db_adeudo

# Actualizar un usuario por id
def update_adeudo(db:Session, id:int, adeudo :schemas.adeudos.AdeudoUpdate):
    db_adeudo = db.query(models.adeudos.Adeudos).filter(models.adeudos.Adeudos.ID == id).first()
    if db_adeudo:
        for var, value in vars(adeudo).items():
            setattr(db_adeudo, var, value) if value else None
        db.commit()
        db.refresh(db_adeudo)
    return db_adeudo

# Eliminar un usuario por id
def delete_adeudo(db:Session, id:int):
    db_adeudo = db.query(models.adeudos.Adeudos).filter(models.adeudos.Adeudos.ID == id).first()
    if db_adeudo:
        db.delete(db_adeudo)
        db.commit()
    return db_adeudo
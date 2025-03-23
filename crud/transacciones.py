
import models.miembros
import models.transacciones
import schemas.transacciones
from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import desc

def get_transaccion(db: Session, id: int):
    return db.query(models.transacciones.Transaccion).filter(models.transacciones.Transaccion.ID == id).first()

def get_transaccion_by_id(db: Session, metodo: str):
    return db.query(models.transacciones.Transaccion).filter(models.transacciones.Transaccion.Metodo_Pago == metodo).first()

def get_transacciones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.transacciones.Transaccion).order_by(desc(models.transacciones.Transaccion.ID)).offset(skip).limit(limit).all()

def create_transacciones(db: Session, nom: schemas.transacciones.TransaccionCreate):
    db_user =models.transacciones.Transaccion(
                                      Usuario_ID=nom.Usuario_ID, 
                                      Metodo_Pago=nom.Metodo_Pago,  
                                      Monto=nom.Monto, 
                                      Estatus=nom.Estatus, 
                                      Fecha_Registro=nom.Fecha_Registro, 
                                      Fecha_Actualizacion=nom.Fecha_Actualizacion )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_transacciones(db: Session, id: int, person: schemas.transacciones.TransaccionUpdate):
    db_user = db.query(models.transacciones.Transaccion).filter(models.transacciones.Transaccion.ID == id).first()
    if db_user:
        for var, value in vars(person).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_transacciones(db: Session, id: int):
    db_user = db.query(models.transacciones.Transaccion).filter(models.transacciones.Transaccion.ID == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
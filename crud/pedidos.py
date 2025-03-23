import models.pedidos
import schemas.pedidos
from sqlalchemy.orm import Session
import models, schemas

# Búsqueda por id
def get_pedido(db: Session, id: int):
    return db.query(models.pedidos.Pedido).filter(models.pedidos.Pedido.ID == id).first()

# Buscar todos los pedidos
def get_pedidos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.pedidos.Pedido).offset(skip).limit(limit).all()

# Crear un nuevo pedido
def create_pedido(db: Session, pedido: schemas.pedidos.PedidoCreate):
    db_pedido = models.pedidos.Pedido(
        Tipo=pedido.Tipo,
        Fecha_Registro=pedido.Fecha_Registro,
        Fecha_Actualizacion=pedido.Fecha_Actualizacion,
        Estatus=pedido.Estatus,
        Total_Productos=pedido.Total_Productos,
        Costo_Total=pedido.Costo_Total
    )
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

# Actualizar un pedido por id
def update_pedido(db: Session, id: int, pedido: schemas.pedidos.PedidoUpdate):
    db_pedido = db.query(models.pedidos.Pedido).filter(models.pedidos.Pedido.ID == id).first()
    if db_pedido:
        for var, value in vars(pedido).items():
            setattr(db_pedido, var, value) if value else None
        db.commit()
        db.refresh(db_pedido)
    return db_pedido

# Eliminar un pedido por id
def delete_pedido(db: Session, id: int):
    db_pedido = db.query(models.pedidos.Pedido).filter(models.pedidos.Pedido.ID == id).first()
    if db_pedido:
        db.delete(db_pedido)
        db.commit()
    return db_pedido
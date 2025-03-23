from sqlalchemy import Column, Boolean, Integer, DateTime, ForeignKey, Enum, Float, func
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyTipo(enum.Enum):
    Promocion = "Promoción"
    Descuento = "Descuento"
    Precio_Tienda = "Precio Tienda"

class Pedido(Base):
    __tablename__ = 'tbb_pedidos'
    ID = Column(Integer, primary_key=True, index=True)
    #Producto_id = Column(Integer, ForeignKey("tbb_productos.ID"), nullable=False)
    #Usuario_id = Column(Integer, ForeignKey("tbb_usuarios.ID"), nullable=False)
    Tipo = Column(Enum(MyTipo), nullable=False)
    Fecha_Registro = Column(DateTime, default=func.now(), nullable=False)
    Fecha_Actualizacion = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    Estatus = Column(Boolean, default=False)
    Total_Productos = Column(Float, nullable=False)
    Costo_Total = Column(Float, nullable=False)

    # Relaciones
    #producto = relationship("Producto", back_populates="pedidos")
    #usuario = relationship("Usuario", back_populates="pedidos")
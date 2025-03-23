from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum, Float, Integer, Date, BIGINT
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum


class MyMetodoPago(str, enum.Enum):
    TarjetaDebito =  "TarjetaDebito"
    TarjetaCredito = "TarjetaCredito"
    
 
class Transaccion(Base):
    __tablename__ = "tbb_transacciones"

    ID= Column(Integer, primary_key=True, index=True)
    # Usuario_ID = Column(Integer, ForeignKey("tbb_usuarios.ID"))
    Usuario_ID = Column(Integer)
    Metodo_Pago = Column( Enum(MyMetodoPago)) 
    Monto = Column(Float)
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    
    # usuario = relationship("User")
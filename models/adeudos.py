from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyDetalle(enum.Enum):
    Producto ="Producto"
    Equipamiento ="Equipamiento"
    Servicio = "Servicio"


class Adeudos(Base):
    __tablename__ = "tbd_aduedos"
    
    ID = Column(Integer, primary_key=True, index=True)
    Area = Column(String(255))
    Cliente = Column(String(255))
    Descripcion = Column(String(255))
    Tipo = Column(String(255))
    Detalle = Column(Enum(MyDetalle))  
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    
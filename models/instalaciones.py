from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Boolean, DECIMAL
from sqlalchemy.dialects.mysql import LONGTEXT
from config.db import Base
import enum
import models.sucursales

class MyCalificacion(enum.Enum):
    Exelente_servicio  = "Exelente servicio"
    Buen_servicio = "Buen servicio"
    Servicio_Regular = "Servicio Regular"
    Puedemejorar_el_servicio = "Puede mejorar el servicio"

class Instalacion(Base):
    __tablename__ = 'tbb_instalaciones'
    Id = Column(Integer, primary_key=True, index=True)
    Sucursal_Id = Column(Integer)
    Descripcion = Column(LONGTEXT)
    Tipo = Column(String(50))
    Calificacion = Column(Enum(MyCalificacion))
    Horario_Disponible = Column(LONGTEXT)
    Servicio = Column(String(100))
    Observaciones = Column(String(100))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    
    
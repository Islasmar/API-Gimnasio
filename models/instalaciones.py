from sqlalchemy import Column, Integer, String, DateTime, func, Enum, Boolean
from sqlalchemy.dialects.mysql import LONGTEXT
from config.db import Base
import enum
import models.sucursales

class MyCalificacion(enum.Enum):
    Exelente_servicio  = "Exelente servicio"
    Buen_servicio = "Buen servicio"
    Servicio_Regular = "Servicio Regular"
    Puedemejorar_el_servicio = "Puede mejorar el servicio"

class MyTipoInstalacion(enum.Enum):
    Gimnasio = "Gimnasio"
    Piscina = "Piscina"
    Sauna = "Sauna"
    Spa = "Spa"
    Otro = "Otro"


class Instalacion(Base):
    __tablename__ = 'tbb_instalaciones'
    Id = Column(Integer, primary_key=True, index=True)
    # Id_horario_disponible = Column(LONGTEXT)
    #Id_Sucursal = Column(Integer)
    Descripcion = Column(String(100), nullable=True)
    Tipo = Column(Enum(MyTipoInstalacion))
    Calificacion = Column(Enum(MyCalificacion))
    #Id_Servicio = Column(Integer)
    Observaciones = Column(String(100), nullable=True)
    Estatus = Column(Boolean, default=True, nullable=False)
    Fecha_Registro = Column(DateTime, default=func.now(), nullable=False)  # CURRENT_TIMESTAMP
    Fecha_Actualizacion = Column(DateTime, nullable=True) 
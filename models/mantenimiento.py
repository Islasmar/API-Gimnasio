from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Boolean, DECIMAL
from sqlalchemy.dialects.mysql import LONGTEXT
from config.db import Base
# import models.persons


class Mantenimiento(Base):
    __tablename__ = 'tbb_mantenimientos'
    Id = Column(Integer, primary_key=True, index=True)
    Equipo = Column(String(100))
    Descripcion = Column(LONGTEXT)
    Responsable = Column(String(80))
    Costo = Column(DECIMAL(10,2))
    Estatus = Column(Boolean, default=False)
    Fecha_mantenimiento = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    
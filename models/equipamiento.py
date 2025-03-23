from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.dialects.mysql import LONGTEXT
from config.db import Base
# import models.persons


class Equipamiento(Base):
    __tablename__ = 'tbb_equipamientos'
    Id = Column(Integer, primary_key=True, index=True)
    Area = Column(String(100))
    Nombre = Column(String(100))
    Marca = Column(String(100))
    Modelo = Column(String(180))
    Fotografia = Column(LONGTEXT)
    Estatus = Column(Boolean, default=False)
    Total_Existencias = Column(Integer, default=0)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    
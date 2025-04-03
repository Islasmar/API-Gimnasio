from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from config.db import Base
# import models.persons


class Equipamiento(Base):
    __tablename__ = 'tbb_equipamientos'
    Id = Column(Integer, primary_key=True, index=True)
    #Id_provedor = Column(Integer)
    Nombre = Column(String(100), nullable=False)
    Marca = Column(String(100), nullable=True)
    Modelo = Column(String(100), nullable=True)
    Fotografia = Column(Text, nullable=True)  # LONGTEXT se maneja como Text
    Estatus = Column(Boolean, default=True, nullable=False)  # b'1' es True en Python
    Total_Existencias = Column(Integer, default=0, nullable=True)
    Fecha_Registro = Column(DateTime, default=func.now(), nullable=False)  # CURRENT_TIMESTAMP
    Fecha_Actualizacion = Column(DateTime, nullable=True) 

    mantenimientos = relationship("Mantenimiento", back_populates="equipamiento")  # Relación inversa

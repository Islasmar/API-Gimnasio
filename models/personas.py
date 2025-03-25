from sqlalchemy import Column,Boolean, Integer, String, DateTime, ForeignKey, Enum,Date
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Persona(Base):
    __tablename__ = 'tbb_personas'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Titulo_Cortesia = Column(String(20))
    Nombre = Column(String(80))
    Primer_Apellido = Column(String(80))
    Segundo_Apellido = Column(String(80))
    Fecha_Nacimiento = Column(Date)
    Fotografia = Column(String(100))
    Genero = Column(String(3))
    Tipo_Sangre = Column(String(3))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

    usuarios = relationship("User", back_populates="persona", uselist=False)  # Relación con Usuario
    # Id_persona = Column(Integer)
    # intems = relationship("Item", back_populates="owner") Clave foranea
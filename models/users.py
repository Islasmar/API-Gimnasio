from sqlalchemy import Column,Boolean, Integer, String, DateTime, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
#import models.personas
import enum

class MyEstatus(str,enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"

class User(Base):
    __tablename__ = 'tbb_usuarios'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre_Usuario = Column(String(60),nullable=False)
    Correo_Electronico = Column(String(100),nullable=False, unique=True)
    Contrasena = Column(String(40),nullable=False)
    Numero_Telefonico_Movil = Column(String(20))
    Estatus = Column( Enum(MyEstatus), default=MyEstatus.Activo)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime,nullable=True)
    # intems = relationship("Item", back_populates="owner") Clave foranea
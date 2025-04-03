from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base
import enum
from datetime import datetime

class MyEstatus(str, enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"

class User(Base):
    __tablename__ = 'tbb_usuarios'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre_Usuario = Column(String(60), nullable=False)
    Correo_Electronico = Column(String(100), nullable=False, unique=True)
    Contrasena = Column(String(40), nullable=False)
    Numero_Telefonico_Movil = Column(String(20), nullable=True)
    Estatus = Column(Enum(MyEstatus, name="estatus_enum"), nullable=False)
    Fecha_Registro = Column(DateTime, default=datetime.utcnow)
    Fecha_Actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True)

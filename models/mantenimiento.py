from sqlalchemy import Column, Integer, String, DateTime, func, Boolean, DECIMAL, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from config.db import Base
# import models.persons


class Mantenimiento(Base):
    __tablename__ = 'tbb_mantenimientos'
    Id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Id_equipamiento = Column(Integer, ForeignKey("tbb_equipamientos.Id"), nullable=False)  # Relación con Equipamiento
    #Id_proveedor = Column(Integer, ForeignKey("tbb_proveedores.Id"), nullable=True)  # Relación con Proveedor
    Descripcion = Column(String(100), nullable=True)
    Costo = Column(DECIMAL(10,2), nullable=False)
    Estatus = Column(Boolean, default=False, nullable=False)
    Fecha_Registro = Column(DateTime, default=func.now(), nullable=False)  # CURRENT_TIMESTAMP
    Fecha_Actualizacion = Column(DateTime, nullable=True)
    
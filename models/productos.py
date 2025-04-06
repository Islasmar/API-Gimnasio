from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, DECIMAL
from config.db import Base
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class Producto(Base):
    __tablename__ = "tbb_productos"
    
    ID = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)  
    marca = Column(String(100), nullable=False)   
    cantidad = Column(Integer, default=0)
    cod_barras = Column(String(50), unique=True, nullable=False)  
    descripcion = Column(String(255))
    presentacion = Column(String(100))
    precio_actual = Column(DECIMAL(6, 2), nullable=False) 
    fotografia = Column(String(100))
    estatus = Column(Boolean, default=False)
    fecha_registro = Column(DateTime, default=func.now(), nullable=False)  
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)  


def convertir_decimal_para_mongo(data_model: BaseModel) -> dict:
    """
    Convierte los Decimals del modelo Pydantic en floats para compatibilidad con MongoDB.
    """
    data_dict = data_model.dict(by_alias=True)

    if "precio_actual" in data_dict and isinstance(data_dict["precio_actual"], Decimal):
        data_dict["precio_actual"] = float(data_dict["precio_actual"])

    return data_dict


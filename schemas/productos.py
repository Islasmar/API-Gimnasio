from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("ID de MongoDB no válido")
        return ObjectId(v)

class ProductoBase(BaseModel):
    nombre: Optional[str] = None
    marca: Optional[str] = None
    cod_barras: Optional[str] = None
    descripcion: Optional[str] = None
    presentacion: Optional[str] = None
    precio_actual: Optional[Decimal] = None
    fotografia: Optional[str] = None
    estatus: Optional[bool] = None
    fecha_registro: Optional[datetime] = None
    fecha_actualizacion: Optional[datetime] = None

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: Optional[str] = Field(alias="_id")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str,
            Decimal: float,
        }

class ProductoEliminado(BaseModel):
    msg: str
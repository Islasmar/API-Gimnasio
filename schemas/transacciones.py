from typing import List, Union
from pydantic import BaseModel
from datetime import datetime, date


class TransaccionesBase(BaseModel):
    Usuario_ID: int
    Metodo_Pago: str
    Monto: float
    Estatus: bool
    Fecha_Registro : datetime
    Fecha_Actualizacion: datetime


class TransaccionCreate(TransaccionesBase):
    pass

class TransaccionUpdate(TransaccionesBase):
    pass

class Transaccion(TransaccionesBase):
    ID: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True
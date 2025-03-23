from typing import List,Union
from pydantic import BaseModel
from datetime import datetime



class AdeudoBase(BaseModel):
    
    Area:str
    Cliente: str
    Descripcion: str
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime
    Estatus:bool
    Tipo: str
    Detalle: str
    
    
class AdeudoCreate(AdeudoBase):
    pass
class AdeudoUpdate(AdeudoBase):
    pass
class Adeudo(AdeudoBase):
    ID: int

    class Config:
        orm_mode = True
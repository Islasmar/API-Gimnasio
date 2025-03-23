from typing import List, Union, Optional
from pydantic  import BaseModel
from datetime import datetime

class InstalacionBase(BaseModel):
    Sucursal_Id : int
    Descripcion : str 
    Tipo : str 
    Calificacion : str
    Horario_Disponible: str
    Servicio : str
    Observaciones : str
    Estatus : bool
    Fecha_Registro :datetime
    Fecha_Actualizacion :datetime
    
    
     
     
class InstalacionesCreate(InstalacionBase):
    pass

class InstalacionUpdate(InstalacionBase):
    pass

class Instalacion(InstalacionBase):
    Id:int
    Sucursal_Id:int
    #Responsablee_Id:int
    
    class Config:
        orm_mode = True

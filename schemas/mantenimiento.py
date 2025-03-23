from typing import List, Union, Optional
from pydantic  import BaseModel
from datetime import datetime

class MantenimientoBase(BaseModel):
    Equipo : str
    Descripcion : str 
    Responsable : str 
    Costo : int
    Estatus : bool
    Fecha_mantenimiento :datetime
    Fecha_Actualizacion :datetime
     
     
     
class MantenimientoCreate(MantenimientoBase):
    pass

class MantenimientoUpdate(MantenimientoBase):
    pass

class Mantenimiento(MantenimientoBase):
    Id:int
    #Responsablee_Id:int
    
    class Config:
        orm_mode = True

from typing import List, Union, Optional
from pydantic  import BaseModel
from datetime import datetime

class SucursalBase(BaseModel):
    Nombre : str
    Direccion : str 
    Responsable_Id :int
    Total_Clientes_Atendidos : int
    Promedio_Clientes_X_Dia : int
    Capacidad_Maxima : int
    Total_Empleados : int
    Horario_Disponibilidad : str
    Estatus : bool
    Fecha_Registro :datetime
    Fecha_Actualizacion :datetime

class SucursalCreate(SucursalBase):
    pass

class SucursalUpdate(SucursalBase):
    pass

class Sucursal(SucursalBase):
    Id:int
    #Responsablee_Id:int
    
    class Config:
        orm_mode = True

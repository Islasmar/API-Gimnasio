from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime, date

class PersonaBase(BaseModel):
    Titulo_Cortesia:str
    Nombre:str
    Primer_Apellido:str
    Segundo_Apellido:str
    Fecha_Nacimiento:datetime
    Fotografia:str
    Genero:str
    Tipo_Sangre:str
    Estatus: bool
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime
    # Id_persona: int

class PersonaCreate(PersonaBase):
    pass

class PersonaUpdate(PersonaBase):
    pass

class Persona(PersonaBase):
    ID:int
    # owner_id: int clave foranea
    class Config:
        orm_mode = True
        
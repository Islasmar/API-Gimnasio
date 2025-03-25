from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# TABLAS SIN RELACIÓN 
from routes.personas import persona


# TABLAS CON RELACIÓN 
from routes.user import user

from routes.pedidos import pedidos
from routes.productos import producto
from routes.transacciones import  transacciones
from routes.sucursales import sucursales
from routes.equipamiento import equipamiento
from routes.adeudos import adeudo
from routes.servicios_clientes import servicio_cliente
from routes.mantenimiento import mantenimiento
from routes.instalaciones import instalacion
from routes.evaluaciones_serv import equipamiento

app = FastAPI()
# TABLAS SIN RELACIÓN 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TABLAS CON RELACIÓN 
app.include_router(user)
app.include_router(persona)
app.include_router(instalacion)
app.include_router(pedidos)
app.include_router(producto)
app.include_router(transacciones)
app.include_router(sucursales)
app.include_router(equipamiento)
app.include_router(adeudo)
app.include_router(servicio_cliente)
app.include_router(mantenimiento)
app.include_router(equipamiento)

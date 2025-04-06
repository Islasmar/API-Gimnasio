from fastapi import APIRouter, HTTPException, Depends
from typing import List
from portadortoken import Portador
import crud.productos, schemas.productos
from config.db import mongo_db
from models.productos import convertir_decimal_para_mongo  # Función auxiliar
from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

producto = APIRouter()

# Obtener todos los productos
@producto.get('/productos/', response_model=List[schemas.productos.Producto], tags=['productos'], dependencies=[Depends(Portador())])
async def read_productos(skip: int = 0, limit: int = 1000):
    db_productos = await crud.productos.get_productos(mongo_db, skip=skip, limit=limit)
    
    # Convertir ObjectId a str para cada producto
    productos = []
    for producto in db_productos:
        if "_id" in producto:
            producto["_id"] = str(producto["_id"])
        productos.append(producto)
    
    return productos

# Obtener un producto por ID
@producto.get("/producto/{id}", response_model=schemas.productos.Producto, tags=["productos"], dependencies=[Depends(Portador())])
async def read_producto(id: str):
    db_producto = await crud.productos.get_producto(mongo_db, id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    # Convertir ObjectId a str si está presente
    if "_id" in db_producto:
        db_producto["_id"] = str(db_producto["_id"])
    
    return db_producto

# Obtener un producto por código de barras
@producto.get("/producto/cod_barras/{cod_barras}", response_model=schemas.productos.Producto, tags=["productos"], dependencies=[Depends(Portador())])
async def read_producto_by_cod_barras(cod_barras: str):
    db_producto = await crud.productos.get_producto_by_cod_barras(mongo_db, cod_barras)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    # Convertir ObjectId a str si está presente
    if "_id" in db_producto:
        db_producto["_id"] = str(db_producto["_id"])
    
    return db_producto

# Crear un producto
@producto.post('/productos/', response_model=schemas.productos.Producto, tags=['productos'], dependencies=[Depends(Portador())])
async def create_producto(producto: schemas.productos.ProductoCreate):
    """Crear un nuevo producto."""
    
    # Asegúrate de que `producto` sea una instancia de `ProductoCreate`
    if isinstance(producto, dict):  # Si `producto` es un diccionario
        producto = schemas.productos.ProductoCreate(**producto)  # Convertir el diccionario a una instancia del modelo

    # Convertir a diccionario, excluyendo campos no necesarios
    producto_data = producto.dict(exclude_unset=True, exclude={"fecha_registro", "fecha_actualizacion"})

    # ✅ Convertir precio_actual de Decimal a float si existe
    if "precio_actual" in producto_data and isinstance(producto_data["precio_actual"], Decimal):
        producto_data["precio_actual"] = float(producto_data["precio_actual"])

    # Agregar fechas
    now = datetime.utcnow()
    producto_data["fecha_registro"] = now
    producto_data["fecha_actualizacion"] = now

    # Insertar en MongoDB
    result = await mongo_db["productosgym"].insert_one(producto_data)

    producto_data["_id"] = str(result.inserted_id)  # Convertir ObjectId a str para la respuesta
    return producto_data

# Actualizar producto
@producto.put('/productos/{id}', response_model=schemas.productos.Producto, tags=['productos'], dependencies=[Depends(Portador())])
async def update_producto(id: str, producto: schemas.productos.ProductoUpdate):
    # Convertir el modelo Pydantic a un diccionario
    producto_data = producto.dict(exclude_unset=True)

    # Convertir Decimal a float si existe
    if "precio_actual" in producto_data and isinstance(producto_data["precio_actual"], Decimal):
        producto_data["precio_actual"] = float(producto_data["precio_actual"])

    # Actualizar el producto en la base de datos
    db_producto = await crud.productos.update_producto(mongo_db, id=id, producto=producto_data)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no existe, no se pudo actualizar")
    return db_producto

# Eliminar producto
@producto.delete("/productos/{id}", response_model=schemas.productos.ProductoEliminado, tags=["productos"], dependencies=[Depends(Portador())])
async def delete_producto_endpoint(id: str):
    return await crud.productos.delete_producto(mongo_db, id)
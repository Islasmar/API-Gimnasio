from decimal import Decimal
from http.client import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from schemas.productos import ProductoCreate, ProductoUpdate
from datetime import datetime


# 1. Obtener productos (paginación)
async def get_productos(mongo_db, skip: int = 0, limit: int = 10):
    """Obtener una lista de productos con paginación."""
    productos = await mongo_db["productosgym"].find().skip(skip).limit(limit).to_list(length=limit)
    return productos

# 2. Obtener un producto por ID
async def get_producto(mongo_db, id: str):
    """Obtener un producto por ID (convertilo a ObjectId)."""
    try:
        producto = await mongo_db["productosgym"].find_one({"_id": ObjectId(id)})
        return producto
    except Exception as e:
        return {"error": "Producto no encontrado"}

async def get_producto_by_cod_barras(mongo_db, cod_barras: str):
    """Obtener un producto por código de barras."""
    producto = await mongo_db["productosgym"].find_one({"cod_barras": cod_barras})
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    # Convertir _id a str
    if "_id" in producto:
        producto["_id"] = str(producto["_id"])
    return producto

# 4. Crear un nuevo producto
async def create_producto(mongo_db, producto: ProductoCreate):
    """Crear un nuevo producto."""
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

# 5. Actualizar un producto
async def update_producto(mongo_db, id: str, producto: ProductoUpdate):
    """Actualizar un producto existente."""
    # Verificar si producto es un diccionario o un modelo Pydantic
    if isinstance(producto, dict):
        producto_data = producto  # Si ya es un diccionario, úsalo directamente
    else:
        producto_data = producto.dict(exclude_unset=True)  # Convertir modelo Pydantic a diccionario

    # Convertir Decimal a float si existe
    for key, value in producto_data.items():
        if isinstance(value, Decimal):
            producto_data[key] = float(value)

    # Actualizar la fecha de modificación
    producto_data["fecha_actualizacion"] = datetime.utcnow()

    # Actualizar el producto en la base de datos
    result = await mongo_db["productosgym"].update_one(
        {"_id": ObjectId(id)}, {"$set": producto_data}
    )
    
    if result.modified_count > 0:
        updated_producto = await mongo_db["productosgym"].find_one({"_id": ObjectId(id)})
        if updated_producto and "_id" in updated_producto:
            updated_producto["_id"] = str(updated_producto["_id"])  # Convertir ObjectId a str
        return updated_producto
    return None

# 6. Eliminar un producto
async def delete_producto(mongo_db, id: str):
    """Eliminar un producto por ID."""
    result = await mongo_db["productosgym"].delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return {"msg": "Producto eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="Producto no encontrado")



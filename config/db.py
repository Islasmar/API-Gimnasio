from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cargar variables de entorno desde .env
load_dotenv()

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('DB_USER', 'root')}:{os.getenv('DB_PASSWORD', '')}"
    f"@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '3309')}/{os.getenv('DB_NAME', 'gym')}"
)
# Crear el motor de base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crear sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

MONGO_URI = os.getenv("MONGO_URI")
mongo_client = AsyncIOMotorClient(MONGO_URI)
mongo_db = mongo_client["gym"]  # <- Aquí accedes a la base gym
coleccion_productos = mongo_db["productosgym"]  # <- Aquí accedes a la colección

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#configuracion de la base de datosm en aiven
#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_TUUjXCnZQAQk-kZ2VKZ@mysql-270c42e9-lorenaascencion2003-2691.d.aivencloud.com:10171/defaultdb"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/gym"
#  Conexión local
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
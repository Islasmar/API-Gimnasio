from fastapi import HTTPException, Request, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from jwt_config import valida_token
import crud.users, config.db, models.users
import bcrypt  # Asegúrate de importar bcrypt

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
class Portador(HTTPBearer):
    async def __call__(self, request: Request, db: Session = Depends(get_db)):
        autorizacion = await super().__call__(request)
        print(f"Token recibido: {autorizacion.credentials}")  # <-- Agregar para depuración
        dato = valida_token(autorizacion.credentials)
        print(f"Datos del token: {dato}")  # <-- Agregar para ver qué retorna `valida_token`

        # Buscar al usuario solo por correo electrónico
        db_userlogin = crud.users.get_user_by_credentials(db, correo=dato['Correo_Electronico'])
        if db_userlogin is None:
            raise HTTPException(status_code=404, detail='Usuario no encontrado')

        # Verificar la contraseña
        if not bcrypt.checkpw(dato['Contrasena'].encode('utf-8'), db_userlogin.Contrasena.encode('utf-8')):
            raise HTTPException(status_code=401, detail='Contraseña incorrecta')

        return db_userlogin
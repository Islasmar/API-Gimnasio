# Proyecto de Gestión de Instalaciones y Sucursales

Este proyecto permite gestionar las instalaciones y sucursales mediante una API creada con FastAPI y SQLAlchemy.

## Requisitos

- Python 3.8 o superior
- MySQL (o cualquier base de datos compatible con SQLAlchemy)

## Pasos para ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone <URL del repositorio>
cd <nombre del directorio>
```

### 2. Crear y activar un entorno virtual (opcional, pero recomendado)

```
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
```

### 3. Instalar las dependencias

```
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Asegúrate de tener MySQL en funcionamiento y crea una base de datos.

Edita el archivo config/db.py para incluir los datos correctos de conexión a la base de datos.

### 5. Crear las tablas en la base de datos

Ejecuta el siguiente comando para crear las tablas necesarias:

```
python main.py
```

### 6. Ejecutar la aplicación

Para correr el servidor de la API, ejecuta:

```
uvicorn main:app --reload
```

La aplicación estará disponible en http://localhost:8000.

### Acceder a la API

Puedes probar las rutas de la API accediendo a la documentación automática proporcionada por FastAPI en:

```
http://localhost:8000/docs
```

### Autenticación
Este proyecto utiliza un middleware de autenticación basado en tokens JWT. Necesitarás un token válido para acceder a las rutas protegidas.

### Contacto

Si tienes alguna duda o necesitas ayuda, no dudes en contactarnos.


Este es el contenido completo del `README.md` en formato código de markdown. ¡Ahora está todo listo!

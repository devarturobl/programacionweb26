# Proyecto CRUD con FastAPI

CRUD representa las cuatro operaciones básicas sobre los datos:

- **Create (crear): `POST`**. Agrega un producto. Ejemplo: `POST /productos` con el cuerpo JSON `{"nombre": "Teclado", "precio": 25.5}`. La API responde con el producto creado y su `id`.
- **Read (leer): `GET`**. Consulta los productos. `GET /productos` muestra la lista completa y `GET /productos/1` obtiene el producto con el identificador 1.
- **Update (actualizar): `PUT`**. Reemplaza los datos de un producto. Ejemplo: `PUT /productos/1` con el cuerpo JSON `{"nombre": "Teclado mecánico", "precio": 45.0}`.
- **Delete (eliminar): `DELETE`**. Elimina un producto. Ejemplo: `DELETE /productos/1`.

Los datos de este ejemplo se guardan en memoria, por lo que se reinician cuando se detiene la aplicación. Para ejecutarla, instala FastAPI y Uvicorn (`pip install fastapi uvicorn`) y luego inicia el servidor con `uvicorn app:app --reload`. La documentación interactiva está disponible en `http://127.0.0.1:8000/docs`.

# Documentacion de la API CRUD con FastAPI

Esta API administra productos con tres datos: `id`, `nombre` y `precio`. FastAPI registra las operaciones mediante sus decoradores HTTP. Los productos se almacenan en la lista `productos`, que vive en la memoria del proceso; por eso, los datos se pierden al detener o reiniciar el servidor.

## Endpoints

### `GET /` — informacion de la API

Devuelve un mensaje de bienvenida, el autor y la version. No modifica la lista de productos.

Ejemplo de respuesta:

```json
{
  "message": "Bienvenidos a este ejemplo de API CRUD con FastAPI",
  "author": "José Arturo Bustamante Lazcano",
  "version": "1.0.0"
}
```

### `GET /productos` — consultar productos

Devuelve todos los productos guardados. Al iniciar la aplicacion, la lista esta vacia y la respuesta es `[]`.

Ejemplo de respuesta:

```json
[
  {
    "id": 1,
    "nombre": "Teclado",
    "precio": 25.5
  }
]
```

### `POST /productos` — crear un producto con parametros

Recibe `nombre` y `precio` como parametros de consulta (query parameters). La funcion llama a `generaid()` para asignar un identificador, crea el producto, lo agrega a `productos` y devuelve un mensaje junto con el producto creado.

Ejemplo de solicitud:

```text
POST /productos?nombre=Teclado&precio=25.5
```

Ejemplo de respuesta:

```json
{
  "message": "Producto creado exitosamente",
  "producto": {
    "id": 1,
    "nombre": "Teclado",
    "precio": 25.5
  }
}
```

### `POST /productos/body` — crear un producto con JSON

Recibe el producto en el cuerpo de la solicitud. `Body(...)` indica que el cuerpo es obligatorio. El codigo agrega el `id` generado al diccionario recibido, lo guarda en la lista y devuelve el resultado.

Ejemplo de solicitud:

```http
POST /productos/body
Content-Type: application/json
```

```json
{
  "nombre": "Mouse",
  "precio": 12.99
}
```

La respuesta incluye el mensaje de exito y el producto con su `id`, igual que en el otro endpoint de creacion.

### `PUT /productos/{id}` — actualizar un producto

El `id` se indica en la ruta. Los nuevos valores de `nombre` y `precio` se envian como parametros de consulta. La funcion recorre la lista y, si encuentra el identificador, reemplaza esos dos valores y devuelve el producto actualizado. Si no lo encuentra, devuelve el mensaje `"Producto no encontrado"`.

Ejemplo de solicitud:

```text
PUT /productos/1?nombre=Teclado%20mecanico&precio=45
```

Ejemplo de respuesta cuando existe:

```json
{
  "message": "Producto actualizado exitosamente",
  "producto": {
    "id": 1,
    "nombre": "Teclado mecanico",
    "precio": 45.0
  }
}
```

### `DELETE /productos/{id}` — eliminar un producto

Recibe el `id` en la ruta, busca el producto y lo quita de la lista. Si lo encuentra, devuelve un mensaje de confirmacion; de lo contrario, devuelve `"Producto no encontrado"`.

Ejemplo de solicitud:

```text
DELETE /productos/1
```

## Como se generan los identificadores

La funcion `generaid()` devuelve `1` cuando no hay productos. Si la lista contiene productos, toma el `id` del ultimo elemento y le suma uno. La funcion se utiliza en ambos endpoints `POST`.

## Ejecutar y probar

Desde la carpeta que contiene `app.py`, inicia el servidor con:

```bash
uvicorn app:app --reload
```

La API queda disponible en `http://127.0.0.1:8000`. FastAPI proporciona una interfaz interactiva para probar los endpoints en `http://127.0.0.1:8000/docs`.

> Las respuestas de `"Producto no encontrado"` se devuelven como JSON normal; el codigo actual no asigna un estado HTTP `404` para esos casos.

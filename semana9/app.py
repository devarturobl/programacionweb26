from fastapi import FastAPI, Body

app = FastAPI()

productos = []

def generaid():
    if len(productos) == 0:
        return 1
    else:
        return productos[-1]["id"] + 1

@app.get("/")
def data_info():
    return {
        "message": "Bienvenidos a este ejemplo de API CRUD con FastAPI",
        "author": "José Arturo Bustamante Lazcano",
        "version": "1.0.0"
        }

@app.get("/productos")
def get_productos():
    return productos

@app.post("/productos")
def create_producto(nombre: str, precio: float):
    id = generaid()
    producto = {"id": id, "nombre": nombre, "precio": precio}
    productos.append(producto)
    return {"message": "Producto creado exitosamente", "producto": producto}   

@app.post("/productos/body")
def create_producto_body(producto: dict = Body(...)):
    id = generaid()
    producto["id"] = id
    productos.append(producto)
    return {"message": "Producto creado exitosamente", "producto": producto}

@app.put("/productos/{id}")
def update_producto(id: int, nombre: str, precio: float):
    for producto in productos:
        if producto["id"] == id:
            producto["nombre"] = nombre
            producto["precio"] = precio
            return {"message": "Producto actualizado exitosamente", "producto": producto}
    return {"message": "Producto no encontrado"}

@app.delete("/productos/{id}")
def delete_producto(id: int):
    for producto in productos:
        if producto["id"] == id:
            productos.remove(producto)
            return {"message": "Producto eliminado exitosamente"}
    return {"message": "Producto no encontrado"}

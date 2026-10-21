from fastapi import FastAPI

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

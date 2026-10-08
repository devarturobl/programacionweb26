# Requisitos para trabajar con fastapi
1 Tener una version superior a python 7
2 instalar fastapi y uvicorn

```pip install fastapi uvicorn```

3 Importamos en el proyecto FastApi
```from fastapi import FastAPI```

4 Creamos la primera aplicacion basica <code>

```
# Importamos libreria de FastApi
from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()

# Define a simple route for the root endpoint
@app.get("/")

# Define una funcion de arranque
def home():
    return {"message": "Welcome to the FastAPI application!"}
```

5 Ejecutar el api usando UVICORN
Terminal > ```uvicorn app:app --port 5000 --reload```

Donde el primer app es el nombre del archivo.py : el nombre de la aplicacion el puerto es opcional reload es para actualizace 

6 Ejecutar el API en RED
Terminal > ```uvicorn app:app host 0.0.0.0 --port 5000 --reload```

Donde host 0.0.0.0 significa todos los miembros de mi red lan






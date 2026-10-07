from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()

# Define a simple route for the root endpoint
@app.get("/")

# Define una funcion de arranque
def home():
    return {
        "message": "Welcome to the FastAPI application!",
        "status": "success",
        "data": {
            "info": "This is a sample FastAPI application.",
            "version": "1.0.0"
        }
    }
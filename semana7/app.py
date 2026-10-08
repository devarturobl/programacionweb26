from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()

app.title = "Sample FastAPI"

app.description = """This is a sample FastAPI application that demonstrates the basic structure and functionality of a FastAPI project. It includes a simple route for the root endpoint and returns a JSON response with a welcome message, status, and additional information."""

# Define a simple route for the root endpoint
@app.get("/", tags=["Home"], summary="Root Endpoint", description="Returns a welcome message and application information.")

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
from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()

app.title = "Sample FastAPI"

app.description = """This is a sample FastAPI application that demonstrates the basic structure and functionality of a FastAPI project. It includes a simple route for the root endpoint and returns a JSON response with a welcome message, status, and additional information."""

## Generar los endpoints de la aplicacion
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


@app.get("/characters", tags=["Characters"], summary="Get Characters Simpson", description="Returns a list of characters from the application.")
def get_characters():
    # Sample data for characters
    return [
        {"name": "Homer Simpson", "occupation": "Nuclear Safety Inspector", "imagen": "https://cdn.thesimpsonsapi.com/500/character/1.webp"},
        {"name": "Marge Simpson", "occupation": "Housewife", "imagen": "https://cdn.thesimpsonsapi.com/500/character/2.webp"},
        {"name": "Bart Simpson", "occupation": "Student", "imagen": "https://cdn.thesimpsonsapi.com/500/character/3.webp"},
        {"name": "Lisa Simpson", "occupation": "Student", "imagen": "https://cdn.thesimpsonsapi.com/500/character/4.webp"},
        {"name": "Maggie Simpson", "occupation": "Baby", "imagen": "https://cdn.thesimpsonsapi.com/500/character/5.webp"}
    ]


simpson_characters = [
        {"id": 1, "name": "Homer Simpson", "occupation": "Nuclear Safety Inspector", "imagen": "https://cdn.thesimpsonsapi.com/500/character/1.webp"},
        {"id": 2, "name": "Marge Simpson", "occupation": "Housewife", "imagen": "https://cdn.thesimpsonsapi.com/500/character/2.webp"},
        {"id": 3, "name": "Bart Simpson", "occupation": "Student", "imagen": "https://cdn.thesimpsonsapi.com/500/character/3.webp"},
        {"id": 4, "name": "Lisa Simpson", "occupation": "Student", "imagen": "https://cdn.thesimpsonsapi.com/500/character/4.webp"},
        {"id": 5, "name": "Maggie Simpson", "occupation": "Baby", "imagen": "https://cdn.thesimpsonsapi.com/500/character/5.webp"}
    ]

@app.get("/characters/{id}", tags=["Characters by ID"], summary="Get Character by ID", description="Returns a character from the application based on the provided ID.")
def character_id(id: int):
    for character in simpson_characters:
        if character["id"] == id:
            return character
    return {"error": "Character not found"} 

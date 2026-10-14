from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def data_info():
    return {
        "message": "Bienvenidos a este ejemplo de API con FastAPI",
        "author": "José Arturo Bustamante Lazcano",
        "version": "1.0.0"
        }

@app.get("/movies")
def data_movies():
    return {
        "api_version": "v1",
        "total_records": 50,
        "filters_applied": {
            "year": 2026
        },
        "data": [
            {
            "id": 1,
            "title": "La Odisea",
            "original_title": "The Odyssey",
            "release_date": "2026-07-17",
            "director": "Christopher Nolan",
            "genres": ["Aventura", "Drama", "Épica"],
            "cast": ["Matt Damon", "Tom Holland"],
            "synopsis": "Adaptación épica del clásico de Homero bajo la dirección de Christopher Nolan.",
            "rating_score": 7.6,
            "status": "Estrenada"
            },
            {
            "id": 2,
            "title": "Vengadores: Doomsday",
            "original_title": "Avengers: Doomsday",
            "release_date": "2026-05-01",
            "director": "Hermanos Russo",
            "genres": ["Acción", "Ciencia Ficción", "Superhéroes"],
            "cast": ["Robert Downey Jr.", "Pedro Pascal"],
            "synopsis": "Nueva entrega coral del universo cinematográfico de Marvel centrada en la amenaza de Doctor Doom.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 3,
            "title": "Dune: Parte 3",
            "original_title": "Dune: Part Three",
            "release_date": "2026-12-18",
            "director": "Denis Villeneuve",
            "genres": ["Ciencia Ficción", "Drama"],
            "cast": ["Timothée Chalamet", "Zendaya"],
            "synopsis": "La continuación de la saga galáctica basada en el universo literario de Frank Herbert.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 4,
            "title": "Spider-Man: Brand New Day",
            "original_title": "Spider-Man: Brand New Day",
            "release_date": "2026-07-10",
            "director": "Destin Daniel Cretton",
            "genres": ["Acción", "Aventura", "Superhéroes"],
            "cast": ["Tom Holland", "Zendaya"],
            "synopsis": "Nuevas aventuras en solitario del trepamuros dentro del UCM.",
            "rating_score": 7.0,
            "status": "Próximamente"
            },
            {
            "id": 5,
            "title": "Toy Story 5",
            "original_title": "Toy Story 5",
            "release_date": "2026-06-19",
            "director": "Andrew Stanton",
            "genres": ["Animación", "Comedia", "Familiar"],
            "cast": ["Tom Hanks", "Tim Allen"],
            "synopsis": "Los juguetes favoritos de la infancia regresan para enfrentarse al reto de la tecnología digital.",
            "rating_score": 6.7,
            "status": "Próximamente"
            },
            {
            "id": 6,
            "title": "The Mandalorian and Grogu",
            "original_title": "The Mandalorian & Grogu",
            "release_date": "2026-05-22",
            "director": "Jon Favreau",
            "genres": ["Ciencia Ficción", "Aventura"],
            "cast": ["Pedro Pascal", "Sigourney Weaver"],
            "synopsis": "El cazarrecompensas mandaloriano y su pequeño protegido dan el salto a la gran pantalla.",
            "rating_score": 6.3,
            "status": "Próximamente"
            },
            {
            "id": 7,
            "title": "Proyecto Salvación",
            "original_title": "Project Hail Mary",
            "release_date": "2026-03-20",
            "director": "Phil Lord, Christopher Miller",
            "genres": ["Ciencia Ficción", "Drama"],
            "cast": ["Ryan Gosling", "Sandra Hüller"],
            "synopsis": "Un astronauta solitario debe salvar a la Tierra de un desastre cósmico basándose en la novela de Andy Weir.",
            "rating_score": 7.2,
            "status": "Estrenada"
            },
            {
            "id": 8,
            "title": "Super Mario Galaxy: La Película",
            "original_title": "The Super Mario Galaxy Movie",
            "release_date": "2026-04-01",
            "director": "Aaron Horvath, Michael Jelenic",
            "genres": ["Animación", "Aventura", "Familiar"],
            "cast": ["Chris Pratt", "Anya Taylor-Joy"],
            "synopsis": "Mario y Luigi extienden sus aventuras por todo el cosmos en esta secuela animada.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 9,
            "title": "Marty Supreme",
            "original_title": "Marty Supreme",
            "release_date": "2026-01-30",
            "director": "Joshua Safdie",
            "genres": ["Drama", "Biopic"],
            "cast": ["Timothée Chalamet", "Gwyneth Paltrow"],
            "synopsis": "Biopic sobre Marty Reisman, el legendario y excéntrico campeón de tenis de mesa.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 10,
            "title": "Scream 7",
            "original_title": "Scream 7",
            "release_date": "2026-02-27",
            "director": "Kevin Williamson",
            "genres": ["Terror", "Suspenso", "Slasher"],
            "cast": ["Neve Campbell"],
            "synopsis": "Ghostface regresa para aterrorizar a una nueva generación de víctimas en esta emblemática saga.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 11,
            "title": "Supergirl",
            "original_title": "Supergirl: Woman of Tomorrow",
            "release_date": "2026-06-26",
            "director": "Craig Gillespie",
            "genres": ["Acción", "Ciencia Ficción", "Superhéroes"],
            "cast": ["Milly Alcock"],
            "synopsis": "Una mirada más cruda y espacial a la prima de Superman en el nuevo universo DC.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 12,
            "title": "El diablo viste a la moda 2",
            "original_title": "The Devil Wears Prada 2",
            "release_date": "2026-04-30",
            "director": "David Frankel",
            "genres": ["Comedia", "Drama"],
            "cast": ["Meryl Streep", "Anne Hathaway", "Emily Blunt"],
            "synopsis": "Miranda Priestly se enfrenta al declive de las revistas impresas frente al auge de los medios digitales.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 13,
            "title": "Michael",
            "original_title": "Michael",
            "release_date": "2026-04-23",
            "director": "Antoine Fuqua",
            "genres": ["Biopic", "Musical", "Drama"],
            "cast": ["Jaafar Jackson", "Colman Domingo"],
            "synopsis": "Película biográfica que explora la vida y carrera artística de Michael Jackson.",
            "rating_score": 6.7,
            "status": "Estrenada"
            },
            {
            "id": 14,
            "title": "Los juegos del hambre: Amanecer en la cosecha",
            "original_title": "The Hunger Games: Sunrise on the Reaping",
            "release_date": "2026-11-20",
            "director": "Francis Lawrence",
            "genres": ["Acción", "Ciencia Ficción", "Drama"],
            "cast": ["Reparto por confirmar"],
            "synopsis": "Precuela de la exitosa saga distópica centrada en los quincuagésimos Juegos del Hambre.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 15,
            "title": "Resident Evil",
            "original_title": "Resident Evil (2026)",
            "release_date": "2026-09-18",
            "director": "Zach Cregger",
            "genres": ["Terror", "Acción", "Ciencia Ficción"],
            "cast": ["Austin Abrams", "Paul Walter Hauser"],
            "synopsis": "Nueva adaptación cinematográfica de la mítica saga de videojuegos de Capcom.",
            "rating_score": 7.0,
            "status": "Estrenada"
            },
            {
            "id": 16,
            "title": "Hoppers",
            "original_title": "Hoppers",
            "release_date": "2026-03-06",
            "director": "Daniel Chong",
            "genres": ["Animación", "Comedia", "Ciencia Ficción"],
            "cast": ["Piper Curda", "Jon Hamm"],
            "synopsis": "Una científica transfiere su conciencia a un castor robótico para comunicarse con los animales.",
            "rating_score": 6.7,
            "status": "Estrenada"
            },
            {
            "id": 17,
            "title": "El drama",
            "original_title": "The Drama",
            "release_date": "2026-04-09",
            "director": "Kristoffer Borgli",
            "genres": ["Comedia Negra", "Romance", "Drama"],
            "cast": ["Zendaya", "Robert Pattinson"],
            "synopsis": "Una pareja experimenta giros inesperados y caóticos poco antes de celebrar su boda.",
            "rating_score": 6.6,
            "status": "Estrenada"
            },
            {
            "id": 18,
            "title": "Mortal Kombat 2",
            "original_title": "Mortal Kombat 2",
            "release_date": "2026-10-23",
            "director": "Simon McQuoid",
            "genres": ["Acción", "Artes Marciales", "Fantasía"],
            "cast": ["Karl Urban", "Lewis Tan"],
            "synopsis": "Los guerreros de la Tierra vuelven al torneo definitivo para frenar las fuerzas del Outworld.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 19,
            "title": "Cumbres borrascosas",
            "original_title": "Wuthering Heights",
            "release_date": "2026-02-12",
            "director": "Emerald Fennell",
            "genres": ["Drama", "Romance", "Gótico"],
            "cast": ["Margot Robbie", "Jacob Elordi"],
            "synopsis": "Intensa y moderna reinterpretación de la clásica novela gótica de Emily Brontë.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 20,
            "title": "¡La novia!",
            "original_title": "The Bride!",
            "release_date": "2026-03-05",
            "director": "Maggie Gyllenhaal",
            "genres": ["Terror", "Drama", "Ciencia Ficción"],
            "cast": ["Christian Bale", "Jessie Buckley"],
            "synopsis": "Ambientada en el Chicago de los años 30, un Frankenstein solitario pide ayuda a un científico para crear a su compañera.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 21,
            "title": "Street Fighter",
            "original_title": "Street Fighter",
            "release_date": "2026-10-16",
            "director": "Kitao Sakurai",
            "genres": ["Acción", "Artes Marciales"],
            "cast": ["Reparto por confirmar"],
            "synopsis": "Nueva adaptación cinematográfica de acción real basada en la icónica franquicia de videojuegos de lucha.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 22,
            "title": "El precio de la red",
            "original_title": "The Social Reckoning",
            "release_date": "2026-10-09",
            "director": "Aaron Sorkin",
            "genres": ["Drama", "Thriller"],
            "cast": ["Reparto por confirmar"],
            "synopsis": "Un análisis profundo sobre el impacto y las repercusiones globales de las redes sociales modernas.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 23,
            "title": "Scary Movie 6",
            "original_title": "Scary Movie 6",
            "release_date": "2026-08-14",
            "director": "Michael Tiddes",
            "genres": ["Comedia", "Parodia"],
            "cast": ["Wayans Brothers (Rumores)"],
            "synopsis": "El regreso de la saga de parodias de terror que satiriza los mayores éxitos taquilleros del cine reciente.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 24,
            "title": "El día de la revelación",
            "original_title": "Disclosure Day",
            "release_date": "2026-06-12",
            "director": "Steven Spielberg",
            "genres": ["Ciencia Ficción", "Misterio"],
            "cast": ["Emily Blunt", "Josh O'Connor"],
            "synopsis": "Un misterioso largometraje de misterio y encuentros cercanos dirigido por Steven Spielberg.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 25,
            "title": "He-Man y los Masters del Universo",
            "original_title": "Masters of the Universe",
            "release_date": "2026-06-05",
            "director": "Travis Knight",
            "genres": ["Fantasía", "Acción", "Aventura"],
            "cast": ["Nicholas Galitzine"],
            "synopsis": "El príncipe Adam emprende su viaje para convertirse en He-Man y defender Eternia de Skeletor.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 26,
            "title": "Minions & Monsters",
            "original_title": "Minions & Monsters",
            "release_date": "2026-07-03",
            "director": "Pierre Coffin",
            "genres": ["Animación", "Comedia", "Familiar"],
            "cast": ["Pierre Coffin"],
            "synopsis": "Nuevas y disparatadas desventuras de los icónicos personajes amarillos en un entorno fantástico.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 27,
            "title": "Vaiana",
            "original_title": "Moana (Live-Action)",
            "release_date": "2026-07-10",
            "director": "Thomas Kail",
            "genres": ["Aventura", "Musical", "Fantasía"],
            "cast": ["Catherine Laga'aia", "Dwayne Johnson"],
            "synopsis": "Versión en acción real del clásico animado de Disney sobre la joven navegante oceánica.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 28,
            "title": "La constelación del perro",
            "original_title": "The Dog Stars",
            "release_date": "2026-11-06",
            "director": "Ridley Scott",
            "genres": ["Ciencia Ficción", "Drama", "Thriller"],
            "cast": ["Paul Mescal"],
            "synopsis": "En un mundo devastado por una pandemia, un piloto sobrevive en una base aérea abandonada.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 29,
            "title": "Coyote vs. ACME",
            "original_title": "Coyote vs. ACME",
            "release_date": "2026-08-28",
            "director": "Dave Green",
            "genres": ["Comedia", "Animación", "Acción"],
            "cast": ["Will Forte", "John Cena"],
            "synopsis": "Wile E. Coyote contrata a un abogado humano para demandar a la corporación ACME por sus productos defectuosos.",
            "rating_score": 6.7,
            "status": "Estrenada"
            },
            {
            "id": 30,
            "title": "Digger",
            "original_title": "Digger",
            "release_date": "2026-05-15",
            "director": "Alejandro González Iñárritu",
            "genres": ["Drama"],
            "cast": ["Tom Cruise", "Riz Ahmed"],
            "synopsis": "Un drama intimista dirigido por el aclamado director mexicano Alejandro González Iñárritu.",
            "rating_score": 6.5,
            "status": "Estrenada"
            },
            {
            "id": 31,
            "title": "El ser querido",
            "original_title": "El ser querido",
            "release_date": "2026-03-12",
            "director": "Rodrigo Sorogoyen",
            "genres": ["Drama", "Thriller"],
            "cast": ["Javier Bardem", "Victoria Luengo"],
            "synopsis": "Un intenso retrato sobre las complejas relaciones familiares y los dilemas morales.",
            "rating_score": 7.2,
            "status": "Estrenada"
            },
            {
            "id": 32,
            "title": "La bola negra",
            "original_title": "La bola negra",
            "release_date": "2026-01-15",
            "director": "Javier Calvo, Javier Ambrossi",
            "genres": ["Drama", "Comedia dramática"],
            "cast": ["Miguel Bernardeau", "Guitarricadelafuente"],
            "synopsis": "Crónica generacional sobre la juventud, la ambición y la búsqueda de identidad artística.",
            "rating_score": 8.0,
            "status": "Estrenada"
            },
            {
            "id": 33,
            "title": "Hamnet",
            "original_title": "Hamnet",
            "release_date": "2026-01-22",
            "director": "Chloé Zhao",
            "genres": ["Drama", "Histórica"],
            "cast": ["Paul Mescal", "Jessie Buckley"],
            "synopsis": "La historia detrás de la creación de la obra maestra Hamlet de William Shakespeare tras una tragedia familiar.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 34,
            "title": "En el corazón de la bestia",
            "original_title": "Heart of the Beast",
            "release_date": "2026-09-25",
            "director": "David Ayer",
            "genres": ["Acción", "Supervivencia", "Thriller"],
            "cast": ["Brad Pitt", "J.K. Simmons"],
            "synopsis": "Un ex-soldado y su perro de combate enfrentan una lucha extrema por la supervivencia en la naturaleza.",
            "rating_score": 6.4,
            "status": "Estrenada"
            },
            {
            "id": 35,
            "title": "Las ovejas detectives",
            "original_title": "Three Bags Full: A Sheep Detective Movie",
            "release_date": "2026-02-20",
            "director": "Kyle Balda",
            "genres": ["Comedia", "Animación", "Misterio"],
            "cast": ["Hugh Jackman", "Emma Thompson"],
            "synopsis": "Un rebaño de ovejas intenta resolver el misterio del asesinato de su querido pastor.",
            "rating_score": 6.4,
            "status": "Estrenada"
            },
            {
            "id": 36,
            "title": "Backrooms",
            "original_title": "Backrooms",
            "release_date": "2026-09-11",
            "director": "Kane Parsons",
            "genres": ["Terror", "Misterio", "Sci-Fi"],
            "cast": ["Chiwetel Ejiofor", "Renate Reinsve"],
            "synopsis": "Adaptación cinematográfica del fenómeno viral de terror psicológico y dimensiones laberínticas.",
            "rating_score": 6.2,
            "status": "Estrenada"
            },
            {
            "id": 37,
            "title": "Ruta de escape",
            "original_title": "The Rip",
            "release_date": "2026-01-16",
            "director": "Bart Layton",
            "genres": ["Thriller", "Acción"],
            "cast": ["Chris Hemsworth", "Mark Ruffalo"],
            "synopsis": "Un grupo de policías de Miami descubre millones de dólares en efectivo ocultos, desatando una red de desconfianza.",
            "rating_score": 6.2,
            "status": "Estrenada"
            },
            {
            "id": 38,
            "title": "Letras robadas",
            "original_title": "Song Sung Blue",
            "release_date": "2026-01-01",
            "director": "John Carney",
            "genres": ["Musical", "Romance", "Drama"],
            "cast": ["Paul Rudd", "Nick Jonas"],
            "synopsis": "Dos músicos desafortunados forman una banda tributo de Neil Diamond y encuentran un nuevo sentido a sus vidas.",
            "rating_score": 6.2,
            "status": "Estrenada"
            },
            {
            "id": 39,
            "title": "Torrente Presidente",
            "original_title": "Torrente Presidente",
            "release_date": "2026-12-04",
            "director": "Santiago Segura",
            "genres": ["Comedia", "Humor Negro"],
            "cast": ["Santiago Segura"],
            "synopsis": "El torpe e incorregible expolicía José Luis Torrente se embarca en una nueva y disparatada misión política.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 40,
            "title": "Peaky Blinders: El hombre inmortal",
            "original_title": "Peaky Blinders: The Immortal Man",
            "release_date": "2026-11-13",
            "director": "Tom Harper",
            "genres": ["Crimen", "Drama", "Thriller"],
            "cast": ["Cillian Murphy", "Rebecca Ferguson"],
            "synopsis": "Continuación cinematográfica de la exitosa serie británica ambientada durante los años de la Segunda Guerra Mundial.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 41,
            "title": "Amarga Navidad",
            "original_title": "Amarga Navidad",
            "release_date": "2026-12-11",
            "director": "Pedro Almodóvar",
            "genres": ["Drama"],
            "cast": ["Penélope Cruz", "Aitana Sánchez-Gijón"],
            "synopsis": "Un drama intimista bajo la particular y colorida visión estética del director manchego.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 42,
            "title": "Buena suerte, pásalo bien y no mueras",
            "original_title": "Good Luck, Have Fun, Don't Die",
            "release_date": "2026-03-09",
            "director": "Gore Verbinski",
            "genres": ["Ciencia Ficción", "Acción", "Comedia"],
            "cast": ["Sam Rockwell", "Zazie Beetz"],
            "synopsis": "Un hombre de el futuro llega a un restaurante de Los Ángeles para reclutar clientes en una guerra contra una inteligencia artificial.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 43,
            "title": "Greenland 2",
            "original_title": "Greenland: Migration",
            "release_date": "2026-02-06",
            "director": "Ric Roman Waugh",
            "genres": ["Acción", "Thriller", "Catástrofe"],
            "cast": ["Gerard Butler", "Morena Baccarin"],
            "synopsis": "La familia Garrity debe abandonar la seguridad del búnker en Groenlandia para buscar un nuevo hogar en el Yermo europeo.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 44,
            "title": "Werwulf",
            "original_title": "Werwulf",
            "release_date": "2026-10-30",
            "director": "Robert Eggers",
            "genres": ["Terror", "Fantasía oscura", "Drama"],
            "cast": ["Anya Taylor-Joy", "Willem Dafoe"],
            "synopsis": "Una atmósfera de terror folclórico medieval enfocada en mitos de hombres lobo en la Europa profunda.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 45,
            "title": "Clayface",
            "original_title": "Clayface",
            "release_date": "2026-09-18",
            "director": "James Watkins",
            "genres": ["Terror", "Thriller", "Superhéroes"],
            "cast": ["Reparto por confirmar"],
            "synopsis": "Spin-off de corte oscuro y atmosférico enfocado en uno de los villanos clásicos de Gotham.",
            "rating_score": 0.0,
            "status": "Próximamente"
            },
            {
            "id": 46,
            "title": "Send Help (Enviad ayuda)",
            "original_title": "Send Help",
            "release_date": "2026-02-06",
            "director": "Sam Raimi",
            "genres": ["Terror", "Thriller de supervivencia"],
            "cast": ["Rachel McAdams"],
            "synopsis": "Un thriller de supervivencia psicológico con tintes de terror dirigido por el especialista Sam Raimi.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 47,
            "title": "Aída y vuelta",
            "original_title": "Aída y vuelta",
            "release_date": "2026-01-30",
            "director": "Paco León",
            "genres": ["Comedia", "Drama"],
            "cast": ["Carmen Machi", "Paco León"],
            "synopsis": "El regreso cinematográfico de los personajes de la mítica serie española de televisión.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 48,
            "title": "El botín",
            "original_title": "The Rip",
            "release_date": "2026-01-09",
            "director": "Joe Carnahan",
            "genres": ["Acción", "Crimen"],
            "cast": ["Matt Damon", "Ben Affleck"],
            "synopsis": "Un thriller de atracos de alto voltaje donde la lealtad de un equipo de veteranos se pone a prueba.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 49,
            "title": "28 años después: El templo de los huesos",
            "original_title": "28 Years Later: The Bone Temple",
            "release_date": "2026-01-02",
            "director": "Nia DaCosta",
            "genres": ["Terror", "Ciencia Ficción", "Zombies"],
            "cast": ["Aaron Taylor-Johnson", "Jodie Comer"],
            "synopsis": "Nueva entrega de la aclamada franquicia de infectados postapocalípticos iniciada por Danny Boyle.",
            "rating_score": 0.0,
            "status": "Estrenada"
            },
            {
            "id": 50,
            "title": "Jumanji 3",
            "original_title": "Jumanji 3",
            "release_date": "2026-12-25",
            "director": "Jake Kasdan",
            "genres": ["Aventura", "Comedia", "Fantasía"],
            "cast": ["Dwayne Johnson", "Kevin Hart", "Jack Black", "Karen Gillan"],
            "synopsis": "El grupo de amigos vuelve a sumergirse en el peligroso y alocado videojuego para una última gran misión.",
            "rating_score": 0.0,
            "status": "Próximamente"
            }
          ]
}
    
#movies = data_movies()["data"]
@app.get("/movies/{id}")
def data_movie(id: int):
    movies = data_movies()["data"]
    for movie in movies:
        if movie["id"] == id:
            return movie
    return {"error": "Movie not found"}
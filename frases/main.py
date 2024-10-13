# frases/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from frases.database import get_db_connection
import random
import datetime
import requests

# Aquí estamos creando la aplicación FastAPI
app = FastAPI()

# Defino el modelo de datos para una frase
class Frase(BaseModel):
    texto: str

# Este endpoint me permite agregar una nueva frase
@app.post("/frases/")
def agregar_frase(frase: Frase):
    # Me conecto a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()

    # Inserto la nueva frase en la base de datos
    cursor.execute(
        "INSERT INTO frases (texto) VALUES (?)", (frase.texto,)
    )
    conn.commit()
    conn.close()

    # Devuelvo un mensaje de éxito
    return {"mensaje": "Frase registrada con éxito"}

# Este endpoint asigna una frase del día a un usuario
@app.post("/frase-del-dia/{id_usuario}")
def asignar_frase(id_usuario: int):
    # Me conecto a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()

    # Obtengo las frases que el usuario ya ha visto
    cursor.execute(
        "SELECT id_frase FROM frases_mostradas WHERE id_usuario = ?",
        (id_usuario,)
    )
    frases_vistas = {row["id_frase"] for row in cursor.fetchall()}

    # Selecciono una frase que el usuario no haya visto
    cursor.execute("SELECT * FROM frases")
    frases = [row for row in cursor.fetchall() if row["id"] not in frases_vistas]

    # Si no hay frases disponibles, lanzo un error
    if not frases:
        raise HTTPException(status_code=404, detail="No hay frases disponibles")

    # Elejimos una frase al azar
    frase = random.choice(frases)

    # Registro que el usuario ha visto esta frase
    fecha_actual = datetime.date.today().isoformat()
    cursor.execute(
        "INSERT INTO frases_mostradas (id_usuario, id_frase, fecha) VALUES (?, ?, ?)",
        (id_usuario, frase["id"], fecha_actual)
    )
    conn.commit()
    conn.close()

    # Envío una notificación al servicio de notificaciones
    requests.post("http://localhost:8004/notificar/", json={"mensaje": f"Se ha asignado la frase: '{frase['texto']}' al usuario {id_usuario}"})

    # Devuelvo la frase asignada
    return {"frase": frase["texto"]}

# usuarios/main.py
import sqlite3
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from .database import get_db_connection, create_tables, add_test_user

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    create_tables()
    add_test_user()  # Añadimos esto aquí para crear un usuario de prueba al iniciar la aplicación

# Modelo para el registro de usuarios
class Usuario(BaseModel):
    nombre: str
    email: str
    password: str

# Ruta para registrar un nuevo usuario
@app.post("/registro/")
def registrar_usuario(usuario: Usuario):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)",
            (usuario.nombre, usuario.email, usuario.password),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    finally:
        conn.close()

    return {"mensaje": f"Usuario {usuario.nombre} registrado con éxito"}

# Ruta para iniciar sesión y validar el usuario
@app.post("/login/")
def iniciar_sesion(email: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE email = ? AND password = ?", (email, password)
    )
    usuario = cursor.fetchone()
    conn.close()

    if usuario is None:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    return {"mensaje": f"Bienvenido, {usuario['nombre']}"}

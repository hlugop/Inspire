# frases/database.py
import sqlite3
import os

def get_db_connection():
    # Obtenemos la ruta del directorio actual
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Construimos la ruta completa de la base de datos
    db_path = os.path.join(base_dir, "frases.db")
    # Nos conectamos a la base de datos
    conn = sqlite3.connect(db_path)
    # Configuramos la conexión para que devuelva filas como diccionarios
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    # Nos conectamos a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()

    # Creamos la tabla de frases si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS frases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL
        )
    """)

    # Creamos la tabla de frases mostradas si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS frases_mostradas (
            id_usuario INTEGER,
            id_frase INTEGER,
            fecha TEXT,
            PRIMARY KEY (id_usuario, id_frase)
        )
    """)
    # Guardamos los cambios y cerramos la conexión
    conn.commit()
    conn.close()

# Ejecutamos la creación de tablas al iniciar
if __name__ == "__main__":
    create_tables()

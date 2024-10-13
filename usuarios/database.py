"""
/microservicios-demo/
│
├── usuarios/
│   ├── main.py  # Código del servicio de usuarios
│   └── database.py  # Conexión y creación de la base de datos SQLite
└── requirements.txt  # Dependencias del proyecto
"""

# usuarios/database.py
import sqlite3
import os

def get_db_connection():
    # Obtenemos la ruta del directorio actual
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Construimos la ruta completa de la base de datos
    db_path = os.path.join(base_dir, "usuarios.db")
    # Nos conectamos a la base de datos
    conn = sqlite3.connect(db_path)
    # Configuramos la conexión para que devuelva filas como diccionarios
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    # Nos conectamos a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()
    # Creamos la tabla de usuarios si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    # Guardamos los cambios y cerramos la conexión
    conn.commit()
    conn.close()
    print("Tabla 'usuarios' creada o ya existente.")

def add_test_user():
    # Nos conectamos a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Verificamos si el usuario ya existe
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", ("test@example.com",))
        existing_user = cursor.fetchone()
        
        if existing_user is None:
            # Si el usuario no existe, lo insertamos
            cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)",
                           ("Usuario de prueba", "test@example.com", "password123"))
            conn.commit()
            print("Usuario de prueba añadido.")
        else:
            print("El usuario de prueba ya existe.")
    except sqlite3.IntegrityError as e:
        print(f"Error de integridad: {e}")
    finally:
        # Cerramos la conexión
        conn.close()

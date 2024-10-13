'''
/microservicios-demo/
├── notificaciones/
│   ├── main.py  # Código del servicio de notificaciones
'''
# notificaciones/main.py
from fastapi import FastAPI

# Aquí estamos creando la aplicación FastAPI
app = FastAPI()

# Este es el endpoint donde recibo las notificaciones
@app.post("/notificar/")
async def recibir_notificacion(mensaje: str):
    # Imprimo el mensaje que recibo para verificar que todo funciona
    print(f"📢 Notificación recibida: {mensaje}")
    # Devuelvo una respuesta indicando que la notificación fue procesada
    return {"mensaje": "Notificación procesada"}

# Inspire
Aplicación de microservicios que maneja frases y notificaciones

Descripción del Proyecto

Este proyecto consiste en una aplicación de microservicios que maneja frases y notificaciones. Está compuesto por dos servicios principales: el servicio de frases y el servicio de notificaciones. Utilizamos FastAPI para crear los endpoints y SQLite para la gestión de bases de datos.

Estructura del Proyecto:

```
/microservicios-demo/
├── frases/
│   ├── main.py          # Servicio de frases
│   ├── database.py      # Conexión y creación de la base de datos de frases
├── notificaciones/
│   ├── main.py          # Servicio de notificaciones
├── usuarios/
│   ├── main.py          # Servicio de usuarios
│   ├── database.py      # Conexión y creación de la base de datos de usuarios
└── requirements.txt     # Dependencias del proyecto
```

Servicios

Servicio de Frases
Endpoint /frases/: Permite agregar nuevas frases a la base de datos.
Endpoint /frase-del-dia/{id_usuario}: Asigna una frase del día a un usuario y envía una notificación al servicio de notificaciones.

Servicio de Notificaciones
Endpoint /notificar/: Recibe notificaciones del servicio de frases y las imprime en la consola.

Instalación
1. Clona el repositorio.
2. Navega al directorio del proyecto.
3. Crea un entorno virtual y actívalo:

   python -m venv .venv
   source .venv/bin/activate  # En Windows usa .venv\Scripts\activate

4. Instala las dependencias

Ejecución de los Servicios
1. Servicio de Notificaciones:
Navega al directorio notificaciones y ejecuta: uvicorn main:app --reload --port 8004

Servicio de Frases:
Navega al directorio frases y ejecuta:   uvicorn main:app --reload --port 8003

Validación de los Servicios

Usar Postman o cURL para enviar solicitudes a los endpoints y verificar las respuestas.
Servicio de Frases:
Agregar una frase: Enviar una solicitud POST a http://localhost:8003/frases/ con un cuerpo JSON.
Obtener la frase del día: Enviar una solicitud POST a http://localhost:8003/frase-del-dia/1.

Servicio de Notificaciones:
Verificar la consola para ver las notificaciones recibidas.
Notas
Asegúrate de que ambos servicios estén corriendo antes de realizar las pruebas.
Verifica que los puertos estén configurados correctamente en las solicitudes.

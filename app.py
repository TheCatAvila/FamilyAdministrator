import os
from dotenv import load_dotenv
from app import create_app

# Cargar las variables de entorno desde .env
load_dotenv()

# Detectar si estamos en producción o desarrollo
env = os.getenv("FLASK_ENV", "development")  # Usa 'production' en producción

# Crear la aplicación con la configuración adecuada
app = create_app(config_name=env)

if __name__ == "__main__":
    app.run(debug=(env == "development"))

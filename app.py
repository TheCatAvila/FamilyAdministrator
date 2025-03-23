import os
from app import create_app

# Crear la aplicación con la configuración adecuada
app = create_app()

if __name__ == "__main__":
    app.run(debug=(True))

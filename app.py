import os
from app import create_app

# Crear la aplicación con la configuración adecuada
app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)

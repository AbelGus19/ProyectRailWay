import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hola Mundo</h1>'

if __name__ == '__main__':
    # Ejecuta la aplicación en 0.0.0.0 para que sea accesible desde fuera del contenedor
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
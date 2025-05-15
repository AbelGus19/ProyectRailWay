
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Comando para ejecutar la aplicación
CMD gunicorn --bind 0.0.0.0:$PORT main:app

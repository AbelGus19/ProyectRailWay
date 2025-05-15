# Hola Mundo para Railway

Un proyecto simple que muestra "Hola Mundo" usando Flask y Docker, preparado para desplegarse en Railway.

## Estructura del Proyecto

- `main.py` - La aplicación Flask
- `requirements.txt` - Dependencias de Python
- `Dockerfile` - Configuración para Docker

## Ejecución Local

1. Clonar el repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar: `python main.py`

## Despliegue en Railway

1. Crea una cuenta en Railway (https://railway.app/)
2. Conecta tu repositorio de GitHub o sube directamente estos archivos
3. Railway detectará automáticamente el Dockerfile y desplegará la aplicación

## Variables de Entorno

- `PORT` - Puerto en el que se ejecutará la aplicación (configurado automáticamente por Railway)
FROM python:3.12-slim


# Variables de Entorno 

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 


# Configurar el directorio de trabajo
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt /app/ 
RUN python -m pip install --no-cache-dir -r requirements.txt


# Copiar el código de Django
COPY . /app/ 


# Exponer el puerto 8000 para Django
EXPOSE 8000
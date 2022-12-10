FROM python:3.8

# Creamos un directorio para nuestro código
RUN mkdir -p /app

# Establecemos /app como nuestro directorio de trabajo
WORKDIR /app

# Copiamos todos los archivos del directorio actual al directorio de trabajo de Docker
COPY . /app/

# Instalamos las dependencias de nuestra aplicación
RUN pip install -r requirements.txt

# Exponemos el puerto 8000 para que podamos acceder a nuestra aplicación desde el exterior
EXPOSE 8000

# Ejecutamos el comando `python manage.py runserver` cuando el contenedor se inicie
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

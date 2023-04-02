# Imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copiar el contenido del directorio actual en el contenedor en /app
COPY . /app

# Instalar cualquier paquete necesario especificado en requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Haz que el puerto 5000 esté disponible para el mundo fuera de este contenedor
EXPOSE 5000

# Definir variable de entorno
ENV NAME OllivandersShop

# Ejecuta app.py cuando se inicie el contenedor
CMD ["python", "app.py"]

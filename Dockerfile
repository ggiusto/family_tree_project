# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Update system packages to minimize vulnerabilities
RUN apt-get update && \
	apt-get dist-upgrade -y && \
	apt-get upgrade -y && \
	apt-get autoremove -y && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, and wheel to latest versions
RUN pip install --upgrade pip setuptools wheel

# Install security updates and remove build dependencies after install
RUN apt-get update && \
	apt-get dist-upgrade -y && \
	apt-get upgrade -y && \
	apt-get autoremove -y && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

# Ensure all system packages are up-to-date to minimize vulnerabilities
RUN apt-get update && apt-get dist-upgrade -y && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usa tu aplicación
EXPOSE 8000

# Comando para ejecutar la app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

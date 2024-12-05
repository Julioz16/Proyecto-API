1. Ingresar al directorio del proyecto que contiene el Dockerfile desde Windows Powershell y construir la imagen Docker mediante el     
   siguiente comando:

   docker build -t mi-app-python .

2. Ejecutar el contenedor basado en la imagen mediante el siguiente comando:

   docker run -d -p 5000:5000 --name mi-contenedor-python mi-app-python
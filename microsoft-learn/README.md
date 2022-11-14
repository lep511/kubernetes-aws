# Extracción y ejecución de una aplicación de ejemplo de Docker Hub

1. Abra una ventana del símbolo del sistema en el equipo local.

2. Escriba el código siguiente para extraer la imagen de aplicación ASP.NET Sample del Registro de Docker Hub. Esta imagen contiene una aplicación web de ejemplo desarrollada por Microsoft y se basa en la plantilla de ASP.NET predeterminada disponible en Visual Studio. 

    >**docker pull mcr.microsoft.com/dotnet/samples:aspnetapp**

3. Escriba el código siguiente para comprobar que la imagen se ha almacenado localmente.

    >**docker images**

4. Escriba el código siguiente para iniciar la aplicación de ejemplo. La marca -d sirve para ejecutarla como una aplicación no interactiva en segundo plano. La marca -p es para asignar el puerto 80 en el contenedor que se crea al puerto 8080 localmente. Esta configuración está pensada para evitar conflictos con las aplicaciones web que ya se ejecutan en el equipo. El comando responderá con un identificador hexadecimal largo para la instancia.

    >**docker run -d -p 8080:80 mcr.microsoft.com/dotnet/samples:aspnetapp**

5. Abra un explorador web y escriba la dirección URL de la aplicación web de ejemplo http://localhost:8080. Debería ver una página con un aspecto similar al de la captura de pantalla siguiente.
<br><br>
![Imagen](https://learn.microsoft.com/es-mx/training/modules/intro-to-containers/media/3-sample-web-app.png)

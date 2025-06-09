# Proyecto de Sistemas Operativos – Sesión 1: ¡Al Contenedor!

## Escenario
Han sido contratados por **HotContainerz™**, una startup que quiere migrar su vieja aplicación monolítica a contenedores. Cuentan con un archivo de código fuente (`app.py`) junto con las librerías requeridas (`requirements.txt`), y su trabajo en este primer entregable consiste en contenerizar esta aplicación.

> Se necesita poder hacer cambios en el código sin reiniciar todo, y el mensaje de bienvenida en la página web debe cambiar según el entorno.

## Objetivos
- Crear un `Dockerfile` desde cero para la aplicación
- Crear un contenedor a partir del `Dockerfile`
- La aplicación debe:
  - Leer una variable de entorno desde el contenedor `WELCOME_MSG`  ---> Esto es lo que se mostrará en la página - ya la aplicación está configurada para esto
  - Montar el código local con volúmenes (para recarga en caliente). Es decir, el contenedor debe ser capaz de leer archivos desde el sistema de archivos local. Cualquier cambio en el código fuente debería reflejarse automáticamente en el contenedor sin crear uno nuevo (pero para probar esta funcionalidad, se debe correr el comando `flask run --reload` dentro del contenedor)
  - Ser accesible desde el host local en el puerto 5000

> NOTA: No deben modificar el código fuente de la aplicación - realmente no es necesario para este proyecto

- Pueden probar que funciona correctamente con el comando `curl` o directamente desde el navegador.

## Archivos proporcionados
- `app.py`
- `requirements.txt`

## Entregables
- `Dockerfile`
- Comando(s) de construcción y ejecución
- Evidencia de que la aplicación responde correctamente (pantallazo o curl)
- Subir un archivo en formato .zip que contenga las evidencias recopiladas

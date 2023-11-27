# Prueba técnica Rocketify

## Descripción

Este programa realiza la descarga de los datos de la base de datos en MongoDB con el filtro de estos por completado o devuelto, realiza una agrupación por meses y año y con esta información realiza un informe separand por mes los usuarios que tienen más de 3 estados en sus envíos.

Al no tener claridad sobre qué mes o rango de meses realizar el filtro (por ejemplo, més actual, ultimos 3 meses, etc) se realizó una extracción completa de datos.

Funciona de forma manual, no se implementó ejecución automática ni notificaciones por correo o bd.

## Instrucciones de ejecución

### Cargar la BD

Se debe realizar el cargue de información en una base de datos de MongoDB, para este caso se usó MongoDB Compass para importar el archivo csv a la base de datos.

### Descargar el proyecto

Descargar el proyecto en la ruta que desee el usuario y descargar las librerías necesarias usando el comando "Pip install".

### Ejecutar el proyecto

Se debe ejecutar el archivo main.py para que el programa empiece a funcionar, el programa buscara en la base de datos los registros necesarios, los procesará y al final los agregará en un archivo de texto llamado reporte.txt que estará ubicado en la carpeta "sources".
La ejecucion tiene un aproximado de 10 minutos
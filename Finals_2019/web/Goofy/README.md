# Goofy - HackDef Finals 2019 (200 pts)
By [**@nogagmx**](https://twitter.com/nogagmx)

> **Descripción:** *Con las credenciales robadas del tarjetahabiente jperez y la capacidad de generar tokens validos, accesa la cuenta de dicho usuario en el portal bancario y trata de encontrar una vulnerabilidad Web que te permita leerinformacion en otro puerto dentro del mismo servidor, esto te dara la flag y la ruta para descargar un archivo muy sensible!* 

> **http://localhost:8002/login.php**

### Instalación del reto:
~~~
1. Ejecutar el archivo setup.sh
  ./setup.sh

Happy Hacking! :)
~~~

### Writeup:
* http://hack-defender-mx.blogspot.com/2019/10/goofy-web-200.html

**NOTA**
* Si existe un problema de conexión con la base de datos, verificar la IP asignada por docker con el siguiente comando
  **`docker inspect goofy_db_1 | grep IPAddress`**

* Escribirla en el archivo **`config.php`** en la variable **`DB_SERVER`**, refrescar la pestaña del browser y listo!!

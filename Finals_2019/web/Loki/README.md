# Loki - HackDef Finals 2019 (100 pts)
By [**@nogagmx**](https://twitter.com/nogagmx)

> **Descripción:** *Este es el sitio web del Banco CaptureBank que tienes que comprometer, trata  
de encontrar una vulnerabilidad en su página de Acceso a tarjetahabientes y  
encuentra el password (que sera la flag) del usuario: jperez. Formato de la flag hackdef{..}* 

> **http://localhost:8001/login.php**

### Instalación del reto:
~~~
1. Inicializar los contendores
   docker-compose up -d

Happy Hacking! :)
~~~

### Writeup:
* http://hack-defender-mx.blogspot.com/2019/10/loki-web-100-blind-sql-injection.html

### NOTA

* Si existe un problema de conexión con la base de datos, verificar la IP asignada por docker con el siguiente comando
  **`docker inspect gophy_db_1 | grep IPAddress`**

* Escribirla en el archivo **`config.php`** en la variable **`DB_SERVER`** , refrescar la pestaña del browser y listo!!

### Otros Recursos
 * [Instalación Docker Compose](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04)

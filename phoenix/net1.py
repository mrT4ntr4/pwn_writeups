from pwn import *
import warnings
warnings.filterwarnings("ignore")


challenge_name = "net-one"

shell = ssh('user','localhost',port=2222,password='user')
conn = shell.process('/opt/phoenix/i486/{}'.format(challenge_name))
conn.recvuntil('\n')
num=u32(conn.recv(4))
print num
conn.sendline(str(num))
conn.interactive()
conn.close()
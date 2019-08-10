from pwn import *
import warnings
warnings.filterwarnings("ignore")


challenge_name = "net-zero"

shell = ssh('user','localhost',port=2222,password='user')
conn = shell.process('/opt/phoenix/i486/{}'.format(challenge_name))
line=conn.recvlines(2)
num = line[1].split()[2].strip("'")
print num
query = p32(int(num))
conn.sendline(str(query))
conn.interactive()
conn.close()
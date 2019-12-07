import os

#python
#run as root

#adduser level1-level4
os.system("adduser --disabled-login  --home /home/pwn/level1 --uid 4001 --gecos ''  level1")

#level file setting
os.system("cp ./prov/bof1 /home/pwn/level1/")
f = open("./prov/bof1.c","r")
data = f.read()
f.close()
data.replace("Network_security_is_So_Fun!","???")
f = open("./prov/bof1.c","w")
f.write(data)
f.close()
os.system("cp ./prov/bof1.c /home/pwn/level1/")
os.system("chown :level1 /home/pwn/level1/bof1;chmod 111 /home/pwn/level1/bof1")

#install xinetd
os.system("apt-get install xinetd -y")
#move level
os.system("cp ./xinetd_files/level1 /etc/xinetd.d/level1")
os.system("service xinetd restart")

#enable local service
os.system('echo "level1 4001/tcp" >> /etc/services')

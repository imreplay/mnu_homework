import os

#python
#run as root

#adduser level1-level4
for i in range(1,5):
    os.system("adduser --disabled-login  --home /home/pwn/level{} --uid 400{} --gecos ''  level{}".format(i,i,i))

#level file setting
os.system("cp ./prov/bof1* /home/pwn/level1/")
os.system("chown :level1 /home/pwn/level1/bof1;chmod 111 /home/pwn/level1/bof1")

#install xinetd
os.system("apt-get install xinetd -y")
#move level
os.system("cp ./xinetd_files/level1 /etc/xinetd.d/level1")

#enable local service
os.system('echo "level1 4001/tcp" >> /etc/services')

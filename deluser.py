import os
for i in range(4001,4005):
    os.system("deluser --remove-home level{}".format(i-4000))

os.system("sed -ie '$d' /etc/services)

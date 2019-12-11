import os
os.system("deluser --remove-home level1")

os.system("sed -ie '$d' /etc/services")

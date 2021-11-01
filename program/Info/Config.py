import os
import json
from urllib.request import build_opener, urlopen
import urllib
from program.depend.ErrorList import *
from program.depend.color import *

monIP = ""
monOS = ""

def config():

	global monIP
	global monOS

	with open('./program/Info/config.json', 'r') as config_json:
		try:
			monIP = json.load(config_json['monIP'])
			monOS = json.load(config_json['monOS'])
		except:
			print(f"{bcolors.FAIL}Error")

	print(f"{bcolors.WARNING}")

	try :
        # IPV 4 ou IPV6 automatique
        	ipPub = urlopen('https://ipv4v6.lafibre.info/ip.php').read()
        	print("Adresse IP publique :", ipPub.decode('ascii'))
        	print("Protocole IP : IPv%d" % (6 if b':' in ipPub else 4))

        #IPV4 seulement
        	ipPub = urlopen('https://ipv4.lafibre.info/ip.php').read()
        	print("Adresse IP publique :", ipPub.decode('ascii'))
        	print("Protocole IP : IPv4" )

	except :
        	print('Pour l\'adresse publique se connecter à https://ip.lafibre.info/')
        	pass

	print("IP : ",monIP)
	print("Operating System : ", monOS)
	print(f"{bcolors.ENDC}")
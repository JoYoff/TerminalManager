import os
import socket
import sys
import socket                                                # pour les sockets
from urllib.request import build_opener, urlopen
import urllib

from program.FileManager.CreateFile import *
from program.ping import *

os.system("clear")

# Init
monIP = socket.gethostbyname(socket.gethostname())  # récupère l'adresse IP locale de la machine (de type '0.0.0.0')
monOS = sys.platform

urllib.request.urlcleanup()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

list_command = ["help", "ping"]

# Def List

    # Supprime un fichier

def removeFile():

    name = input("Donnez le nom du fichier à supprimer : ")
    os.system('rm ' + name)
    print(f"{bcolors.OKBLUE}" + name + ' à bien été supprimé')


    # Help

def help():
    print("")
    print(f"{bcolors.HEADER}\t\t\t############ Help ############")
    print("")
    print("\tconfig --> Permet d'avoir des informations système")
    print("\texit --> Permet de quitté le programme")
    print("\tping --> Permet d'avoir des information à partir d'une IP / d'un nom de domaine")
    print("\tclear --> Permet de d'éffacé les messages de la console")
    print("")

    print("\n\t\t--- Gestion de Fichiers ---\n")
    print("\tls --> Permet d'afficher les fichiers dans le dossier ciblé")
    print("\tcr --> Permet de crée un fichier")
    print("\trm --> Permet de supprimer un fichier")

    print("\n\t\t--- Démarrage de programme ---\n")
    print("\tstart --> Permet de lancé une application / script listé dans PiManager [INDISPONIBLE]")
    print(f"{bcolors.ENDC}")

# Program

while True:
    ask = input(f"{bcolors.OKGREEN}TerminalManager : {bcolors.ENDC}") # PiManager Start Terminal

    if ask == "config":
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


        # Commandes

    if ask == "ping":
        ask = input('Quelle machine / domaine ? ')
        pingPy(ask)

    '''#if ask == "start":
        start_program()'''
    
    if ask == "clear":
        os.system("clear")
    
    if ask == "help":
        help()
    
    if ask == "ls":
        os.system("ls")
    
    if ask == "cd":
        file_directory = (input("Whats directory ? "))
        os.system("cd " + file_directory)

    if ask == "cr":
        createFile()

    if ask == "rm":
        removeFIle()

    if ask == "exit":
        exit()
    
    #else:
    #    print(f"{bcolors.WARNING}Commande inexistante")
    #    print(list_command)
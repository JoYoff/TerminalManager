import os
import socket
import sys
import socket                                                # pour les sockets
from urllib.request import build_opener, urlopen
import urllib
import json

from program.FileManager.CreateFile import *
from program.FileManager.RemoveFile import *
from program.Info.Config import *
from program.ping import *

os.system("clear")

with open('./json/list_command.json') as cmd_json:
    pass

# Init
monIP = socket.gethostbyname(socket.gethostname())  # récupère l'adresse IP locale de la machine (de type '0.0.0.0')
monOS = sys.platform

config_for_json = {
        "monIP": str(monIP), 
        "monOS": str(monOS)
    }

with open('./program/Info/config.json', 'w') as config_json:
    try:
        json.dumps(config_for_json)
    except:
        print(f"{bcolors.FAIL}Error : cant write")

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

        # Commandes
    if ask == "config":
        config()

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
        removeFile()

    if ask == "exit":
        exit()
    
    #else:
    #    print(f"{bcolors.WARNING}Commande inexistante")
    #    print(list_command)
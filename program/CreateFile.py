import os
from  program.depend.ErrorList import *

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

    # Crée un fichier
def createFile():
    name = input("Donnez un nom au fichier (avec une extenssion par exemple .py) : ")

    if name != "":
        os.system("touch " + str(name) + " : ")
        print(f"{bcolors.OKBLUE}" + name + ' à bien été crée')
    
    else:
        fail_error('Aucun nom n\'a été donné au fichier')
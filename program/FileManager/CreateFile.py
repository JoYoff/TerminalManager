import os
from program.depend.ErrorList import *

    # Crée un fichier
def createFile():
    name = input("Donnez un nom au fichier (avec une extenssion par exemple .py) : ")

    if name != "":
        os.system("touch " + str(name) + " : ")
        print(f"{bcolors.OKBLUE}" + name + ' à bien été crée')
    
    else:
        fail_error('Aucun nom n\'a été donné au fichier')
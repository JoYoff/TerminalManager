import os
from program.depend.ErrorList import *

def removeFile():
	name = input("Donnez le nom du fichier à supprimer : ")
	os.system('rm ' + name)
	print(f"{bcolors.OKBLUE}" + name + ' à bien été supprimé')
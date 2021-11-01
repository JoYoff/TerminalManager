import os
import socket
import sys
import socket                                                # pour les sockets
from urllib.request import build_opener, urlopen


monIP = socket.gethostbyname(socket.gethostname())  # récupère l'adresse IP locale de la machine (de type '0.0.0.0')
monOS = sys.platform

    # Ping
def pingPy(adrIP) :
    option = '-c 2 ' # nbre de requètes pour linux
    if monOS == 'win32' :
        option = '-n 2 ' # nbre de requètes pour windows

    reponse = os.system('ping ' + option + adrIP) # lance une commande ping
    print("")
    print('Réponse', reponse)
    print("")
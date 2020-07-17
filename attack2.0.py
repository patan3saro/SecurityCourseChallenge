import base64
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import threading
import bs4
import pyDes
import italian_dictionary

#import ftplib
 
# Lista dei caratteri possibili in una password.
listaCaratteri = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
"R", "S", "T", "U", "V", "W", "X", "Y", "Z", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
  'z','0','1','2','3','4','5','6','7','8','9']
 
# Funzione che verifica se la password passata come parametro
# e' quella corretta e di conseguenza e' stata indovinata.
def testaPassword(password):
    f2 = open("C:\\Users\\Utente\\Desktop\\660000_parole_italiane.txt","r")
    paroleitaliane = f2.readlines()
    f2.close()
        
    key = pyDes.des(bytes(password, encoding= 'utf-8'))
    cipher_text = base64.b64decode("dpi4c+NIZxM=")
    plain_text = key.decrypt(cipher_text)
         #siccome decode non può codificare tutto posso 
         #evitare di controllare nella lista dizionario risparmiando tempo
         #usando proprio il fatto che genera un errore
    try:
        #text=plain_text.decode('utf-8')+'\n'
        try:
            definizione=italian_dictionary.get_only_definition('anatra',limit=None)
            print (definizione)
            for elemento in definizione:
                 print (elemento)
        except italian_dictionary.exceptions.WordNotFoundError:
            i=0
            
    except UnicodeDecodeError:
          i=0


for c1 in listaCaratteri:
    for c2 in listaCaratteri:
        for c3 in listaCaratteri:
            for c4 in listaCaratteri:
            
                for c5 in listaCaratteri:
                  
                    for c6 in listaCaratteri:
                        
                        for c7 in listaCaratteri:
                           
                            for c8 in listaCaratteri:
                                psw = c1+c2+c3+c4+c5+c6+c7+c8
                                testaPassword(psw)
                                                
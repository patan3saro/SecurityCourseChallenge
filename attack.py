import base64
import bs4
import pyDes
import italian_dictionary
#prendo il contenuto dal file e lo 
# metto in una lista da poter iterare  per non accedere troppe volte al file
f = open("C:\\Users\\Utente\\Desktop\\Top353Million-probable-v2.txt.005.txt.001.txt","r",errors='ignore')
content = f.readlines()
print ("Parole da testare: "+str(len(content)))
f.close()
#print(content)
#devo eliminare il \n e lo faccio sono per le stringhe 9 
#  caratteri cosi' non lo faccio per le stringhe per cui non serve
f2 = open("C:\\Users\\Utente\\Desktop\\parole_8caratteri_plus.txt","r")
paroleitaliane = f2.readlines()
f2.close()
j=0
for var in content:
    if(len(var)==9):
       # j=(j+1)
        #print(j)
        if(len(bytes(var[0:8], encoding= 'utf-8'))==8):#verifico la lunghezza in 
            #byte perchè ci sono caratteri codificati con più di un byte
         key = pyDes.des(bytes(var[0:8], encoding= 'utf-8'))
         cipher_text = base64.b64decode("dpi4c+NIZxM=")
         plain_text = key.decrypt(cipher_text)
         #siccome decode non può codificare tutto posso 
         #evitare di controllare nella lista dizionario risparmiando tempo
         #usando proprio il fatto che genera un errore
         try:
            text=plain_text.decode('utf-8')+'\n'
            if(text in paroleitaliane):
                print ('chiave:'+var)#uso var perchè nella ricerca il \n e' compreso
                print('plain_text:'+text)
                break
         except UnicodeDecodeError:
          i=0

         
         
        
         #print (base64.b64encode(plain_text))
         #try:
          #soup = BeautifulSoup(var[0:8], "html5lib")
           #  definizione=italian_dictionary.get_only_definition(var[0:8],limit=None)
            # print (definizione)
             #for elemento in definizione:
              #   print (elemento)
        # except italian_dictionary.exceptions.WordNotFoundError:
         #    print("Parola non trovata")
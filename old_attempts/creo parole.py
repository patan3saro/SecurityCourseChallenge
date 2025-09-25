f = open("C:\\Users\\Utente\\Desktop\\660000_parole_italiane.txt","r",errors='ignore')
content = f.readlines()
parole=['']
for var in content:
    if(len(var)==9):
        parole.append(var)
f=open("C:\\Users\\Utente\\Desktop\\parole_8caratteri_plus.txt","w",errors='ignore')
f.writelines(parole)
f.close()

#Demanem el nom a l'usuari i també la seva edat
nom = input("Digues el teu nom: ")
edat = input("Digues la teva edat: ")

if nom == "" or edat == "": #si falta nom o edat
    print("No has completat tota la informació solicitada!")
else: #si no, vol dir que tenim totes les dades
    print("Hola "+nom) #el saludem
    edat = int(edat) #transformem la variable edat a un valor enter per a poder comparar amb el valor 18
    if edat >= 18: #si l'edat és mes gran o igual que 18
        print("Ets major d'edat")
    else: #si no...
        print("Ets menor d'edat")

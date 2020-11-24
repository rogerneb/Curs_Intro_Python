'''
PASSWORD GENERATOR V1.0
Exercici de resum per a consolidar coneixements.

És un generador de contrasenyes.
L'usuari introdueix el núm de minúscules, manjúscules, números i caràcters especials
i l'script li genera el nombre de contrasenyes que demani
'''

import random #importem la llibreria per crear números random

#contrasenya
password = ""
password_print = "" #contrasenya que imprimirem per pantalla

#cadenes de caracters
minus = "abcdefghijkmnopqrstuvwxyz" #despreciem la l pq es pot confondre amb la I majuscula
mayus = "ABCDEFGHJKLMNOPQRSTUVWXYZ" #despreciem la I pq es pot confondre amb la l minuscula
special = "!¡?¿()$%&"

#variables de la contrasenya
qminus = 0 #quantes minuscules volem
qmayus = 0 #quantes mayusvolem
qnums = 0 #quants nums volem
qspecial = 0 #quants caràcters especials volem

print("Benvingut al PASSWORD GENERATOR V1.0: ")
print("A continuació has de definir el número de caràcters de la contrasenya.")

#Demanem les minúscules
while qminus < 1 or qminus > 10: #mínim 1 màxim 10
    qminus = int(input("Minúscules: "))
    if (qminus > 10):
        print("Màxim 10 caràcters.")
    elif(qminus <= 0):
        print("Mínim 1 caràcter.")

#Demanem les majúscules
while qmayus < 1 or qmayus > 10: #mínim 1 màxim 10
    qmayus = int(input("Majúscules: "))
    if (qmayus > 10):
        print("Màxim 10 caràcters.")
    elif(qmayus <= 0):
        print("Mínim 1 caràcter.")

#Demanem els nums
while qnums < 1 or qnums > 10: #mínim 1 màxim 10
    qnums = int(input("Números: "))
    if (qnums > 10):
        print("Màxim 10 números")
    elif(qnums <= 0):
        print("Mínim 1 número")

#Demanem els caràcters especials
while qspecial < 1 or qspecial > 10: #mínim 1 màxim 10
    qspecial = int(input("Caràcters especials: "))
    if (qspecial > 10):
        print("Màxim 10 caràcters.")
    elif(qspecial <= 0):
        print("Mínim 1 caràcter.")



#COMENCEM A GENERAR LA CONTRASENYA
caracterscontrasenya = qminus+qmayus+qspecial+qnums #comptem el num total de caràcters
print("La contrasenya serà de "+str(caracterscontrasenya)+" caràcters.")

#quantitat de passowords a generar
qpasswords = int(input("Indica quantes contrasenyes vols generar (max 1000): "))

if qpasswords > 1000: #si l'user posa més de 1000, assignem 1000
    qpasswords = 1000
elif qpasswords < 1: #si l'user posa menys de 1, assignem 1
    qpasswords = 1

'''
per fer randoms utilitzem:
int(numero_maxim * random.random() + numero_minim)
'''

for m in range (0, qpasswords): #generem tantes contrasenyes com s'han demanat
    #minúscules
    for n in range (0, qminus): #des de 0 fins al total de minuscules solicitades
        password = password + minus[int(len(minus) * random.random())] #concatenem posicions random de la cadena de minuscules
    #majuscules
    for n in range (0, qmayus): #des de 0 fins al total de majuscules solicitades
        password = password + mayus[int(len(mayus) * random.random())] #concatenem posicions random de la cadena de majuscules
        #majuscules
    for n in range (0, qnums): #des de 0 fins al total de nums solicitats. Nums entre 0 i 9
        password = password + str(int(9 * random.random())) #concatenem posicions random de la cadena de majuscules
    #especials
    for n in range (0, qspecial): #des de 0 fins al total d'escpecials solicitats
        password = password + special[int(len(special) * random.random())] #concatenem posicions random de la cadena d'especials

    #barregem les lletres de la contrasenya generada
    password = list(password) #transformem la cadena en llista per randomitzar-la
    random.shuffle(password) #la randomitzem

    #concatenem la llista en una cadena
    for caracter in password:
        password_print = password_print+caracter

    print(password_print)  #imprimim la contrasenya
    password = "" #netegem la variable password (cadena buida)
    password_print = "" #netegem la variable password_print (cadena buida)

input("Programa acabat.")

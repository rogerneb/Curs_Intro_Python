import random #importem la llibreria per crear números random

user_num = "" #el num que introduirà l'usuari
num_rand = int(10 * random.random() + 1) #el numero generat entre 1 i 10
intents = 0 #aquí vaig guardant el número d'intents
print(num_rand) #l'imprimeixo per comprovar el que ha pensat.

print("Digues el numero que estic pensant (entre 1 i 10).")

while user_num != num_rand: #mentre no endevinem el número...
	user_num = int(input("Digues el num >> ")) #demanem el num

	if (user_num > num_rand): #el numero aleatori és més petit
		print("Es mes petit")
	elif (user_num < num_rand): #el num aleatori és més gran
		print("Es mes gran")
	else: #l'hem endevinat
		print("Bingo")
	intents += 1 #sumem 1 als intents
else: #els while també poden tenir else.
	print("Has necessitat "+str(intents)+" intents") #mostrem els intents

#puc utilitzar la funció str() per convertir els ints a enter i concatenar millor la variable amb el text.

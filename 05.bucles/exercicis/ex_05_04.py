acumulat = 0 #variable en la que anem acumulant.

while acumulat < 100: #mentre sigui més petit que 100
	num = int(input("num >>")) #demanem el num a sumar
	acumulat = acumulat + num #l'acumulem
	print("Acumulat:",acumulat) #el mostrem

print("Ja has arribat o passat dels 100.")

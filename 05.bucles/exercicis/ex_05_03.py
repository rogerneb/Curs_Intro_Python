import random #importem la llibreria per crear números random

num = 0 #num actual
pas = 0 #de quants en quants anirem
max = 0	#num més gran
min = 0 #num més petit

#Demanem el max i el min
while (max < min or max == min):
	min = int(input("Min: "))
	max = int(input("Max: "))
	if (max<min): #si el max es més petit que el min
		print("No és vàlid. El min ha de ser més petit que el max.")
	elif (max == min): #si son iguals
		print("No és valid. Has posat els mateixos nums")

#demanem el pas
while (pas == 0 or pas > max):
	pas = int(input("Pas: "))
	if (pas>max): #si el pas es més gran que el num max
		print("No és vàlid. El pas no pot ser més gran que el max")
	elif (pas == 0): #si el pas és 0
		print("No és valid. El pas no pot ser zero!")

#comptem
while (min <= max):
	print(min)
	min += pas

input("\nPress ENTER")

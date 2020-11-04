#Demanem dos numeros enters al usuari
x = int(input("x: "))
y = int(input("y: "))

### CONDICIONALS AMB OPERADORS LÒGICS ###
#Comprovarem que les dos variables tenen o no valor igual o superior a 5
if x >= 5 and y >= 5: #X i Y son iguals o superiors a 5
    print("X i Y son igual o superior a 5.")
elif x >= 5 or y >= 5: #o una o l'altre. No les dos ni tampoc cap d'elles
    print("Una de les dos és igual o superior a 5.")
elif not(x >= 5 and y >= 5): #es igual que la primera condició pero la invertim amb el not
    print("Ni X ni Y son igual o superior a 5.")

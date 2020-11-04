#Demanem dos numeros enters al usuari
x = int(input("x: "))
y = int(input("y: "))

### CONDICIONALS ###
#Ara comprovarem quin dels dos numeros és més gran
if x > y: #Si la x és més gran que la y
    print("La x és més gran.")
elif x < y: #si no, si la x és més petita que la y
    print("La y és més gran.")
else: #si no és més gran ni més petita es que son iguals.
    print("Son iguals.")

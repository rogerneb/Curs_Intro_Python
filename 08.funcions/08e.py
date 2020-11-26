#Retornant true o false
def verdader_o_fals(nota): #definim la funció i els seus arguments
    if nota >= 5: #si la nota és igual o superior a 5 retornem verdader
        return True
    else: #si no retornem fals
        return False

nota_alumne = int(input("Quina nota has tret?: ")) #recollim el valor de l'usuari pasat a enter

if (verdader_o_fals(nota_alumne) == True): #si la funció retorna verdader ha aprovat
    print("Has aprovat!")
else: #si no, ha suspès
    print("Ups! Has suspès!")

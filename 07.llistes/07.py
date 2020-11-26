'''
llistes
Les llistes serveixen principalment per guardar varis valors
en una sola variable
'''

#definim una llista
dies = ["Lunes","dimarts", "dimecres", "dijous", "divendres", "dissabte"]

print (dies) #imprimim la llista
print (dies[2]) #o una posició concreta de la llista. dimecres
print (dies[-1]) #podem usar negatius. dissabte

dies[0] = "dilluns" #podem canviar el valor d'un element

#podem quedar-nos amb nomes una part
print(dies[2:4])

#algunes funcions i mètodes
#len: retorna la longitud de la llista
print(len(dies))

#insert: inserir un element en la posició que vulgeum
dies.insert(6,"diumenge")

#append: afegeix l'element en l'última posició
dies.append("dilluns un altre cop")

#pop: eliminem l'ultim element
dies.pop()

#sort: ordenem la llista alfabeticament
dies.sort()

#reverse: inverteix l'ordre
dies.reverse()


#recorre una llista amb un for
for dia in dies:
    print(dia)
'''
Pots trobar molts més exemples aquí:
https://likegeeks.com/python-list-functions/
'''

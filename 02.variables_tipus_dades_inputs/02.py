#Variables, tipus de dades simples i inputs
a = 7 #enter
print("Enter: ",a)

b = 9.85 #flotant
print("Flotant: ",b)

d = True #boleà true
e = False #boleà false
f = 3 > 10 #boleà false
print("Booleans: ",d,e,f)

#Cadenes de text.
g = "Estic programant en Python!"
print("La cadena és: ",g)
#podem partir les cadenes com si fos una llista. En parlarem més endavant de les llistes
print("La tercera lletra de la cadena és: ",g[2]) #posició 2 de la cadena

#podem imprimir un tros de la cadena usant el format posició inicial:final.
print(g[7:11]) #posició 7 i posició 11 no inclòses.

#Amb input podem demanar dades al usuari
text = input("Digues alguna cosa: ")
print(text)

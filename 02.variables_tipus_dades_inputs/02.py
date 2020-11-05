#Variables, tipus de dades simples i inputs
a = 7 #enter
print("Enter: ",a)

b = 9.85 #flotant
print("Flotant: ",b)

c = True #boleà true
d = False #boleà false
e = 3 > 10 #boleà false
print("Booleans: ",c,d,e)

#Cadenes de text.
f = "Estic programant en Python!"
print("La cadena és: "+f) #concatenem cadenes amb +
#podem partir les cadenes com si fos una llista. En parlarem més endavant de les llistes
print("La tercera lletra de la cadena és: "+g[2]) #posició 2 de la cadena

#podem imprimir un tros de la cadena usant el format posició inicial:final.
print(g[0:8]) #posició 8 no inclòsa.

#Amb input podem demanar dades al usuari
text = input("Digues alguna cosa: ")
print(text)

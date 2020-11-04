#demanem 2 enters
a = int(input("a: "))
b = int(input("b: "))

#per saber si un nombre es parell només hem de comprovar si al dividir entre 2 el mòdul és 0
#comprovem si a és parell o imparell
if a%2 == 0:
    print("a és parell.")
else:
    print("a és imparell.")

#comprovem si b és parell o imparell
if b%2 == 0:
    print("b és parell.")
else:
    print("b és imparell.")

#comprovem quin és el més gran
if a>b:
    print("a és més gran que b.")
elif b>a:
    print("b és més gran que a.")
else:
    print("a i b son el mateix nombre.")

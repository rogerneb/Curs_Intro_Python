#demanem 3 enters
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a+b+c >= 10: #si la suma és més gran o igual a 10
    print("Enhorabona")
elif a+b+c >= 5 and a+b+c < 10: #si la suma és més gran o igual a 5 i al mateix temps més petit de 10
    print("Ok!")
else: #si no, vol dir que és més petit de 5
    print("Oh no!")

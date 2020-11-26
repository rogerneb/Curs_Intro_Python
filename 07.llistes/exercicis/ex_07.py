exemple = ["Lorem","Ipsum","Dolor","Sit"]

print(exemple)

print(len(exemple))

a = exemple[1:3]
print(a)

exemple.insert(3, "Hola!")
print(exemple)

exemple.append("Hey!")
print(exemple)

exemple.sort()
print(exemple)

exemple.reverse()
print(exemple)

a = exemple.index("Ipsum")
print(a)

exemple.pop()
print(exemple)

exemple.remove("Ipsum")
print(exemple)

input("Press ENTER")
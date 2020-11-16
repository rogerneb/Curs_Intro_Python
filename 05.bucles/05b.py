#tenim una variable resposta que val una cadena buida
resposta = ""

# BUCLE WHILE
#mentre la resposta no sigui  n, N, y o Y anirem demanant que escrigui
while resposta != "n" and resposta != "N" and resposta != "y" and resposta != "Y":
  resposta = input("Escriu si o no [Y/N] ")


#l'usuari ja ha escrit que si o que no i simplement li diem què ha escollit.
if resposta == "n" or resposta == "N":
    print("Has dit que no.")
else:
    print("Has dit que sí.")

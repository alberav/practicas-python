import re

s = input("Dame un nombre: ")
while not(re.search("salir", s)):
    if (re.search("pepe", s)):
        print("Acertaste!")
        s = "salir"
    else:
        s = input("Prueba otra vez: ")

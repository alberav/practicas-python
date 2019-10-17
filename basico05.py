import re

s = "Hola mundo"
espacio  = s.count(' ')
caracter = re.findall("([A-Z]|[a-z])", s)

print("Cantidad de carácteres", len(caracter),"y de espacios",espacio)


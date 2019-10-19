import re

email = input("Dirección de correo: ")
#x = re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)


if(re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$)", email)):
    print("Email correcto")
else:
    print("Email incorrecto")


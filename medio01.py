import re


def compruebaEmail(email):
    if(re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$)", email)):
        return print("Email correcto")
    else:
        return print("Email incorrecto")


def compruebaDNI(dni):

    # NIE
    # re.search("^[XxYyZz]{1}\d{7}[a-zA-Z]{1}$", dni)

    letras = ("T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X",
              "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E")

    comprueba = re.search("^\d{8}[a-zA-Z]{1}$", dni)

    if(comprueba):
        numeroDNI = (int)(dni[0:8])
        letraDNI = dni[8]
        if(letraDNI.upper() == letras[numeroDNI % 23]):
            return print("DNI correcto")
        elif(letraDNI.upper() != letras[numeroDNI % 23]):
            return print("Letra incorrecta")
    else:
        return print("DNI incorrecto")


email = input("Dirección de correo: ")
dni = input("Introduce DNI: ")
compruebaEmail(email)
compruebaDNI(dni)

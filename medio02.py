import math


def calculaCubo(base):
    volumen = base * base * base
    return volumen


def calculaEsfera(radio):
    volumen = 4/3 * math.pi * radio**3
    return volumen


def calculaCilindro(altura, radio):
    volumen = altura * math.pi * radio**2
    return volumen


base = int(input("base del cubo: "))
volumenCubo = calculaCubo(base)
print("El volumen del cubo es:", volumenCubo)

radio = int(input("radio de la esfera: "))
volumenEsfera = calculaEsfera(radio)
print("El volumen de la esfera es:", round(volumenEsfera,2))

altura = int(input("altura del cilindro: "))
radio = radio = int(input("radio del cilindro: "))
volumenCilindro = calculaCilindro(altura, base)
print("El volumen del cilindro es:", round(volumenCilindro,2))
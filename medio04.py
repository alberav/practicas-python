import csv

while True:
    numero = input('Numero: ')
    nombre_completo = input("Nombre completo: ")
    edad = input("Edad: ")
    with open('file.csv', 'a') as fichero:
        w = csv.writer(fichero, csv.QUOTE_ALL)
        w.writerow([numero, nombre_completo, edad])

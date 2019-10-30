import re


def calculadora():
    string = input("Introduce la operación: ")
    match = re.search("([0-9]+)( )?([+-/*x])( )?([0-9]+)", string)
    if (match):
        print("Operacion reconocida")
        if ((match.group(3)) == '+'):
            resultado = int(match.group(1)) + int(match.group(5))
            print(match.group(1), match.group(3),
                  match.group(5), '=',  resultado)
        elif ((match.group(3)) == '-'):
            resultado = int(match.group(1)) - int(match.group(5))
            print(match.group(1), match.group(3),
                  match.group(5), '=',  resultado)
        elif ((match.group(3)) == '*' or (match.group(3)) == 'x'):
            resultado = int(match.group(1)) * int(match.group(5))
            print(match.group(1), match.group(3),
                  match.group(5), '=',  resultado)
        elif ((match.group(3)) == '/'):
            try:
                resultado = int(match.group(1)) / int(match.group(5))
            except:
                print("---- ERROR: El divisor no puede ser 0 ----")
                calculadora()
            finally:
                print(match.group(1), match.group(3), match.group(5), '=',  resultado)
    else:
        print("operacion no reconocida")

calculadora()
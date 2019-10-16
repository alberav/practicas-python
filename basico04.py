nombres = ["Maria", "Julia", "Ana", "Miguel", "Pepe", "Popeye"]
print("Tengo " ,(len(nombres)), " nombres en mi lista")
print("Que nombre quieres?")
x = int(input())
print("Has escogido el numero",x, "que es",nombres[x-1])
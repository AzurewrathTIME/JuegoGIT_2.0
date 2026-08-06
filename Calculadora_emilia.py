print("Bienvenido a la Multi-suma Emilia, Hola soy Emilia y soy TRANSportable porfavor\n")

def multi (num1, num2):
        suma=0
        for i in range (num1):
                suma=suma+num2
        return suma

verdin = int(input("ingrese el numero 1: "))
emilia = int(input("Ingrese el numero 2: "))

print(f"El resultado de la multiplicacion es: {multi(verdin, emilia)}")
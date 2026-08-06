from math import pi

opcion = input(
    "Introduce una figura geométrica:\n"
    "1) Círculo\n"
    "2) Cuadrado\n"
    "3) Triángulo\n"
    "4) Rectángulo\n> "
)

def circulo(radio):
    return pi * radio**2, 2 * pi * radio

def cuadrado(lado):
    return lado * lado, lado * 4

def triangulo(base, altura, lado1, lado2, lado3):
    return (base * altura) / 2, lado1 + lado2 + lado3

def rectangulo(base, altura):
    return base * altura, 2 * base + 2 * altura

if opcion == "1":
    radio = float(input("Introduce el radio: "))
    area, perimetro = circulo(radio)
    print(f"El área es {area}, el perímetro es {perimetro}")

elif opcion == "2":
    lado = float(input("Introduce el lado: "))
    area, perimetro = cuadrado(lado)
    print(f"El área es {area}, el perímetro es {perimetro}")

elif opcion == "3":
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    lado1 = float(input("Introduce el lado 1: "))
    lado2 = float(input("Introduce el lado 2: "))
    lado3 = float(input("Introduce el lado 3: "))

    area, perimetro = triangulo(base, altura, lado1, lado2, lado3)
    print(f"El área es {area}, el perímetro es {perimetro}")

elif opcion == "4":
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))

    area, perimetro = rectangulo(base, altura)
    print(f"El área es {area}, el perímetro es {perimetro}")

else:
    print("Opción no válida")
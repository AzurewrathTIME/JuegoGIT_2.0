import numpy as np

def suma(matriz1, matriz2):
    resultado = matriz1 + matriz2
    print("Resultado:")
    print(resultado)

def resta(matriz1, matriz2):
    resultado = matriz1 - matriz2
    print("Resultado:")
    print(resultado)

def multi(matriz1, matriz2):
    resultado = np.dot(matriz1, matriz2)
    print("Resultado:")
    print(resultado)

def trans(matriz):
    resultado = matriz.T
    print("Resultado:")
    print(resultado)

def generador(tama):
    matriz = []

    for i in range(tama):
        fila = []
        for j in range(tama):
            num = int(input(f"Introduce el valor [{i}][{j}]: "))
            fila.append(num)
        matriz.append(fila)

    return np.array(matriz)


tama = int(input("Introduce el tamaño de la matriz: "))

print("Introduce la matriz 1")
matriz1 = generador(tama)

print("Introduce la matriz 2")
matriz2 = generador(tama)

print("\nMatriz 1:")
print(matriz1)

print("\nMatriz 2:")
print(matriz2)

print("\n¿Qué quieres hacer con las matrices?")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. Traspuesta de la matriz 1")

opcion = int(input("Opción: "))

if opcion == 1:
    suma(matriz1, matriz2)
elif opcion == 2:
    resta(matriz1, matriz2)
elif opcion == 3:
    multi(matriz1, matriz2)
elif opcion == 4:
    trans(matriz1)
else:
    print("Opción no válida.")
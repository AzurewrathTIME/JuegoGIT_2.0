import time

inicio = time.time()

# Código a medir

matriz1=[
    [4, 2, 4],
    [2, 7, 8],
    [6, 5, 3]
    ]

matriz2=[
    [5, 3, 9],
    [4, 1, 7],
    [2, 8, 3]
    ]
for mat in range (10000):
 matrizF=[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]
 for i in range(len(matrizF)):
    for j in range(3):
        for k in range(3):
            matrizF[i][j]=matrizF[i][j]+matriz1[i][k]*matriz2[k][j]

for elemento in matrizF:
    print(elemento)

fin = time.time()

print("Tiempo de ejecución:", fin - inicio, "segundos")

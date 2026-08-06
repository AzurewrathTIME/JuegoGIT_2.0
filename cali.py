import time
import random

stu = int(input("Cuantos estudiantes seran?  "))
print("Procesando datos"+"."+".")

def cal_prom(stu):
    time.sleep(4)
    cal_fin = 0
    lista = []

    for i in range(stu):
        calificacion = random.randint(10, 100)
        cal_fin = cal_fin + calificacion
        lista.append(calificacion)

    print("Calificaciones generadas:", lista)

    prom = cal_fin / stu
    return prom

prom_fin = cal_prom(stu)
print("El promedio general es:", prom_fin)
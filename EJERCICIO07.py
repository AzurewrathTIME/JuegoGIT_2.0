try:
    archivo = open("estudiantes.txt", "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    suma = 0
    cantidad = 0

    for linea in lineas:
        linea = linea.strip()

        if not linea:
            continue

        partes = linea.split(",")

        if len(partes) != 2:
            raise ValueError("Formato incorrecto en el archivo.")

        nombre = partes[0].strip()
        calificacion = float(partes[1].strip())

        suma += calificacion
        cantidad += 1

    if cantidad == 0:
        raise ValueError("No hay estudiantes en el archivo.")

    promedio = suma / cantidad

    archivo = open("reporte.txt", "w", encoding="utf-8")

    for linea in lineas:
        archivo.write(linea)

    archivo.write(f"Promedio general: {promedio:.1f}\n")
    archivo.close()

    print("Reporte generado correctamente.")
    print(f"Promedio general: {promedio:.1f}")

    agregar = input("¿Deseas agregar un nuevo estudiante? (s/n): ")

    if agregar.lower() == "s":
        nombre = input("Nombre del estudiante: ")
        calificacion = float(input("Calificación: "))

        archivo = open("estudiantes.txt", "a", encoding="utf-8")
        archivo.write(f"{nombre},{calificacion}\n")
        archivo.close()

        print("Estudiante agregado correctamente.")

except FileNotFoundError:
    print("Error: No se encontró el archivo estudiantes.txt.")

except ValueError as error:
    print("Error de formato:", error)

except Exception as error:
    print("Ocurrió un error:", error)

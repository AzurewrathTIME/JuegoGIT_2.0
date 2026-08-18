estudiantes = {}

def agregar():
    id = input("ID: ")

    if id in estudiantes:
        print("Ese ID ya existe")
        return

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    notas = []
    for i in range(3):
        notas.append(float(input(f"Calificación {i+1}: ")))

    estudiantes[id] = {
        "nombre": nombre,
        "edad": edad,
        "calificaciones": notas
    }

def mostrar():
    for id, datos in estudiantes.items():
        print(id, datos["nombre"], datos["edad"], datos["calificaciones"])

def promedio():
    id = input("ID: ")

    if id in estudiantes:
        notas = estudiantes[id]["calificaciones"]
        print("Promedio:", sum(notas) / len(notas))
    else:
        print("No existe")

def eliminar():
    id = input("ID: ")

    if id in estudiantes:
        del estudiantes[id]
        print("Eliminado")
    else:
        print("No existe")

opcion = 0

while opcion != 5:
    print("\n1. Agregar")
    print("2. Mostrar")
    print("3. Promedio")
    print("4. Eliminar")
    print("5. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        agregar()
    elif opcion == 2:
        mostrar()
    elif opcion == 3:
        promedio()
    elif opcion == 4:
        eliminar()

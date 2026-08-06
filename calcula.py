print("Bienvenido a la calculadora UTC")

while True:
    try:
        opcion = input("Elige una opción: 1. Suma 2. Resta 3. Multiplicación 4. División 0. Salir \n")
    
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))

        match opcion:
            case "1":
                print(f"La suma de {num1} y {num2} es {num1 + num2}")
    
            case "2":
                print(f"La resta de {num1} y {num2} es {num1 - num2}")
    
            case "3":
                print(f"La multiplicación de {num1} y {num2} es {num1 * num2}")
    
            case "4":
                if num2!=0:
                    print(f"La división de {num1} y {num2} es {num1 / num2}")
                else:
                    print("Entre ese no lo dividas")

            case "0":
                print(f"Salido")
    except:
        input("Error. Vuelve a introducir los valores")
        break
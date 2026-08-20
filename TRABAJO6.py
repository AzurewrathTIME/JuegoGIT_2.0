import opera
import txt
import util


while True:
    print("\n=== MENÚ PRINCIPAL ====")
    print("1. Operaciones matemáticas")
    print("2. Herramientas de texto")
    print("3. Utilidades")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- Operaciones matemáticas ---")

        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        print("Suma:", opera.suma(numero1, numero2))
        print("Resta:", opera.resta(numero1, numero2))
        print("Multiplicación:", opera.multiplicaion(numero1, numero2))
        print("División:", opera.divicion(numero1, numero2))

    elif opcion == "2":
        print("\n--- Herramientas de texto ---")

        texto_ingresado = input("Ingrese un texto: ")

        print("Cantidad de caracteres:", txt.count_let(texto_ingresado))
        print("Texto en mayúsculas:", txt.make_upper(texto_ingresado))
        print("Texto en minúsculas:", txt.make_lower(texto_ingresado))

    elif opcion == "3":
        print("\n--- Utilidades ---")

        numero = int(input("Ingrese un número: "))

        if util.divicion(numero):
            print("El número es par.")
        else:
            print("El número es impar.")

        print("\nTabla de multiplicar:")
        util.tbl_multiplo(numero)

    elif opcion == "4":
        util.show_messsage()
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
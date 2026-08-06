#Variable para reopetir codigo al final de la aventura
play="si" or "Si" or "SI"
while play=="si" or "Si" or "SI":
    print("\n=== Arcane Lineage ===")
    print("Te encuentras en pueblo caldera un lugar donde puedes ser lo que tu quieras.")
    print("Decides salir a explorar a las afueras con el equipo necesario")

    print("Te encuentras con un slime como primer enemigo")
    op1=input("Escribe A para atacar o B para huir: ")
    if op1=="A":
         print("\nMatas al slime ¡felicidades has subido de nivel!")

        # Segunda decisión
         print("Durante tu camino encuentras un portal alado de una cueva misteriosa a donde iras?")
         op2 = input("Escribe A para ir a la cueva o B para entrar a Illustris: ")

         if op2== "A":

            print("\nEscuchas un ruido extraño y aparece un dragón.")

            # Tercera decisión
            op3 = input("Escribe A para luchar o B para escapar: ")

            if op3 == "A":
                print("\n¡Derrotaste al dragón y encontraste el tesoro! FINAL FELIZ.")
            elif op3 == "B":
                print("\nEscapar del combate de un jefe te mata. Moriste, FINAL MALO.")
            else:
                print("\nOpción no válida.")

         elif op2 == "B":
            print("\nFelicidades ahora formas parte de los hijos de Raphdon. FINAL SANTO")
         else:
            print("\nOpción no válida.")

    elif op1 == "B":
        print("\nDecides volver a casa, Fin de la aventura.FINAL NEUTRAL")

    else:
        print("\nOpción no válida.")

    # Pregunta si desea jugar otra vez
    jugar = input("\n¿Quieres jugar otra vez? (si/no): ")

print("\nGracias por jugar.")
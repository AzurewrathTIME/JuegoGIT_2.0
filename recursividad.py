lis = [1, [2, 3], [4, [5, 6]]]

def recorrer(lis):
    for elemento in lis:
        if type(elemento) == list:
            recorrer(elemento)
        else:
            print(elemento)

recorrer(lis)

play = "si"

while play == "si" or play == "Si" or play == "SI":
    print("\n=== Arcane Lineage ===")
    print("Te encuentras en pueblo caldera un lugar donde puedes ser lo que tu quieras.")
    print("Decides salir a explorar a las afueras con el equipo necesario")

    print("Te encuentras con un slime como primer enemigo")
    op1 = input("Escribe A para atacar o B para huir: ")

    if op1 == "A":
        print("\nMatas al slime ¡felicidades has subido de nivel!")

        print("Durante tu camino encuentras un portal al lado de una cueva misteriosa a donde irás?")
        op2 = input("Escribe A para ir a la cueva o B para entrar a Illustris: ")

        if op2 == "A":
            print("\nEscuchas un ruido extraño y aparece un dragón.")
            op3 = input("Escribe A para luchar o B para escapar: ")

            if op3 == "A":
                print("\n¡Derrotaste al dragón y encontraste el tesoro! FINAL FELIZ.")
            elif op3 == "B" or "b":
                print("\nEscapar del combate de un jefe te mata. Moriste, FINAL MALO.")
            else:
                print("\nOpción no válida.")

        elif op2 == "B":
            print("\nFelicidades ahora formas parte de los hijos de Raphdon. FINAL SANTO")
        else:
            print("\nOpción no válida.")

    elif op1 == "B":
        print("\nDecides volver a casa. FINAL NEUTRAL")

    else:
        print("\nOpción no válida.")

    play = input("\n¿Quieres jugar otra vez? (si/no): ")

print("\nGracias por jugar.")
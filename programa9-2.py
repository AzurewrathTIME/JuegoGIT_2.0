import subprocess

try:
    with open("contraseñas.txt", "r", encoding="utf-8") as archivo:
        contrasenas = archivo.readlines()

    for contrasena in contrasenas:
        contrasena = contrasena.strip()

        resultado = subprocess.run(
            ["python3", "programa9-1.py", contrasena],
            capture_output=True,
            text=True
        )

        print(f"Probando contraseña: {contrasena}")
        print(resultado.stdout.strip())

        if "Login exitoso." in resultado.stdout:
            print("\n¡Contraseña encontrada!")
            print("La contraseña correcta es:", contrasena)
            break

except FileNotFoundError:
    print("Error: No se encontró contraseñas.txt o programa9-1.py.")

except Exception as error:
    print("Ocurrió un error:", error)

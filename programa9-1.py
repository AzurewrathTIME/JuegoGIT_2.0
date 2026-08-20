import sys


CONTRASENA_CORRECTA = "holamundo"


def verificar_login(contrasena):
    if contrasena == CONTRASENA_CORRECTA:
        print("Login exitoso.")
        return True
    else:
        print("Contraseña incorrecta.")
        return False


try:
    if len(sys.argv) != 2:
        print("Uso: python programa1.py <contraseña>")
        sys.exit(1)

    contrasena = sys.argv[1]
    verificar_login(contrasena)

except Exception as error:
    print("Ocurrió un error:", error)

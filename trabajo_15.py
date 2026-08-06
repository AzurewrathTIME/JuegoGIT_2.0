def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def fac(n):
    rebula = 1
    for i in range(1, n + 1):
        rebula *= i
    return rebula

def dCaF(c):
    return (c * 9/5) + 32

if __name__ == "__main__":
    print("Prueba de funciones implementadas en el programa, para validar su funcionamiento.")
    print("7 es primo?:", prime(7))
    print("Factorial de 5:", fac(5))
    print("25°C en Fahrenheit:", dCaF(25))
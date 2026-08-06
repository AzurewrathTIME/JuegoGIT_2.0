def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def fac(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def dCaF(c):
    return (c * 9/5) + 32

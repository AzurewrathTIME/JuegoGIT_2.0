iteraciones=int(input("Ingrese el numero de iteraciones a ingresar: "))
suma=0
for i in range(iteraciones):
 termino=((-1)**i)/(2*i+1)
 suma+=termino

pi_aprox=4*suma
pi_real=3.141592
diferencia= abs(pi_real-pi_aprox)
#abs busca dar el resultado de la diferencia sin importar que sea positivo o negativo

print(f"\nPi aproximado : {pi_aprox:.6f}")
print(f"Pi real       : {pi_real:.6f}")
print(f"Diferencia    : {diferencia:.6f}")
import os,time,random
i=0
e=0
ganador=False
Velocidad=0
Velocidad=0
limite=10
meta="[META]"

while True:
    i=i+random.randint(-1,3)
    e=e+random.randint(1,1)
    Velocidad=Velocidad+random.randint(1,2)
    print(" "*i+"🐇"+(limite-i+len("🐇"))*" "+meta)
    time.sleep(0.1)
    print()
    print(" "*e+"𓆉"+(limite-e+len("𓆉"))*" "+meta)
    time.sleep(0.5)
    if e>=limite or i>=limite:
     if i<=limite:
        ganador="🐇"
     if e>=limite:
        ganador="𓆉"
        break
    os.system("clear")
print("el ganador es:", ganador)
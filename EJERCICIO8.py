import sys
import random

cantidad = int(sys.argv[1])

for i in range(cantidad):
    print(random.randint(1, 50), end=" ")

num = int(input("Introduce la Altura del diamante: "))

for i in range(1, num+1, 2):
    print(" " * ((num-i)//2) + "o"*i)

for i in range(num-2+(num%2==0), 0, -2):
    print(" " * ((num-i)//2) + "o"*i)
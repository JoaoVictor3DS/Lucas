import random

n = random.randint(0, 11)

o = int(input("Tente: "))
while(o != n):
    o = int(input("Tente: "))

print("Parabéns")
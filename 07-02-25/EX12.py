n = int(input("Diga o número: "))

f1 = 0
f2 = 1

while f1 < n:
    print(f1)
    f1, f2 = f2, f1 + f2
    
n = int(input("Diga o número: "))

p = False

for i in range(2, round(n / 2) + 1):
    if n % i == 0:
        p = True

if n == 0:
    p = True

if p:
    print("Nao é Primo")
else:
    print("Primo")

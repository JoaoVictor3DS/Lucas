n = int(input("Diga o número: "))

divs = 0

for i in range(1, round(n / 2) + 1):
    if n % i == 0:
        divs += i

if n == divs:
    print("Perfeito")
else:
    print("Não perfeito")
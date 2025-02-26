cinquenta = 0
vinte = 0
dez = 0
cinco = 0

n = int(input("Diga um valor a ser pago: "))

while n >= 50:
    n -= 50
    cinquenta += 1

while n >= 20:
    n -= 20
    vinte += 1

while n >= 10:
    n -= 10
    dez += 1

while n >= 5:
    n -= 5
    cinco += 1

print(f"50$: {cinquenta}\n"
      f"20$: {vinte}\n"
      f"10$: {dez}\n"
      f"5$:  {cinco}\n")
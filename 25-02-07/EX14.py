nota = []

for i in range(0, 3):
    nota.append(int(input("Diga um número: ")))

print("A média é ", sum(nota) / 3)

if sum(nota) / 3 >= 6:
    print("Passou")

else:
    print("Não passou")
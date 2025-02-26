s = str(input("Diga a frase: "))

v = 0

for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        v += 1

print(f"São {v} vogais")
import sys

user = "Usuário"
senha = "123"

tentativa_user = input("Usuário: ")
tentativa_senha  = input("Senha: ")

if tentativa_senha != senha or tentativa_user != user:
    print("INVÁLIDO")
    exit()

saldo = float(input("Saldo Inicial: "))
print("Seu saldo inicial: ", saldo)

while True:
    print("Pressione: [D]epositar [S]acar [F]inalizar")
    bot = sys.stdin.read(1)
    
    print("")
    print("CONTA DE ", user,": ")

    if bot == 'D' or bot == 'd':
        deposito = float(input("Valor do deposito: "))
        saldo += deposito
    
    if bot == 'S' or bot == 's':
        saque = float(input("Valor do deposito: "))
        saldo -= saque

    print("Saldo atual: ", saldo)
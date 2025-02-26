class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0
    
    def depositar(self, n):
        self.__saldo += n 

    def sacar(self, n):
        if self.__saldo - n < 0:
            self.sacar(float(input('Saldo insuficiente, reinsira: ')))
        else:
            self.__saldo -= n
    
    def exibir_saldo(self):
        print(f'Saldo: {self.__saldo}')

contaJoao = ContaBancaria('João')
contaJoao.depositar(float(input('Diga o valor para depositar: ')))
contaJoao.sacar(float(input('Diga o valor para sacar: ')))

contaJoao.exibir_saldo()
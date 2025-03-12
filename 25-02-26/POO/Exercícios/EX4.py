class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_informacoes(self):
        print(f'Nome: {self.nome}\nSalário: {self.salario}')

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Bonus: {self.bonus}')

f = Funcionario('Joaozin', 'Minimo')
g = Gerente('Joaozao', 'Maximo', '1.25')

f.exibir_informacoes()
print('')
g.exibir_informacoes()
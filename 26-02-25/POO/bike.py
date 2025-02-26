class Bike:
    def __init__(self, modelo, cor, ano, valor):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print('Biiiii')
    
    def parar(self):
        self.correndo = False
        self.parada = True

    def correr(self):
        self.correndo = True
        self.parada = False

bicicleta_amarela = Bike(input('Diga o modelo: '), input('Diga a cor: '), input('Diga o ano: '), input('Diga o valor: '))

print(f''' 
Modelo: {bicicleta_amarela.modelo}
Cor: {bicicleta_amarela.cor}
Ano: {bicicleta_amarela.ano}
Valor: {bicicleta_amarela.valor}
''')

bicicleta_amarela.parar()
print(f'Parada: {bicicleta_amarela.parada}')
print(f'Correndo: {bicicleta_amarela.correndo}')

bicicleta_amarela.correr()
print(f'Parada: {bicicleta_amarela.parada}')
print(f'Correndo: {bicicleta_amarela.correndo}')

bicicleta_amarela.buzinar()
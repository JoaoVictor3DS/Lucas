class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def __str__(self):
        return f'Objeto: {self.__class__.__name__}\nMarca: {self.marca}\nAno: {self.ano}'
    
chevrolet = Carro('Chevrolet', 'Camaro', '2000')
print(chevrolet)
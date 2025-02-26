class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitirSom(self):
        print(f'Som de {self.nome}')

class Gato(Animal):
    def emitirSom(self):
        print(f'Miau')

class Cachorro(Animal):
    def emitirSom(self):
        print(f'Aauau')

animal = Animal('animal ae')
gato = Gato('Napoleão')
cachorro = Cachorro('Lua')

animal.emitirSom()
gato.emitirSom()
cachorro.emitirSom()
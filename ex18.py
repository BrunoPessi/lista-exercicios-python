# 18 - Crie uma classe animal com o método comer, este método deve  escrever na tela "o animal esta comendo". Depois
# disso crie as classes cachorro, cavalo e gato e implemente o método comer de acordo com o que cada animal come.
# Crie uma classe AnimalTeste e coloque os três animais dentro de uma lista de animais e chame o método comer
# polimorficamente (com um for).

class Animal():
    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f"O {self.__nome} está comendo")


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

class Cavalo(Animal):
    def __init__(self, nome):
        super().__init__(nome)

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

class AnimalTeste(Animal):

    cachorro = Cachorro("Cachorro")
    cavalo = Cavalo("Cavalo")
    gato = Gato("Gato")

    cachorro.comer()
    cavalo.comer()
    gato.comer()
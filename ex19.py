# Crie uma classe chamada Bicicleta. Ela terá os seguintes métodos: quantidadeMarchas(); tipoFreio() e marca(); Crie
# também duas classes que estendem esta classe, uma se chamará BicicletaPasseio e a outra BicicletaProfissional. Para
# ﬁnalizar crie uma classe onde deverá estar o método main e crie uma instancia de cada tipo de bicicleta e mostre o
# resultado dos métodos.

class Bicicleta:

    def quantidadeMarchas(self):
        print("Marchas: ")

    def tipoFreio(self):
        print("Freios: ")

    def marca(self):
        print("Marca: ")

class BicicletaPasseio(Bicicleta):

    def quantidadeMarchas(self):
        super().quantidadeMarchas()
        print('18')

    def tipoFreio(self):
        super().tipoFreio()
        print('normal')

    def marca(self):
        super().marca()
        print('caloi')

class BicicletaProfissional(Bicicleta):

    def quantidadeMarchas(self):
        super().quantidadeMarchas()
        print('24')

    def tipoFreio(self):
        super().tipoFreio()
        print('num sei')

    def marca(self):
        super().marca()
        print('sense')

class main():

    b_passeio = BicicletaPasseio()

    b_passeio.quantidadeMarchas()
    b_passeio.tipoFreio()
    b_passeio.marca()

    b_profissional = BicicletaProfissional()

    b_profissional.quantidadeMarchas()
    b_profissional.tipoFreio()
    b_profissional.marca()

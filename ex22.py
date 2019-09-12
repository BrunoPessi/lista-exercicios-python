# Crie a classe Imóvel, que possui um endereço e um preço.
# a. crie uma classe Novo, que herda Imóvel e possui um adicional no preço. Crie
# métodos de acesso e impressão deste valor adicional.
# b. crie uma classe Velho, que herda Imóvel e possui um desconto no preço. Crie
# métodos de acesso e impressão para este desconto.

class Imovel:

    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco


class Novo(Imovel):

    def __init__(self, preco):
        super().__init__(self, preco)

    def preco_adicional(self):
        self.preco += 50
        print("Valor novo com adicional:", self.preco)


class Velho(Imovel):

    def __init__(self, preco):
        super().__init__(self, preco)

    def preco_desconto(self):
        self.preco -= 100
        print("Valor novo com desconto:", self.preco)


if __name__ == '__main__':
    imovel_novo = Novo(1000)
    imovel_velho = Velho(500)

    imovel_novo.preco_adicional()
    imovel_velho.preco_desconto()
